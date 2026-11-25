import { resolve } from "node:path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import reacthon from "reacthon"
import { defineConfig } from "vite"

// https://vite.dev/config/
export default defineConfig({
  // Relative paths, so that Pages serves the demo under the repository's name.
  base: "./",
  plugins: [reacthon({ path: ["src/lib", "src/components/ui"] }), react(), tailwindcss()],
  resolve: {
    alias: {
      "@": resolve(import.meta.dirname, "./src"),
    },
    // Reacthon is linked from ../reacthon, which has a React of its own.
    dedupe: ["react", "react-dom"],
  },
})
