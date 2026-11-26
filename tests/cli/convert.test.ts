// `npx reacthon-ui convert` in a project of its own: its components and
// pages written in Python beside them, a page importing a component of the
// project as Python, a `.py` already there kept unless --overwrite says.
import { spawnSync } from "node:child_process"
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { afterAll, describe, expect, it } from "vitest"

const cli = fileURLToPath(new URL("../../bin/reacthon-ui.js", import.meta.url))
const project = mkdtempSync(join(tmpdir(), "reacthon-ui-convert-"))
const FILES: Record<string, string> = {
  "tsconfig.json": JSON.stringify({
    compilerOptions: { jsx: "react-jsx", strict: true, module: "esnext", moduleResolution: "bundler", target: "es2022", skipLibCheck: true, paths: { "@/*": ["./src/*"] } },
    include: ["src"],
  }),
  "src/components/team-card.tsx": `import { Button } from "@/components/ui/button"
import { StarIcon } from "lucide-react"

export function TeamCard({ name, onPick }: { name: string; onPick: (name: string) => void }) {
  return (
    <div className="card">
      <StarIcon />
      {name}
      <Button onClick={() => onPick(name)}>pick</Button>
    </div>
  )
}
`,
  "src/app/page.tsx": `import { TeamCard } from "@/components/team-card"

export default function Page() {
  return <main>{["one", "two"].map((name) => <TeamCard key={name} name={name} onPick={() => null} />)}</main>
}
`,
}

for (const [path, text] of Object.entries(FILES)) {
  mkdirSync(dirname(join(project, path)), { recursive: true })
  writeFileSync(join(project, path), text)
}
afterAll(() => rmSync(project, { recursive: true, force: true }))

const run = (...args: string[]) => spawnSync(process.execPath, [cli, "convert", ...args], { cwd: project, encoding: "utf8" })
const read = (path: string) => readFileSync(join(project, path), "utf8")

describe("npx reacthon-ui convert", () => {
  it("writes a folder's components and pages in Python beside them", () => {
    const { status, stdout } = run("src")

    expect([status, stdout.trim().split("\n").sort()]).toEqual([0, ["written src/app/page.py", "written src/components/team_card.py"]])
    expect(read("src/components/team_card.py")).toContain('from button import Button\n\n__js__ = {"lucide-react": ["StarIcon"]}')
    expect(read("src/app/page.py")).toContain("\nfrom team_card import TeamCard\n")
  })

  it("keeps a .py already there, and writes it again with --overwrite", () => {
    writeFileSync(join(project, "src/app/page.py"), "# mine\n")

    expect(run("src/app/page.tsx").stdout.trim()).toBe("kept src/app/page.py, which is there: --overwrite writes it again")
    expect(read("src/app/page.py")).toBe("# mine\n")
    expect(run("src/app/page.tsx", "--overwrite").stdout.trim()).toBe("written src/app/page.py")
    expect(read("src/app/page.py")).toContain("\nfrom team_card import TeamCard\n")
  })

  it("names what it cannot convert, and what is not there", () => {
    writeFileSync(join(project, "src/components/odd.tsx"), "export function Odd() {\n  label: for (;;) break label\n  return null\n}\n")

    const odd = run("src/components/odd.tsx")
    const none = run("src/nowhere")

    expect([odd.status, odd.stdout]).toEqual([1, expect.stringMatching(/^left out src\/components\/odd\.tsx: /)])
    expect([none.status, none.stderr.trim()]).toEqual([1, "reacthon-ui: no file or folder src/nowhere"])
  })
})
