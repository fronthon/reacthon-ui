// The shadcn registries of the components and the blocks written in Python, one
// a preset:
//   node tools/registry.js
// For each preset of src/presets, a registry built by shadcn's CLI into
// public/r/<preset>/: one item a component and one a block, with the Python
// files it imports, the files of its own folder they read, a block's data, the
// npm packages their `__js__` name, and the project's own JavaScript they
// import, an item of shadcn/ui's own registry: `@/hooks/use-mobile` is its
// `use-mobile`; and all that shadcn's item of the component or the block
// takes, in items.json, imported or not, its components in Python, its
// packages at its versions. Each file lands where shadcn's CLI puts the TSX one: a
// component in components/ui, a block's own in components, its page and its
// data in the routes of the app, of the type shadcn gives them, which writes a
// page only into a project whose routes are files, as Next.js's are. The
// others are each a `registry:file`, which the CLI writes as it is, where it
// transforms a component as TypeScript.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const UTILS = 'src/lib/utils.py';
const shadcn = fileURLToPath(import.meta.resolve('shadcn'));

const packageOf = (from) => (from.startsWith('@') ? from.split('/').slice(0, 2) : from.split('/').slice(0, 1)).join('/');
// `recharts@3.8.0` is recharts.
const unversioned = (spec) => spec.replace(/^(@?[^@]+)@.*$/, '$1');

// A Python file's own imports, files of its folder, npm packages and shadcn/ui items.
function read(path) {
    const text = readFileSync(path, 'utf8');
    const js = text.match(/^__js__ = \{[\s\S]*?\}$/m)?.[0] ?? '';
    const froms = [...js.matchAll(/"([^"]+)": \[/g)].map((match) => match[1]);

    return {
        modules: [...text.matchAll(/^from (\w+) import /gm)].map((match) => match[1]).filter((one) => !['browser', 'javascript', 'reacthon'].includes(one)),
        files: froms.filter((from) => from.startsWith('./')).map((from) => from.slice(2)),
        packages: froms.filter((from) => !from.startsWith('@/') && !from.startsWith('./')).map(packageOf),
        items: froms.filter((from) => from.startsWith('@/')).map((from) => from.split('/').pop()),
        icons: [...(/"lucide-react": \[([^\]]*)\]/.exec(js)?.[1] ?? '').matchAll(/"([^"]+)"/g)].map((match) => match[1])
    };
}

// An item and what it takes with it, from its first file: each module where
// Reacthon finds it, in its importer's folder, then in the helpers' and the
// components'; what shadcn's item of the item and of each of its components
// takes; and, in `meta.icons`, the icons of each of its files in the other
// libraries, in the file's order, by which the CLI writes them in the
// project's (bin/icons.js).
function item(root, name, first, { iconNames, declared }, placed, head) {
    const ui = `${root}/components/ui`;
    const files = [];
    const packages = new Map();
    const items = new Set();
    const icons = {};
    // A package at shadcn's version where shadcn names one.
    const take = (spec, shadcns) => {
        if (shadcns || !packages.has(unversioned(spec))) packages.set(unversioned(spec), spec);
    };
    const visit = (path) => {
        if (files.includes(path)) return;
        if (!existsSync(path)) throw new Error(`it imports ${path}, not written in Python yet`);
        files.push(path);
        if (!path.endsWith('.py')) return;

        const own = read(path);
        const tsx = `${relative(root, dirname(path))}/${basename(path, '.py').replace(/_/g, '-')}.tsx`;
        const shadcns = declared[path === first ? name : dirname(path) === ui ? basename(tsx, '.tsx') : ''];

        own.packages.forEach((one) => take(one, false));
        own.items.forEach((one) => items.add(one));
        if (own.icons.length) icons[placed(path).target] = iconNames[tsx];
        own.files.forEach((file) => visit(join(dirname(path), file)));
        own.modules.forEach((module) => {
            const found = [dirname(path), 'src/lib', ui].map((folder) => `${folder}/${module}.py`);

            visit(found.find((one) => existsSync(one)) ?? found.at(-1));
        });
        shadcns?.dependencies?.forEach((one) => take(one, true));
        shadcns?.registryDependencies?.forEach((one) => (existsSync(`${ui}/${one}.tsx`) ? visit(`${ui}/${one.replace(/-/g, '_')}.py`) : items.add(one)));
    };

    visit(first);

    return {
        ...head,
        dependencies: [...packages.values()].sort(),
        ...(items.size ? { registryDependencies: [...items].sort() } : {}),
        files: files.map((path) => ({ path, ...placed(path) })),
        ...(Object.keys(icons).length ? { meta: { icons } } : {})
    };
}

