// @vitest-environment jsdom
// Each component written in Python against shadcn/ui's own, rendered with the
// same props: the same page, to the character.
import { act, createElement, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { describe, expect, it } from "vitest"

import * as tsxButton from "@/components/ui/button"
import * as tsxCard from "@/components/ui/card"
import * as tsxInput from "@/components/ui/input"
import * as tsxLabel from "@/components/ui/label"
import * as tsxCheckbox from "@/components/ui/checkbox"
// @ts-expect-error a Python module
import * as pyButton from "@/components/ui/button.py"
// @ts-expect-error a Python module
import * as pyCard from "@/components/ui/card.py"
// @ts-expect-error a Python module
import * as pyInput from "@/components/ui/input.py"
// @ts-expect-error a Python module
import * as pyLabel from "@/components/ui/label.py"
// @ts-expect-error a Python module
import * as pyCheckbox from "@/components/ui/checkbox.py"
import * as tsxDialog from "@/components/ui/dialog"
import * as tsxTabs from "@/components/ui/tabs"
// @ts-expect-error a Python module
import * as pyDialog from "@/components/ui/dialog.py"
// @ts-expect-error a Python module
import * as pyTabs from "@/components/ui/tabs.py"

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

type Kit = Record<string, ComponentType<Record<string, unknown>>>
type Tree = (kit: Kit) => ReturnType<typeof createElement>

// React's ids count every root the page has rendered: each one is named by the
// order it first appears in, so two pages compare where they use them.
function numbered(page: string) {
  const ids = new Map<string, number>()

  return page.replace(/_r_[0-9a-z]+_/g, (id) => {
    if (!ids.has(id)) ids.set(id, ids.size)
    return `_id${ids.get(id)}_`
  })
}

// The whole body, where a portal renders as well.
async function html(tree: Tree, kit: Kit) {
  const container = document.createElement("div")
  const root = createRoot(container)

  document.body.append(container)
  await act(() => root.render(tree(kit)))
  const out = numbered(document.body.innerHTML)
  await act(() => root.unmount())
  container.remove()
  return out
}

const twins: [string, Kit, Kit, Tree][] = []
const pair = (name: string, tsx: object, py: object, tree: Tree) => twins.push([name, tsx as Kit, py as Kit, tree])
const h = createElement

for (const variant of ["default", "outline", "secondary", "ghost", "destructive", "link", undefined]) {
  for (const size of ["default", "xs", "sm", "lg", "icon", "icon-xs", "icon-sm", "icon-lg", undefined]) {
    pair(`Button ${variant} ${size}`, tsxButton, pyButton, (k) => h(k.Button, { variant, size }, "go"))
  }
}
pair("Button className overrides", tsxButton, pyButton, (k) => h(k.Button, { className: "mt-2 px-8 bg-red-500" }, "go"))
pair("Button props", tsxButton, pyButton, (k) => h(k.Button, { id: "x", disabled: true, type: "submit", "aria-label": "send" }, "go"))
pair("Button asChild", tsxButton, pyButton, (k) => h(k.Button, { asChild: true, variant: "link" }, h("a", { href: "/docs" }, "docs")))
pair("Card", tsxCard, pyCard, (k) =>
  h(k.Card, { size: "sm", className: "w-80" },
    h(k.CardHeader, null, h(k.CardTitle, null, "Title"), h(k.CardDescription, null, "Text"), h(k.CardAction, null, "x")),
    h(k.CardContent, { className: "flex" }, "body"),
    h(k.CardFooter, null, "foot"))
)
pair("Input", tsxInput, pyInput, (k) => h(k.Input, { type: "email", placeholder: "you@", className: "w-40", defaultValue: "a" }))
pair("Input no type", tsxInput, pyInput, (k) => h(k.Input, { disabled: true }))
pair("Label", tsxLabel, pyLabel, (k) => h(k.Label, { htmlFor: "name", className: "mb-1" }, "Name"))
pair("Checkbox", tsxCheckbox, pyCheckbox, (k) => h(k.Checkbox, { id: "news", defaultChecked: true, className: "ml-2" }))
pair("Checkbox unchecked", tsxCheckbox, pyCheckbox, (k) => h(k.Checkbox, { disabled: true }))
for (const showCloseButton of [true, false]) {
  pair(`Dialog open, close button ${showCloseButton}`, tsxDialog, pyDialog, (k) =>
    h(k.Dialog, { defaultOpen: true },
      h(k.DialogTrigger, null, "open"),
      h(k.DialogContent, { showCloseButton, className: "sm:max-w-md" },
        h(k.DialogHeader, null, h(k.DialogTitle, null, "Title"), h(k.DialogDescription, null, "Text")),
        h(k.DialogFooter, { showCloseButton: !showCloseButton }, "footer")))
  )
}
pair("Dialog closed", tsxDialog, pyDialog, (k) =>
  h(k.Dialog, null, h(k.DialogTrigger, { className: "t" }, "open"), h(k.DialogContent, null, "hidden"))
)
for (const variant of ["default", "line", undefined]) {
  pair(`Tabs ${variant}`, tsxTabs, pyTabs, (k) =>
    h(k.Tabs, { defaultValue: "a" },
      h(k.TabsList, { variant },
        h(k.TabsTrigger, { value: "a" }, "A"),
        h(k.TabsTrigger, { value: "b", disabled: true }, "B")),
      h(k.TabsContent, { value: "a" }, "first"),
      h(k.TabsContent, { value: "b" }, "second"))
  )
}
pair("Tabs vertical", tsxTabs, pyTabs, (k) =>
  h(k.Tabs, { defaultValue: "b", orientation: "vertical", className: "w-60" },
    h(k.TabsList, null, h(k.TabsTrigger, { value: "a" }, "A"), h(k.TabsTrigger, { value: "b" }, "B")),
    h(k.TabsContent, { value: "b" }, "second"))
)

describe("shadcn/ui's components written in Python", () => {
  it.each(twins)("%s renders as the TSX one does", async (_name, tsx, py, tree) => {
    const expected = await html(tree, tsx)
    const got = await html(tree, py)
    let at = 0

    while (at < expected.length && expected[at] === got[at]) at++
    // Where the two first part, with what leads to it.
    expect(got.slice(Math.max(0, at - 60), at + 80)).toBe(expected.slice(Math.max(0, at - 60), at + 80))
  })
})
