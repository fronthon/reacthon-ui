// Every component of the preset written in Python, its icons in each library
// shadcn's CLI writes them in, as `npx reacthon-ui add` writes them for a
// project of that library: each icon of each file found in it, in its place,
// and no Lucide left. The pages themselves were twinned against the CLI's TSX
// in each library.
import { describe, expect, it } from "vitest"

import { iconLibraries, withIcons } from "../bin/icons.js"
import icons from "@/icons.json"

const files = import.meta.glob("@/components/ui/*.py", { query: "?raw", import: "default", eager: true }) as Record<string, string>

describe.each(iconLibraries.filter((one) => one !== "lucide"))("%s", (library) => {
  it("writes every icon of every component in it", () => {
    for (const [path, content] of Object.entries(files)) {
      const file = path.split("/").pop()!
      const own = (icons as Record<string, unknown>)[`components/ui/${file.replace(/_/g, "-").replace(/\.py$/, ".tsx")}`]

      if (!own) continue

      const target = `src/components/ui/${file}`
      const [written] = withIcons({ files: [{ target, content }], meta: { icons: { [target]: own } } }, library).files

      expect(written.content, file).not.toMatch(/lucide-react/)
      expect(written.content.match(/<\{/g)?.length, file).toBe(content.match(/<\{/g)?.length)
    }
  })
})
