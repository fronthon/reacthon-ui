// The twin run on the components tools/tsx2py.js writes, in generated/, in
// place of the ones written by hand.
import { resolve } from "node:path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import reacthon from "reacthon"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [reacthon({ path: ["src/lib", "generated"] }), react(), tailwindcss()],
  resolve: {
    alias: [
      { find: /^@\/components\/ui\/(.*)\.py$/, replacement: resolve(import.meta.dirname, "./generated/$1.py") },
      { find: "@", replacement: resolve(import.meta.dirname, "./src") },
    ],
    dedupe: ["react", "react-dom"],
  },
})
