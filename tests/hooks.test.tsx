// @vitest-environment jsdom
// The components written with React's hooks, against shadcn/ui's own: the same
// tree rendered from TSX and from Python, then the same clicks and keys on
// each, and the same page after every one.
import { CalendarDate } from "@internationalized/date"
import { act, createElement, Fragment, type ComponentType } from "react"
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
import * as tooltip from "@/components/ui/tooltip"
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

// The provider the application's root holds tooltips in, where the preset has one.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

// What Radix, Base UI, embla and the media queries ask of the page and jsdom does not have.
Object.assign(Element.prototype, { scrollIntoView() {}, hasPointerCapture: () => false, releasePointerCapture() {}, getAnimations: () => [] })
;(globalThis as { CSS?: object }).CSS ??= { escape: (value: string) => value.replace(/[^\w-]/g, "\\$&") }
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
// The sidebar's skeleton draws its width at random: each scene draws the same
// numbers, from a seed set again before it. Not one number: React Aria's table
// draws two keys until they differ.
let seed = 1
Math.random = () => (seed = (seed * 16807) % 2147483647) / 2147483647
Object.defineProperty(navigator, "clipboard", { value: { writeText: () => Promise.resolve() }, configurable: true })

type Kit = Record<string, ComponentType<Record<string, unknown>>>
type Tree = (kit: Kit, seen: string[]) => ReturnType<typeof createElement>
type Step = [string, (page: HTMLElement) => void | Promise<void>]

