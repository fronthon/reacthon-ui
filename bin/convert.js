// `reacthon-ui convert <file or folder>...`: the project's own TSX, its
// components and pages, written in Python beside it, as tools/tsx2py.js writes
// shadcn/ui's. A `.py` the project holds already is kept, as one may have
// changed it, unless `--overwrite` says, as shadcn's CLI keeps a file it would
// write.
import { existsSync, readdirSync, statSync, writeFileSync } from "node:fs"
import { basename, dirname, join, relative } from "node:path"

import { convertFiles } from "../tools/tsx2py.js"

const SKIPPED = new Set(["node_modules", ".git", ".next", "dist", "build"])

// A file as it is, a folder as its TSX and its folders', none of a library's.
function tsx(path) {
  if (!statSync(path).isDirectory()) return [path]

  return readdirSync(path).flatMap((name) => {
    const one = join(path, name)

    if (SKIPPED.has(name)) return []
    return statSync(one).isDirectory() ? tsx(one) : name.endsWith(".tsx") ? [one] : []
  })
}

export function convert(args) {
  const overwrite = args.includes("-o") || args.includes("--overwrite")
  const paths = args.filter((arg) => !arg.startsWith("-"))
  const missing = paths.find((path) => !existsSync(path))

  if (paths.length === 0) {
    console.error("Usage: reacthon-ui convert <file or folder>... [--overwrite]")
    return 1
  }
  if (missing !== undefined) {
    console.error(`reacthon-ui: no file or folder ${missing}`)
    return 1
  }

  let left = 0

  for (const { file, python, error } of convertFiles(paths.flatMap(tsx))) {
    const out = join(dirname(file), `${basename(file).replace(/\.tsx?$/, "").replace(/-/g, "_")}.py`)
    const shown = relative(process.cwd(), out)

    if (error) {
      left += 1
      console.log(`left out ${relative(process.cwd(), file)}: ${error}`)
    } else if (existsSync(out) && !overwrite) {
      console.log(`kept ${shown}, which is there: --overwrite writes it again`)
    } else {
      writeFileSync(out, python)
      console.log(`written ${shown}`)
    }
  }

  return left === 0 ? 0 : 1
}
