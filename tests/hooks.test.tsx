// @vitest-environment jsdom
// The components written with React's hooks, against shadcn/ui's own: the same
// tree rendered from TSX and from Python, then the same clicks and keys on
// each, and the same page after every one.
import { act, createElement, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { describe, expect, it } from "vitest"

import * as tsxCalendar from "@/components/ui/calendar"
import * as tsxCarousel from "@/components/ui/carousel"
import * as tsxChart from "@/components/ui/chart"
import * as tsxCodeBlock from "@/components/ui/code-block"
import * as tsxCombobox from "@/components/ui/combobox"
import * as tsxField from "@/components/ui/field"
import * as tsxInputOtp from "@/components/ui/input-otp"
import * as tsxInputGroup from "@/components/ui/input-group"
import * as tsxSidebar from "@/components/ui/sidebar"
import * as tsxSlider from "@/components/ui/slider"
import * as tsxToggleGroup from "@/components/ui/toggle-group"
import { TooltipProvider } from "@/components/ui/tooltip"
// @ts-expect-error a Python module
import * as pyCalendar from "@/components/ui/calendar.py"
// @ts-expect-error a Python module
import * as pyCarousel from "@/components/ui/carousel.py"
// @ts-expect-error a Python module
import * as pyChart from "@/components/ui/chart.py"
// @ts-expect-error a Python module
import * as pyCodeBlock from "@/components/ui/code_block.py"
// @ts-expect-error a Python module
import * as pyCombobox from "@/components/ui/combobox.py"
// @ts-expect-error a Python module
import * as pyField from "@/components/ui/field.py"
// @ts-expect-error a Python module
import * as pyInputOtp from "@/components/ui/input_otp.py"
// @ts-expect-error a Python module
import * as pyInputGroup from "@/components/ui/input_group.py"
// @ts-expect-error a Python module
import * as pySidebar from "@/components/ui/sidebar.py"
// @ts-expect-error a Python module
import * as pySlider from "@/components/ui/slider.py"
// @ts-expect-error a Python module
import * as pyToggleGroup from "@/components/ui/toggle_group.py"

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

// What Radix, embla and the media queries ask of the page and jsdom does not have.
Object.assign(Element.prototype, { scrollIntoView() {}, hasPointerCapture: () => false, releasePointerCapture() {} })
;(globalThis as { ResizeObserver?: unknown }).ResizeObserver ??= class {
  observe() {}
  unobserve() {}
  disconnect() {}
}
;(globalThis as { IntersectionObserver?: unknown }).IntersectionObserver ??= class {
  observe() {}
  unobserve() {}
  disconnect() {}
}
window.matchMedia ??= (() => ({ matches: false, addEventListener() {}, removeEventListener() {} })) as never
document.elementFromPoint ??= () => null
// The sidebar's skeleton draws its width at random.
Math.random = () => 0.5
Object.defineProperty(navigator, "clipboard", { value: { writeText: () => Promise.resolve() }, configurable: true })

type Kit = Record<string, ComponentType<Record<string, unknown>>>
type Tree = (kit: Kit, seen: string[]) => ReturnType<typeof createElement>
type Step = [string, (page: HTMLElement) => void | Promise<void>]

function numbered(page: string) {
  const ids = new Map<string, number>()

  return page
    .replace(/_r_[0-9a-z]+_/g, (id) => {
      if (!ids.has(id)) ids.set(id, ids.size)
      return `_id${ids.get(id)}_`
    })
    .replace(/ data-input-otp-ms[se]="\d+"/g, "")
}

const press = (target: EventTarget, init: KeyboardEventInit) =>
  target.dispatchEvent(new KeyboardEvent("keydown", { bubbles: true, cancelable: true, ...init }))
const click = (page: HTMLElement, selector: string, at = 0) => (page.querySelectorAll(selector)[at] as HTMLElement).click()

// Text typed into an input, as React hears it.
function type(input: HTMLInputElement, value: string) {
  Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, "value")!.set!.call(input, value)
  input.dispatchEvent(new Event("input", { bubbles: true }))
}

