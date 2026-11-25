// shadcn/ui's TSX components written as Python for Reacthon:
//   node tools/tsx2py.js <out-folder> <component.tsx>...
// Each component file becomes a `.py` of the same components, its JSX a
// t-string, its imports from JavaScript a `__js__`. What it cannot write, it
// names rather than guesses: the file is reported and left out.
import ts from 'typescript';
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, join } from 'node:path';

class Unsupported extends Error {}

const unsupported = (node, what) => {
    throw new Unsupported(`${what}: ${node.getText().slice(0, 80).replace(/\s+/g, ' ')}`);
};

// Python modules for the JavaScript ones shadcn/ui's sources name.
const PYTHON_MODULES = { cn: 'utils', '@/lib/utils': 'utils', 'class-variance-authority': 'utils' };
const pythonModule = (from) =>
    PYTHON_MODULES[from] ?? (from.startsWith('@/components/ui/') ? from.slice('@/components/ui/'.length).replace(/-/g, '_') : null);

const QUOTES = ['"""', "'''", '"', "'"];
const DOM_NAMES = { className: 'class', htmlFor: 'for' };
const OPERATORS = {
    [ts.SyntaxKind.EqualsEqualsEqualsToken]: '==',
    [ts.SyntaxKind.EqualsEqualsToken]: '==',
    [ts.SyntaxKind.ExclamationEqualsEqualsToken]: '!=',
    [ts.SyntaxKind.ExclamationEqualsToken]: '!=',
    [ts.SyntaxKind.AmpersandAmpersandToken]: 'and',
    [ts.SyntaxKind.BarBarToken]: 'or',
    [ts.SyntaxKind.PlusToken]: '+',
    [ts.SyntaxKind.MinusToken]: '-',
    [ts.SyntaxKind.AsteriskToken]: '*',
    [ts.SyntaxKind.SlashToken]: '/',
    [ts.SyntaxKind.LessThanToken]: '<',
    [ts.SyntaxKind.GreaterThanToken]: '>',
    [ts.SyntaxKind.LessThanEqualsToken]: '<=',
    [ts.SyntaxKind.GreaterThanEqualsToken]: '>='
};

const string = (text) => JSON.stringify(text);
const braces = (text) => text.replace(/\\/g, '\\\\').replace(/\{/g, '{{').replace(/\}/g, '}}');

// JSX's text as React reads it: each line trimmed where it meets another, the
// lines left empty dropped, the rest joined by a space.
function jsxText(raw) {
    const lines = raw.split(/\r\n|\n|\r/);
    let text = '';

    lines.forEach((line, at) => {
        let one = line.replace(/\t/g, ' ');

        if (at !== 0) one = one.replace(/^ +/, '');
        if (at !== lines.length - 1) one = one.replace(/ +$/, '');
        if (one) text += (text && at !== 0 ? ' ' : '') + one;
    });

    return text;
}

