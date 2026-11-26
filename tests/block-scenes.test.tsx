// @vitest-environment jsdom
// The blocks whose handlers do something, against shadcn/ui's own: the same
// page rendered from TSX and from Python, then the same clicks and keys on
// each, and the same page after every one; an error a handler raises is
// part of what is compared.
import { act, createElement, Fragment, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { describe, expect, it } from "vitest"

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

// The provider the application's root holds tooltips in, where the preset has one.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType

const tsx = import.meta.glob("@/blocks/*/page.tsx")
const py = import.meta.glob("@/blocks/*/page.py")

type Step = [string, (page: HTMLElement) => void]

const click = (page: HTMLElement, selector: string, at = 0) => (page.querySelectorAll(selector)[at] as HTMLElement).click()
const button = (page: HTMLElement, text: string) => [...page.querySelectorAll("button")].find((one) => one.textContent?.includes(text))!.click()

// The frame a library waits for, Radix's tabs theirs, passed on both alike,
// however long a render takes.
const settled = () => new Promise((resolve) => setTimeout(resolve, 30))

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
      root.render(createElement(TooltipProvider, null, createElement(Page)))
      await settled()
    })
    out.push(numbered(document.body.innerHTML))
    for (const [, step] of steps) {
      await act(async () => {
        step(container)
        await settled()
      })
      out.push(numbered(document.body.innerHTML))
    }
    out.push(`errors: ${errors.join(" | ")}`)
  } finally {
    await act(() => root.unmount())
    container.remove()
    document.body.innerHTML = ""
    window.removeEventListener("error", heard)
    console.error = quiet
  }
  return out
}

const scenes: [string, Step[]][] = [
  ["sidebar-07", [["open a group", (page) => click(page, "[data-slot=collapsible-trigger]")]]],
  ["sidebar-09", [["pick the drafts", (page) => click(page, "[data-slot=sidebar-menu-button]", 2)]]],
  [
    "dashboard-01",
    [
      ["select all", (page) => click(page, '[aria-label="Select all"]')],
      ["select a row", (page) => click(page, '[aria-label="Select row"]', 1)],
      ["next page", (page) => button(page, "Go to next page")],
      ["save a target", (page) => page.querySelector("form")!.requestSubmit()],
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
  // A scene of Radix's parts, which this preset's TSX cannot play either, says
  // nothing of the Python: skipped, and counted so.
  it.for(scenes.map((scene, at) => [...scene, ...loaded[at]] as const))("%s renders and behaves as the TSX one does", async ([, steps, Page, PyPage], { skip }) => {
    let expected: string[] = []

    try {
      expected = await pages(Page, steps)
    } catch (error) {
      skip(`not this preset's components: ${String(error).slice(0, 80)}`)
    }

    const got = await pages(PyPage, steps)

    expect(expected[0]).toMatch(/<[a-z]/)
    expected.forEach((page, at) => {
      let from = 0

      while (from < page.length && page[from] === got[at][from]) from++
      const label = at === 0 ? "rendered" : at <= steps.length ? `after ${steps[at - 1][0]}` : "errors"

      expect(got[at].slice(Math.max(0, from - 60), from + 80), label).toBe(page.slice(Math.max(0, from - 60), from + 80))
    })
  })
})