// Each page of the scene: rendered, then after each step. What the tree saw
// through its callbacks comes last.
async function pages(tree: Tree, kit: Kit, steps: Step[]) {
  const container = document.createElement("div")
  const root = createRoot(container)
  const seen: string[] = []
  const out: string[] = []

  document.cookie = "sidebar_state=; max-age=0; path=/"
  document.body.append(container)
  try {
    await act(() => root.render(tree(kit, seen)))
    out.push(numbered(document.body.innerHTML))
    for (const [, step] of steps) {
      // What the step sets off later, input-otp's selection, lands before the
      // page is read, however long a render takes.
      await act(async () => {
        await step(container)
        await new Promise((resolve) => setTimeout(resolve, 30))
      })
      out.push(numbered(document.body.innerHTML))
    }
    out.push(`seen: ${seen.join(" | ")}`, `cookie: ${document.cookie}`)
  } finally {
    await act(() => root.unmount())
    container.remove()
    document.body.innerHTML = ""
  }
  return out
}

const scenes: [string, Kit, Kit, Tree, Step[]][] = []
const scene = (name: string, tsx: object, py: object, tree: Tree, steps: Step[] = []) =>
  scenes.push([name, tsx as Kit, py as Kit, tree, steps])
const h = createElement

scene("Carousel", tsxCarousel, pyCarousel, (k, seen) =>
  h(k.Carousel, { opts: { loop: true }, setApi: (api: { canScrollNext?: unknown }) => seen.push(`api ${typeof api?.canScrollNext}`), className: "w-60" },
    h(k.CarouselContent, null, ...["one", "two", "three"].map((text) => h(k.CarouselItem, { key: text }, text))),
    h(k.CarouselPrevious),
    h(k.CarouselNext)),
  [
    ["arrow right", (page) => void press(page.querySelector("[data-slot=carousel]")!, { key: "ArrowRight" })],
    ["next", (page) => click(page, "[data-slot=carousel-next]")]
  ]
)
scene("Carousel vertical", tsxCarousel, pyCarousel, (k) =>
  h(k.Carousel, { orientation: "vertical" }, h(k.CarouselContent, null, h(k.CarouselItem, null, "one")), h(k.CarouselNext))
)

scene("Sidebar", tsxSidebar, pySidebar, (k, seen) =>
  h(TooltipProvider, null, h(k.SidebarProvider, { onOpenChange: (open: boolean) => seen.push(`open ${open}`) },
    h(k.Sidebar, { collapsible: "icon" },
      h(k.SidebarHeader, null, "head"),
      h(k.SidebarContent, null,
        h(k.SidebarGroup, null,
          h(k.SidebarGroupLabel, null, "Group"),
          h(k.SidebarMenu, null,
            h(k.SidebarMenuItem, null, h(k.SidebarMenuButton, { tooltip: "Home", isActive: true }, "Home")),
            h(k.SidebarMenuItem, null, h(k.SidebarMenuButton, { tooltip: { children: "Inbox", side: "left" } }, "Inbox")),
            h(k.SidebarMenuItem, null, h(k.SidebarMenuSkeleton, { showIcon: true }))))),
      h(k.SidebarRail)),
    h(k.SidebarInset, null, h(k.SidebarTrigger), "main"))),
  [
    ["trigger", (page) => click(page, "[data-slot=sidebar-trigger]")],
    ["ctrl+b", () => void press(window, { key: "b", ctrlKey: true })],
    ["rail", (page) => click(page, "[data-slot=sidebar-rail]")]
  ]
)
scene("Sidebar uncontrolled", tsxSidebar, pySidebar, (k) =>
  h(k.SidebarProvider, { defaultOpen: false },
    h(k.Sidebar, { side: "right", variant: "floating" }, h(k.SidebarContent, null, "x")),
    h(k.SidebarTrigger)),
  [["ctrl+b", () => void press(window, { key: "b", metaKey: true })]]
)
scene("Sidebar none", tsxSidebar, pySidebar, (k) =>
  h(k.SidebarProvider, null, h(k.Sidebar, { collapsible: "none" }, "fixed"))
)

