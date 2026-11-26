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

// A tree is written with the parts of the preset's base, as shadcn's own
// examples write it there: React Aria's dialog opens from its trigger, its
// tabs and items take an `id`, its states `isDisabled` or `defaultSelected`.
const BASE = process.env.PRESET!.split("-")[0]
const ARIA = BASE === "aria"

// What the TSX page must show, so that a tree renders the state it is named
// after, and not a page both sides leave the same by rendering nothing of it.
const twins: [string, Kit, Kit, Tree, string[]][] = []
const pair = (name: string, tsx: object, py: object, tree: Tree, shows: string[] = []) => twins.push([name, tsx as Kit, py as Kit, tree, shows])
const h = createElement
// A dialog or a menu opened by a button of the preset's own.
const tsxWithButton = (kit: object) => ({ ...kit, ...tsxButton })
const pyWithButton = (kit: object) => ({ ...kit, ...pyButton })

for (const variant of ["default", "outline", "secondary", "ghost", "destructive", "link", undefined]) {
  for (const size of ["default", "xs", "sm", "lg", "icon", "icon-xs", "icon-sm", "icon-lg", undefined]) {
    pair(`Button ${variant} ${size}`, tsxButton, pyButton, (k) => h(k.Button, { variant, size }, "go"))
  }
}
pair("Button className overrides", tsxButton, pyButton, (k) => h(k.Button, { className: "mt-2 px-8 bg-red-500" }, "go"))
pair("Button props", tsxButton, pyButton, (k) => h(k.Button, { id: "x", [ARIA ? "isDisabled" : "disabled"]: true, type: "submit", "aria-label": "send" }, "go"), ["disabled"])
if (ARIA) pair("Button as a link", tsxButton, pyButton, (k) => h(k.LinkButton, { href: "/docs", variant: "link" }, "docs"), ['href="/docs"'])
else pair("Button asChild", tsxButton, pyButton, (k) => h(k.Button, { asChild: true, variant: "link" }, h("a", { href: "/docs" }, "docs")), ['href="/docs"'])
pair("Card", tsxCard, pyCard, (k) =>
  h(k.Card, { size: "sm", className: "w-80" },
    h(k.CardHeader, null, h(k.CardTitle, null, "Title"), h(k.CardDescription, null, "Text"), h(k.CardAction, null, "x")),
    h(k.CardContent, { className: "flex" }, "body"),
    h(k.CardFooter, null, "foot"))
)
pair("Input", tsxInput, pyInput, (k) => h(k.Input, { type: "email", placeholder: "you@", className: "w-40", defaultValue: "a" }))
pair("Input no type", tsxInput, pyInput, (k) => h(k.Input, { disabled: true }))
pair("Label", tsxLabel, pyLabel, (k) => h(k.Label, { htmlFor: "name", className: "mb-1" }, "Name"))
pair("Checkbox", tsxCheckbox, pyCheckbox, (k) => h(k.Checkbox, { id: "news", [ARIA ? "defaultSelected" : "defaultChecked"]: true, className: "ml-2" }), ["lucide-check"])
pair("Checkbox unchecked", tsxCheckbox, pyCheckbox, (k) => h(k.Checkbox, { [ARIA ? "isDisabled" : "disabled"]: true }), ["disabled"])

