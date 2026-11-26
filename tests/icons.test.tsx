// Every component and every block of the preset written in Python, its icons
// in each library shadcn's CLI writes them in, as `npx reacthon-ui add` writes
// them for a project of that library: each icon of each file found in it, in
// its place, and no Lucide left. The pages themselves were twinned against the
// CLI's TSX in each library.
import { describe, expect, it } from "vitest"

import { iconLibraries, withIcons } from "../bin/icons.js"
import icons from "@/icons.json"

const files = import.meta.glob(["@/components/ui/*.py", "@/blocks/*/*.py"], { query: "?raw", import: "default", eager: true }) as Record<string, string>

describe.each(iconLibraries.filter((one) => one !== "lucide"))("%s", (library) => {
  it("writes every icon of every component and block in it", () => {
    for (const [path, content] of Object.entries(files)) {
      if (!content.includes('"lucide-react"')) continue

      // Its place in the preset's folder, as icons.json names its TSX one.
      const placed = /(components\/ui|blocks\/[^/]+)\/[^/]+$/.exec(path)![0]
      const own = (icons as Record<string, unknown>)[placed.replace(/[^/]+$/, (file) => file.replace(/_/g, "-").replace(/\.py$/, ".tsx"))]

      expect(own, placed).toBeDefined()

      const [written] = withIcons({ files: [{ target: placed, content }], meta: { icons: { [placed]: own } } }, library).files

      expect(written.content, placed).not.toMatch(/lucide-react/)
      expect(written.content.match(/<\{/g)?.length, placed).toBe(content.match(/<\{/g)?.length)
    }
  })
})