for (const type_ of ["single", "multiple"]) {
  scene(`ToggleGroup ${type_}`, tsxToggleGroup, pyToggleGroup, (k) =>
    h(k.ToggleGroup, { type: type_, variant: "outline", size: "sm", spacing: 0 },
      h(k.ToggleGroupItem, { value: "bold" }, "B"),
      h(k.ToggleGroupItem, { value: "italic", variant: "default" }, "I")),
    [
      ["bold", (page) => click(page, "[data-slot=toggle-group-item]", 0)],
      ["italic", (page) => click(page, "[data-slot=toggle-group-item]", 1)]
    ]
  )
}
scene("ToggleGroup default", tsxToggleGroup, pyToggleGroup, (k) =>
  h(k.ToggleGroup, { type: "single", orientation: "vertical" }, h(k.ToggleGroupItem, { value: "a" }, "A"))
)

scene("InputOTP", tsxInputOtp, pyInputOtp, (k) =>
  h(k.InputOTP, { maxLength: 4 },
    h(k.InputOTPGroup, null, h(k.InputOTPSlot, { index: 0 }), h(k.InputOTPSlot, { index: 1 })),
    h(k.InputOTPSeparator),
    h(k.InputOTPGroup, null, h(k.InputOTPSlot, { index: 2 }), h(k.InputOTPSlot, { index: 3 }))),
  [
    ["focus", (page) => (page.querySelector("input") as HTMLInputElement).focus()],
    ["type 12", (page) => type(page.querySelector("input") as HTMLInputElement, "12")],
    ["type 1234", (page) => type(page.querySelector("input") as HTMLInputElement, "1234")]
  ]
)

scene("CodeBlock", tsxCodeBlock, pyCodeBlock, (k) =>
  h(k.CodeBlock, { size: "sm" },
    h(k.CodeBlockHeader, null, h(k.CodeBlockTitle, null, "app.py"), h(k.CodeBlockActions, null, h(k.CodeBlockCopyButton, { value: "print(1)" }))),
    h(k.CodeBlockContent, { lineNumbers: true, startLine: 3, wrap: true, style: { color: "red" } }, "a = 1\n\nb = 2\n"),
    h(k.CodeBlockContent, null, h(k.CodeBlockLine, { variant: "added" }, "x"), h(k.CodeBlockLine, null)),
    h(k.CodeBlockFooter, null, "foot")),
  [["copy", (page) => click(page, "[data-slot=code-block-copy-button]")]]
)

scene("Slider", tsxSlider, pySlider, (k) => h(k.Slider, { defaultValue: [20, 80], max: 100, step: 10 }))
scene("Slider value", tsxSlider, pySlider, (k) => h(k.Slider, { value: [30] }))
scene("Slider bare", tsxSlider, pySlider, (k) => h(k.Slider, { min: 5 }))

scene("Field", tsxField, pyField, (k) =>
  h(k.FieldSet, null,
    h(k.FieldLegend, { variant: "label" }, "Account"),
    h(k.FieldGroup, null,
      h(k.Field, { orientation: "horizontal", "data-invalid": true },
        h(k.FieldLabel, { htmlFor: "email" }, "Email"),
        h(k.FieldContent, null,
          h(k.FieldDescription, null, "We never share it."),
          h(k.FieldError, { errors: [{ message: "Required" }, { message: "Required" }, { message: "Too short" }] }))),
      h(k.Field, null, h(k.FieldError, { errors: [{ message: "Only one" }] })),
      h(k.Field, null, h(k.FieldError, { errors: [] })),
      h(k.Field, null, h(k.FieldError, null, "Given")),
      h(k.FieldSeparator, null, "or")))
)

scene("InputGroup", tsxInputGroup, pyInputGroup, (k) =>
  h(k.InputGroup, null,
    h(k.InputGroupInput, { placeholder: "search" }),
    h(k.InputGroupAddon, { align: "inline-end" }, h(k.InputGroupText, null, "⌘K"), h(k.InputGroupButton, { size: "icon-xs" }, "x"))),
  [
    ["addon", (page) => click(page, "[data-slot=input-group-addon]")],
    ["focused", () => void document.body.setAttribute("data-focus", document.activeElement?.getAttribute("data-slot") ?? "none")]
  ]
)

