// shadcn/ui's TSX components written as Python for Reacthon:
//   node tools/tsx2py.js <out-folder> <component.tsx>...
// Each component file becomes a `.py` of the same components, laid out as one
// writes Python by hand: its JSX a t-string, its imports from JavaScript a
// `__js__`, React's hooks Reacthon's, its own names in snake_case. TypeScript's
// own checker tells what each value is: plain data, which Brython hands Python
// as a dict, or an object. What it cannot write, it names rather than guesses:
// the file is reported and left out.
import ts from 'typescript';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { basename, dirname, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

class Unsupported extends Error {}

const unsupported = (node, what) => {
    throw new Unsupported(`${what}: ${node.getText().slice(0, 80).replace(/\s+/g, ' ')}`);
};

const WIDTH = 120;
const pad = (level) => '    '.repeat(level);

// Python modules for the JavaScript ones shadcn/ui's sources name: a component
// of its own, or one beside the file, as a block's page imports its form.
const PYTHON_MODULES = { cn: 'utils', '@/lib/utils': 'utils', 'class-variance-authority': 'utils' };
const pythonModule = (from) =>
    PYTHON_MODULES[from] ??
    (from.startsWith('@/components/ui/')
        ? from.slice('@/components/ui/'.length).replace(/-/g, '_')
        : /^\.\/[\w-]+$/.test(from)
          ? from.slice(2).replace(/-/g, '_')
          : null);

// React's API under Reacthon's names.
const HOOKS = {
    useState: 'use_state',
    useReducer: 'use_reducer',
    useEffect: 'use_effect',
    useLayoutEffect: 'use_layout_effect',
    useMemo: 'use_memo',
    useCallback: 'use_callback',
    useRef: 'use_ref',
    useContext: 'use_context',
    useId: 'use_id',
    createContext: 'create_context',
    memo: 'memo'
};

// The page's own names, from Brython's modules.
// The methods of a list that call their callback before they return.
const CALLED_AT_ONCE = new Set(['map', 'filter', 'flatMap', 'some', 'every', 'find', 'findIndex', 'findLast', 'findLastIndex', 'forEach', 'reduce', 'reduceRight', 'sort', 'toSorted']);

// React's own values a component may read, as a library's.
const REACT_VALUES = new Set(['Children', 'Fragment', 'cloneElement', 'isValidElement']);

const GLOBALS = { window: ['browser', 'window'], document: ['browser', 'document'], Math: ['javascript', 'Math'], Date: ['javascript', 'Date'] };
const ON_WINDOW = new Set(['navigator', 'setTimeout', 'clearTimeout', 'matchMedia', 'innerWidth', 'Promise']);

// Python's keywords, which no name can be, `from` of a date range, and its own
// functions, which a name would hide: CPython 3.14's keyword.kwlist and the
// lowercase names of dir(builtins). And utils.py's, which the translation calls.
const KEYWORDS = new Set(
    'False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield'.split(' ')
);
const BUILTINS = new Set(
    [
        'abs aiter all anext any ascii bin bool breakpoint bytearray bytes callable chr classmethod compile complex copyright credits',
        'delattr dict dir divmod enumerate eval exec exit filter float format frozenset getattr globals hasattr hash help hex id input',
        'int isinstance issubclass iter len license list locals map max memoryview min next object oct open ord pow print property',
        'quit range repr reversed round set setattr slice sorted staticmethod str sum super tuple type vars zip',
        'closest sort'
    ]
        .join(' ')
        .split(' ')
);

// A name the Python modules make, as Python spells it: buttonVariants is
// button_variants; a component's, a constant's and a prop's stay as they are.
const spell = (name) => {
    const [, lead, rest] = /^(_*)(.*)$/.exec(name);

    return /^[a-z]/.test(rest) && /[A-Z]/.test(rest)
        ? lead + rest.replace(/([a-z0-9])([A-Z])/g, '$1_$2').replace(/([A-Z])([A-Z][a-z])/g, '$1_$2').toLowerCase()
        : name;
};

// And one that is Python's own takes a trailing underscore: `list` is list_.
const snake = (name) => {
    const spelled = spell(name);

    return KEYWORDS.has(spelled) || BUILTINS.has(spelled) ? `${spelled}_` : spelled;
};

// Python's precedence, lowest first: an operand goes in parentheses where its
// own binds less than its place asks for.
const LAMBDA = 0;
const WHOLE = 0;
const CONDITIONAL = 1;
const OR = 2;
const AND = 3;
const NOT = 4;
const COMPARE = 5;
const ADD = 10;
const MULTIPLY = 11;
const UNARY = 12;
const PRIMARY = 15;

const k = ts.SyntaxKind;
const BINARY = {
    [k.EqualsEqualsEqualsToken]: ['==', COMPARE],
    [k.EqualsEqualsToken]: ['==', COMPARE],
    [k.ExclamationEqualsEqualsToken]: ['!=', COMPARE],
    [k.ExclamationEqualsToken]: ['!=', COMPARE],
    [k.LessThanToken]: ['<', COMPARE],
    [k.GreaterThanToken]: ['>', COMPARE],
    [k.LessThanEqualsToken]: ['<=', COMPARE],
    [k.GreaterThanEqualsToken]: ['>=', COMPARE],
    [k.InKeyword]: ['in', COMPARE],
    [k.AmpersandAmpersandToken]: ['and', AND],
    [k.BarBarToken]: ['or', OR],
    [k.PlusToken]: ['+', ADD],
    [k.MinusToken]: ['-', ADD],
    [k.AsteriskToken]: ['*', MULTIPLY],
    [k.SlashToken]: ['/', MULTIPLY],
    [k.PercentToken]: ['%', MULTIPLY]
};
const ASSIGNMENTS = { [k.EqualsToken]: '=', [k.PlusEqualsToken]: '+=', [k.MinusEqualsToken]: '-=' };
const TYPEOF = { string: 'str', number: '(int, float)', boolean: 'bool', object: 'dict' };
const UTILITY_TYPES = new Set(['Partial', 'Required', 'Readonly', 'Pick', 'Omit', 'Record', 'NonNullable']);

const DOM_NAMES = { className: 'class', htmlFor: 'for' };

const string = (text) => JSON.stringify(text);
const braces = (text) => text.replace(/\\/g, '\\\\').replace(/\{/g, '{{').replace(/\}/g, '}}');
const unwrap = (node) =>
    node && (ts.isParenthesizedExpression(node) || ts.isAsExpression(node) || ts.isNonNullExpression(node) || ts.isSatisfiesExpression(node))
        ? unwrap(node.expression)
        : node;
const isJsx = (node) => {
    const one = unwrap(node);

    return Boolean(one) && (ts.isJsxElement(one) || ts.isJsxSelfClosingElement(one) || ts.isJsxFragment(one));
};
const isFunction = (node) => {
    const one = unwrap(node);

    return Boolean(one) && (ts.isArrowFunction(one) || ts.isFunctionExpression(one));
};

// JSX's character references, which its compiler reads as their characters and
// htm leaves as they are written.
const ENTITIES = { amp: '&', apos: "'", quot: '"', gt: '>', nbsp: ' ' };

function decoded(text) {
    return text.replace(/&(?:#x([\da-f]+)|#(\d+)|(\w+));/gi, (whole, hex, decimal, name) => {
        const one = hex ? String.fromCodePoint(parseInt(hex, 16)) : decimal ? String.fromCodePoint(Number(decimal)) : ENTITIES[name];

        return one === undefined || one === '<' ? unsupported({ getText: () => whole }, 'a character reference') : one;
    });
}

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

    return decoded(text);
}

// The quotes of a t-string: ones its text does not hold, and where they can be,
// not the ones of the t-string it stands in, which Python 3.12 allows them to be.
function quotes(text, multiline, around) {
    const bare = literal(text);
    const pick = (avoid) =>
        (multiline ? undefined : ['"', "'"].find((one) => one !== avoid && !bare.includes(one))) ??
        ['"""', "'''"].find((one) => one[0] !== avoid && !bare.includes(one) && !bare.endsWith(one[0]));

    return pick(around) ?? pick(null) ?? unsupported({ getText: () => text }, 'a t-string no quotes can hold');
}

// A t-string's text without its fields, where its quotes end it.
function literal(text) {
    let out = '';
    let depth = 0;

    for (let at = 0; at < text.length; at += 1) {
        const one = text[at];

        if (depth === 0 && (text.startsWith('{{', at) || text.startsWith('}}', at))) {
            out += one;
            at += 1;
        } else if (one === '{') {
            depth += 1;
        } else if (one === '}' && depth > 0) {
            depth -= 1;
        } else if (depth === 0) {
            out += one;
        }
    }

    return out;
}

// A regular expression's replace as Python's str methods do it: every `:` of
// /:/g, the `\n` that /\n$/ ends on.
function replaced(regex, replacement) {
    const [, source, flags] = /^\/(.*)\/([a-z]*)$/.exec(regex.text);
    const special = /[\^$.*+?()[\]{}|]/;
    const bare = source.replace(/\\./g, '');
    const text = (one) => one.replace(/\\(.)/g, (whole, letter) => ({ n: '\n', t: '\t' })[letter] ?? letter);

    if (flags === 'g' && !special.test(bare)) return ['replace', text(source)];
    if (flags === '' && source.endsWith('$') && !special.test(bare.slice(0, -1)) && replacement === '') return ['removesuffix', text(source.slice(0, -1))];
    return null;
}