for (const showCloseButton of [true, false]) {
  const inside = (k: Kit) => [
    h(k.DialogHeader, { key: "header" }, h(k.DialogTitle, null, "Title"), h(k.DialogDescription, null, "Text")),
    h(k.DialogFooter, { key: "footer", showCloseButton: !showCloseButton }, "footer"),
  ]

  pair(`Dialog open, close button ${showCloseButton}`, tsxWithButton(tsxDialog), pyWithButton(pyDialog), (k) =>
    ARIA
      ? h(k.DialogTrigger, { defaultOpen: true }, h(k.Button, { variant: "outline" }, "open"), h(k.Dialog, { showCloseButton, className: "sm:max-w-md" }, ...inside(k)))
      : h(k.Dialog, { defaultOpen: true }, h(k.DialogTrigger, null, "open"), h(k.DialogContent, { showCloseButton, className: "sm:max-w-md" }, ...inside(k))),
    ["Title", "Text", "footer", ...(showCloseButton ? ["sr-only"] : [])]
  )
}
pair("Dialog closed", tsxWithButton(tsxDialog), pyWithButton(pyDialog), (k) =>
  ARIA
    ? h(k.DialogTrigger, null, h(k.Button, { className: "t" }, "open"), h(k.Dialog, null, "hidden"))
    : h(k.Dialog, null, h(k.DialogTrigger, { className: "t" }, "open"), h(k.DialogContent, null, "hidden")),
  ["open"]
)

// React Aria's keys are its items' `id`, Radix's and Base UI's their `value`.
const key = (one: string) => (ARIA ? { id: one } : { value: one })
const disabled = ARIA ? { isDisabled: true } : { disabled: true }
const tabs = (selected: string) => (ARIA ? { defaultSelectedKey: selected } : { defaultValue: selected })

for (const variant of ["default", "line", undefined]) {
  pair(`Tabs ${variant}`, tsxTabs, pyTabs, (k) =>
    h(k.Tabs, tabs("a"),
      h(k.TabsList, { variant },
        h(k.TabsTrigger, key("a"), "A"),
        h(k.TabsTrigger, { ...key("b"), ...disabled }, "B")),
      h(k.TabsContent, key("a"), "first"),
      h(k.TabsContent, key("b"), "second")),
    ["first"]
  )
}
for (const value of ["one", undefined]) {
  const opened = ARIA ? { defaultExpandedKeys: value ? [value] : [] } : { type: "single", collapsible: true, defaultValue: value }

  pair(`Accordion ${value ?? "closed"}`, tsxAccordion, pyAccordion, (k) =>
    h(k.Accordion, { ...opened, className: "w-80" },
      h(k.AccordionItem, key("one"), h(k.AccordionTrigger, null, "One?"), h(k.AccordionContent, { className: "px-2" }, "Yes.")),
      h(k.AccordionItem, { ...key("two"), className: "x" }, h(k.AccordionTrigger, { className: "t" }, "Two?"), h(k.AccordionContent, null, "No."))),
    value ? ['aria-expanded="true"'] : ["One?", 'aria-expanded="false"']
  )
}
// Each base's select: Radix places its list over the trigger or under it,
// Base UI the same by `alignItemWithTrigger` and shows the label its `items`
// give a value, React Aria places it under the trigger or over it.
const SELECT = {
  radix: { root: {}, value: { placeholder: "plan" }, places: ["item-aligned", "popper"], content: (place: string) => ({ position: place }) },
  base: {
    root: { items: [{ label: "Free", value: "free" }, { label: "Pro", value: "pro" }, { label: "Team", value: "team" }] },
    value: null,
    places: ["item-aligned", "popper"],
    content: (place: string) => ({ alignItemWithTrigger: place === "item-aligned" }),
  },
  aria: { root: { placeholder: "plan", "aria-label": "Plan" }, value: null, places: ["bottom", "top"], content: (place: string) => ({ placement: place }) },
}[BASE]!

