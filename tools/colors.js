// shadcn/ui's colors, those its create page offers, into src/colors.json for
// the demo: its seven grays, each the whole of a theme's variables, light and
// dark, and its other colors, an accent each that sets the primary, the
// charts and the sidebar's primary over a gray:
//   node tools/colors.js
import { writeFileSync } from 'node:fs';
import ts from 'typescript';

const SOURCE = 'https://raw.githubusercontent.com/shadcn-ui/ui/main/apps/v4/registry';
const source = async (file) => (await fetch(`${SOURCE}/${file}`)).text();
const { outputText } = ts.transpileModule(await source('themes.ts'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } });
const { THEMES } = await import(`data:text/javascript,${encodeURIComponent(outputText)}`);
const grays = JSON.parse(/\[([^\]]*)\]/.exec(await source('base-colors.ts'))[0]);
const colors = THEMES.map(({ name, title, cssVars }) => ({ name, title, gray: grays.includes(name), light: cssVars.light, dark: cssVars.dark }));

writeFileSync('src/colors.json', `${JSON.stringify(colors, null, 2)}\n`);
console.log(`src/colors.json: ${colors.filter((one) => one.gray).length} grays, ${colors.filter((one) => !one.gray).length} colors`);
