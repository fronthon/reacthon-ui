// The demo of every preset, each built in a folder of its own of dist/, which
// its toolbar switches between, keeping the page it shows; dist/ itself opens
// shadcn's default preset, and holds the public folder once, the registry:
//   node tools/demo.js
import { spawnSync } from 'node:child_process';
import { cpSync, readdirSync, rmSync, writeFileSync } from 'node:fs';

// What `npx shadcn init --defaults` makes.
const DEFAULT = 'base-nova';

rmSync('dist', { recursive: true, force: true });
for (const preset of readdirSync('src/presets')) {
    const { status } = spawnSync(process.execPath, ['node_modules/vite/bin/vite.js', 'build', '--outDir', `dist/${preset}`, '--logLevel', 'warn'], {
        stdio: 'inherit',
        env: { ...process.env, DEMO_PRESET: preset, DEMO_ALL: '1' }
    });

    if (status !== 0) process.exit(status ?? 1);
    console.log(`dist/${preset}`);
}
cpSync('public', 'dist', { recursive: true });
writeFileSync(
    'dist/index.html',
    `<!doctype html>\n<meta charset="utf-8">\n<title>Reacthon UI</title>\n<script>location.replace("${DEFAULT}/" + location.hash)</script>\n`
);
