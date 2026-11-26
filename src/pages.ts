import type { ComponentType } from "react"

// The demo's pages, each in Python and its TSX twin, loaded when it is shown:
// shadcn/ui's showcases, the canvas of its create page, and its blocks, whole
// pages. Each block has its own `app_sidebar`, which Python knows by that name
// alone, as a program has one.
const python = import.meta.glob<Record<string, ComponentType>>(["@/previews/*/page.py", "@/blocks/*/page.py"])
const tsx = import.meta.glob<{ default: ComponentType }>(["@/previews/*/page.tsx", "@/blocks/*/page.tsx"])
const sources = import.meta.glob<string>(["@/previews/*/page.tsx", "@/blocks/*/page.tsx"], { query: "?raw", import: "default" })

const named = (path: string) => path.split("/").at(-2)!

// shadcn's order: the showcases, the dashboard, the sidebars, the logins, the
// signups.
const ORDER = ["preview", "dashboard", "sidebar", "login", "signup"]

export const pages = Object.keys(python)
  .map(named)
  .sort((one, other) => ORDER.indexOf(one.split("-")[0]) - ORDER.indexOf(other.split("-")[0]) || one.localeCompare(other))

// A page's component: the TSX's default export, and in Python the function
// of the name its source gives it, which a build minifies in the TSX, among
// what its module also hands on of its imports, `BreadcrumbPage`.
export async function page(name: string, side: "python" | "tsx"): Promise<ComponentType> {
  const at = (paths: Record<string, unknown>) => Object.keys(paths).find((path) => named(path) === name)!

  if (side === "tsx") return (await tsx[at(tsx)]()).default

  const [, component] = /export default function (\w+)/.exec(await sources[at(sources)]())!

  return (await python[at(python)]())[component]
}
