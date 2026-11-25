// shadcn/ui's blocks, each in its own folder of src/blocks, as shadcn's CLI
// writes them into a project:
//   node tools/blocks.js [block...]
// The CLI writes a block's page only into a Next.js project: the files are read
// with --dry-run from one made for the purpose, of the same components.json. A
// page and its components stand side by side, each component imported as
// ./name, which is where Python looks first.
import { spawnSync } from 'node:child_process';
import { copyFileSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const BLOCKS = 'src/blocks';
const shadcn = fileURLToPath(import.meta.resolve('shadcn'));
const { style } = JSON.parse(readFileSync('components.json', 'utf8'));

async function blockNames() {
    const response = await fetch(`https://ui.shadcn.com/r/styles/${style}/registry.json`);
    const { items } = await response.json();

    return items.filter((item) => item.type === 'registry:block').map((item) => item.name);
}

function nextProject() {
    const project = mkdtempSync(join(tmpdir(), 'reacthon-ui-blocks-'));

    for (const file of ['components.json', 'package.json', 'tsconfig.json', 'tsconfig.app.json', 'tsconfig.node.json']) {
        copyFileSync(file, join(project, file));
    }
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
function shown(output) {
    const files = new Map();
    let path = null;
    let lines = null;

    for (const line of output.split('\n')) {
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

function add(project, name) {
    const { stdout, status } = spawnSync(process.execPath, [shadcn, 'add', name, '--dry-run', '--view', 'src', '--cwd', project], {
        encoding: 'utf8',
        env: { ...process.env, NO_COLOR: '1' }
    });

    if (status !== 0) throw new Error(`shadcn add ${name} failed:\n${stdout}`);

    const folder = join(BLOCKS, name);
    const files = new Map();

    for (const [path, text] of shown(stdout)) {
        if (!path.startsWith('src/app/') && !/^src\/components\/[^/]+$/.test(path)) continue;
        files.set(basename(path), text.replace(/"@\/components\/(?!ui\/)([\w-]+)"/g, '"./$1"'));
    }

    // shadcn/ui's previews import cards its CLI does not write.
    const resolves = (from) =>
        from.startsWith('./')
            ? files.has(`${from.slice(2)}.tsx`) || files.has(from.slice(2))
            : existsSync(`src${from.slice(1)}.tsx`) || existsSync(`src${from.slice(1)}.ts`);
    const missing = [...files.values()]
        .flatMap((text) => [...text.matchAll(/from "(\.\/[^"]+|@\/[^"]+)"/g)].map((match) => match[1]))
        .filter((from) => !resolves(from));

    rmSync(folder, { recursive: true, force: true });
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
    const names = process.argv.length > 2 ? process.argv.slice(2) : await blockNames();

    for (const name of names) add(project, name);
} finally {
    rmSync(project, { recursive: true, force: true });
}