for (const open of [false, true]) {
  for (const position of SELECT.places) {
    pair(`Select ${open ? "open" : "closed"} ${position}`, tsxSelect, pySelect, (k) =>
      h(k.Select, { ...SELECT.root, defaultValue: "pro", defaultOpen: open },
        h(k.SelectTrigger, { size: "sm", className: "w-40" }, h(k.SelectValue, SELECT.value)),
        h(k.SelectContent, SELECT.content(position),
          h(k.SelectGroup, null,
            h(k.SelectLabel, null, "Plans"),
            h(k.SelectItem, key("free"), "Free"),
            h(k.SelectItem, key("pro"), "Pro")),
          h(k.SelectSeparator),
          h(k.SelectItem, { ...key("team"), ...disabled }, "Team"))),
      open ? ["Plans", "Free", "Team"] : ["Pro"]
    )
  }
}
pair("DropdownMenu open", tsxWithButton(tsxMenu), pyWithButton(pyMenu), (k) => {
  const account = h(k.DropdownMenuGroup, { key: "account" },
    h(k.DropdownMenuLabel, { inset: true }, "Account"),
    h(k.DropdownMenuItem, null, "Profile", h(k.DropdownMenuShortcut, null, "⇧⌘P")),
    h(k.DropdownMenuItem, { variant: "destructive", ...disabled }, "Delete"))
  const more = h(k.DropdownMenuSub, { key: "more" }, h(k.DropdownMenuSubTrigger, { inset: true }, "More"), h(k.DropdownMenuSubContent, null, h(k.DropdownMenuItem, null, "x")))

  // React Aria's checked and chosen items are a group's selection.
  return ARIA
    ? h(k.DropdownMenuTrigger, { defaultOpen: true },
        h(k.Button, null, "menu"),
        h(k.DropdownMenu, { className: "w-56", placement: "bottom end" },
          account,
          h(k.DropdownMenuSeparator),
          h(k.DropdownMenuGroup, { selectionMode: "multiple", selectedKeys: ["bar"] }, h(k.DropdownMenuItem, { id: "bar" }, "Bar"), h(k.DropdownMenuItem, { id: "panel", inset: true }, "Panel")),
          h(k.DropdownMenuGroup, { selectionMode: "single", selectedKeys: ["b"] }, h(k.DropdownMenuItem, { id: "a" }, "A"), h(k.DropdownMenuItem, { id: "b" }, "B")),
          more))
    : h(k.DropdownMenu, { defaultOpen: true },
        h(k.DropdownMenuTrigger, null, "menu"),
        h(k.DropdownMenuContent, { className: "w-56", align: "end" },
          account,
          h(k.DropdownMenuSeparator),
          h(k.DropdownMenuCheckboxItem, { checked: true }, "Bar"),
          h(k.DropdownMenuCheckboxItem, { checked: false, inset: true }, "Panel"),
          h(k.DropdownMenuRadioGroup, { value: "b" },
            h(k.DropdownMenuRadioItem, { value: "a" }, "A"),
            h(k.DropdownMenuRadioItem, { value: "b" }, "B")),
          more))
}, ["Account", "Profile", "Delete", "Panel", "More"])
pair("DropdownMenu closed", tsxWithButton(tsxMenu), pyWithButton(pyMenu), (k) =>
  ARIA
    ? h(k.DropdownMenuTrigger, null, h(k.Button, { className: "t" }, "menu"), h(k.DropdownMenu, null, h(k.DropdownMenuItem, null, "x")))
    : h(k.DropdownMenu, null, h(k.DropdownMenuTrigger, { className: "t" }, "menu")),
  ["menu"]
)
pair("Tabs vertical", tsxTabs, pyTabs, (k) =>
  h(k.Tabs, { ...tabs("b"), orientation: "vertical", className: "w-60" },
    h(k.TabsList, null, h(k.TabsTrigger, key("a"), "A"), h(k.TabsTrigger, key("b"), "B")),
    h(k.TabsContent, key("b"), "second")),
  ["second"]
)

describe("shadcn/ui's components written in Python", () => {
  it.for(twins)("%s renders as the TSX one does", async ([, tsx, py, tree, shows]) => {
    const expected = await html(tree, tsx)
    const got = await html(tree, py)
    let at = 0

    expect(expected).toMatch(/<[a-z]/)
    for (const one of shows) expect(expected, `the page shows ${one}`).toContain(one)
    while (at < expected.length && expected[at] === got[at]) at++
    // Where the two first part, with what leads to it.
    expect(got.slice(Math.max(0, at - 60), at + 80)).toBe(expected.slice(Math.max(0, at - 60), at + 80))
  })
})
