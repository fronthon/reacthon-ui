// A preset of shadcn/ui, its components and its blocks, in its folder of
// src/presets, as shadcn's CLI writes them into a project of that preset:
//   node tools/preset.js <preset> [block...]
// Its components, its hooks and its lib, the helpers aside, which every preset
// shares; then each block in a folder of its own of blocks/, its page beside
// its components, each imported as ./name, which is where Python looks first.
// Given blocks, those alone. The CLI writes a block's page only into a Next.js
// project: the files are read with --dry-run from one made for the purpose.
import { spawnSync } from 'node:child_process';
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const shadcn = fileURLToPath(import.meta.resolve('shadcn'));
const [preset, ...given] = process.argv.slice(2);
const root = join('src/presets', preset ?? '');

if (!preset) {
    console.error('Usage: node tools/preset.js <preset> [block...]');
    process.exit(1);
}

async function blockNames() {
    const response = await fetch(`https://ui.shadcn.com/r/styles/${preset}/registry.json`);
    const { items } = await response.json();

    return items.filter((item) => item.type === 'registry:block').map((item) => item.name);
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

function components(project) {
    const written = [];

    for (const [path, text] of viewed(project, ['--all'])) {
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

const project = nextProject();

try {
    if (!given.length) components(project);
    for (const name of given.length ? given : await blockNames()) block(project, name);
} finally {
    rmSync(project, { recursive: true, force: true });
}
