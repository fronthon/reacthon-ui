// A preset of shadcn/ui, its components and its blocks, in its folder of
// src/presets, as shadcn's CLI writes them into a project of that preset:
//   node tools/preset.js <preset> [block...]
//   node tools/preset.js <preset> --icons
//   node tools/preset.js <preset> --items
// Its components, its hooks and its lib, the helpers aside, which every preset
// shares; then each block in a folder of its own of blocks/, its page beside
// its components, each imported as ./name, which is where Python looks first;
// then icons.json, each icon's name in every library the CLI writes icons in,
// and items.json, what the registry says of each component and block beside
// its files. Given blocks, those alone; given --icons or --items, that file
// alone. The
// CLI writes a block's page only into a project whose routes are files, as
// Next.js's are: the files are read with --dry-run from one made for the
// purpose, its icons Lucide's.
import { spawnSync } from 'node:child_process';
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { COMPONENTS_HIDDEN_FROM_SELECTION } from '@shadcn/registry/internal/registry/constants';

const shadcn = fileURLToPath(import.meta.resolve('shadcn'));
const [preset, ...given] = process.argv.slice(2);
const root = join('src/presets', preset ?? '');

if (!preset) {
    console.error('Usage: node tools/preset.js <preset> [block...]');
    process.exit(1);
}

const base = `https://ui.shadcn.com/r/styles/${preset}`;
const index = async () => (await (await fetch(`${base}/registry.json`)).json()).items;

async function blockNames() {
    return (await index()).filter((item) => item.type === 'registry:block').map((item) => item.name);
}

// What shadcn's registry says of each component and block, beside its files:
// the npm packages and the items it takes, which its CLI installs whether its
// code imports them or not; and of a block, its title, its description and its
// categories, and the type and the place of its page and its data, which the
// CLI writes in the routes of the app, each by its file's name.
async function items() {
    const found = {};

    for (const { name, type, title, description, categories, dependencies, registryDependencies, files } of await index()) {
        const isBlock = type === 'registry:block';

        if (!existsSync(join(root, isBlock ? `blocks/${name}/page.tsx` : `components/ui/${name}.tsx`))) continue;
        if (!isBlock && type !== 'registry:ui') continue;
        found[name] = {
            ...(isBlock ? { title, description, categories } : {}),
            ...(dependencies ? { dependencies } : {}),
            ...(registryDependencies ? { registryDependencies } : {}),
            ...(isBlock
                ? { files: Object.fromEntries(files.filter((file) => file.target).map((file) => [basename(file.path), { type: file.type, target: file.target }])) }
                : {})
        };
    }
    writeFileSync(join(root, 'items.json'), `${JSON.stringify(found, null, 2)}\n`);
    console.log(`${root}/items.json: ${Object.keys(found).length} items`);
}

