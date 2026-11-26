// @vitest-environment jsdom
// The blocks whose handlers do something, against shadcn/ui's own: the same
// page rendered from TSX and from Python, then the same clicks and keys on
// each, and the same page after every one; an error a handler raises is
// part of what is compared.
import { act, createElement, Fragment, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { toast } from "sonner"
import { describe, expect, it } from "vitest"

import { Toaster } from "@/components/ui/sonner"
import * as tooltip from "@/components/ui/tooltip"

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

// What Radix, Base UI, the charts and the media queries ask of the page and jsdom does not have.
Object.assign(Element.prototype, { scrollIntoView() {}, hasPointerCapture: () => false, releasePointerCapture() {}, getAnimations: () => [] })
;(globalThis as { CSS?: object }).CSS ??= { escape: (value: string) => value.replace(/[^\w-]/g, "\\$&") }
;(globalThis as { ResizeObserver?: unknown }).ResizeObserver ??= class {
  observe() {}
  unobserve() {}
  disconnect() {}
}
window.matchMedia ??= (() => ({ matches: false, addEventListener() {}, removeEventListener() {} })) as never
document.elementFromPoint ??= () => null
// Base UI's exits wait for jsdom's frames, which come or not before a page is
// read: off, by Base UI's own switch, a checkbox's tick leaves at once.
;(globalThis as { BASE_UI_ANIMATIONS_DISABLED?: boolean }).BASE_UI_ANIMATIONS_DISABLED = true
// The blocks draw at random, sidebar-09 its mails: each scene draws the same
// numbers, from a seed set again before it.
let seed = 1
Math.random = () => (seed = (seed * 16807) % 2147483647) / 2147483647

// The provider the application's root holds tooltips in, where the preset has
// one, and the toaster it shows a block's toasts in.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType

const tsx = import.meta.glob("@/blocks/*/page.tsx")
const py = import.meta.glob("@/blocks/*/page.py")

type Step = [string, (page: HTMLElement) => void | Promise<unknown>]

const click = (page: HTMLElement, selector: string, at = 0) => (page.querySelectorAll(selector)[at] as HTMLElement).click()
// A press of the main button, which a menu's trigger opens on, as a click does.
const press = (page: HTMLElement, selector: string, at = 0) => {
  const one = page.querySelectorAll(selector)[at] as HTMLElement

  one.dispatchEvent(new MouseEvent("pointerdown", { bubbles: true, button: 0 }))
  one.dispatchEvent(new MouseEvent("mousedown", { bubbles: true, button: 0 }))
}
const button = (page: HTMLElement, text: string) => [...page.querySelectorAll("button")].find((one) => one.textContent?.includes(text))!.click()

// The frames a library waits for, Radix's tabs theirs, React Aria the focus it
// gives back once its menu has closed: passed until the page holds still, on
// both alike, however long a render takes under the load of the whole suite.
async function settled() {
  let before = ""

  for (let tries = 0; tries < 20; tries++) {
    await new Promise((resolve) => setTimeout(resolve, 30))
    if (document.body.innerHTML === before) return
    before = document.body.innerHTML
  }
}

function numbered(page: string) {
  const ids = new Map<string, number>()

  return page.replace(/_r_[0-9a-z]+_|\bDnd\w+-\d+|\breact-aria-description-\d+/g, (id) => {
    if (!ids.has(id)) ids.set(id, ids.size)
    return `_id${ids.get(id)}_`
  })
}

async function pages(Page: ComponentType, steps: Step[]) {
  const container = document.createElement("div")
  const root = createRoot(container)
  const errors: string[] = []
  const heard = (event: ErrorEvent) => errors.push(String(event.error?.message ?? event.message))
  const out: string[] = []
  const quiet = console.error

  console.error = () => {}
  window.addEventListener("error", heard)
  document.body.append(container)
  seed = 1
  try {
    await act(async () => {
      root.render(createElement(TooltipProvider, null, createElement(Page), createElement(Toaster)))
      await settled()
    })
    out.push(numbered(document.body.innerHTML))
    for (const [, step] of steps) {
      await act(async () => {
        await step(container)
        await settled()
      })
      out.push(numbered(document.body.innerHTML))
    }
    out.push(`errors: ${errors.join(" | ")}`)
  } finally {
    // Sonner hands a toaster that mounts the toasts still up, which the next
    // page would show: dismissed with the page.
    await act(() => void toast.dismiss())
    await act(() => root.unmount())
    container.remove()
    document.body.innerHTML = ""
    window.removeEventListener("error", heard)
    console.error = quiet
  }
  return out
}

// The gestures of the preset's base, as one makes them there: React Aria
// opens a menu on a press of the button its trigger wraps, which a click is
// to it, and selects a table's rows by checkboxes of its own naming.
const ARIA = process.env.PRESET!.startsWith("aria-")

const scenes: [string, Step[]][] = [
  [
    "sidebar-07",
    [
      // React Aria's group opens from the button its disclosure names its trigger.
      ["open a group", (page) => click(page, ARIA ? "[data-slot=sidebar-content] [aria-expanded]" : "[data-slot=collapsible-trigger]")],
      // Its menu in a portal, outside the page.
      ["open the teams", (page) => (ARIA ? click(page, "[data-slot=sidebar-header] [aria-haspopup]") : press(page, "[data-slot=dropdown-menu-trigger]"))],
      ["pick a team", () => click(document.body, "[data-slot=dropdown-menu-item]", 1)],
    ],
  ],
  ["sidebar-09", [["pick the drafts", (page) => click(page, "[data-slot=sidebar-menu-button]", 2)]]],
  [
    "dashboard-01",
    [
      ["select all", (page) => click(page, ARIA ? '[aria-label="Select All"]' : '[aria-label="Select all"]')],
      ["select a row", (page) => click(page, ARIA ? '[aria-label="Select"]' : '[aria-label="Select row"]', 1)],
      ["next page", (page) => button(page, "Go to next page")],
      ["save a target", (page) => page.querySelector("form")!.requestSubmit()],
      // The toast of the save, a second later.
      ["saved", () => new Promise((resolve) => setTimeout(resolve, 1100))],
    ],
  ],
]

// Each page and its Python, loaded before the scenes, since compiling them is
// not what the scenes time, and one after the other: each block has its own
// `app_sidebar`, which Python knows by that name alone, as a program has one.
const loaded: [ComponentType, ComponentType][] = []

for (const [name] of scenes) {
  const Page = ((await tsx[Object.keys(tsx).find((path) => path.includes(`/${name}/`))!]()) as { default: ComponentType }).default
  const pyModule = (await py[Object.keys(py).find((path) => path.includes(`/${name}/`))!]()) as Record<string, ComponentType>

  loaded.push([Page, pyModule[Page.name]])
}

describe("shadcn/ui's blocks, written in Python, in use", () => {
  // Each step changes shadcn's own page, or it plays nothing the two could
  // differ in.
  // Four pages of each scene, the dashboard's each waiting a second for its toast.
  it.for(scenes.map((scene, at) => [...scene, ...loaded[at]] as const))("%s renders and behaves as the TSX one does", { timeout: 30_000 }, async ([, steps, Page, PyPage]) => {
    // React Aria keeps how the last page was used, by pointer or not, for the
    // next one, and sidebar-09 shuffles its own mails in place: each of the two
    // compared is its second, after a page of the same scene.
    await pages(Page, steps)
    await pages(PyPage, steps)
    const expected = await pages(Page, steps)
    const got = await pages(PyPage, steps)

    expect(expected[0]).toMatch(/<[a-z]/)
    steps.forEach(([name], at) => expect(expected[at + 1], `${name} changes the page`).not.toBe(expected[at]))
    expected.forEach((page, at) => {
      let from = 0

      while (from < page.length && page[from] === got[at][from]) from++
      const label = at === 0 ? "rendered" : at <= steps.length ? `after ${steps[at - 1][0]}` : "errors"

      expect(got[at].slice(Math.max(0, from - 60), from + 80), label).toBe(page.slice(Math.max(0, from - 60), from + 80))
    })
  })
})