scene("Calendar", tsxCalendar, pyCalendar, (k, seen) =>
  h(k.Calendar, {
    mode: "single",
    defaultMonth: new Date(2026, 0, 1),
    selected: new Date(2026, 0, 10),
    onSelect: (day?: Date) => seen.push(`picked ${day?.getDate()}`),
    showWeekNumber: true,
    className: "rounded-md border"
  }),
  [
    ["pick the 15th", (page) => click(page, "[data-day]", 18)],
    ["next month", (page) => click(page, ".rdp-button_next")]
  ]
)
scene("Calendar dropdown", tsxCalendar, pyCalendar, (k) =>
  h(k.Calendar, { mode: "range", captionLayout: "dropdown", defaultMonth: new Date(2026, 5, 1), buttonVariant: "outline", numberOfMonths: 2 })
)

const config = {
  desktop: { label: "Desktop", color: "#2563eb" },
  mobile: { label: "Mobile", theme: { light: "#60a5fa", dark: "#1e3a8a" } },
  other: { label: "Other" }
}
const payload = [
  { dataKey: "desktop", name: "desktop", value: 1280, color: "#2563eb", payload: { fill: "#111" } },
  { dataKey: "mobile", name: "mobile", value: 3.5, type: "line" },
  { dataKey: "hidden", name: "hidden", value: 1, type: "none" }
]
scene("ChartContainer", tsxChart, pyChart, (k) =>
  h(k.ChartContainer, { id: "sales", config, className: "h-40" }, h("div", null, "plot"))
)
scene("ChartStyle", tsxChart, pyChart, (k) => h("div", null, h(k.ChartStyle, { id: "x", config }), h(k.ChartStyle, { id: "y", config: { other: {} } })))
for (const indicator of ["dot", "line", "dashed"]) {
  scene(`ChartTooltipContent ${indicator}`, tsxChart, pyChart, (k) =>
    h(k.ChartContainer, { config },
      h(k.ChartTooltipContent, { active: true, payload, indicator, label: "desktop", labelKey: undefined, className: "w-40" }))
  )
}
scene("ChartTooltipContent one, formatted", tsxChart, pyChart, (k) =>
  h(k.ChartContainer, { config },
    h(k.ChartTooltipContent, {
      active: true,
      payload: payload.slice(0, 1),
      indicator: "line",
      labelFormatter: (value: unknown) => `label ${String(value)}`,
      formatter: (value: unknown, name: unknown) => `${String(name)} = ${String(value)}`
    }))
)
scene("ChartTooltipContent hidden", tsxChart, pyChart, (k) =>
  h(k.ChartContainer, { config }, h("div", null, h(k.ChartTooltipContent, { active: false, payload }), h(k.ChartTooltipContent, { active: true, payload, hideLabel: true, hideIndicator: true })))
)
scene("ChartLegendContent", tsxChart, pyChart, (k) =>
  h(k.ChartContainer, { config }, h(k.ChartLegendContent, { payload, verticalAlign: "top" }))
)

scene("Combobox", tsxCombobox, pyCombobox, (k) =>
  h(k.Combobox, { items: ["Apple", "Banana"], defaultOpen: true },
    h(k.ComboboxInput, { placeholder: "fruit", showClear: true }),
    h(k.ComboboxContent, null,
      h(k.ComboboxEmpty, null, "None"),
      h(k.ComboboxList, null, (item: string) => h(k.ComboboxItem, { key: item, value: item }, item))))
)

describe("shadcn/ui's components of React's hooks, written in Python", () => {
  it.each(scenes)("%s renders and behaves as the TSX one does", async (_name, tsx, py, tree, steps) => {
    // A library may keep what an instance did for the next one, input-otp its
    // selection: each of the two compared renders after one more.
    await pages(tree, tsx, steps)
    const expected = await pages(tree, tsx, steps)
    const got = await pages(tree, py, steps)

    expect(expected[0].length).toBeGreaterThan(100)
    expected.forEach((page, at) => {
      let from = 0

      while (from < page.length && page[from] === got[at][from]) from++
      // Where the two first part, with what leads to it.
      const label = at === 0 ? "rendered" : at <= steps.length ? `after ${steps[at - 1][0]}` : "callbacks"

      expect(got[at].slice(Math.max(0, from - 60), from + 80), label).toBe(page.slice(Math.max(0, from - 60), from + 80))
    })
  })
})