function translator(variantMakers) {
    const py = (node, depth) => {
        const k = ts.SyntaxKind;

        switch (node.kind) {
            case k.StringLiteral:
            case k.NoSubstitutionTemplateLiteral:
                return string(node.text);
            case k.NumericLiteral:
                return node.text;
            case k.TrueKeyword:
                return 'True';
            case k.FalseKeyword:
                return 'False';
            case k.NullKeyword:
                return 'None';
            case k.Identifier:
                return node.text === 'undefined' ? 'None' : node.text;
            case k.ParenthesizedExpression:
                return ts.isJsxElement(node.expression) || ts.isJsxSelfClosingElement(node.expression) || ts.isJsxFragment(node.expression)
                    ? py(node.expression, depth)
                    : `(${py(node.expression, depth)})`;
            case k.AsExpression:
            case k.NonNullExpression:
            case k.SatisfiesExpression:
            case k.TypeAssertionExpression:
                return py(node.expression, depth);
            case k.PropertyAccessExpression:
                if (node.expression.kind === k.Identifier && node.expression.text === 'React') unsupported(node, "React's own API");
                return `${py(node.expression, depth)}.${node.name.text}`;
            case k.ElementAccessExpression:
                return `${py(node.expression, depth)}[${py(node.argumentExpression, depth)}]`;
            case k.CallExpression:
                return call(node, depth);
            case k.PrefixUnaryExpression:
                if (node.operator === k.ExclamationToken) return `not ${py(node.operand, depth)}`;
                if (node.operator === k.MinusToken) return `-${py(node.operand, depth)}`;
                return unsupported(node, 'an operator');
            case k.BinaryExpression: {
                // `a ?? b` of a name, which reading twice changes nothing.
                if (node.operatorToken.kind === k.QuestionQuestionToken) {
                    if (!ts.isIdentifier(node.left) && !ts.isPropertyAccessExpression(node.left)) unsupported(node, 'a ?? of an expression');

                    const left = py(node.left, depth);

                    return `(${left} if ${left} is not None else ${py(node.right, depth)})`;
                }

                const operator = OPERATORS[node.operatorToken.kind];

                if (operator === undefined) unsupported(node, 'an operator');
                return `${py(node.left, depth)} ${operator} ${py(node.right, depth)}`;
            }
            case k.ConditionalExpression:
                return `(${py(node.whenTrue, depth)} if ${py(node.condition, depth)} else ${py(node.whenFalse, depth)})`;
            case k.TemplateExpression: {
                let text = braces(node.head.text);

                for (const span of node.templateSpans) text += `{${py(span.expression, depth)}}${braces(span.literal.text)}`;
                return `f${string(text).replace(/\\\\/g, '\\')}`;
            }
            case k.TaggedTemplateExpression: {
                const raw = node.template.rawText;

                if (node.tag.getText() !== 'String.raw' || !ts.isNoSubstitutionTemplateLiteral(node.template)) unsupported(node, 'a tagged template');
                if (raw.includes('"') || raw.endsWith('\\')) unsupported(node, 'a raw string Python cannot write');
                return `r"${raw}"`;
            }
            case k.ObjectLiteralExpression:
                return `{${node.properties.map((one) => entry(one, depth)).join(', ')}}`;
            case k.ArrayLiteralExpression:
                return `[${node.elements.map((one) => py(one, depth)).join(', ')}]`;
            case k.JsxElement:
            case k.JsxSelfClosingElement:
            case k.JsxFragment:
                return tstring(node, depth);
            default:
                return unsupported(node, ts.SyntaxKind[node.kind]);
        }
    };

    const key = (name) => (ts.isIdentifier(name) || ts.isStringLiteral(name) ? string(name.text) : unsupported(name, 'a computed key'));

    const entry = (one, depth) => {
        if (ts.isShorthandPropertyAssignment(one)) return `${string(one.name.text)}: ${one.name.text}`;
        if (ts.isPropertyAssignment(one)) return `${key(one.name)}: ${py(one.initializer, depth)}`;
        if (ts.isSpreadAssignment(one)) return `**${py(one.expression, depth)}`;
        return unsupported(one, 'an object member');
    };

    // cva(base, { variants, defaultVariants, compoundVariants }) is utils.cva's
    // three dicts; what cva made is called with keywords.
    const call = (node, depth) => {
        const callee = py(node.expression, depth);
        const args = node.arguments;

        if (callee === 'cva') {
            const options = args[1];
            const field = (name) => options?.properties.find((one) => one.name?.text === name)?.initializer;
            const parts = [py(args[0], depth)];

            if (options && !ts.isObjectLiteralExpression(options)) unsupported(node, "cva's options");
            for (const name of ['variants', 'defaultVariants', 'compoundVariants']) parts.push(field(name) ? py(field(name), depth) : 'None');
            while (parts.at(-1) === 'None') parts.pop();
            return `cva(${parts.join(', ')})`;
        }

        if (variantMakers.has(callee) && args.length === 1 && ts.isObjectLiteralExpression(args[0])) {
            const keywords = args[0].properties.map((one) => {
                if (ts.isShorthandPropertyAssignment(one)) return `${one.name.text}=${one.name.text}`;
                if (ts.isPropertyAssignment(one) && ts.isIdentifier(one.name)) return `${one.name.text}=${py(one.initializer, depth)}`;
                return unsupported(one, 'a variant');
            });

            return `${callee}(${keywords.join(', ')})`;
        }

        return `${callee}(${args.map((one) => py(one, depth)).join(', ')})`;
    };

    const tagName = (name) => {
        if (ts.isIdentifier(name) && /^[a-z]/.test(name.text)) return name.text;
        if (ts.isIdentifier(name) || ts.isPropertyAccessExpression(name)) return `{${name.getText()}}`;
        return unsupported(name, 'a tag');
    };

    // A field of the t-string: a dict apart from its braces, which `{{` would
    // escape.
    const field = (node, depth) => {
        const value = py(node, depth + 1);

        return value.startsWith('{') ? `{ ${value} }` : `{${value}}`;
    };

    const attribute = (one, depth) => {
        if (ts.isJsxSpreadAttribute(one)) return `...${field(one.expression, depth)}`;

        const name = DOM_NAMES[one.name.getText()] ?? one.name.getText();
        const value = one.initializer;

        if (value === undefined) return name;
        if (ts.isStringLiteral(value)) return `${name}="${braces(value.text)}"`;
        if (value.expression && ts.isStringLiteral(value.expression)) return `${name}="${braces(value.expression.text)}"`;
        if (value.expression === undefined) return unsupported(one, 'an empty attribute');
        return `${name}=${field(value.expression, depth)}`;
    };

    // The children as a t-string writes them: an element's on lines of their
    // own, which htm drops as JSX does, text and fields where they stand.
    const children = (list, depth, indent) => {
        const parts = [];

        for (const one of list) {
            if (ts.isJsxText(one)) {
                const text = jsxText(one.text);

                if (text) parts.push({ inline: true, text: braces(text) });
            } else if (ts.isJsxExpression(one)) {
                if (one.expression) parts.push({ inline: true, text: field(one.expression, depth) });
            } else {
                parts.push({ inline: false, text: markup(one, depth, indent + 1) });
            }
        }

        if (parts.every((one) => !one.inline) && parts.length) {
            return `\n${parts.map((one) => `${'    '.repeat(indent + 1)}${one.text}`).join('\n')}\n${'    '.repeat(indent)}`;
        }

        return parts.map((one) => one.text).join('');
    };

    const markup = (node, depth, indent) => {
        if (ts.isJsxFragment(node)) return children(node.children, depth, indent - 1).trim();

        const opening = ts.isJsxElement(node) ? node.openingElement : node;
        const tag = tagName(opening.tagName);
        const attributes = opening.attributes.properties.map((one) => attribute(one, depth));
        let head = [tag, ...attributes].join(' ');

        // A long tag, one attribute a line, where the t-string has lines.
        if (depth === 0 && attributes.length > 1 && indent * 4 + head.length > 100) {
            head = `${tag}\n${attributes.map((one) => `${'    '.repeat(indent + 1)}${one}`).join('\n')}\n${'    '.repeat(indent)}`;
        }

        if (ts.isJsxSelfClosingElement(node)) return `<${head}${head.endsWith(' ') ? '' : ' '}/>`;
        return `<${head}>${children(node.children, depth, indent)}</${tag}>`;
    };

    // A dict or a list too long for its line, one entry a line.
    const pretty = (node, level) => {
        const flat = py(node, 1);
        const pad = '    '.repeat(level + 1);

        if (flat.length + level * 4 <= 96) return flat;
        if (ts.isObjectLiteralExpression(node)) {
            const lines = node.properties.map((one) =>
                ts.isPropertyAssignment(one) ? `${pad}${key(one.name)}: ${pretty(one.initializer, level + 1)},` : `${pad}${entry(one, 1)},`
            );

            return `{\n${lines.join('\n')}\n${'    '.repeat(level)}}`;
        }
        if (ts.isArrayLiteralExpression(node)) {
            return `[\n${node.elements.map((one) => `${pad}${pretty(one, level + 1)},`).join('\n')}\n${'    '.repeat(level)}]`;
        }
        return flat;
    };

    py.pretty = pretty;

    const tstring = (node, depth) => {
        const quote = QUOTES[Math.min(depth, QUOTES.length - 1)];
        const text = markup(node, depth, depth === 0 ? 2 : 0);

        return depth === 0 ? `t${quote}\n        ${text}\n    ${quote}` : `t${quote}${text}${quote}`;
    };

    return py;
}

