// The shadcn registries of the components written in Python, one a preset:
//   node tools/registry.js
// For each preset of src/presets, a registry built by shadcn's CLI into
// public/r/<preset>/: one item a component, with the Python files it imports,
// the npm packages its `__js__` and theirs name, and the project's own
// JavaScript they import, an item of shadcn/ui's own registry: `@/hooks/use-mobile`
// is its `use-mobile`. Each file lands where shadcn's CLI puts the component's own.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const UTILS = 'src/lib/utils.py';
const shadcn = fileURLToPath(import.meta.resolve('shadcn'));

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

function item(ui, name) {
    const files = [];
    const packages = new Set();
    const items = new Set();
    const pathOf = (module) => (module === 'utils' ? UTILS : `${ui}/${module}.py`);
    const visit = (path) => {
        if (files.includes(path)) return;
        if (!existsSync(path)) throw new Error(`it imports ${path}, not written in Python yet`);
        files.push(path);

        const own = read(path);

        own.packages.forEach((one) => packages.add(one));
        own.items.forEach((one) => items.add(one));
        own.modules.forEach((module) => visit(pathOf(module)));
    };

    visit(`${ui}/${name}.py`);

    const title = name.replace(/_/g, ' ');

    return {
        name: name.replace(/_/g, '-'),
        type: 'registry:ui',
        title: `${title[0].toUpperCase()}${title.slice(1)}, in Python`,
        dependencies: [...packages].sort(),
        ...(items.size ? { registryDependencies: [...items].sort() } : {}),
        files: files.map((path) => ({ path, type: 'registry:file', target: path === UTILS ? path : `src/components/ui/${path.split('/').pop()}` }))
    };
}

for (const preset of readdirSync('src/presets')) {
    const ui = `src/presets/${preset}/components/ui`;
    const names = readdirSync(ui)
        .filter((file) => file.endsWith('.py'))
        .map((file) => file.slice(0, -3))
        .sort();
    const items = names.flatMap((name) => {
        try {
            return [item(ui, name)];
        } catch (error) {
            console.log(`${preset}: left out ${name}: ${error.message}`);
            return [];
        }
    });
    const registry = {
        $schema: 'https://ui.shadcn.com/schema/registry.json',
        name: 'reacthon-ui',
        homepage: 'https://github.com/svelthon/reacthon-ui',
        items
    };
    const folder = mkdtempSync(join(tmpdir(), 'reacthon-ui-registry-'));

    try {
        writeFileSync(join(folder, 'registry.json'), `${JSON.stringify(registry, null, 2)}\n`);

        const built = spawnSync(process.execPath, [shadcn, 'build', join(folder, 'registry.json'), '--output', `public/r/${preset}`], { encoding: 'utf8' });

        if (built.status !== 0) throw new Error(`shadcn build failed for ${preset}:\n${built.stdout}${built.stderr}`);
    } finally {
        rmSync(folder, { recursive: true, force: true });
    }
    console.log(`public/r/${preset}: ${items.length} components`);
}
