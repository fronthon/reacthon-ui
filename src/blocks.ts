import type { ComponentType } from "react"

// The blocks of the demo's preset, each page in Python and its TSX twin,
// loaded when it is shown: each block has its own `app_sidebar`, which Python
// knows by that name alone, as a program has one.
const python = import.meta.glob<Record<string, ComponentType>>("@/blocks/*/page.py")
const tsx = import.meta.glob<{ default: ComponentType }>("@/blocks/*/page.tsx")

const named = (path: string) => path.split("/").at(-2)!

// shadcn's order: the dashboard, the sidebars, the logins, the signups.
const ORDER = ["dashboard", "sidebar", "login", "signup"]

export const blocks = Object.keys(python)
  .map(named)
  .sort((one, other) => ORDER.indexOf(one.split("-")[0]) - ORDER.indexOf(other.split("-")[0]) || one.localeCompare(other))

// A block's page, `Page`, `LoginPage` or `SignupPage` as its TSX names it,
// among what its module also hands on of its imports, `BreadcrumbPage`.
export async function page(name: string, side: "python" | "tsx"): Promise<ComponentType> {
  const at = (paths: Record<string, unknown>) => Object.keys(paths).find((path) => named(path) === name)!

  if (side === "tsx") return (await tsx[at(tsx)]()).default

  const module = await python[at(python)]()

  return Object.entries(module).find(([key]) => /^(Login|Signup)?Page$/.test(key))![1]
}