// Each icon of each file in the other libraries, in the file's order, as
// shadcn's own registry writes it for its CLI, which writes each in its place:
// `<IconPlaceholder lucide="ChevronDownIcon" hugeicons="UnfoldMoreIcon" … />`,
// the same Lucide icon another one of Hugeicons elsewhere in the file.
async function icons() {
    const items = await index();
    const files = [];
    const names = {};

    // Ten at a time, which the resolver keeps up with.
    for (let at = 0; at < items.length; at += 10) {
        files.push(...(await Promise.all(items.slice(at, at + 10).map(async ({ name }) => (await (await fetch(`${base}/${name}.json`)).json()).files ?? []))));
    }

    // Its path as the preset's folder has it: ui/x.tsx in components/ui, a
    // block's components beside its page.
    const placed = (path) =>
        path
            .replace(`registry/${preset}/`, '')
            .replace(/^ui\//, 'components/ui/')
            .replace(/^(blocks\/[^/]+)\/components\//, '$1/');

    for (const file of files.flat()) {
        const found = [...(file.content ?? '').matchAll(/<IconPlaceholder[\s\S]*?\/>/g)].map(([tag]) => {
            const { className, ...names } = Object.fromEntries([...tag.matchAll(/(\w+)="([^"]*)"/g)].map(([, key, value]) => [key, value]));

            return names;
        });

        if (found.length) names[placed(file.path)] = found;
    }

    const sorted = Object.fromEntries(Object.keys(names).sort().map((path) => [path, names[path]]));

    writeFileSync(join(root, 'icons.json'), `${JSON.stringify(sorted, null, 2)}\n`);
    console.log(`${root}/icons.json: ${Object.keys(sorted).length} files`);
}

function nextProject() {
    const project = mkdtempSync(join(tmpdir(), 'reacthon-ui-preset-'));
    const config = JSON.parse(readFileSync('components.json', 'utf8'));

    writeFileSync(join(project, 'components.json'), JSON.stringify({ ...config, style: preset }, null, 2));
    for (const file of ['package.json', 'tsconfig.json']) copyFileSync(file, join(project, file));
    mkdirSync(join(project, 'src/app'), { recursive: true });
    copyFileSync('src/index.css', join(project, 'src/index.css'));
    writeFileSync(join(project, 'next.config.mjs'), 'export default {}\n');
    symlinkSync(resolve('node_modules'), join(project, 'node_modules'));
    return project;
}

// The files the CLI shows, each under its path:
//   ├ src/components/login-form.tsx (create) 97 lines
//   │ ┌───
//   │ │ <one line of the file>
//   │ └───
function viewed(project, items) {
    const { stdout, status } = spawnSync(process.execPath, [shadcn, 'add', ...items, '--dry-run', '--view', 'src', '--cwd', project], {
        encoding: 'utf8',
        env: { ...process.env, NO_COLOR: '1' }
    });

    if (status !== 0) throw new Error(`shadcn add ${items.join(' ')} failed:\n${stdout}`);

    const files = new Map();
    let path = null;
    let lines = null;

    for (const line of stdout.split('\n')) {
        const header = /^├ (\S+) \(/.exec(line);

        if (header) path = header[1];
        else if (line.startsWith('│ ┌')) lines = [];
        else if (line.startsWith('│ └')) {
            files.set(path, `${lines.join('\n')}\n`);
            lines = null;
        } else if (lines !== null) lines.push(line.replace(/^│ │ ?/, ''));
    }
    return files;
}

// The components of `add --all`, and those it hides on this base, which `add`
// adds by name and a block takes: Base UI's sonner, beside its own toast.
function components(project) {
    const written = [];
    const hidden = COMPONENTS_HIDDEN_FROM_SELECTION.filter((one) => one.hiddenIn.includes(preset.split('-')[0])).map((one) => one.name);
    const files = new Map([...viewed(project, ['--all']), ...(hidden.length ? viewed(project, hidden) : [])]);

    for (const [path, text] of files) {
        if (!/^src\/(components\/ui|hooks|lib)\/[^/]+$/.test(path) || path === 'src/lib/utils.ts') continue;
        mkdirSync(dirname(join(root, path.slice(4))), { recursive: true });
        writeFileSync(join(root, path.slice(4)), text);
        written.push(path.slice(4));
    }
    console.log(`${root}: ${written.length} files`);
}

function block(project, name) {
    const folder = join(root, 'blocks', name);
    const files = new Map();

    for (const [path, text] of viewed(project, [name])) {
        if (!path.startsWith('src/app/') && !/^src\/components\/[^/]+$/.test(path)) continue;
        files.set(basename(path), text.replace(/"@\/components\/(?!ui\/)([\w-]+)"/g, '"./$1"'));
    }

    // shadcn/ui's previews, showcases of its site, have no page, and import
    // cards its CLI does not write.
    const resolves = (from) =>
        from.startsWith('./')
            ? files.has(`${from.slice(2)}.tsx`) || files.has(from.slice(2))
            : from === '@/lib/utils' || ['.tsx', '.ts'].some((ext) => existsSync(`${root}${from.slice(1)}${ext}`));
    const missing = [...files.values()]
        .flatMap((text) => [...text.matchAll(/from "(\.\/[^"]+|@\/[^"]+)"/g)].map((match) => match[1]))
        .filter((from) => !resolves(from));

    rmSync(folder, { recursive: true, force: true });
    if (!files.has('page.tsx')) {
        console.log(`left out ${name}: it has no page`);
        return;
    }
    if (missing.length) {
        console.log(`left out ${name}: it imports ${missing[0]}, which shadcn's CLI does not write`);
        return;
    }
    mkdirSync(folder, { recursive: true });
    for (const [file, text] of files) writeFileSync(join(folder, file), text);
    console.log(`${folder}: ${[...files.keys()].join(', ')}`);
}

// shadcn/ui's examples of each component, the pages of its site, each in a
// folder of its own of examples/, beside example.tsx, the frame its examples
// are shown in, as its CLI writes them.
async function examples(project) {
    const names = (await index()).filter((item) => item.type === 'registry:example').map((item) => item.name);

    for (const name of names) {
        const folder = join(root, 'examples', name);

        const files = new Map();

        for (const [path, text] of viewed(project, [name])) {
            if (/^src\/components\/[^/]+$/.test(path)) files.set(basename(path), text.replace(/"@\/components\/(?!ui\/)([\w-]+)"/g, '"./$1"'));
        }

        // One that imports a file of shadcn/ui's site, which its CLI does not
        // write, works in no project.
        const missing = [...files.values()]
            .flatMap((text) => [...text.matchAll(/from "(\.\/[^"]+|@\/[^"]+)"/g)].map((match) => match[1]))
            .find((from) =>
                from.startsWith('./')
                    ? !files.has(`${from.slice(2)}.tsx`) && !files.has(from.slice(2))
                    : from !== '@/lib/utils' && !['.tsx', '.ts'].some((ext) => existsSync(`${root}${from.slice(1)}${ext}`))
            );

        rmSync(folder, { recursive: true, force: true });
        if (missing) {
            console.log(`left out ${name}: it imports ${missing}, which shadcn's CLI does not write`);
            continue;
        }
        mkdirSync(folder, { recursive: true });
        for (const [file, text] of files) writeFileSync(join(folder, file), text);
    }
    console.log(`${root}/examples: ${names.length} examples`);
}

if (given[0] === '--icons') {
    await icons();
} else if (given[0] === '--items') {
    await items();
} else if (given[0] === '--examples') {
    const project = nextProject();

    try {
        await examples(project);
    } finally {
        rmSync(project, { recursive: true, force: true });
    }
} else {
    const project = nextProject();

    try {
        if (!given.length) components(project);
        for (const name of given.length ? given : await blockNames()) block(project, name);
        if (!given.length) {
            await icons();
            await items();
        }
    } finally {
        rmSync(project, { recursive: true, force: true });
    }
}
