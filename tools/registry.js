// registry.json, the shadcn registry of the components written in Python:
//   node tools/registry.js
// One item a component, with the Python files it imports, the npm packages its
// `__js__` and theirs name, and the project's own JavaScript they import, a
// hook of shadcn/ui's own registry: `@/hooks/use-mobile` is its `use-mobile`.
import { existsSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';

const UI = 'src/components/ui';
const UTILS = 'src/lib/utils.py';

const pathOf = (module) => (module === 'utils' ? UTILS : `${UI}/${module}.py`);
const packageOf = (from) => (from.startsWith('@') ? from.split('/').slice(0, 2) : from.split('/').slice(0, 1)).join('/');

// A Python file's own imports, npm packages and shadcn/ui items.
function read(path) {
    const text = readFileSync(path, 'utf8');
    const js = text.match(/^__js__ = \{[\s\S]*?\}$/m)?.[0] ?? '';
    const froms = [...js.matchAll(/"([^"]+)": \[/g)].map((match) => match[1]);

    return {
        modules: [...text.matchAll(/^from (\w+) import /gm)].map((match) => match[1]).filter((one) => !['browser', 'javascript', 'reacthon'].includes(one)),
        packages: froms.filter((from) => !from.startsWith('@/')).map(packageOf),
        items: froms.filter((from) => from.startsWith('@/')).map((from) => from.split('/').pop())
    };
}

function item(name) {
    const files = [];
    const packages = new Set();
    const items = new Set();
    const visit = (path) => {
        if (files.includes(path)) return;
        if (!existsSync(path)) throw new Error(`it imports ${path}, not written in Python yet`);
        files.push(path);

        const own = read(path);

        own.packages.forEach((one) => packages.add(one));
        own.items.forEach((one) => items.add(one));
        own.modules.forEach((module) => visit(pathOf(module)));
    };

    visit(`${UI}/${name}.py`);

    const title = name.replace(/_/g, ' ');

    return {
        name: name.replace(/_/g, '-'),
        type: 'registry:ui',
        title: `${title[0].toUpperCase()}${title.slice(1)}, in Python`,
        dependencies: [...packages].sort(),
        ...(items.size ? { registryDependencies: [...items].sort() } : {}),
        files: files.map((path) => ({ path, type: 'registry:file', target: path }))
    };
}

const names = readdirSync(UI)
    .filter((file) => file.endsWith('.py'))
    .map((file) => file.slice(0, -3))
    .sort();

const items = names.flatMap((name) => {
    try {
        return [item(name)];
    } catch (error) {
        console.log(`left out ${name}: ${error.message}`);
        return [];
    }
});

const registry = {
    $schema: 'https://ui.shadcn.com/schema/registry.json',
    name: 'reacthon-ui',
    homepage: 'https://github.com/svelthon/reacthon-ui',
    items
};

writeFileSync('registry.json', `${JSON.stringify(registry, null, 2)}\n`);
console.log(`registry.json: ${items.length} components`);
