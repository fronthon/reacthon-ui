#!/usr/bin/env node
import { spawnSync } from "node:child_process"
import { existsSync, readdirSync, readFileSync } from "node:fs"
import { join } from "node:path"
import { fileURLToPath } from "node:url"

const registries = fileURLToPath(new URL("../public/r/", import.meta.url))
const valued = new Set(["-c", "--cwd", "-p", "--path"])

const [command, ...args] = process.argv.slice(2)
if (command !== "add") {
  console.error("Usage: reacthon-ui add <component>...")
  process.exit(1)
}

// The components of the project's preset, which its components.json names.
const at = args.findIndex((arg) => arg === "-c" || arg === "--cwd")
const config = join(at === -1 ? process.cwd() : args[at + 1], "components.json")
if (!existsSync(config)) {
  console.error("reacthon-ui: no components.json: npx shadcn init makes it")
  process.exit(1)
}
const { style } = JSON.parse(readFileSync(config, "utf8"))
const registry = join(registries, style, "/")
if (!existsSync(registry)) {
  console.error(`reacthon-ui: no preset ${style} yet, only ${readdirSync(registries).join(", ")}`)
  process.exit(1)
}

// shadcn's own names would fetch its TSX components: every name, and --all, are ours.
const passed = []
for (let i = 0; i < args.length; i++) {
  const arg = args[i]
  if (arg === "-a" || arg === "--all") {
    for (const file of readdirSync(registry)) {
      if (file !== "registry.json") passed.push(registry + file)
    }
  } else if (arg.startsWith("-")) {
    passed.push(arg)
    if (valued.has(arg)) passed.push(args[++i])
  } else if (existsSync(`${registry}${arg}.json`)) {
    passed.push(`${registry}${arg}.json`)
  } else {
    console.error(`reacthon-ui: no component named ${arg}`)
    process.exit(1)
  }
}

const shadcn = fileURLToPath(import.meta.resolve("shadcn"))
const { status } = spawnSync(process.execPath, [shadcn, "add", ...passed], { stdio: "inherit" })
process.exit(status ?? 1)
