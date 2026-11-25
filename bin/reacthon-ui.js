#!/usr/bin/env node
import { spawnSync } from "node:child_process"
import { existsSync, readdirSync } from "node:fs"
import { fileURLToPath } from "node:url"

const registry = fileURLToPath(new URL("../public/r/", import.meta.url))
const valued = new Set(["-c", "--cwd", "-p", "--path"])

const [command, ...args] = process.argv.slice(2)
if (command !== "add") {
  console.error("Usage: reacthon-ui add <component>...")
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
