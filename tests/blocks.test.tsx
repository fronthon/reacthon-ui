// @vitest-environment jsdom
// Every block of the preset written in Python, its page rendered against
// shadcn/ui's own: the same page, to the character.
import { act, createElement, Fragment, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { describe, expect, it } from "vitest"

import * as tooltip from "@/components/ui/tooltip"

// The provider the application's root holds tooltips in, where the preset has one.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType

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
// The sidebar's skeleton draws its width at random: each render draws the same
// numbers, from a seed set again before it. Not one number: React Aria's table
// draws two keys until they differ.
let seed = 1
Math.random = () => (seed = (seed * 16807) % 2147483647) / 2147483647

const tsx = import.meta.glob("@/blocks/*/page.tsx")
const py = import.meta.glob("@/blocks/*/page.py")
// A block is written in Python once each of its files is: login-form.tsx as login_form.py.
const sources = Object.keys(import.meta.glob("@/blocks/*/*.tsx"))
const written = new Set(Object.keys(import.meta.glob("@/blocks/*/*.py")))
const python = (path: string) => path.replace(/[^/]+$/, (file) => file.replace(/-/g, "_").replace(/\.tsx$/, ".py"))
const whole = (name: string) => sources.filter((path) => path.split("/").at(-2) === name).every((path) => written.has(python(path)))

// React's ids count every root the page has rendered, dnd-kit's every context
// and React Aria's its descriptions: each one is named by the order it first
// appears in.
function numbered(page: string) {
  const ids = new Map<string, number>()

  return page.replace(/_r_[0-9a-z]+_|\bDnd\w+-\d+|\breact-aria-description-\d+/g, (id) => {
    if (!ids.has(id)) ids.set(id, ids.size)
    return `_id${ids.get(id)}_`
  })
}

// A page as the application's root holds it, inside the tooltips' provider.
async function html(Page: ComponentType) {
  const container = document.createElement("div")
  let failed: unknown = null
  const root = createRoot(container, { onUncaughtError: (error) => (failed = error), onCaughtError: (error) => (failed = error) })
  const quiet = console.error

  console.error = () => {}
  document.body.append(container)
  seed = 1
  try {
    await act(() => root.render(createElement(TooltipProvider, null, createElement(Page))))
    if (failed) throw failed
    return numbered(document.body.innerHTML)
  } finally {
    await act(() => root.unmount())
    container.remove()
    document.body.innerHTML = ""
    console.error = quiet
  }
}

const blocks = Object.keys(tsx).map((path) => [path.split("/").at(-2)!, path.replace(/page\.tsx$/, "page.py")])

describe.each(blocks)("%s", (name, path) => {
  it("renders its page as the TSX one does", async ({ skip }) => {
    if (!whole(name)) skip("not all its files are written in Python yet")

    const Page = ((await tsx[path.replace(/page\.py$/, "page.tsx")]()) as { default: ComponentType }).default
    const pyModule = (await py[path]()) as Record<string, ComponentType>

    expect(await html(pyModule[Page.name])).toBe(await html(Page))
  })
})