export function translate(text, file) {
    const source = ts.createSourceFile(file, text, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
    const python = new Map();
    const js = new Map();
    const variantMakers = new Set();
    const body = [];

    const add = (map, from, name) => map.set(from, [...(map.get(from) ?? []), name]);

    for (const node of source.statements) {
        if (ts.isImportDeclaration(node)) {
            const from = node.moduleSpecifier.text;
            const clause = node.importClause;

            if (from === 'react' || clause?.isTypeOnly) continue;

            const module = pythonModule(from);
            const whole = clause?.namedBindings && ts.isNamespaceImport(clause.namedBindings) ? clause.namedBindings.name.text : null;

            // A default and a namespace import, as `__js__` renames them.
            if ((clause?.name || whole) && module) unsupported(node, 'a default or namespace import of Python');
            if (clause?.name) add(js, from, `default as ${clause.name.text}`);
            if (whole) add(js, from, `* as ${whole}`);

            for (const one of whole ? [] : (clause?.namedBindings?.elements ?? [])) {
                if (one.isTypeOnly) continue;

                const name = one.propertyName ? `${one.propertyName.text} as ${one.name.text}` : one.name.text;

                if (module) add(python, module, one.name.text);
                else add(js, from, name);
                // Another component's variants, `buttonVariants`, take keywords
                // as its own module's do.
                if (module && /Variants$/.test(one.name.text)) variantMakers.add(one.name.text);
            }
        }
    }

    const py = translator(variantMakers);

    const component = (name, parameters, statements) => {
        const binding = parameters[0]?.name;
        const params = [];

        if (binding && !ts.isObjectBindingPattern(binding)) unsupported(parameters[0], 'props not destructured');
        for (const one of binding?.elements ?? []) {
            if (one.propertyName) unsupported(one, 'a renamed prop');
            if (one.dotDotDotToken) params.push(`**${one.name.text}`);
            else params.push(`${one.name.text}=${one.initializer ? py(one.initializer, 0) : 'None'}`);
        }

        const lines = statements.map((one) => {
            if (ts.isReturnStatement(one)) return `    return ${py(one.expression, 0)}`;
            if (ts.isVariableStatement(one)) {
                return one.declarationList.declarations
                    .map((d) => (ts.isIdentifier(d.name) ? `    ${d.name.text} = ${py(d.initializer, 1)}` : unsupported(d, 'a destructured variable')))
                    .join('\n');
            }
            return unsupported(one, 'a statement');
        });

        return `def ${name}(${params.join(', ')}):\n${lines.join('\n\n')}`;
    };

    for (const node of source.statements) {
        if (ts.isImportDeclaration(node) || ts.isExportDeclaration(node)) continue;
        if (ts.isExpressionStatement(node) && ts.isStringLiteral(node.expression)) continue;
        if (ts.isTypeAliasDeclaration(node) || ts.isInterfaceDeclaration(node)) continue;

        if (ts.isFunctionDeclaration(node)) {
            body.push(component(node.name.text, node.parameters, node.body.statements));
        } else if (ts.isVariableStatement(node)) {
            for (const one of node.declarationList.declarations) {
                const value = one.initializer;

                if (ts.isArrowFunction(value) && ts.isBlock(value.body)) body.push(component(one.name.text, value.parameters, value.body.statements));
                else if (ts.isCallExpression(value) && value.expression.getText() === 'cva') {
                    // cva(base, variants, defaults, compound), one a line.
                    const [base, options] = value.arguments;
                    const field = (name) => options?.properties.find((p) => p.name?.text === name)?.initializer;
                    const parts = [py(base, 1), ...['variants', 'defaultVariants', 'compoundVariants'].map((name) => (field(name) ? py.pretty(field(name), 1) : 'None'))];

                    while (parts.at(-1) === 'None') parts.pop();
                    variantMakers.add(one.name.text);
                    body.push(`${one.name.text} = cva(\n${parts.map((part) => `    ${part},`).join('\n')}\n)`);
                } else {
                    body.push(`${one.name.text} = ${py(value, 1)}`);
                }
            }
        } else {
            unsupported(node, ts.SyntaxKind[node.kind]);
        }
    }

    const head = [...python].map(([module, names]) => `from ${module} import ${names.join(', ')}`);
    const jsEntries = [...js].map(([from, names]) => `    ${string(from)}: [${names.map(string).join(', ')}],`);

    if (jsEntries.length) head.push('', `__js__ = {\n${jsEntries.join('\n')}\n}`);

    return `${head.join('\n')}\n\n\n${body.join('\n\n\n')}\n`;
}

const [out, ...files] = process.argv.slice(2);

if (out) {
    mkdirSync(out, { recursive: true });
    for (const file of files) {
        const name = `${basename(file, '.tsx').replace(/-/g, '_')}.py`;

        try {
            writeFileSync(join(out, name), translate(readFileSync(file, 'utf8'), file));
            console.log(`written ${name}`);
        } catch (error) {
            if (!(error instanceof Unsupported)) throw error;
            console.log(`left out ${basename(file)}: ${error.message}`);
        }
    }
}
