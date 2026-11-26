import { existsSync, readdirSync } from "node:fs"
import { resolve } from "node:path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import reacthon from "reacthon"
import { defineConfig } from "vite"

// A preset of shadcn/ui laid out as a project of its own: `@` is its folder,
// as `src` is in a project shadcn's CLI writes into, the helpers aside, which
// every preset shares.
const preset = (name: string) => ({
  plugins: [reacthon({ path: ["src/lib", `src/presets/${name}/components/ui`] }), react(), tailwindcss()],
  resolve: {
    alias: [
      { find: /^@\/lib\/utils$/, replacement: resolve(import.meta.dirname, "src/lib/utils") },
      { find: /^@\//, replacement: `${resolve(import.meta.dirname, "src/presets", name)}/` },
    ],
    // Reacthon is linked from ../reacthon, which has a React of its own.
    dedupe: ["react", "react-dom"],
  },
  // The demo's preset, and with DEMO_ALL the presets `tools/demo.js` builds
  // beside it, which its toolbar switches between.
  define: {
    __DEMO_PRESET__: JSON.stringify(name),
    __DEMO_PRESETS__: process.env.DEMO_ALL ? JSON.stringify(readdirSync("src/presets")) : "null",
  },
})

// https://vite.dev/config/
export default defineConfig({
  // Relative paths, so that Pages serves the demo under the repository's name.
  base: "./",
  // The registry, which `tools/demo.js` copies once beside the presets' builds.
  publicDir: process.env.DEMO_ALL ? false : "public",
  // The demo, on the preset the project was made with, or the one DEMO_PRESET
  // names.
  ...preset(process.env.DEMO_PRESET ?? "radix-nova"),
  // The twins, on each preset, which they are told: a tree is written with
  // the parts of its base, as one writes it there; the CLI, once; and the
  // demo's blocks in Chrome, on one preset of each base, whose parts the
  // browser sees behave: a style is the same parts in other classes, which the
  // twins compare. Each page a minute at most.
  test: {
    projects: [
      ...readdirSync("src/presets").map((name) => ({
        ...preset(name),
        // The pages of shadcn/ui's site the preset has fetched, its showcases
        // and on one of each base its examples, Next.js's image and link theirs
        // as a page renders them elsewhere.
        test: {
          name,
          include: ["tests/*.test.tsx", ...(["examples", "previews"].some((one) => existsSync(`src/presets/${name}/${one}`)) ? ["tests/examples/*.test.tsx"] : [])],
          env: { PRESET: name },
          // A page of shadcn's showcases, its 30 cards twice, under the load
          // of the 24 presets at once.
          testTimeout: 30_000,
          alias: { "next/image": resolve(import.meta.dirname, "tests/examples/next.tsx"), "next/link": resolve(import.meta.dirname, "tests/examples/next.tsx") },
        },
      })),
      { test: { name: "cli", include: ["tests/cli/*.test.ts"], environment: "node" } },
      ...["radix-nova", "base-nova", "aria-nova"].map((name) => ({
        test: { name: `browser ${name}`, include: ["tests/browser/*.test.ts"], environment: "node", env: { DEMO_PRESET: name }, testTimeout: 60_000, hookTimeout: 120_000 },
      })),
    ],
  },
})