// Where a component's files land.
const component = (path) => ({ type: 'registry:file', target: path === UTILS ? path : `src/components/ui/${basename(path)}` });

// Where a block's land: its page and its data as shadcn's, a page of Python
// where its is of TypeScript, and its own components in components.
const block = (folder, own) => (path) => {
    if (dirname(path) !== folder) return component(path);

    const shadcns = own[basename(path).replace(/\.py$/, '.tsx')] ?? own[basename(path)];

    return shadcns ? { type: shadcns.type, target: shadcns.target.replace(/\.tsx$/, '.py') } : { type: 'registry:file', target: `src/components/${basename(path)}` };
};

for (const preset of readdirSync('src/presets')) {
    const root = `src/presets/${preset}`;
    const ui = `${root}/components/ui`;
    const shadcns = { iconNames: JSON.parse(readFileSync(`${root}/icons.json`, 'utf8')), declared: JSON.parse(readFileSync(`${root}/items.json`, 'utf8')) };
    const named = (kind, name, make) => {
        try {
            return [make()];
        } catch (error) {
            console.log(`${preset}: left out the ${kind} ${name}: ${error.message}`);
            return [];
        }
    };
    const components = readdirSync(ui)
        .filter((file) => file.endsWith('.py'))
        .map((file) => file.slice(0, -3))
        .sort()
        .flatMap((name) => {
            const title = name.replace(/_/g, ' ');

            return named('component', name, () =>
                item(root, name.replace(/_/g, '-'), `${ui}/${name}.py`, shadcns, component, {
                    name: name.replace(/_/g, '-'),
                    type: 'registry:ui',
                    title: `${title[0].toUpperCase()}${title.slice(1)}, in Python`
                })
            );
        });
    const blocks = Object.entries(shadcns.declared).filter(([, { files }]) => files);
    const pages = blocks.flatMap(([name, { title, description, categories, files }]) =>
        named('block', name, () =>
            item(root, name, `${root}/blocks/${name}/page.py`, shadcns, block(`${root}/blocks/${name}`, files), {
                name,
                type: 'registry:block',
                title: `${title}, in Python`,
                description,
                categories
            })
        )
    );
    const registry = {
        $schema: 'https://ui.shadcn.com/schema/registry.json',
        name: 'reacthon-ui',
        homepage: 'https://github.com/fronthon/reacthon-ui',
        items: [...components, ...pages]
    };
    const folder = mkdtempSync(join(tmpdir(), 'reacthon-ui-registry-'));

    try {
        writeFileSync(join(folder, 'registry.json'), `${JSON.stringify(registry, null, 2)}\n`);

        const built = spawnSync(process.execPath, [shadcn, 'build', join(folder, 'registry.json'), '--output', `public/r/${preset}`], { encoding: 'utf8' });

        if (built.status !== 0) throw new Error(`shadcn build failed for ${preset}:\n${built.stdout}${built.stderr}`);
    } finally {
        rmSync(folder, { recursive: true, force: true });
    }
    console.log(`public/r/${preset}: ${components.length} components, ${pages.length} blocks`);
}
