// @vitest-environment jsdom
// Every block of src/blocks written in Python, its page rendered against
// shadcn/ui's own: the same page, to the character.
import { act, createElement, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { describe, expect, it } from "vitest"

import { TooltipProvider } from "@/components/ui/tooltip"

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

// What Radix, the charts and the media queries ask of the page and jsdom does not have.
Object.assign(Element.prototype, { scrollIntoView() {}, hasPointerCapture: () => false, releasePointerCapture() {} })
;(globalThis as { ResizeObserver?: unknown }).ResizeObserver ??= class {
  observe() {}
  unobserve() {}
  disconnect() {}
}
window.matchMedia ??= (() => ({ matches: false, addEventListener() {}, removeEventListener() {} })) as never
document.elementFromPoint ??= () => null
// The sidebar's skeleton draws its width at random.
Math.random = () => 0.5

const tsx = import.meta.glob("/src/blocks/*/page.tsx")
const py = import.meta.glob("/src/blocks/*/page.py")
// A block is written in Python once each of its files is: login-form.tsx as login_form.py.
const sources = Object.keys(import.meta.glob("/src/blocks/*/*.tsx"))
const written = new Set(Object.keys(import.meta.glob("/src/blocks/*/*.py")))
const python = (path: string) => path.replace(/[^/]+$/, (file) => file.replace(/-/g, "_").replace(/\.tsx$/, ".py"))
const whole = (name: string) => sources.filter((path) => path.split("/").at(-2) === name).every((path) => written.has(python(path)))

// React's ids count every root the page has rendered, and dnd-kit's every
// context: each one is named by the order it first appears in.
function numbered(page: string) {
  const ids = new Map<string, number>()

  return page.replace(/_r_[0-9a-z]+_|\bDnd\w+-\d+/g, (id) => {
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

const blocks = Object.keys(py)
  .map((path) => [path.split("/").at(-2)!, path])
  .filter(([name]) => whole(name))

describe.each(blocks)("%s", (name, path) => {
  it("renders its page as the TSX one does", async () => {
    const Page = ((await tsx[`/src/blocks/${name}/page.tsx`]()) as { default: ComponentType }).default
    const pyModule = (await py[path]()) as Record<string, ComponentType>

    expect(await html(pyModule[Page.name])).toBe(await html(Page))
  })
})