function numbered(page: string) {
  const ids = new Map<string, number>()

  return page
    .replace(/_r_[0-9a-z]+_|\breact-aria-description-\d+/g, (id) => {
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

// Each page of the scene: rendered, then after each step, each with what the
// tree saw through its callbacks so far; then the cookie.
async function pages(tree: Tree, kit: Kit, steps: Step[]) {
  const container = document.createElement("div")
  const root = createRoot(container)
  const seen: string[] = []
  const out: string[] = []

  document.cookie = "sidebar_state=; max-age=0; path=/"
  document.body.append(container)
  seed = 1
  try {
    const page = () => `${numbered(document.body.innerHTML)}\nseen: ${seen.join(" | ")}`

    await act(() => root.render(tree(kit, seen)))
    out.push(page())
    for (const [, step] of steps) {
      // What the step sets off later, input-otp's selection, lands before the
      // page is read: the page held still, however long a render takes under
      // the load of the whole suite.
      await act(async () => {
        await step(container)
        let before = ""

        for (let tries = 0; tries < 20; tries++) {
          await new Promise((resolve) => setTimeout(resolve, 30))
          if (document.body.innerHTML === before) break
          before = document.body.innerHTML
        }
      })
      out.push(page())
    }
    out.push(`cookie: ${document.cookie}`)
  } finally {
    await act(() => root.unmount())
    container.remove()
    document.body.innerHTML = ""
  }
  return out
}

// A scene is written with the parts of the preset's base, as shadcn's own
// examples write it there.
const ARIA = process.env.PRESET!.startsWith("aria-")

// What the TSX page must show once rendered, so that a scene renders the
// state it is named after; and each step changes that page, or it plays
// nothing both sides could differ in.
const scenes: [string, Kit, Kit, Tree, Step[], string[]][] = []
const scene = (name: string, tsx: object, py: object, tree: Tree, steps: Step[] = [], shows: string[] = []) =>
  scenes.push([name, tsx as Kit, py as Kit, tree, steps, shows])
const h = createElement

// jsdom lays nothing out, so embla moves nothing on the page: what the
// carousel asks of it is seen instead.
type Api = Record<"canScrollNext" | "scrollNext" | "scrollPrev", (...args: unknown[]) => unknown>
const WATCHED = new WeakSet<Api>()
const watched = (seen: string[]) => (api: Api) => {
  seen.push(`api ${typeof api?.canScrollNext}`)
  if (!api || WATCHED.has(api)) return
  WATCHED.add(api)
  for (const name of ["scrollNext", "scrollPrev"] as const) {
    const own = api[name]

    api[name] = (...args) => (seen.push(name), own.apply(api, args))
  }
}

scene("Carousel", tsxCarousel, pyCarousel, (k, seen) =>
  h(k.Carousel, { opts: { loop: true }, setApi: watched(seen), className: "w-60" },
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

// React Aria's keys are its items' `id`, the others' their `value`; its toggle
// group says `selectionMode` where the others say `type`.
const key = (one: string) => (ARIA ? { id: one } : { value: one })
const toggles = (mode: string) => (ARIA ? { selectionMode: mode } : { type: mode })

for (const mode of ["single", "multiple"]) {
  scene(`ToggleGroup ${mode}`, tsxToggleGroup, pyToggleGroup, (k) =>
    h(k.ToggleGroup, { ...toggles(mode), variant: "outline", size: "sm", spacing: 0 },
      h(k.ToggleGroupItem, key("bold"), "B"),
      h(k.ToggleGroupItem, { ...key("italic"), variant: "default" }, "I")),
    [
      ["bold", (page) => click(page, "[data-slot=toggle-group-item]", 0)],
      ["italic", (page) => click(page, "[data-slot=toggle-group-item]", 1)]
    ]
  )
}
scene("ToggleGroup default", tsxToggleGroup, pyToggleGroup, (k) =>
  h(k.ToggleGroup, { ...toggles("single"), orientation: "vertical" }, h(k.ToggleGroupItem, key("a"), "A")),
  [],
  ["vertical"]
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

// React Aria's slider bounds itself by `minValue` and `maxValue`.
const bounds = (min: number | undefined, max: number | undefined) => (ARIA ? { minValue: min, maxValue: max } : { min, max })

scene("Slider", tsxSlider, pySlider, (k) => h(k.Slider, { defaultValue: [20, 80], ...bounds(undefined, 100), step: 10, "aria-label": "Range" }), [], ['"20"', '"80"'])
scene("Slider value", tsxSlider, pySlider, (k) => h(k.Slider, { value: [30], "aria-label": "Value" }), [], ['"30"'])
scene("Slider bare", tsxSlider, pySlider, (k) => h(k.Slider, { ...bounds(5, undefined), "aria-label": "Bare" }), [], ['"5"'])

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
  // The addon focuses the input, which the page says once told.
  [
    ["addon", (page) => {
      click(page, "[data-slot=input-group-addon]")
      page.setAttribute("data-focus", document.activeElement?.getAttribute("data-slot") ?? "none")
    }]
  ]
)

// React Aria's calendar is its own, of `@internationalized/date`'s dates, its
// days the cells of a grid; the others' is react-day-picker's, its days
// buttons in the cells.
const day = (page: HTMLElement, text: string) =>
  ([...page.querySelectorAll(ARIA ? "td [role=button]" : "td button")] as HTMLElement[])
    .find((one) => one.textContent === text && !one.hasAttribute("data-outside-month") && !one.closest("[data-outside]"))!
    .click()

if (ARIA) {
  scene("Calendar", tsxCalendar, pyCalendar, (k, seen) =>
    h(k.Calendar, {
      defaultValue: new CalendarDate(2026, 1, 10),
      onChange: (value: CalendarDate) => seen.push(`picked ${value.day}`),
      showWeekNumber: true,
      className: "rounded-md border"
    }),
    [
      ["pick the 15th", (page) => day(page, "15")],
      ["next month", (page) => click(page, "[slot=next]")]
    ],
    ["January 2026"]
  )
  scene("Calendar dropdown", tsxCalendar, pyCalendar, (k) =>
    h(k.RangeCalendar, { captionLayout: "dropdown", defaultFocusedValue: new CalendarDate(2026, 6, 1), buttonVariant: "outline", numberOfMonths: 2 }),
    [],
    ["June", "July"]
  )
} else {
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
      ["pick the 15th", (page) => day(page, "15")],
      ["next month", (page) => click(page, ".rdp-button_next")]
    ],
    ["January 2026"]
  )
  scene("Calendar dropdown", tsxCalendar, pyCalendar, (k) =>
    h(k.Calendar, { mode: "range", captionLayout: "dropdown", defaultMonth: new Date(2026, 5, 1), buttonVariant: "outline", numberOfMonths: 2 }),
    [],
    ["Jun", "Jul"]
  )
}

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

// React Aria's combobox lists its items as children, each its `id`, and
// opens as one types; the others' take `items` and a function of each.
scene("Combobox", tsxCombobox, pyCombobox, (k) =>
  ARIA
    ? h(k.Combobox, { allowsEmptyCollection: true, "aria-label": "Fruit" },
        h(k.ComboboxInput, { placeholder: "fruit", showClear: true }),
        h(k.ComboboxContent, null,
          h(k.ComboboxList, { renderEmptyState: () => h(k.ComboboxEmpty, null, "None") }, ...["Apple", "Banana"].map((item) => h(k.ComboboxItem, { key: item, id: item }, item)))))
    : h(k.Combobox, { items: ["Apple", "Banana"], defaultOpen: true },
        h(k.ComboboxInput, { placeholder: "fruit", showClear: true }),
        h(k.ComboboxContent, null,
          h(k.ComboboxEmpty, null, "None"),
          h(k.ComboboxList, null, (item: string) => h(k.ComboboxItem, { key: item, value: item }, item)))),
  ARIA ? [["type a", (page) => type(page.querySelector("input") as HTMLInputElement, "a")]] : [],
  ARIA ? ["fruit"] : ["Apple", "Banana"]
)

describe("shadcn/ui's components of React's hooks, written in Python", () => {
  it.for(scenes)("%s renders and behaves as the TSX one does", async ([, tsx, py, tree, steps, shows]) => {
    // A library may keep what an instance did for the next one, input-otp its
    // selection: each of the two compared renders after one more.
    await pages(tree, tsx, steps)
    const expected = await pages(tree, tsx, steps)
    const got = await pages(tree, py, steps)

    expect(expected[0]).toMatch(/<[a-z]/)
    for (const one of shows) expect(expected[0], `the page shows ${one}`).toContain(one)
    steps.forEach(([name], at) => expect(expected[at + 1], `${name} changes the page`).not.toBe(expected[at]))
    expected.forEach((page, at) => {
      let from = 0

      while (from < page.length && page[from] === got[at][from]) from++
      // Where the two first part, with what leads to it.
      const label = at === 0 ? "rendered" : at <= steps.length ? `after ${steps[at - 1][0]}` : "callbacks"

      expect(got[at].slice(Math.max(0, from - 60), from + 80), label).toBe(page.slice(Math.max(0, from - 60), from + 80))
    })
  })
})
