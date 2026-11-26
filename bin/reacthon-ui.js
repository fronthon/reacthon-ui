#!/usr/bin/env node
import { spawnSync } from "node:child_process"
import { existsSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs"
import { tmpdir } from "node:os"
import { basename, join } from "node:path"
import { fileURLToPath } from "node:url"

import { withIcons } from "./icons.js"

const registries = fileURLToPath(new URL("../public/r/", import.meta.url))
const valued = new Set(["-c", "--cwd", "-p", "--path"])
// shadcn's options of a value one may leave out, which take the next argument
// where it is not an option, as its CLI reads them.
const optional = new Set(["--diff", "--view"])

const [command, ...args] = process.argv.slice(2)
if (command !== "add") {
  console.error("Usage: reacthon-ui add <component or block>...")
  process.exit(1)
}

// The components of the project's preset, which its components.json names.
const at = args.findIndex((arg) => arg === "-c" || arg === "--cwd")
const config = join(at === -1 ? process.cwd() : args[at + 1], "components.json")
if (!existsSync(config)) {
  console.error("reacthon-ui: no components.json: npx shadcn init makes it")
  process.exit(1)
}
const { style, iconLibrary = "lucide" } = JSON.parse(readFileSync(config, "utf8"))
const registry = join(registries, style, "/")
if (!existsSync(registry)) {
  console.error(`reacthon-ui: no preset ${style} yet, only ${readdirSync(registries).join(", ")}`)
  process.exit(1)
}

// shadcn's own names would fetch its TSX components: every name, and --all, are
// ours, --all its components and not its blocks, as shadcn's.
const passed = []
for (let i = 0; i < args.length; i++) {
  const arg = args[i]
  if (arg === "-a" || arg === "--all") {
    for (const file of readdirSync(registry)) {
      if (file !== "registry.json" && JSON.parse(readFileSync(registry + file, "utf8")).type === "registry:ui") passed.push(registry + file)
    }
  } else if (arg.startsWith("-")) {
    passed.push(arg)
    if (valued.has(arg) || (optional.has(arg) && i + 1 < args.length && !args[i + 1].startsWith("-"))) passed.push(args[++i])
  } else if (existsSync(`${registry}${arg}.json`)) {
    passed.push(`${registry}${arg}.json`)
  } else {
    console.error(`reacthon-ui: no component or block named ${arg}`)
    process.exit(1)
  }
}

// The items with their icons in the project's library, as shadcn's CLI writes
// its own for it.
const written = mkdtempSync(join(tmpdir(), "reacthon-ui-"))
const items = passed.map((one) => {
  if (!one.startsWith(registry)) return one

  const path = join(written, basename(one))
  writeFileSync(path, JSON.stringify(withIcons(JSON.parse(readFileSync(one, "utf8")), iconLibrary)))
  return path
})

const shadcn = fileURLToPath(import.meta.resolve("shadcn"))
const { status } = spawnSync(process.execPath, [shadcn, "add", ...items], { stdio: "inherit" })
rmSync(written, { recursive: true, force: true })
process.exit(status ?? 1)