function moduleTranslator(source, checker, program, translated = new Set()) {
    const python = new Map();
    const js = new Map();
    const react = new Map();
    const brython = new Map();
    const hooks = new Set();
    const variantMakers = new Set();
    const imported = new Set();
    const used = new Set();
    const own = new Set();
    let reactNamespace = null;

    const add = (map, from, entry) => map.set(from, [...(map.get(from) ?? []), entry]);
    // React's own value, `Children`, imported by `__js__` as a library's is.
    const reactValue = (local) => {
        if (!js.get('react')?.some((one) => one.local === local)) add(js, 'react', { local, entry: local });
        used.add(local);
        return local;
    };
    // One of utils.py's own, for what Python's or Brython's does otherwise,
    // imported under its own name, which a name of the module's gives way to.
    const helper = (local) => {
        if (!python.get('utils')?.some((one) => one.local === local)) add(python, 'utils', { local, own: true });
        used.add(local);
    };
    const need = (module, name) => brython.set(module, new Set([...(brython.get(module) ?? []), name]));
    // A file of the project that is Python, translated with this one or before
    // it, its `.py` beside it: imported by its file's name, as Reacthon finds
    // it, `@/components/app-sidebar` as `app_sidebar`.
    const projectModule = (from) => {
        const file = ts.resolveModuleName(from, source.fileName, program.getCompilerOptions(), ts.sys).resolvedModule?.resolvedFileName;

        if (!file || /[\\/]node_modules[\\/]/.test(file) || file.endsWith('.d.ts')) return null;

        const named = basename(file).replace(/\.tsx?$/, '').replace(/-/g, '_');

        return translated.has(resolve(file)) || existsSync(join(dirname(file), `${named}.py`)) ? named : null;
    };

    for (const node of source.statements) {
        if (!ts.isImportDeclaration(node)) continue;

        const from = node.moduleSpecifier.text;
        const clause = node.importClause;

        if (clause?.isTypeOnly) continue;
        if (from === 'react') {
            if (clause?.namedBindings && ts.isNamespaceImport(clause.namedBindings)) reactNamespace = clause.namedBindings.name.text;
            for (const one of clause?.namedBindings?.elements ?? []) if (!one.isTypeOnly) react.set(one.name.text, (one.propertyName ?? one.name).text);
            continue;
        }

        const pyModule = pythonModule(from) ?? projectModule(from);
        const whole = clause?.namedBindings && ts.isNamespaceImport(clause.namedBindings) ? clause.namedBindings.name.text : null;

        // A default and a namespace import, as `__js__` renames them; the
        // namespace of a Python module, the module itself: `import edition`.
        if (clause?.name && pyModule) unsupported(node, 'a default import of Python');
        if (clause?.name) add(js, from, { local: clause.name.text, entry: `default as ${clause.name.text}` });
        if (whole) add(pyModule ? python : js, pyModule ?? from, pyModule ? { local: whole, whole: true } : { local: whole, entry: `* as ${whole}` });

        for (const one of whole ? [] : (clause?.namedBindings?.elements ?? [])) {
            if (one.isTypeOnly) continue;

            const local = one.name.text;

            imported.add(local);
            if (pyModule) {
                add(python, pyModule, { local });
                own.add(local);
            } else {
                add(js, from, { local, entry: one.propertyName ? `${one.propertyName.text} as ${local}` : local });
            }
            // Another component's variants, `buttonVariants`, take keywords
            // as its own module's do.
            if (pyModule && /Variants$/.test(local)) variantMakers.add(local);
        }
        if (clause?.name) imported.add(clause.name.text);
        if (whole) imported.add(whole);
    }

    for (const node of source.statements) {
        if (ts.isVariableStatement(node)) for (const one of node.declarationList.declarations) if (ts.isIdentifier(one.name)) own.add(one.name.text);
        if (ts.isFunctionDeclaration(node) && node.name) own.add(node.name.text);
    }

    // --- What a value is ---------------------------------------------------

    const fromLibrary = (declaration) => {
        const file = declaration.getSourceFile();

        return program.isSourceFileDefaultLibrary(file) || /node_modules[\\/]@types[\\/]react[\\/]/.test(file.fileName);
    };

    // Plain data: an object of no class, which Brython hands over as a dict.
    const plain = (type) => {
        if (type.isUnion()) return type.types.filter((one) => !(one.flags & (ts.TypeFlags.Null | ts.TypeFlags.Undefined))).every(plain);
        if (type.isIntersection()) return type.types.some(plain) && !type.types.some((one) => one.getCallSignatures().length);
        if (type.flags & ts.TypeFlags.NonPrimitive) return true;
        if (!(type.flags & ts.TypeFlags.Object)) return false;
        if (checker.isArrayType(type) || checker.isTupleType(type) || type.getCallSignatures().length || type.getConstructSignatures().length) return false;

        // Partial<T>, Pick<T, K>…: what T is; a Record, plain.
        if (type.aliasSymbol && UTILITY_TYPES.has(type.aliasSymbol.name) && type.aliasSymbol.getDeclarations()?.some(fromLibrary)) {
            return type.aliasSymbol.name === 'Record' || plain(type.aliasTypeArguments[0]);
        }

        const symbol = type.aliasSymbol ?? type.getSymbol();
        const declarations = symbol?.getDeclarations() ?? [];

        if (declarations.some((one) => ts.isClassDeclaration(one) || ts.isClassExpression(one) || fromLibrary(one))) return false;
        if (symbol && symbol.flags & (ts.SymbolFlags.ValueModule | ts.SymbolFlags.Function)) return false;
        return true;
    };

    // A type of a package's own with methods: what its JavaScript makes is an
    // object to Python, `table.getAllColumns()`, wherever Reacthon has not
    // copied it. Its data alone, a dict's reads read it, and the dict Python
    // handed the package and reads back as well: `table.state.pagination`.
    const packaged = (type) => inPackage(type) && type.getProperties().some((one) => checker.getTypeOfSymbol(one).getCallSignatures().length);
    const inPackage = (type) => {
        if (type.isIntersection()) return type.types.some(inPackage);

        const symbol = type.aliasSymbol ?? type.getSymbol();

        return Boolean(symbol?.getDeclarations()?.some((one) => /[\\/]node_modules[\\/]/.test(one.getSourceFile().fileName) && !fromLibrary(one)));
    };

    const isComponent = (fn) => {
        const named = fn.name ?? (ts.isVariableDeclaration(fn.parent) || ts.isPropertyAssignment(fn.parent) ? fn.parent.name : undefined);

        return Boolean(named) && /^[A-Z]/.test(named.getText()) && fn.parameters.length <= 1;
    };

    // How many arguments Python may hand a function a prop of the project's
    // own component holds, where that component calls it itself, as its TSX
    // does, with as many as the prop's type says: `labelFormatter(value,
    // payload)` of a function that reads one. One it hands on to JavaScript,
    // `onClick` to Radix, is cut to the function's arguments at Bryntime's door.
    const calledProp = (component, prop) => {
        const fn = ts.isFunctionDeclaration(component) ? component : ts.isVariableDeclaration(component) ? unwrap(component.initializer ?? component) : null;
        const first = fn && ts.isFunctionLike(fn) ? fn.parameters?.[0] : null;

        if (!first || !fn.body) return false;

        const element = ts.isObjectBindingPattern(first.name) ? first.name.elements.find((one) => (one.propertyName ?? one.name).getText() === prop) : null;
        const local = element && !element.dotDotDotToken ? element.name.getText() : null;
        let called = false;
        const look = (node) => {
            if (ts.isCallExpression(node)) {
                const callee = unwrap(node.expression);

                called ||= local !== null ? ts.isIdentifier(callee) && callee.text === local : ts.isPropertyAccessExpression(callee) && callee.name.text === prop && ts.isIdentifier(first.name);
            }
            if (!called) ts.forEachChild(node, look);
        };

        look(fn.body);
        return called;
    };
    const pythonArity = (fn) => {
        let at = fn;

        while (ts.isParenthesizedExpression(at.parent)) at = at.parent;
        if (!ts.isJsxExpression(at.parent) || !ts.isJsxAttribute(at.parent.parent)) return 0;

        const attribute = at.parent.parent;
        const tag = attribute.parent.parent.tagName;
        let symbol = ts.isIdentifier(tag) && checker.getSymbolAtLocation(tag);

        if (symbol && symbol.flags & ts.SymbolFlags.Alias) symbol = checker.getAliasedSymbol(symbol);

        const own = symbol?.getDeclarations()?.filter((one) => !/[\\/]node_modules[\\/]/.test(one.getSourceFile().fileName)) ?? [];

        if (!own.some((one) => calledProp(one, attribute.name.getText()))) return 0;

        const type = checker.getContextualType(fn);
        const signatures = type ? checker.getNonNullableType(type).getCallSignatures() : [];

        return Math.max(0, ...signatures.map((one) => (one.getDeclaration()?.parameters?.some((param) => param.dotDotDotToken) ? Infinity : one.getParameters().length)));
    };

    // Whether React renders this `null`: a child of the markup, or what a
    // component hands back, where null and undefined are one empty node, and
    // Python's None says it.
    const rendered = (node) => {
        let at = node;

        while (ts.isParenthesizedExpression(at.parent) || (ts.isConditionalExpression(at.parent) && at.parent.condition !== at)) at = at.parent;
        if (ts.isJsxExpression(at.parent)) return !ts.isJsxAttribute(at.parent.parent);
        if (ts.isReturnStatement(at.parent)) {
            const fn = ts.findAncestor(at.parent, ts.isFunctionLike);

            return Boolean(fn) && isComponent(fn);
        }
        return ts.isArrowFunction(at.parent) && at.parent.body === at && isComponent(at.parent);
    };

    // Whether Reacthon copied a value into Python's dicts and lists: a
    // component's props, and what is read off them, an item of a list of them.
    const copied = (node) => {
        let one = unwrap(node);

        while (ts.isPropertyAccessExpression(one) || ts.isElementAccessExpression(one)) one = unwrap(one.expression);
        if (ts.isCallExpression(one) && ts.isPropertyAccessExpression(one.expression) && ['filter', 'slice', 'find', 'at'].includes(one.expression.name.text)) {
            return copied(one.expression.expression);
        }
        if (!ts.isIdentifier(one)) return false;

        let holder = checker.getSymbolAtLocation(one)?.valueDeclaration;

        while (holder && (ts.isBindingElement(holder) || ts.isObjectBindingPattern(holder) || ts.isArrayBindingPattern(holder))) holder = holder.parent;
        if (holder && ts.isVariableDeclaration(holder)) return Boolean(holder.initializer) && copied(holder.initializer);
        if (!holder || !ts.isParameter(holder)) return false;

        const fn = holder.parent;
        const call = fn.parent;

        if (isComponent(fn)) return fn.parameters[0] === holder;
        return ts.isCallExpression(call) && call.arguments.includes(fn) && ts.isPropertyAccessExpression(call.expression) && copied(call.expression.expression);
    };

    const typeOf = (node) => checker.getTypeAtLocation(node);
    // What TypeScript does not type, read from plain data, is plain data too:
    // Brython hands it over whole.
    const isDict = (node) => {
        const type = checker.getNonNullableType(typeOf(node));
        const one = unwrap(node);

        if (type.flags & (ts.TypeFlags.Any | ts.TypeFlags.Unknown)) {
            return (ts.isPropertyAccessExpression(one) || ts.isElementAccessExpression(one)) && isDict(one.expression);
        }
        return plain(type) && (!packaged(type) || copied(node));
    };
    const nullable = (node) => {
        const type = typeOf(node);

        return Boolean(type.flags & (ts.TypeFlags.Any | ts.TypeFlags.Unknown)) || (type.isUnion() && type.types.some((one) => one.flags & (ts.TypeFlags.Null | ts.TypeFlags.Undefined | ts.TypeFlags.Void)));
    };
    const sized = (node) => {
        const type = checker.getNonNullableType(typeOf(node));

        return checker.isArrayType(type) || checker.isTupleType(type) || Boolean(type.flags & ts.TypeFlags.StringLike);
    };
    const numeric = (node) => Boolean(checker.getNonNullableType(typeOf(node)).flags & ts.TypeFlags.NumberLike);
    const boolean = (node) => Boolean(checker.getNonNullableType(typeOf(node)).flags & ts.TypeFlags.BooleanLike);
    // An element of the page, which Brython hands over as its DOMNode.
    const domElement = (node) => {
        const symbol = checker.getNonNullableType(typeOf(node)).getSymbol();

        return Boolean(symbol && /Element$/.test(symbol.name) && symbol.getDeclarations()?.some(fromLibrary));
    };
    const optional = (object, name) => {
        const property = checker.getPropertyOfType(checker.getNonNullableType(typeOf(object)), name);

        return !property || Boolean(property.flags & ts.SymbolFlags.Optional);
    };
    // The default a component gives a prop it destructures, `isActive = false`:
    // JavaScript applies it to a prop handed as undefined, Python not to one
    // handed None.
    const propDefault = (tag, prop, cx) => {
        let symbol = checker.getSymbolAtLocation(tag);

        if (symbol && symbol.flags & ts.SymbolFlags.Alias) symbol = checker.getAliasedSymbol(symbol);

        const declaration = symbol?.valueDeclaration;
        const pattern = declaration && ts.isFunctionDeclaration(declaration) ? declaration.parameters[0]?.name : undefined;
        const one = pattern && ts.isObjectBindingPattern(pattern) ? pattern.elements.find((element) => (element.propertyName ?? element.name).getText() === prop) : undefined;

        return one?.initializer && constant(one.initializer) ? expr(one.initializer, cx) : null;
    };

    // --- Names ---------------------------------------------------------------

    const reactName = (callee) => {
        if (ts.isPropertyAccessExpression(callee) && ts.isIdentifier(callee.expression) && callee.expression.text === reactNamespace) return callee.name.text;
        if (ts.isIdentifier(callee) && react.has(callee.text)) return react.get(callee.text);
        return null;
    };

    // `memo(function Row(...) {...})`, React's memo of one component: that
    // function, which Python writes as a def under `@memo`.
    const memoized = (value) => {
        const made = value && unwrap(value);

        if (!made || !ts.isCallExpression(made) || reactName(made.expression) !== 'memo' || made.arguments.length !== 1 || !isFunction(made.arguments[0])) return null;
        hooks.add('memo');
        return unwrap(made.arguments[0]);
    };

    const name = (node, cx) => {
        const text = node.text;

        if (cx.aliases?.has(text)) return cx.aliases.get(text);
        if (text === 'undefined') return 'None';
        if (cx.scope.has(text)) {
            used.add(text);
            return snake(text);
        }
        if (GLOBALS[text]) {
            need(...GLOBALS[text]);
            return GLOBALS[text][1];
        }
        if (ON_WINDOW.has(text)) {
            need('browser', 'window');
            return `window.${text}`;
        }
        // Any other global of the browser's, `URL` or `Blob`: the window's.
        if (checker.getSymbolAtLocation(node)?.getDeclarations()?.some((one) => /[\\/]lib\.dom\.d\.ts$/.test(one.getSourceFile().fileName))) {
            need('browser', 'window');
            return `window.${text}`;
        }
        used.add(text);
        return text;
    };

    const isVariantCall = (node) => ts.isCallExpression(node) && ts.isIdentifier(node.expression) && variantMakers.has(node.expression.text);

    // --- Expressions -----------------------------------------------------------

    // An expression and how tightly it binds.
    const emit = (node, cx) => {
        if (!cx.inChain && node.flags & ts.NodeFlags.OptionalChain && (ts.isPropertyAccessExpression(node) || ts.isElementAccessExpression(node) || ts.isCallExpression(node))) {
            const [whole, guards] = chain(node, cx);

            return guards.length ? [`${whole} if ${guards.join(' and ')} else None`, CONDITIONAL] : [whole, PRIMARY];
        }

        const inner = { ...cx, inChain: false };

        switch (node.kind) {
            case k.StringLiteral:
            case k.NoSubstitutionTemplateLiteral:
                return [string(node.text), PRIMARY];
            case k.NumericLiteral:
                return [node.text, PRIMARY];
            case k.TrueKeyword:
                return ['True', PRIMARY];
            case k.FalseKeyword:
                return ['False', PRIMARY];
            // null is javascript.NULL, undefined None, as Bryntime hands them.
            case k.NullKeyword:
                if (rendered(node)) return ['None', PRIMARY];
                need('javascript', 'NULL');
                return ['NULL', PRIMARY];
            case k.Identifier:
                return [name(node, cx), PRIMARY];
            case k.ParenthesizedExpression:
            case k.AsExpression:
            case k.NonNullExpression:
            case k.SatisfiesExpression:
            case k.TypeAssertionExpression:
                return emit(node.expression, cx);
            case k.PropertyAccessExpression:
                return property(node, cx, 'read');
            case k.ElementAccessExpression:
                return element(node, cx, 'read');
            case k.CallExpression:
                return call(node, cx);
            case k.NewExpression:
                return construct(node, inner);
            case k.PrefixUnaryExpression:
                return prefix(node, inner);
            case k.BinaryExpression:
                return binary(node, inner);
            case k.ConditionalExpression:
                return [
                    `${expr(node.whenTrue, inner, OR)} if ${expr(node.condition, inner, OR)} else ${expr(node.whenFalse, inner, CONDITIONAL)}`,
                    CONDITIONAL
                ];
            case k.TemplateExpression: {
                // The text escaped, the fields as they are, which Python 3.12
                // lets hold quotes of their own.
                const text = (one) =>
                    one
                        .replace(/\\/g, '\\\\')
                        .replace(/"/g, '\\"')
                        .replace(/\n/g, '\\n')
                        .replace(/\r/g, '\\r')
                        .replace(/\t/g, '\\t')
                        .replace(/\{/g, '{{')
                        .replace(/\}/g, '}}');
                let out = text(node.head.text);

                // A boolean as JavaScript writes it: `true`, not `True`.
                for (const span of node.templateSpans) {
                    const value = boolean(span.expression) ? `str(${expr(span.expression, inner)}).lower()` : expr(span.expression, inner);

                    out += `{${value.startsWith('{') ? ` ${value} ` : value}}${text(span.literal.text)}`;
                }
                return [`f"${out}"`, PRIMARY];
            }
            case k.TaggedTemplateExpression: {
                const raw = node.template.rawText;

                if (node.tag.getText() !== 'String.raw' || !ts.isNoSubstitutionTemplateLiteral(node.template)) unsupported(node, 'a tagged template');
                if (raw.includes('"') || raw.endsWith('\\')) unsupported(node, 'a raw string Python cannot write');
                return [`r"${raw}"`, PRIMARY];
            }
            case k.ObjectLiteralExpression:
                // In a t-string's field, Brython's tokenizer refuses a dict
                // of a name on one line, `{ {"a": x} }`: one entry a line.
                if (cx.inField && node.properties.some((one) => !ts.isPropertyAssignment(one) || !constant(one.initializer))) {
                    const lines = node.properties.map((one) => `${pad(cx.level + 1)}${entry(one, { ...inner, level: cx.level + 1 })},`);

                    return [`{\n${lines.join('\n')}\n${pad(cx.level)}}`, PRIMARY];
                }
                return [`{${node.properties.map((one) => entry(one, inner)).join(', ')}}`, PRIMARY];
            case k.ArrayLiteralExpression:
                return array(node, inner);
            case k.ArrowFunction:
            case k.FunctionExpression:
                return [callable(node, inner, 'callback'), PRIMARY];
            case k.JsxElement:
            case k.JsxSelfClosingElement:
            case k.JsxFragment:
                return [nested(node, inner), PRIMARY];
            default:
                return unsupported(node, ts.SyntaxKind[node.kind]);
        }
    };

    const expr = (node, cx, need_ = WHOLE) => {
        const [text, level] = emit(node, cx);

        return level < need_ ? `(${text})` : text;
    };

    // `a?.b.c`: the chain written whole, and what it reads guarded first,
    // where TypeScript says it can be missing.
    const chain = (node, cx) => {
        const guards = [];

        for (let link = node; link && link.flags & ts.NodeFlags.OptionalChain; link = link.expression) {
            // A dict's `.get()` can hand back None where TypeScript's index says not.
            const read = unwrap(link.expression);
            const missing = nullable(link.expression) || (ts.isElementAccessExpression(read) && isDict(read.expression));

            if (link.questionDotToken && missing) guards.unshift(expr(link.expression, { ...cx, inChain: true }, AND + 1));
            if (!(ts.isPropertyAccessExpression(link) || ts.isElementAccessExpression(link) || ts.isCallExpression(link) || ts.isNonNullExpression(link))) break;
        }

        return [expr(node, { ...cx, inChain: true }, OR), guards];
    };

    const property = (node, cx, role) => {
        const object = node.expression;
        const field = node.name.text;

        if (ts.isIdentifier(object) && object.text === reactNamespace) {
            if (!REACT_VALUES.has(field)) unsupported(node, "React's own API");
            return [reactValue(field), PRIMARY];
        }
        if (field === 'length' && role === 'read' && sized(object)) return [`len(${expr(object, { ...cx, inChain: cx.inChain }, WHOLE)})`, PRIMARY];

        const base = expr(object, { ...cx, fallback: null }, PRIMARY);

        if (!imported.has(object.getText()) && isDict(object)) {
            if (role !== 'read' || !optional(object, field)) return [`${base}[${string(field)}]`, PRIMARY];
            return [`${base}.get(${string(field)}${cx.fallback ? `, ${cx.fallback}` : ''})`, PRIMARY];
        }
        // What a JavaScript object may not have, read as None where it has not.
        if (role === 'read' && optional(object, field) && packaged(checker.getNonNullableType(typeOf(object)))) {
            return [`getattr(${base}, ${string(field)}, ${cx.fallback ?? 'None'})`, PRIMARY];
        }
        // `range.from`, an attribute Python's syntax cannot name.
        if (KEYWORDS.has(field)) {
            if (role === 'write') unsupported(node, 'a write to an attribute named as a Python keyword');
            return [`getattr(${base}, ${string(field)})`, PRIMARY];
        }
        return [`${base}.${field}`, PRIMARY];
    };

    const element = (node, cx, role) => {
        const object = node.expression;
        const base = expr(object, cx, PRIMARY);
        const index = expr(node.argumentExpression, { ...cx, inChain: false });

        if (role === 'read' && isDict(object)) return [`${base}.get(${index})`, PRIMARY];
        return [`${base}[${index}]`, PRIMARY];
    };

    // A key of a dict: a name or a string its str, a number JavaScript's text of
    // it, and a computed one, `[tab]`, its value.
    const key = (one, cx) => {
        if (ts.isIdentifier(one) || ts.isStringLiteral(one)) return string(one.text);
        if (ts.isNumericLiteral(one)) return string(String(Number(one.text)));
        if (ts.isComputedPropertyName(one) && cx) return expr(one.expression, cx);
        return unsupported(one, 'a computed key');
    };

    const owner = (dict) => {
        const id = dict.properties.find((one) => ts.isPropertyAssignment(one) && one.name.getText() === 'id' && ts.isStringLiteral(one.initializer));
        const call = ts.isCallExpression(dict.parent) ? dict.parent : null;
        const before = call && call.arguments.indexOf(dict) > 0 ? call.arguments[call.arguments.indexOf(dict) - 1] : null;
        const text = id ? id.initializer.text : before && ts.isStringLiteral(before) ? before.text : '';

        return /^[a-z]\w*$/i.test(text) ? `${spell(text)}_` : '';
    };

    const entry = (one, cx) => {
        if (ts.isShorthandPropertyAssignment(one)) return `${string(one.name.text)}: ${name(one.name, cx)}`;
        if (ts.isPropertyAssignment(one)) {
            // A function of a dict is named after its key: `Root`, a component
            // a library renders with; and after what the dict is of where a
            // string names it, its `id` or the argument before it, a table's
            // column: `target_cell`.
            const named = ts.isIdentifier(one.name) ? (/^[a-z]/.test(one.name.text) ? owner(one.parent) : '') + one.name.text : null;
            const at = isFunction(one.initializer) && named ? { ...cx, hoistAs: named } : cx;

            return `${key(one.name, cx)}: ${expr(one.initializer, at)}`;
        }
        if (ts.isSpreadAssignment(one)) return `**${spreadable(one.expression, cx)}`;
        // `onReorder(e) { … }`, a method of the dict: a def named after its key.
        if (ts.isMethodDeclaration(one) && ts.isIdentifier(one.name)) {
            return `${key(one.name)}: ${callable(one, { ...cx, hoistAs: snake(one.name.text) }, snake(one.name.text), true)}`;
        }
        return unsupported(one, 'an object member');
    };

    // What `...x` spreads: nothing where x is missing, as JavaScript's does.
    const spreadable = (node, cx) => (nullable(node) ? `(${expr(node, cx, OR)} or {})` : expr(node, cx, PRIMARY));

    const array = (node, cx) => {
        const items = node.elements;

        // `[...iterable]`, a list of what it holds.
        if (items.length === 1 && ts.isSpreadElement(items[0])) return [`list(${expr(items[0].expression, cx)})`, PRIMARY];
        return [`[${items.map((one) => (ts.isSpreadElement(one) ? `*${expr(one.expression, cx, PRIMARY)}` : expr(one, cx))).join(', ')}]`, PRIMARY];
    };

    const prefix = (node, cx) => {
        const operand = unwrap(node.operand);

        if (node.operator === k.ExclamationToken) {
            // `!x.length`: an empty list or text is false in Python.
            if ((ts.isPropertyAccessExpression(operand) && operand.name.text === 'length' && sized(operand.expression))) {
                return [`not ${expr(operand.expression, { ...cx, inChain: true }, NOT)}`, NOT];
            }
            if (ts.isPrefixUnaryExpression(operand) && operand.operator === k.ExclamationToken) return [`bool(${expr(operand.operand, cx)})`, PRIMARY];
            return [`not ${expr(node.operand, cx, NOT)}`, NOT];
        }
        if (node.operator === k.MinusToken) return [`-${expr(node.operand, cx, UNARY)}`, UNARY];
        return unsupported(node, 'an operator');
    };

    const binary = (node, cx) => {
        const operator = node.operatorToken.kind;
        const left = unwrap(node.left);
        const right = unwrap(node.right);

        if (ASSIGNMENTS[operator]) unsupported(node, 'an assignment inside an expression');

        // `a ?? b ?? c` of what reading twice changes nothing: past None and
        // NULL both, JavaScript's undefined and null.
        if (operator === k.QuestionQuestionToken) {
            need('javascript', 'NULL');
            const operands = [];

            for (let one = node; ts.isBinaryExpression(unwrap(one)) && unwrap(one).operatorToken.kind === k.QuestionQuestionToken; one = unwrap(one).left) {
                operands.unshift(unwrap(one).right);
                if (!(ts.isBinaryExpression(unwrap(unwrap(one).left)) && unwrap(unwrap(one).left).operatorToken.kind === k.QuestionQuestionToken)) operands.unshift(unwrap(one).left);
            }
            // `Array.from(value)[0] ?? "90d"`: what it reads once, a name the
            // line before the statement binds, where no function stands between.
            if (!operands.slice(0, -1).every(pure)) {
                let inside = false;

                for (let up = node.parent; up && up !== cx.statement; up = up.parent) inside ||= ts.isFunctionLike(up);
                if (operands.length !== 2 || !cx.hoists || inside) unsupported(node, 'a ?? of an expression');

                const [left, right] = operands;
                const local = fresh(ts.isElementAccessExpression(unwrap(left)) && unwrap(left).argumentExpression.getText() === '0' ? 'first' : 'value', cx);

                cx.hoists.push(Object.assign([`${pad(cx.statementLevel)}${local} = ${expr(left, cx)}`], { tight: true }));
                return [`${local} if ${local} not in (None, NULL) else ${expr(right, cx, CONDITIONAL)}`, CONDITIONAL];
            }

            const text = operands
                .slice(0, -1)
                .reduceRight(
                    (rest, one) => `${expr(one, cx, OR)} if ${expr(one, cx, COMPARE + 1)} not in (None, NULL) else ${rest}`,
                    expr(operands.at(-1), cx, CONDITIONAL)
                );

            return [text, CONDITIONAL];
        }

        const equality = [k.EqualsEqualsEqualsToken, k.ExclamationEqualsEqualsToken, k.EqualsEqualsToken, k.ExclamationEqualsToken].includes(operator);
        const negated = operator === k.ExclamationEqualsEqualsToken || operator === k.ExclamationEqualsToken;
        const loose = operator === k.EqualsEqualsToken || operator === k.ExclamationEqualsToken;

        if (equality) {
            // `typeof x === "string"`, Python's own tests.
            const [test, other] = ts.isTypeOfExpression(left) ? [left, right] : ts.isTypeOfExpression(right) ? [right, left] : [];

            if (test && ts.isStringLiteral(other)) {
                const value = expr(test.expression, cx, PRIMARY);
                const word = other.text === 'function' ? `callable(${value})` : other.text === 'undefined' ? null : TYPEOF[other.text] ? `isinstance(${expr(test.expression, cx)}, ${TYPEOF[other.text]})` : unsupported(node, 'a typeof');

                if (word === null) return [`${expr(test.expression, cx, COMPARE + 1)} is ${negated ? 'not ' : ''}None`, COMPARE];
                return negated ? [`not ${word}`, NOT] : [word, PRIMARY];
            }

            // null is javascript.NULL, undefined None.
            const [nil, value] = right.kind === k.NullKeyword ? [right, left] : left.kind === k.NullKeyword ? [left, right] : ts.isIdentifier(right) && right.text === 'undefined' ? [right, left] : ts.isIdentifier(left) && left.text === 'undefined' ? [left, right] : [];

            if (nil) {
                const subject = expr(value, cx, COMPARE + 1);

                if (loose) {
                    need('javascript', 'NULL');
                    return [`${subject} ${negated ? 'not in' : 'in'} (None, NULL)`, COMPARE];
                }
                if (nil.kind === k.NullKeyword) need('javascript', 'NULL');
                return [`${subject} is ${negated ? 'not ' : ''}${nil.kind === k.NullKeyword ? 'NULL' : 'None'}`, COMPARE];
            }
        }

        const [word, level] = BINARY[operator] ?? unsupported(node, 'an operator');

        return [`${expr(node.left, cx, level === COMPARE ? level + 1 : level)} ${word} ${expr(node.right, cx, level + 1)}`, level];
    };

    // A name, or a member of one, which reading twice changes nothing.
    const pure = (node) => {
        const one = unwrap(node);

        if (ts.isIdentifier(one)) return true;
        if (ts.isPropertyAccessExpression(one)) return pure(one.expression);
        if (ts.isElementAccessExpression(one)) return pure(one.expression) && (ts.isIdentifier(unwrap(one.argumentExpression)) || ts.isLiteralExpression(unwrap(one.argumentExpression)));
        return false;
    };

    const construct = (node, cx) => {
        const callee = node.expression.getText();

        if (callee === 'Map' && node.arguments?.length === 1) {
            // `new Map(xs.map((x) => [key, value]))`, a dict of them.
            const pairs = unwrap(node.arguments[0]);

            if (ts.isCallExpression(pairs) && ts.isPropertyAccessExpression(pairs.expression) && pairs.expression.name.text === 'map') {
                const fn = unwrap(pairs.arguments[0]);
                const body = fn && ts.isArrowFunction(fn) && unwrap(fn.body);

                if (body && ts.isArrayLiteralExpression(body) && body.elements.length === 2) {
                    const loop = comprehension(pairs.expression.expression, fn, cx);

                    return [`{${expr(body.elements[0], loop.cx)}: ${expr(body.elements[1], loop.cx)} ${loop.text}}`, PRIMARY];
                }
            }
        }
        return [`${expr(node.expression, cx, PRIMARY)}.new(${(node.arguments ?? []).map((one) => expr(one, cx)).join(', ')})`, PRIMARY];
    };

    // `for x in xs`, or `for i, x in enumerate(xs)`, of a callback's own names.
    const comprehension = (iterable, fn, cx) => comprehensionOver(expr(iterable, cx, PRIMARY), fn, cx);

    const comprehensionOver = (source, fn, cx) => {
        const scope = new Set(cx.scope);
        const aliases = new Map(cx.aliases);
        const targets = fn.parameters.map((one) => (ts.isObjectBindingPattern(one.name) ? item(one, scope, aliases) : target(one.name, scope)));
        const each = targets[0]?.includes(',') ? `(${targets[0]})` : targets[0];
        const text = targets.length > 1 ? `for ${targets[1]}, ${each} in enumerate(${source})` : `for ${targets[0] ?? '_'} in ${source}`;

        return { text, cx: { ...cx, scope, aliases, inChain: false } };
    };

    // `({ id }) => id`: the item, each name it destructures read off it where
    // it is named.
    const item = (parameter, scope, aliases) => {
        let local = 'item';

        for (let n = 2; scope.has(local); n += 1) local = `item_${n}`;
        scope.add(local);
        for (const one of parameter.name.elements) {
            if (one.dotDotDotToken || one.initializer || !ts.isIdentifier(one.name)) unsupported(one, 'a destructured item');

            const prop = (one.propertyName ?? one.name).getText();

            aliases.set(one.name.text, isDict(parameter) ? `${local}[${string(prop)}]` : `${local}.${prop}`);
        }
        return local;
    };

    // A name, or the names a list is unpacked into: its first ones, the rest
    // left as JavaScript leaves it, unless it is a tuple of as many.
    const target = (binding, scope) => {
        if (ts.isIdentifier(binding)) {
            scope.add(binding.text);
            return snake(binding.text);
        }
        if (ts.isArrayBindingPattern(binding)) {
            const names = binding.elements.map((one) => (ts.isOmittedExpression(one) ? '_' : `${one.dotDotDotToken ? '*' : ''}${target(one.name, scope)}`));
            const unpacked = checker.getTypeAtLocation(binding);
            const exact = checker.isTupleType(unpacked) && checker.getTypeArguments(unpacked).length === names.length;

            if (!exact && !binding.elements.some((one) => !ts.isOmittedExpression(one) && one.dotDotDotToken)) names.push('*_');
            return names.join(', ');
        }
        return unsupported(binding, 'a destructured parameter');
    };

    const call = (node, cx) => {
        const callee = unwrap(node.expression);
        const args = node.arguments;
        const inner = { ...cx, inChain: false };
        const hook = reactName(callee);

        if (hook) {
            if (!HOOKS[hook]) unsupported(node, "React's own API");
            hooks.add(HOOKS[hook]);
            return [`${HOOKS[hook]}(${hookArguments(hook, args, inner).join(', ')})`, PRIMARY];
        }

        if (isVariantCall(node) && args.length === 1 && ts.isObjectLiteralExpression(args[0])) {
            // A variant named as a Python keyword, `in`, handed in a dict.
            const keyword = (key, value) => (KEYWORDS.has(key) ? `**{${string(key)}: ${value}}` : `${key}=${value}`);
            const keywords = args[0].properties.map((one) => {
                if (ts.isShorthandPropertyAssignment(one)) return keyword(one.name.text, name(one.name, inner));
                if (ts.isPropertyAssignment(one) && ts.isIdentifier(one.name)) return keyword(one.name.text, expr(one.initializer, inner));
                // React Aria's render props, `{ ...renderProps, showWeekNumber }`:
                // keywords take a dict, not the object JavaScript made.
                if (ts.isSpreadAssignment(one)) {
                    const made = inPackage(checker.getNonNullableType(typeOf(one.expression))) && !copied(one.expression);

                    return made ? `**dict(${expr(one.expression, inner)})` : `**${expr(one.expression, inner, PRIMARY)}`;
                }
                return unsupported(one, 'a variant');
            });

            return [`${expr(callee, cx, PRIMARY)}(${keywords.join(', ')})`, PRIMARY];
        }

        if (ts.isIdentifier(callee) && callee.text === 'cva') {
            const parts = [expr(args[0], inner), ...cvaFields(args[1]).map((one) => (one ? expr(one, inner) : 'None'))];

            while (parts.at(-1) === 'None') parts.pop();
            return [`cva(${parts.join(', ')})`, PRIMARY];
        }

        const text = callee.getText();

        if (text === 'Array.isArray') return [`isinstance(${expr(args[0], inner)}, list)`, PRIMARY];
        if (text === 'String') return [`str(${expr(args[0], inner)})`, PRIMARY];
        if (text === 'Number' && args.length === 1) return [`float(${expr(args[0], inner)})`, PRIMARY];
        if (text === 'Array.from' && args.length === 1 && !ts.isObjectLiteralExpression(unwrap(args[0]))) return [`list(${expr(args[0], inner)})`, PRIMARY];
        if (text === 'Object.entries') return [`${expr(args[0], inner, PRIMARY)}.items()`, PRIMARY];
        if (text === 'Object.keys') return [`list(${expr(args[0], inner)})`, PRIMARY];
        if (text === 'Object.values') return [`list(${expr(args[0], inner, PRIMARY)}.values())`, PRIMARY];
        if (text === 'Object.fromEntries') return [`dict(${expr(args[0], inner)})`, PRIMARY];
        if (text === 'Array.from' && args.length === 2 && ts.isObjectLiteralExpression(unwrap(args[0]))) {
            // `Array.from({ length: n }, (_, i) => ...)`, a list over range(n).
            const length = unwrap(args[0]).properties.find((one) => one.name?.text === 'length');
            const fn = unwrap(args[1]);
            const scope = new Set(cx.scope);
            const index = fn.parameters[1] ? target(fn.parameters[1].name, scope) : '_';

            return [`[${expr(fn.body, { ...inner, scope })} for ${index} in range(${expr(length.initializer, inner)})]`, PRIMARY];
        }

        if (ts.isPropertyAccessExpression(callee)) {
            const method = callee.name.text;
            const object = callee.expression;

            if (method === 'map' && isFunction(args[0]) && sized(object)) return [mapped(object, unwrap(args[0]), inner), PRIMARY];
            if (method === 'filter' && isFunction(args[0])) return [filtered(object, unwrap(args[0]), inner), PRIMARY];

            const textual = Boolean(checker.getNonNullableType(typeOf(object)).flags & ts.TypeFlags.StringLike);
            const list = sized(object) && !textual;
            const own = expr(object, inner, PRIMARY);

            // A list's searches, as Python's builtins and a generator write
            // them, None or -1 where JavaScript's find nothing.
            if (list && ['find', 'findIndex', 'some', 'every'].includes(method) && isFunction(args[0])) {
                const fn = unwrap(args[0]);
                const scope = new Set(inner.scope);
                const item = fn.parameters[0] ? target(fn.parameters[0].name, scope) : '_';
                const each = item.includes(',') ? `(${item})` : item;
                const index = fn.parameters[1] ? target(fn.parameters[1].name, scope) : method === 'findIndex' ? (scope.has('at') ? 'index' : 'at') : null;
                const over = index ? `for ${index}, ${each} in enumerate(${expr(object, inner)})` : `for ${each} in ${expr(object, inner)}`;
                const test = expr(body(fn) ?? unsupported(fn, `a ${method} of statements`), { ...inner, scope }, OR);

                if (method === 'find') return [`next((${each} ${over} if ${test}), None)`, PRIMARY];
                if (method === 'findIndex') return [`next((${index} ${over} if ${test}), -1)`, PRIMARY];
                return [`${method === 'some' ? 'any' : 'all'}(${test} ${over})`, PRIMARY];
            }
            if (method === 'includes' && args.length === 1 && sized(object)) return [`${expr(args[0], inner, COMPARE + 1)} in ${expr(object, inner, COMPARE + 1)}`, COMPARE];
            // A list grows by append() or extend(), which hand back None where
            // push() hands back its length: a statement of its own.
            if (method === 'push' && list) {
                if (!ts.isExpressionStatement(node.parent)) unsupported(node, 'the length push() hands back');
                return [args.length === 1 ? `${own}.append(${expr(args[0], inner)})` : `${own}.extend([${args.map((one) => expr(one, inner)).join(', ')}])`, PRIMARY];
            }
            // A str's methods under Python's names: a pad of one character, a
            // replace() of a string its first occurrence alone, as JavaScript's.
            if (textual) {
                const pad = args[1] === undefined || (ts.isStringLiteral(args[1]) && [...args[1].text].length === 1);
                const plain = { trim: 'strip', trimStart: 'lstrip', trimEnd: 'rstrip', toLowerCase: 'lower', toUpperCase: 'upper' };

                if (plain[method] && args.length === 0) return [`${own}.${plain[method]}()`, PRIMARY];
                if (method === 'startsWith' && args.length <= 2) return [`${own}.startswith(${args.map((one) => expr(one, inner)).join(', ')})`, PRIMARY];
                if (method === 'endsWith' && args.length === 1) return [`${own}.endswith(${expr(args[0], inner)})`, PRIMARY];
                if ((method === 'padStart' || method === 'padEnd') && pad) {
                    return [`${own}.${method === 'padStart' ? 'rjust' : 'ljust'}(${args.map((one) => expr(one, inner)).join(', ')})`, PRIMARY];
                }
                if (method === 'repeat' && args.length === 1) return [`${expr(object, inner, MULTIPLY)} * ${expr(args[0], inner, MULTIPLY + 1)}`, MULTIPLY];
                if (method === 'replaceAll' && args.length === 2 && !ts.isRegularExpressionLiteral(args[0])) return [`${own}.replace(${expr(args[0], inner)}, ${expr(args[1], inner)})`, PRIMARY];
                if (method === 'replace' && args.length === 2 && !ts.isRegularExpressionLiteral(args[0]) && !isFunction(args[1])) {
                    return [`${own}.replace(${expr(args[0], inner)}, ${expr(args[1], inner)}, 1)`, PRIMARY];
                }
            }
            if (method === 'join' && sized(object)) return [`${expr(args[0] ?? ts.factory.createStringLiteral(','), inner, PRIMARY)}.join(${expr(object, inner)})`, PRIMARY];
            if (method === 'replace' && args.length === 2 && ts.isRegularExpressionLiteral(args[0]) && ts.isStringLiteral(args[1])) {
                const done = replaced(args[0], args[1].text);

                if (!done) unsupported(node, 'a regular expression');
                return done[0] === 'replace'
                    ? [`${expr(object, inner, PRIMARY)}.replace(${string(done[1])}, ${string(args[1].text)})`, PRIMARY]
                    : [`${expr(object, inner, PRIMARY)}.removesuffix(${string(done[1])})`, PRIMARY];
            }
            if (method === 'toLocaleString' && args.length === 0 && numeric(object)) return [`format(${expr(object, inner)}, ",")`, PRIMARY];
            if (method === 'toString' && args.length === 0) return [`str(${expr(object, inner)})`, PRIMARY];
            // A string's find() is -1 where it finds nothing, as indexOf is; a
            // list's index() raises.
            if (method === 'indexOf' && args.length === 1 && sized(object)) {
                const text = Boolean(checker.getNonNullableType(typeOf(object)).flags & ts.TypeFlags.StringLike);

                return [`${expr(object, inner, PRIMARY)}.${text ? 'find' : 'index'}(${expr(args[0], inner)})`, PRIMARY];
            }
            if (method === 'slice' && args.length <= 2 && sized(object)) {
                return [`${expr(object, inner, PRIMARY)}[${args.map((one) => expr(one, inner)).join(':')}${args.length < 2 ? ':' : ''}]`, PRIMARY];
            }
            // Brython's DOMNode.closest() raises KeyError where the DOM's is null.
            if (method === 'closest' && args.length === 1 && domElement(object)) {
                helper('closest');
                return [`closest(${expr(object, inner)}, ${expr(args[0], inner)})`, PRIMARY];
            }
            // Python's sort() takes a key, not a function that compares two
            // items, which JavaScript's hands both of them.
            if (method === 'sort' && args.length === 1 && isFunction(args[0]) && sized(object)) {
                helper('sort');
                return [`sort(${expr(object, inner)}, ${callable(unwrap(args[0]), { ...inner, arity: 2 }, 'compare')})`, PRIMARY];
            }
        }

        const callText = ts.isPropertyAccessExpression(callee) ? property(callee, cx, 'call')[0] : ts.isElementAccessExpression(callee) ? element(callee, cx, 'call')[0] : expr(callee, cx, PRIMARY);

        return [`${callText}(${args.map((one) => expr(one, inner)).join(', ')})`, PRIMARY];
    };

    // `xs.map(fn)`, a list comprehension: `xs.filter(f).map(g)`, one, on the
    // filtered items where the map counts them.
    const mapped = (object, fn, cx) => {
        const inner = unwrap(object);

        // `Array.from({ length: n }).map((_, i) => ...)`, over range(n).
        if (ts.isCallExpression(inner) && inner.expression.getText() === 'Array.from' && inner.arguments.length === 1 && ts.isObjectLiteralExpression(unwrap(inner.arguments[0]))) {
            const length = unwrap(inner.arguments[0]).properties.find((one) => one.name?.text === 'length');
            const scope = new Set(cx.scope);
            const index = fn.parameters[1] ? target(fn.parameters[1].name, scope) : '_';

            return `[${element_(fn, { ...cx, scope, inChain: false })} for ${index} in range(${expr(length.initializer, cx)})]`;
        }

        if (ts.isCallExpression(inner) && ts.isPropertyAccessExpression(inner.expression) && inner.expression.name.text === 'filter' && isFunction(inner.arguments[0])) {
            const filter = unwrap(inner.arguments[0]);
            const iterable = inner.expression.expression;
            // The same item, or the map's unpacking of it, of which the
            // filter's takes the first names.
            const names = (one) => (ts.isArrayBindingPattern(one.name) ? one.name.elements.map((item) => (ts.isOmittedExpression(item) ? null : item.name.getText())) : null);
            const kept = filter.parameters.length === 1 && names(filter.parameters[0]);
            const read = fn.parameters.length === 1 && names(fn.parameters[0]);
            const same =
                fn.parameters.length === 1 &&
                filter.parameters.length === 1 &&
                (filter.parameters[0].name.getText() === fn.parameters[0].name.getText() ||
                    (kept && read && kept.length <= read.length && kept.every((one, at) => one === null || one === read[at])));

            if (same) {
                const loop = comprehension(iterable, fn, cx);

                return `[${element_(fn, loop.cx)} ${loop.text} if ${expr(test(filter), loop.cx, OR)}]`;
            }

            const loop = comprehensionOver(filtered(iterable, filter, cx, true), fn, cx);

            return `[${element_(fn, loop.cx)} ${loop.text}]`;
        }

        const loop = comprehension(object, fn, cx);

        return `[${element_(fn, loop.cx)} ${loop.text}]`;
    };

    const test = (fn) => body(fn) ?? unsupported(fn, 'a filter of statements');

    // A filter of statements keeps the items its def `keep` keeps.
    const filtered = (iterable, fn, cx, generator = false) => {
        const loop = comprehension(iterable, fn, cx);
        const params = fn.parameters[0] ? target(fn.parameters[0].name, new Set()) : '_';
        const item = params.includes(',') ? `(${params})` : params;
        const kept = body(fn) ? expr(body(fn), loop.cx, OR) : `${callable(fn, { ...cx, hoistAs: 'keep' }, 'keep', true)}(${params})`;
        const text = `${item} ${loop.text} if ${kept}`;

        return generator ? text : `[${text}]`;
    };

    // What a callback hands back: its expression, or the call of the function
    // it becomes where its body has statements.
    const body = (fn) => {
        const one = fn.body;

        if (!ts.isBlock(one)) return one;
        if (one.statements.length === 1 && ts.isReturnStatement(one.statements[0]) && one.statements[0].expression) return one.statements[0].expression;
        return null;
    };

    // A callback of statements becomes `def render_item(item, index)`, called
    // with the loop's names: a pair `[key, value]` as two parameters.
    const element_ = (fn, cx) => {
        const value = body(fn);

        if (value && !holdsHandler(value, fn)) return expr(value, cx);

        const parameter = fn.parameters[0]?.name;
        // Named after the item, or the first name it is unpacked into.
        const first = parameter && ts.isArrayBindingPattern(parameter) ? parameter.elements.find((one) => !ts.isOmittedExpression(one))?.name : parameter;
        const outer = loopNames(fn, cx);
        const local = callable(fn, { ...cx, hoistAs: first && ts.isIdentifier(first) ? `render_${snake(first.text)}` : 'render', flatParams: true, extraParams: outer }, 'render', true);
        const args = fn.parameters.flatMap((one) =>
            ts.isArrayBindingPattern(one.name) ? one.name.elements.map((item) => (ts.isOmittedExpression(item) ? '_' : target(item.name, new Set()))) : [target(one.name, new Set())]
        );

        return `${local}(${[...args, ...outer].join(', ')})`;
    };

    // A function the item's element keeps for later, a handler or a render
    // prop, that reads the item: a Python closure reads a comprehension's names
    // when it is called, the last item's by then, so the element becomes a def,
    // whose call binds each item's own. A callback of a list's method is
    // called at once.
    const holdsHandler = (node, fn) => {
        const names = new Set();
        const bind = (binding) => (ts.isIdentifier(binding) ? names.add(binding.text) : binding.elements?.forEach((one) => !ts.isOmittedExpression(one) && bind(one.name)));
        const reads = (one) => (ts.isIdentifier(one) && names.has(one.text)) || Boolean(ts.forEachChild(one, reads));
        const immediate = (one) => ts.isCallExpression(one.parent) && ts.isPropertyAccessExpression(one.parent.expression) && CALLED_AT_ONCE.has(one.parent.expression.name.text);
        const handler = (one) => isFunction(one) && !immediate(one);
        const holds = (one) => (handler(one) && reads(one.body)) || Boolean(ts.forEachChild(one, holds));

        fn.parameters.forEach((one) => bind(one.name));
        return holds(node);
    };

    // The names of the loops around a callback that it reads: a def taken out of
    // them is handed them.
    const loopNames = (fn, cx) => {
        const bound = new Set();
        const names = (binding) => {
            if (ts.isIdentifier(binding)) bound.add(binding.text);
            else binding.elements?.forEach((one) => !ts.isOmittedExpression(one) && names(one.name));
        };

        for (let up = fn.parent; up && up !== cx.statement; up = up.parent) {
            if (ts.isArrowFunction(up) || ts.isFunctionExpression(up)) up.parameters.forEach((one) => names(one.name));
        }

        const read = new Set();
        const visit = (node) => {
            if (ts.isIdentifier(node) && bound.has(node.text)) read.add(node.text);
            ts.forEachChild(node, visit);
        };

        visit(fn.body);
        return [...read].map(snake);
    };

    const hookArguments = (hook, args, cx) => {
        const [first, ...rest] = args;
        const names = { useEffect: 'effect', useLayoutEffect: 'effect', useState: 'initial', useMemo: 'compute', useCallback: 'callback' };

        if (!first) return hook === 'useState' ? ['None'] : [];
        if (isFunction(first)) {
            const fn = unwrap(first);
            const lambda = hook !== 'useEffect' && hook !== 'useLayoutEffect' && body(fn);

            const effect = hook === 'useEffect' || hook === 'useLayoutEffect';

            return [lambda ? callable(fn, cx, names[hook]) : callable(fn, { ...cx, forceDef: true, effectBody: effect }, names[hook]), ...rest.map((one) => expr(one, cx))];
        }
        return args.map((one) => expr(one, cx));
    };

    const cvaFields = (options) => {
        if (options && !ts.isObjectLiteralExpression(options)) unsupported(options, "cva's options");
        return ['variants', 'defaultVariants', 'compoundVariants'].map((field) => options?.properties.find((one) => one.name?.text === field)?.initializer);
    };

    // A function as Python writes one where it stands: a lambda of an
    // expression, else a def of its own before the statement.
    const callable = (fn, cx, base, forceDef = false) => {
        // `() => {}`, which does nothing.
        if (ts.isBlock(fn.body) && fn.body.statements.length === 0 && !forceDef && !cx.forceDef) return 'lambda *args: None';

        const value = !cx.forceDef && !forceDef && body(fn);

        if (value && fn.parameters.every((one) => ts.isIdentifier(one.name))) {
            const scope = new Set(cx.scope);
            const params = fn.parameters.map((one) => target(one.name, scope));

            // The arguments a JavaScript function leaves unread.
            if (params.length < (cx.arity ?? pythonArity(fn))) params.push('*_');
            return `lambda${params.length ? ` ${params.join(', ')}` : ''}: ${expr(value, { ...cx, scope, arity: undefined }, LAMBDA)}`;
        }
        if (!cx.hoists) unsupported(fn, 'a function outside a function');
        if (cx.hoisted.has(fn)) return cx.hoisted.get(fn);
        if (!cx.extraParams && loopNames(fn, cx).length) unsupported(fn, "a function of statements reading a callback's names");

        const local = fresh(cx.hoistAs ?? base, cx);

        cx.hoisted.set(fn, local);
        cx.hoists.push(def(local, fn, { ...cx, level: cx.statementLevel }));
        return local;
    };

    const fresh = (base, cx) => {
        let local = base;

        for (let n = 2; cx.taken.has(local); n += 1) local = `${base}_${n}`;
        cx.taken.add(local);
        return local;
    };

    // --- JSX ------------------------------------------------------------------

    const tagName = (tag, cx) => {
        if (ts.isIdentifier(tag) && /^[a-z]/.test(tag.text) && !tag.text.includes('.')) return tag.text;
        // A fragment with a key, React's own component.
        if (tag.getText() === `${reactNamespace}.Fragment` || (ts.isIdentifier(tag) && react.get(tag.text) === 'Fragment')) return `{${reactValue('Fragment')}}`;
        if (ts.isIdentifier(tag) || ts.isPropertyAccessExpression(tag)) return `{${expr(tag, cx, PRIMARY)}}`;
        return unsupported(tag, 'a tag');
    };

    // A field of the t-string: a dict apart from its braces, which `{{` would
    // escape.
    const field = (node, cx) => {
        const value = expr(node, { ...cx, inField: true });

        // A lambda's colon would start the field's format: Python asks for
        // its parentheses.
        if (/^lambda\b/.test(value)) return `{(${value})}`;
        return value.startsWith('{') ? `{ ${value} }` : `{${value}}`;
    };

    const constant = (node) => {
        const one = unwrap(node);

        return ts.isStringLiteral(one) || ts.isNumericLiteral(one) || ts.isNoSubstitutionTemplateLiteral(one) || [k.TrueKeyword, k.FalseKeyword, k.NullKeyword].includes(one.kind);
    };

    // An attribute on its line at `level`: a call or a dict too long for it,
    // one argument or one entry a line.
    const attribute = (one, cx, level, flat) => {
        if (ts.isJsxSpreadAttribute(one)) return `...${field(one.expression, { ...cx, level })}`;

        const attr = DOM_NAMES[one.name.getText()] ?? one.name.getText();
        const value = one.initializer;
        const text = value && (ts.isStringLiteral(value) ? decoded(value.text) : value.expression && ts.isStringLiteral(value.expression) ? value.expression.text : null);

        if (value === undefined) return attr;
        if (text !== null && !text.includes('"')) return `${attr}="${braces(text)}"`;
        if (text !== null) return `${attr}={${string(text)}}`;
        if (value.expression === undefined) return unsupported(one, 'an empty attribute');

        const inner = unwrap(value.expression);
        const fallback = ts.isPropertyAccessExpression(inner) ? propDefault(one.parent.parent.tagName, one.name.getText(), cx) : null;
        // A function is named after its attribute as JSX spells it: className's
        // is class_name, `class` being Python's own.
        const named = snake(one.name.getText());
        const at = { ...cx, level, hoistAs: /^on[A-Z]/.test(attr) || isFunction(inner) ? named : cx.hoistAs, fallback };
        const line = `${attr}=${field(value.expression, at)}`;

        if (flat || line.includes('\n') || pad(level).length + line.length <= WIDTH) return line;
        // A lambda too long for its line, a def of its own; kept where it
        // reads a loop's names, which a def taken out of the loop would not see.
        if (isFunction(inner) && cx.hoists && !loopNames(inner, at).length) return `${attr}={${callable(inner, at, named, true)}}`;
        if (ts.isObjectLiteralExpression(inner)) return `${attr}={ ${pretty(inner, { ...at, inField: true }, level)} }`;

        const long = ts.isCallExpression(inner) && inner.arguments.filter((arg) => expr(arg, cx).length > 40).length > 1;

        if (!long) return line;

        const args = inner.arguments.map((arg) => `${pad(level + 1)}${expr(arg, { ...at, level: level + 1 })},`);

        return `${attr}={${expr(inner.expression, cx, PRIMARY)}(\n${args.join('\n')}\n${pad(level)})}`;
    };

    // The children, in runs a t-string can put on lines of their own: htm drops
    // a line break and the spaces around it as JSX does, so a run ends where a
    // text does not touch its neighbour.
    const runs = (list) => {
        const parts = [];

        for (const one of list) {
            if (ts.isJsxText(one)) {
                const text = jsxText(one.text);

                if (text) {
                    parts.push({
                        text: braces(text),
                        before: !/^[ \t]*[\r\n]/.test(one.text),
                        after: !/[\r\n][ \t]*$/.test(one.text),
                        space: [text.startsWith(' '), text.endsWith(' ')]
                    });
                }
            } else if (ts.isJsxExpression(one)) {
                if (one.expression) parts.push({ node: one.expression });
            } else {
                parts.push({ node: one, element: true });
            }
        }

        const grouped = [];

        parts.forEach((part, at) => {
            const previous = parts[at - 1];
            const tight = previous && ((previous.text !== undefined && previous.after) || (part.text !== undefined && part.before));

            if (tight) grouped.at(-1).push(part);
            else grouped.push([part]);
        });

        return grouped;
    };

    const run = (parts, cx, level, flat) =>
        parts
            .map((part) => {
                if (part.text !== undefined) return part.text;
                if (part.element) return markup(part.node, cx, level, flat || parts.length > 1);
                return field(part.node, { ...cx, level });
            })
            .join('');

    // An element whose first line stands at `level`; `flat` keeps it on one,
    // `spread` puts its attributes on lines of their own.
    const markup = (node, cx, level, flat = false, spread = false) => {
        if (ts.isJsxFragment(node)) {
            const lines = runs(node.children).map((parts) => run(parts, cx, level, flat));

            return lines.join(flat ? '' : `\n${pad(level)}`);
        }

        const opening = ts.isJsxElement(node) ? node.openingElement : node;
        const tag = tagName(opening.tagName, cx);
        let attributes = opening.attributes.properties.map((one) => attribute(one, cx, level + 1, flat));
        let head = [tag, ...attributes].join(' ');
        const long = pad(level).length + head.length > WIDTH;
        // A lone dict too long for the tag's line goes on its own, as Prettier puts it.
        const [lone] = opening.attributes.properties;
        const dict = attributes.length === 1 && ts.isJsxAttribute(lone) && lone.initializer?.expression && ts.isObjectLiteralExpression(unwrap(lone.initializer.expression));
        const split = !flat && (attributes.length > 1 ? spread || long || head.includes('\n') : dict && pad(level).length + head.length + 2 > WIDTH && !head.includes('\n'));

        // A lone attribute of several lines stays on the tag's own.
        if (!split && head.includes('\n')) {
            attributes = opening.attributes.properties.map((one) => attribute(one, cx, level, flat));
            head = [tag, ...attributes].join(' ');
        }
        const open = split ? `<${tag}\n${attributes.map((one) => `${pad(level + 1)}${one}`).join('\n')}\n${pad(level)}` : `<${head}`;

        if (ts.isJsxSelfClosingElement(node)) return split ? `${open}/>` : `${open} />`;

        const close = `</${tag}>`;
        const groups = runs(node.children);

        if (groups.length === 0) return `${open}>${close}`;

        const first = groups[0][0];
        const last = groups.at(-1).at(-1);
        const touching = first.space?.[0] || last.space?.[1];
        const inline = `${open}>${groups.map((parts) => run(parts, cx, level, true)).join('')}${close}`;

        if (flat || touching) return inline;
        if (!split && groups.length === 1 && !groups[0].some((part) => part.element) && !inline.includes('\n') && pad(level).length + inline.length <= WIDTH) {
            return inline;
        }

        const lines = groups.map((parts) => `${pad(level + 1)}${run(parts, cx, level + 1, false)}`);

        return `${open}>\n${lines.join('\n')}\n${pad(level)}${close}`;
    };

    const hasElementChildren = (node) =>
        (ts.isJsxElement(node) || ts.isJsxFragment(node)) && node.children.some((one) => !ts.isJsxText(one) && !ts.isJsxExpression(one));

    // A JSX tree as a t-string, at `column` of a line at `cx.level`: there if it
    // fits on that line, else its markup on lines of its own.
    const tstring = (tree, cx, column) => {
        const node = unwrap(tree);
        const level = cx.level;
        const flat = markup(node, cx, 0, true);
        const fits = !flat.includes('\n') && !hasElementChildren(node) && column + flat.length + 3 <= WIDTH;

        if (fits) {
            const quote = quotes(flat, false, cx.quote);

            return `t${quote}${flat}${quote}`;
        }

        // An element of no other element that its line could not hold: one
        // attribute a line.
        const spread = !hasElementChildren(node);
        const quote = quotes(markup(node, { ...cx, quote: '"' }, level + 1, false, spread), true, cx.quote);
        const text = markup(node, { ...cx, quote: quote[0] }, level + 1, false, spread);

        return `t${quote}\n${pad(level + 1)}${text}\n${pad(level)}${quote}`;
    };

    // JSX inside an expression: a t-string where it stands if it holds on one
    // line, else a local of its own before the statement, where building it
    // early can fail on nothing.
    const nested = (node, cx) => {
        if (cx.hoisted?.has(node)) return cx.hoisted.get(node);

        const inline = tstring(node, { ...cx, keepJsx: true }, pad(cx.level).length + 20);

        if (cx.hoists && !cx.keepJsx && inline.includes('\n') && safe(node, cx)) {
            const tag = ts.isJsxFragment(node) ? 'fragment' : (ts.isJsxElement(node) ? node.openingElement : node).tagName.getText().split('.').at(-1);
            const local = fresh(snake(tag[0].toLowerCase() + tag.slice(1)), cx);
            const text = tstring(node, { ...cx, keepJsx: true, quote: null, inField: false, level: cx.statementLevel }, pad(cx.statementLevel).length + local.length + 3);

            cx.hoisted.set(node, local);
            cx.hoists.push([`${pad(cx.statementLevel)}${local} = ${text}`]);
            return local;
        }

        return inline;
    };

    const safe = (node, cx) => {
        for (let up = node.parent; up && up !== cx.statement; up = up.parent) {
            if (ts.isArrowFunction(up) || ts.isFunctionExpression(up)) return false;
        }

        const ok = (one) => {
            if (ts.isJsxText(one) || ts.isStringLiteral(one) || ts.isNumericLiteral(one)) return true;
            if (one.kind === k.TrueKeyword || one.kind === k.FalseKeyword || one.kind === k.NullKeyword) return true;
            if (ts.isIdentifier(one)) return true;
            if (ts.isPropertyAccessExpression(one)) return ts.isIdentifier(one.expression) && imported.has(one.expression.text);
            if (ts.isCallExpression(one)) {
                return ts.isIdentifier(one.expression) && (one.expression.text === 'cn' || variantMakers.has(one.expression.text)) && one.arguments.every(ok);
            }
            if (ts.isJsxElement(one) || ts.isJsxSelfClosingElement(one) || ts.isJsxFragment(one) || ts.isJsxOpeningElement(one)) {
                return ts.forEachChild(one, (child) => (ts.isJsxClosingElement(child) || ok(child) ? undefined : true)) === undefined;
            }
            if (ts.isJsxAttributes(one) || ts.isJsxAttribute(one) || ts.isJsxExpression(one) || ts.isJsxSpreadAttribute(one) || ts.isParenthesizedExpression(one) || ts.isBinaryExpression(one) || ts.isConditionalExpression(one) || ts.isTemplateExpression(one) || ts.isTemplateSpan(one) || ts.isObjectLiteralExpression(one) || ts.isPropertyAssignment(one) || ts.isShorthandPropertyAssignment(one) || ts.isPrefixUnaryExpression(one)) {
                return ts.forEachChild(one, (child) => (ok(child) ? undefined : true)) === undefined;
            }
            return one.kind === k.TemplateHead || one.kind === k.TemplateMiddle || one.kind === k.TemplateTail || ts.isToken(one);
        };

        return ok(node);
    };

    // --- Layout of long expressions ----------------------------------------

    // A dict or a list too long for its line, one entry a line; a call, one
    // argument a line.
    const pretty = (node, cx, level, column = level * 4) => {
        const flat = expr(node, cx);
        const indent = pad(level + 1);
        const one = unwrap(node);
        const at = { ...cx, level: level + 1 };

        if (!flat.includes('\n') && flat.length + column <= WIDTH - 4) return flat;
        if (ts.isObjectLiteralExpression(one)) {
            const lines = one.properties.map((member) => {
                if (ts.isPropertyAssignment(member)) return `${indent}${key(member.name, at)}: ${pretty(member.initializer, at, level + 1, (level + 1) * 4 + key(member.name, at).length + 2)},`;
                return `${indent}${entry(member, at)},`;
            });

            return `{\n${lines.join('\n')}\n${pad(level)}}`;
        }
        if (ts.isArrayLiteralExpression(one)) {
            return `[\n${one.elements.map((item) => `${indent}${pretty(item, at, level + 1)},`).join('\n')}\n${pad(level)}]`;
        }
        if (ts.isCallExpression(one) && !flat.endsWith(']') && one.arguments.length) {
            const head = flat.slice(0, flat.indexOf('('));
            const hook = reactName(unwrap(one.expression));
            const args = hook ? hookArguments(hook, one.arguments, at) : null;
            const texts = args ?? one.arguments.map((arg) => pretty(arg, at, level + 1));

            if (head && !head.includes(' ')) {
                return `${head}(\n${texts.map((text, at_) => `${indent}${args ? prettyText(one.arguments[at_], text, at, level + 1) : text},`).join('\n')}\n${pad(level)})`;
            }
        }
        if (isFunction(one) && body(one)) {
            const scope = new Set(cx.scope);
            const params = one.parameters.map((p) => target(p.name, scope));

            return `lambda${params.length ? ` ${params.join(', ')}` : ''}: ${pretty(body(one), { ...cx, scope }, level, column + 8)}`;
        }
        return flat;
    };

    const prettyText = (node, text, cx, level) => {
        if (text.length + level * 4 <= WIDTH - 4 || !node) return text;
        if (isFunction(node) && body(unwrap(node)) && text.startsWith('lambda')) return pretty(node, cx, level);
        return text;
    };

    // --- Statements -------------------------------------------------------

    // A function as a def at `cx.level`: a component's props as keywords, a
    // hook's or a helper's parameters as they are.
    const def = (title, fn, cx, decorated = []) => {
        const level = cx.level;
        const scope = new Set(cx.scope);
        const taken = new Set(cx.taken);
        const params = [];
        const head = [];
        const first = fn.parameters[0];
        const component = /^[A-Z]/.test(title) && fn.parameters.length <= 1;

        if (component && first && ts.isObjectBindingPattern(first.name)) {
            const rest = first.name.elements.find((one) => one.dotDotDotToken)?.name.text ?? 'props';
            // `"data-slot": dataSlot` and `from`, props no keyword argument can
            // name, taken out of the others as JavaScript's rest leaves them out.
            const quoted = first.name.elements.filter(
                (one) => (one.propertyName && ts.isStringLiteral(one.propertyName)) || (!one.dotDotDotToken && KEYWORDS.has((one.propertyName ?? one.name).getText()))
            );

            for (const one of first.name.elements) {
                const prop = (one.propertyName ?? one.name).getText();

                // A prop keeps the name its callers hand it under.
                scope.delete(one.name.text);
                if (quoted.includes(one)) {
                    const named = string((one.propertyName ?? one.name).text);

                    scope.add(one.name.text);
                    taken.add(snake(one.name.text));
                    head.push(`${pad(level + 1)}${snake(one.name.text)} = ${rest}.pop(${named}${one.initializer ? `, ${expr(one.initializer, { ...cx, scope })}` : ', None'})`);
                    continue;
                }
                if (one.dotDotDotToken) {
                    params.push(`**${one.name.text}`);
                    continue;
                }
                params.push(`${prop}=${one.initializer ? expr(one.initializer, { ...cx, scope }) : 'None'}`);
                taken.add(prop);
                if (one.propertyName) {
                    // `open: openProp`, the prop under the name the body reads.
                    scope.add(one.name.text);
                    taken.add(snake(one.name.text));
                    head.push(`${pad(level + 1)}${snake(one.name.text)} = ${prop}`);
                }
            }
            // Handed props it does not take, as `<CalendarInner {...props} />`
            // hands them or recharts its tooltip's content, a component leaves
            // them, as JavaScript's does.
            if (!first.name.elements.some((one) => one.dotDotDotToken)) params.push(quoted.length ? `**${rest}` : '**_');
        } else if (component && first && ts.isIdentifier(first.name)) {
            params.push(`**${first.name.text}`);
            taken.add(first.name.text);
        } else {
            for (const one of fn.parameters) {
                if (cx.flatParams && ts.isArrayBindingPattern(one.name)) {
                    for (const item of one.name.elements) params.push(ts.isOmittedExpression(item) ? fresh('_', { taken }) : target(item.name, scope));
                    continue;
                }
                // `({ row }) => ...`, the props a library hands, read as a
                // declaration reads them.
                if (ts.isObjectBindingPattern(one.name)) {
                    const local = fresh('props', { taken });

                    params.push(local);
                    head.push(...unpacked(one.name, local, one, { ...cx, scope, taken, level: level + 1 }));
                    continue;
                }
                if (!ts.isIdentifier(one.name)) {
                    const local = fresh('pair', { taken });

                    params.push(local);
                    head.push(`${pad(level + 1)}${target(one.name, scope)} = ${local}`);
                    continue;
                }
                scope.add(one.name.text);
                taken.add(snake(one.name.text));
                params.push(one.initializer ? `${snake(one.name.text)}=${expr(one.initializer, { ...cx, scope })}` : snake(one.name.text));
            }
            params.push(...(cx.extraParams ?? []));
            if (fn.parameters.length < pythonArity(fn)) params.push('*_');
        }

        const inner = {
            ...cx,
            scope,
            taken,
            level: level + 1,
            statementLevel: level + 1,
            hoistAs: undefined,
            keepJsx: false,
            inField: false,
            quote: null,
            forceDef: false,
            flatParams: false,
            extraParams: undefined,
            effect: Boolean(cx.effectBody),
            effectBody: false
        };
        const lines = ts.isBlock(fn.body) ? block(fn.body.statements, inner) : [...returned(fn.body, inner)];
        const bodyLines = [...head, ...(head.length && lines.length ? [''] : []), ...lines];
        // A prop keeps its name, and one named as a function the translation
        // calls in the body, `format`, would hide it: named, not written.
        const hidden = params.map((one) => one.split('=')[0]).find((one) => BUILTINS.has(one) && bodyLines.some((line) => new RegExp(`(?<![\\w.])${one}\\(`).test(line)));

        if (hidden) unsupported(fn, `a prop named as ${hidden}(), which the body calls`);
        return [...decorated, `${pad(level)}def ${title}(${params.join(', ')}):`, ...(bodyLines.length ? bodyLines : [`${pad(level + 1)}pass`])];
    };

    const returned = (value, cx) => {
        const hoists = [];
        // What an effect hands back is its cleanup.
        const at = { ...cx, hoists, hoisted: new Map(), statement: value, hoistAs: cx.effect && isFunction(value) ? 'cleanup' : cx.hoistAs };
        const line = isJsx(value) ? `${pad(cx.level)}return ${tstring(value, at, pad(cx.level).length + 7)}` : `${pad(cx.level)}return ${pretty(value, at, cx.level, pad(cx.level).length + 7)}`;

        return [...flush(hoists), line];
    };

    // Statements, with the blank lines and the comments their source has, and
    // one around each def, as PEP 8 has it.
    const block = (statements, cx) => {
        const lines = [];
        const text = source.text;
        const isDef = (line) => line.startsWith(`${pad(cx.level)}def `);
        let afterDef = false;

        statements.forEach((one, at) => {
            if (ts.isEmptyStatement(one)) return;

            const before = text.slice(at === 0 ? one.getFullStart() : statements[at - 1].end, one.getStart());
            const comments = (ts.getLeadingCommentRanges(text, one.getFullStart()) ?? []).map((range) => text.slice(range.pos, range.end));
            const chunk = [];

            for (const comment of comments) {
                for (const line of comment.replace(/^\/\*+|\*+\/$/g, '').replace(/^\/\/ ?/gm, '').split('\n')) {
                    const words = line.replace(/^\s*\*? ?/, '').trimEnd();

                    if (words || comment.startsWith('//')) chunk.push(`${pad(cx.level)}# ${words}`.trimEnd());
                }
            }

            const own = statement(one, cx);
            const hasDef = own.some(isDef);

            if (lines.length && lines.at(-1) !== '' && (afterDef || (hasDef && isDef(own.find((line) => line.trim())) ) || /\n[ \t]*\n/.test(before.split(/\/[/*]/)[0]))) lines.push('');
            lines.push(...chunk, ...own);
            afterDef = hasDef;
        });

        return lines;
    };

    // Each def taken out before its statement, a blank line after it; a name
    // the statement reads, none.
    const flush = (hoists) => hoists.flatMap((lines) => (lines.tight ? lines : [...lines, '']));

    const statement = (node, cx) => {
        const hoists = [];
        const at = { ...cx, hoists, hoisted: new Map(), statement: node, statementLevel: cx.level };
        const indent = pad(cx.level);
        let lines;

        if (ts.isReturnStatement(node)) {
            if (!node.expression) lines = [`${indent}return`];
            else return returned(node.expression, cx);
        } else if (ts.isVariableStatement(node)) {
            lines = node.declarationList.declarations.flatMap((one) => declaration(one, at));
        } else if (ts.isExpressionStatement(node)) {
            lines = expressionStatement(node.expression, at);
        } else if (ts.isIfStatement(node)) {
            lines = conditional(node, at, 'if');
        } else if (ts.isThrowStatement(node)) {
            const error = unwrap(node.expression);

            if (!ts.isNewExpression(error) || error.expression.getText() !== 'Error') unsupported(node, 'a throw');
            lines = [`${indent}raise RuntimeError(${(error.arguments ?? []).map((one) => expr(one, at)).join(', ')})`];
        } else if (ts.isFunctionDeclaration(node)) {
            at.scope.add(node.name.text);
            lines = def(snake(node.name.text), node, at);
        } else if (ts.isBlock(node)) {
            lines = block(node.statements, cx);
        } else if (ts.isForOfStatement(node) || ts.isForInStatement(node) || ts.isForStatement(node) || ts.isWhileStatement(node)) {
            lines = loop(node, at);
        } else if ((ts.isBreakStatement(node) || ts.isContinueStatement(node)) && !node.label) {
            lines = [`${indent}${ts.isBreakStatement(node) ? 'break' : 'continue'}`];
        } else {
            unsupported(node, 'a statement');
        }

        return [...flush(hoists), ...lines];
    };

    // A loop, as Python writes it: over a list, a str or a set as JavaScript
    // walks it, a Map's pairs by `.items()`, a dict's keys; `for (let i = a;
    // i < b; i++)` over a range; a `while` as it is.
    const loop = (node, cx) => {
        const indent = pad(cx.level);
        const inner = { ...cx, level: cx.level + 1 };
        const body = ts.isBlock(node.statement) ? block(node.statement.statements, inner) : statement(node.statement, inner);
        const lines = body.some((line) => line.trim()) ? body : [`${pad(inner.level)}pass`];

        if (ts.isWhileStatement(node)) return [`${indent}while ${expr(node.expression, cx)}:`, ...lines];

        const declared = node.initializer && ts.isVariableDeclarationList(node.initializer) && node.initializer.declarations.length === 1 ? node.initializer.declarations[0] : null;

        if (!declared) unsupported(node, 'a loop over a name not declared by it');
        if (ts.isForStatement(node)) {
            const name = declared.name;
            const test = node.condition && unwrap(node.condition);
            const step = node.incrementor && unwrap(node.incrementor);
            const counts =
                ts.isIdentifier(name) &&
                declared.initializer &&
                test &&
                ts.isBinaryExpression(test) &&
                test.operatorToken.kind === k.LessThanToken &&
                ts.isIdentifier(unwrap(test.left)) &&
                unwrap(test.left).text === name.text &&
                step &&
                (ts.isPostfixUnaryExpression(step) || ts.isPrefixUnaryExpression(step)) &&
                step.operator === k.PlusPlusToken &&
                ts.isIdentifier(step.operand) &&
                step.operand.text === name.text;

            if (!counts) unsupported(node, 'a loop of another shape than a range');

            const local = target(name, cx.scope);
            const from = expr(declared.initializer, cx);

            return [`${indent}for ${local} in range(${from === '0' ? '' : `${from}, `}${expr(test.right, cx)}):`, ...lines];
        }

        const binding = declared.name;
        let over = expr(node.expression, cx);
        let targets;

        if (ts.isForInStatement(node)) {
            if (!isDict(node.expression)) unsupported(node, "a loop over the keys of an object Python does not hand over as a dict");
            return [`${indent}for ${target(binding, cx.scope)} in ${over}:`, ...lines];
        }
        if (typeOf(node.expression).getSymbol()?.getName() === 'Map') over = `${expr(node.expression, cx, PRIMARY)}.items()`;
        if (ts.isArrayBindingPattern(binding)) {
            const names = binding.elements.map((one) => (ts.isOmittedExpression(one) ? '_' : target(one.name, cx.scope)));
            const rest = binding.elements.some((one) => !ts.isOmittedExpression(one) && one.dotDotDotToken);
            const item = checker.getTypeAtLocation(binding);
            // A tuple of as many items as the names, unpacked as it is; any
            // other list, its first ones, the rest left, as JavaScript leaves it.
            const exact = checker.isTupleType(item) && checker.getTypeArguments(item).length === names.length;

            targets = binding.elements.map((one, at) => (!ts.isOmittedExpression(one) && one.dotDotDotToken ? `*${names[at]}` : names[at]));
            if (!rest && !exact) targets.push('*_');
            targets = targets.join(', ');
        } else {
            targets = target(binding, cx.scope);
        }
        return [`${indent}for ${targets} in ${over}:`, ...lines];
    };

    const conditional = (node, cx, word) => {
        const indent = pad(cx.level);
        const inner = { ...cx, level: cx.level + 1 };
        const branch = (one) => (ts.isBlock(one) ? block(one.statements, inner) : statement(one, inner));
        const lines = [`${indent}${word} ${expr(node.expression, cx)}:`, ...branch(node.thenStatement)];

        if (node.elseStatement && ts.isIfStatement(node.elseStatement)) return [...lines, ...conditional(node.elseStatement, cx, 'elif')];
        if (node.elseStatement) return [...lines, `${indent}else:`, ...branch(node.elseStatement)];
        return lines;
    };

    const declaration = (one, cx) => {
        const indent = pad(cx.level);
        const value = one.initializer;
        const binding = one.name;

        if (ts.isIdentifier(binding)) {
            const local = snake(binding.text);

            cx.scope.add(binding.text);
            cx.taken.add(local);
            if (!value) return [`${indent}${local} = None`];
            if (isFunction(value)) return def(local, unwrap(value), cx);
            if (memoized(value)) return [`${indent}@memo`, ...def(local, memoized(value), cx)];

            const hook = ts.isCallExpression(unwrap(value)) && reactName(unwrap(value).expression);

            // `const f = useCallback(() => {...}, deps)`: the def, then the hook.
            if ((hook === 'useCallback' || hook === 'useMemo') && isFunction(unwrap(value).arguments[0]) && !body(unwrap(unwrap(value).arguments[0]))) {
                const [fn, ...rest] = unwrap(value).arguments;

                hooks.add(HOOKS[hook]);
                return [...def(local, unwrap(fn), cx), '', `${indent}${local} = ${HOOKS[hook]}(${[local, ...rest.map((arg) => expr(arg, cx))].join(', ')})`];
            }
            if (isJsx(value)) return [`${indent}${local} = ${tstring(value, cx, indent.length + local.length + 3)}`];

            // `x = a ?? b` of more than a name: a, then b where a is None or NULL.
            if (ts.isBinaryExpression(unwrap(value)) && unwrap(value).operatorToken.kind === k.QuestionQuestionToken && !ts.isIdentifier(unwrap(unwrap(value).left))) {
                need('javascript', 'NULL');
                return [`${indent}${local} = ${expr(unwrap(value).left, cx)}`, `${indent}if ${local} in (None, NULL):`, `${pad(cx.level + 1)}${local} = ${expr(unwrap(value).right, cx)}`];
            }
            return [`${indent}${local} = ${pretty(value, cx, cx.level, indent.length + local.length + 3)}`];
        }

        if (ts.isArrayBindingPattern(binding)) {
            const names = binding.elements.map((item) => (ts.isOmittedExpression(item) ? '_' : target(item.name, cx.scope)));
            const targets = binding.elements.map((item, at) => (item.dotDotDotToken ? `*${names[at]}` : names[at])).join(', ');

            names.forEach((item) => cx.taken.add(item));
            if (names.length === 1 && !binding.elements[0].dotDotDotToken) return [`${indent}${names[0]} = ${expr(value, cx, PRIMARY)}[0]`];
            return [`${indent}${targets} = ${pretty(value, cx, cx.level, indent.length + targets.length + 3)}`];
        }

        // `const { a, b = 1 } = value`: each read as a dict's, missing as None.
        const lines = [];
        let from = unwrap(value);
        let source_ = expr(value, cx);

        if (!ts.isIdentifier(from) || binding.elements.length === 1) {
            if (binding.elements.length > 1) {
                // The temporary named after what it holds: `sidebar` of
                // useSidebar(), `slot` of `slots[index] ?? {}`.
                const named = ts.isBinaryExpression(from) && from.operatorToken.kind === k.QuestionQuestionToken ? unwrap(from.left) : from;
                const callee = ts.isCallExpression(named) ? named.expression.getText().replace(/^use/, '') : '';
                const fromName = callee
                    ? snake(callee[0].toLowerCase() + callee.slice(1))
                    : ts.isElementAccessExpression(named) && ts.isPropertyAccessExpression(named.expression)
                      ? named.expression.name.text.replace(/s$/, '')
                      : 'value';
                const temp = fresh(snake(fromName), cx);

                if (ts.isBinaryExpression(from) && from.operatorToken.kind === k.QuestionQuestionToken && !pure(from.left)) {
                    need('javascript', 'NULL');
                    lines.push(`${indent}${temp} = ${expr(from.left, cx)}`, `${indent}if ${temp} in (None, NULL):`, `${pad(cx.level + 1)}${temp} = ${expr(from.right, cx)}`);
                } else {
                    lines.push(`${indent}${temp} = ${source_}`);
                }
                source_ = temp;
                from = null;
            } else {
                source_ = expr(value, cx, PRIMARY);
            }
        }

        // `slots[index] ?? {}`, an object or an empty dict, read by getattr().
        const either = ts.isBinaryExpression(unwrap(value)) && unwrap(value).operatorToken.kind === k.QuestionQuestionToken && ts.isObjectLiteralExpression(unwrap(unwrap(value).right));

        return [...lines, ...unpacked(binding, source_, value, cx, either)];
    };

    // `{ a, b = 1 }` read off `source_`, the value of `node`: a dict's keys,
    // missing as None, or an object's attributes, one it may not have by
    // getattr().
    const unpacked = (binding, source_, node, cx, either = false) => {
        const dict = isDict(node);
        const indent = pad(cx.level);
        const names = [];
        const reads = [];
        const defaults = [];

        for (const item of binding.elements) {
            if (item.dotDotDotToken || !ts.isIdentifier(item.name)) unsupported(item, 'a destructured rest');

            const prop = (item.propertyName ?? item.name).getText();
            const local = target(item.name, cx.scope);

            cx.taken.add(local);
            names.push(local);
            reads.push(
                dict
                    ? `${source_}.get(${string(prop)})`
                    : either || optional(node, prop)
                      ? `getattr(${source_}, ${string(prop)}, None)`
                      : KEYWORDS.has(prop)
                        ? `getattr(${source_}, ${string(prop)})`
                        : `${source_}.${prop}`
            );
            if (item.initializer) defaults.push([local, expr(item.initializer, cx)]);
        }

        return [
            `${indent}${names.join(', ')} = ${reads.join(', ')}`,
            ...defaults.flatMap(([local, fallback]) => [`${indent}if ${local} is None:`, `${pad(cx.level + 1)}${local} = ${fallback}`])
        ];
    };

    const expressionStatement = (node, cx) => {
        const indent = pad(cx.level);
        const one = unwrap(node);

        // `f?.(x)` and `a?.b()`: called where it stands.
        if (one.flags & ts.NodeFlags.OptionalChain) {
            const [whole, guards] = chain(one, cx);

            return guards.length ? [`${indent}if ${guards.join(' and ')}:`, `${pad(cx.level + 1)}${whole}`] : [`${indent}${whole}`];
        }
        if (ts.isBinaryExpression(one) && ASSIGNMENTS[one.operatorToken.kind]) {
            const left = unwrap(one.left);
            const target_ = ts.isPropertyAccessExpression(left) ? property(left, cx, 'write')[0] : ts.isElementAccessExpression(left) ? element(left, cx, 'write')[0] : expr(left, cx);

            if (ts.isIdentifier(left)) cx.scope.add(left.text);
            return [`${indent}${target_} ${ASSIGNMENTS[one.operatorToken.kind]} ${pretty(one.right, cx, cx.level, indent.length + target_.length + 3)}`];
        }
        return [`${indent}${pretty(one, cx, cx.level, indent.length)}`];
    };

    // --- The module ------------------------------------------------------------

    const translate = () => {
        const moduleScope = new Set(own);
        const taken = new Set([...own].map(snake));
        const items = [];
        const cx = { scope: moduleScope, taken, level: 0, statementLevel: 0, quote: null };

        for (const node of source.statements) {
            // `export { DirectionProvider } from "…"`, names of the module's
            // own taken from JavaScript.
            if (ts.isExportDeclaration(node) && node.moduleSpecifier && node.exportClause && ts.isNamedExports(node.exportClause) && !node.isTypeOnly) {
                for (const one of node.exportClause.elements) {
                    if (one.isTypeOnly) continue;

                    const from = (one.propertyName ?? one.name).text;
                    const local = snake(one.name.text);

                    add(js, node.moduleSpecifier.text, { local, entry: from === local ? from : `${from} as ${local}` });
                    used.add(local);
                }
                continue;
            }
            // `export { ComboBoxPrimitive as Combobox }`, a name the module
            // hands out under another: bound to it.
            if (ts.isExportDeclaration(node) && !node.moduleSpecifier && node.exportClause && ts.isNamedExports(node.exportClause) && !node.isTypeOnly) {
                for (const one of node.exportClause.elements) {
                    if (one.isTypeOnly || !one.propertyName) continue;
                    items.push({ def: false, lines: [`${snake(one.name.text)} = ${name(one.propertyName, cx)}`] });
                }
                continue;
            }
            if (ts.isImportDeclaration(node) || ts.isExportDeclaration(node)) continue;
            if (ts.isExpressionStatement(node) && ts.isStringLiteral(node.expression)) continue;
            if (ts.isTypeAliasDeclaration(node) || ts.isInterfaceDeclaration(node)) continue;

            if (ts.isFunctionDeclaration(node)) {
                items.push({ def: true, lines: def(snake(node.name.text), node, { ...cx, hoists: [], hoisted: new Map() }) });
            } else if (ts.isVariableStatement(node)) {
                for (const one of node.declarationList.declarations) {
                    const value = one.initializer;
                    const title = snake(one.name.text);

                    if (isFunction(value)) {
                        items.push({ def: true, lines: def(title, unwrap(value), { ...cx, hoists: [], hoisted: new Map() }) });
                    } else if (memoized(value)) {
                        items.push({ def: true, lines: ['@memo', ...def(title, memoized(value), { ...cx, hoists: [], hoisted: new Map() })] });
                    } else if (ts.isCallExpression(value) && value.expression.getText() === 'cva') {
                        // cva(base, variants, defaults, compound), one a line.
                        const [base, options] = value.arguments;
                        const parts = [expr(base, cx), ...cvaFields(options).map((field_) => (field_ ? pretty(field_, cx, 1) : 'None'))];

                        while (parts.at(-1) === 'None') parts.pop();
                        used.add('cva');
                        variantMakers.add(one.name.text);
                        items.push({ def: false, lines: [`${title} = cva(`, ...parts.map((part) => `    ${part},`), ')'] });
                    } else {
                        // Its functions, defs of the module's before it.
                        const hoists = [];
                        const line = `${title} = ${pretty(value, { ...cx, hoists, hoisted: new Map(), statement: one }, 0, title.length + 3)}`;

                        for (const lines of hoists) items.push({ def: true, lines });
                        items.push({ def: false, lines: [line] });
                    }
                }
            } else {
                unsupported(node, ts.SyntaxKind[node.kind]);
            }
        }

        const usedEntry = (one) => used.has(one.local);
        const head = [];

        for (const module of ['browser', 'javascript']) {
            if (brython.has(module)) head.push(`from ${module} import ${[...brython.get(module)].sort().join(', ')}`);
        }
        if (hooks.size) head.push(`from reacthon import ${[...hooks].sort().join(', ')}`);
        for (const [from, names] of python) {
            for (const one of names.filter((one) => one.whole && usedEntry(one))) head.push(one.local === from ? `import ${from}` : `import ${from} as ${one.local}`);
        }
        for (const [from, names] of python) {
            const kept = names.filter((one) => !one.whole && usedEntry(one)).map((one) => (one.own ? one.local : snake(one.local))).sort();
            const line = `from ${from} import ${kept.join(', ')}`;
            const wrapped = `    ${kept.join(', ')},`;

            if (!kept.length) continue;
            if (line.length <= WIDTH) head.push(line);
            else head.push(`from ${from} import (`, ...(wrapped.length <= WIDTH ? [wrapped] : kept.map((one) => `    ${one},`)), ')');
        }

        const jsEntries = [...js].map(([from, names]) => [from, names.filter(usedEntry)]).filter(([, names]) => names.length);

        if (jsEntries.length) {
            const listed = ([from, names]) => `${string(from)}: [${names.map((one) => string(one.entry)).join(', ')}]`;
            const flat = `__js__ = {${jsEntries.map(listed).join(', ')}}`;
            // An entry too long for its line, one name a line.
            const entry = ([from, names]) =>
                `    ${listed([from, names])},`.length <= WIDTH
                    ? `    ${listed([from, names])},`
                    : `    ${string(from)}: [\n${names.map((one) => `        ${string(one.entry)},`).join('\n')}\n    ],`;

            if (head.length) head.push('');
            head.push(flat.length <= WIDTH ? flat : `__js__ = {\n${jsEntries.map(entry).join('\n')}\n}`);
        }

        // Two blank lines around a function, one between two assignments.
        let text = head.join('\n');

        items.forEach((item, at) => {
            const previous = at === 0 ? null : items[at - 1];
            const blank = item.def || previous?.def ? 2 : 1;

            text += text ? `${'\n'.repeat(blank + 1)}${item.lines.join('\n')}` : item.lines.join('\n');
        });

        return `${text.replace(/[ \t]+$/gm, '')}\n`;
    };

    return translate;
}

// The TypeScript program of the files, for its checker: the project's own
// tsconfig where there is one, a Vite project's `tsconfig.app.json`, which
// holds its paths, or a Next.js project's `tsconfig.json`.
function makeProgram(files) {
    const config =
        ts.findConfigFile(process.cwd(), ts.sys.fileExists, 'tsconfig.app.json') ?? ts.findConfigFile(process.cwd(), ts.sys.fileExists, 'tsconfig.json');
    const options = config
        ? ts.parseJsonConfigFileContent(ts.readConfigFile(config, ts.sys.readFile).config, ts.sys, dirname(config)).options
        : { jsx: ts.JsxEmit.Preserve, strict: true, skipLibCheck: true, moduleResolution: ts.ModuleResolutionKind.Bundler, module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 };
    // A preset's files read `@` as its folder, as Vite has them.
    const preset = files.map((file) => /[\\/]src[\\/]presets[\\/]([^\\/]+)[\\/]/.exec(file)?.[1]).find(Boolean);
    const paths = preset ? { '@/lib/utils': ['./src/lib/utils'], '@/*': [`./src/presets/${preset}/*`] } : options.paths;

    return ts.createProgram(files, { ...options, paths, noEmit: true });
}

export function convertFiles(files) {
    const paths = files.map((file) => resolve(file));
    const program = makeProgram(paths);
    const checker = program.getTypeChecker();
    const translated = new Set(paths);

    return paths.map((path) => {
        try {
            return { file: path, python: moduleTranslator(program.getSourceFile(path), checker, program, translated)() };
        } catch (error) {
            if (!(error instanceof Unsupported)) throw error;
            return { file: path, error: error.message };
        }
    });
}

const [out, ...files] = process.argv.slice(2);

if (out && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
    mkdirSync(out, { recursive: true });
    for (const { file, python, error } of convertFiles(files)) {
        const name = `${basename(file).replace(/\.tsx?$/, '').replace(/-/g, '_')}.py`;

        if (error) {
            console.log(`left out ${basename(file)}: ${error}`);
        } else {
            writeFileSync(join(out, name), python);
            console.log(`written ${name}`);
        }
    }
}
