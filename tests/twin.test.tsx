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
import * as tsxAccordion from "@/components/ui/accordion"
import * as tsxSelect from "@/components/ui/select"
import * as tsxMenu from "@/components/ui/dropdown-menu"
// @ts-expect-error a Python module
import * as pyAccordion from "@/components/ui/accordion.py"
// @ts-expect-error a Python module
import * as pySelect from "@/components/ui/select.py"
// @ts-expect-error a Python module
import * as pyMenu from "@/components/ui/dropdown_menu.py"

// What Radix's select, Base UI's animations and React Aria's ids ask of the
// page and jsdom does not have.
Object.assign(Element.prototype, {
  scrollIntoView() {},
  hasPointerCapture: () => false,
  releasePointerCapture() {},
  getAnimations: () => [],
})
;(globalThis as { CSS?: object }).CSS ??= { escape: (value: string) => value.replace(/[^\w-]/g, "\\$&") }

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

type Kit = Record<string, ComponentType<Record<string, unknown>>>
type Tree = (kit: Kit) => ReturnType<typeof createElement>

// React's ids count every root the page has rendered, and React Aria's its
// descriptions: each one is named by the order it first appears in, so two
// pages compare where they use them.
function numbered(page: string) {
  const ids = new Map<string, number>()

  return page.replace(/_r_[0-9a-z]+_|\breact-aria-description-\d+/g, (id) => {
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
for (const value of ["one", undefined]) {
  pair(`Accordion ${value ?? "closed"}`, tsxAccordion, pyAccordion, (k) =>
    h(k.Accordion, { type: "single", collapsible: true, defaultValue: value, className: "w-80" },
      h(k.AccordionItem, { value: "one" }, h(k.AccordionTrigger, null, "One?"), h(k.AccordionContent, { className: "px-2" }, "Yes.")),
      h(k.AccordionItem, { value: "two", className: "x" }, h(k.AccordionTrigger, { className: "t" }, "Two?"), h(k.AccordionContent, null, "No.")))
  )
}
for (const open of [false, true]) {
  for (const position of ["item-aligned", "popper"]) {
    pair(`Select ${open ? "open" : "closed"} ${position}`, tsxSelect, pySelect, (k) =>
      h(k.Select, { defaultValue: "pro", defaultOpen: open },
        h(k.SelectTrigger, { size: "sm", className: "w-40" }, h(k.SelectValue, { placeholder: "plan" })),
        h(k.SelectContent, { position },
          h(k.SelectGroup, null,
            h(k.SelectLabel, null, "Plans"),
            h(k.SelectItem, { value: "free" }, "Free"),
            h(k.SelectItem, { value: "pro" }, "Pro")),
          h(k.SelectSeparator),
          h(k.SelectItem, { value: "team", disabled: true }, "Team")))
    )
  }
}
pair("DropdownMenu open", tsxMenu, pyMenu, (k) =>
  h(k.DropdownMenu, { defaultOpen: true },
    h(k.DropdownMenuTrigger, null, "menu"),
    h(k.DropdownMenuContent, { className: "w-56", align: "end" },
      h(k.DropdownMenuGroup, null,
        h(k.DropdownMenuLabel, { inset: true }, "Account"),
        h(k.DropdownMenuItem, null, "Profile", h(k.DropdownMenuShortcut, null, "⇧⌘P")),
        h(k.DropdownMenuItem, { variant: "destructive", disabled: true }, "Delete")),
      h(k.DropdownMenuSeparator),
      h(k.DropdownMenuCheckboxItem, { checked: true }, "Bar"),
      h(k.DropdownMenuCheckboxItem, { checked: false, inset: true }, "Panel"),
      h(k.DropdownMenuRadioGroup, { value: "b" },
        h(k.DropdownMenuRadioItem, { value: "a" }, "A"),
        h(k.DropdownMenuRadioItem, { value: "b" }, "B")),
      h(k.DropdownMenuSub, null, h(k.DropdownMenuSubTrigger, { inset: true }, "More"), h(k.DropdownMenuSubContent, null, h(k.DropdownMenuItem, null, "x")))))
)
pair("DropdownMenu closed", tsxMenu, pyMenu, (k) => h(k.DropdownMenu, null, h(k.DropdownMenuTrigger, { className: "t" }, "menu")))
pair("Tabs vertical", tsxTabs, pyTabs, (k) =>
  h(k.Tabs, { defaultValue: "b", orientation: "vertical", className: "w-60" },
    h(k.TabsList, null, h(k.TabsTrigger, { value: "a" }, "A"), h(k.TabsTrigger, { value: "b" }, "B")),
    h(k.TabsContent, { value: "b" }, "second"))
)

describe("shadcn/ui's components written in Python", () => {
  // A tree of another preset's components, which this preset's TSX cannot
  // render either, says nothing of the Python: skipped, and counted so.
  it.for(twins)("%s renders as the TSX one does", async ([, tsx, py, tree], { skip }) => {
    let expected = ""

    try {
      expected = await html(tree, tsx)
    } catch (error) {
      skip(`not this preset's components: ${String(error).slice(0, 80)}`)
    }

    const got = await html(tree, py)
    let at = 0

    expect(expected).toMatch(/<[a-z]/)
    while (at < expected.length && expected[at] === got[at]) at++
    // Where the two first part, with what leads to it.
    expect(got.slice(Math.max(0, at - 60), at + 80)).toBe(expected.slice(Math.max(0, at - 60), at + 80))
  })
})
