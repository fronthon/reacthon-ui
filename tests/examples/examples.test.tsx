// @vitest-environment jsdom
// The pages of shadcn/ui's site, converted by `reacthon-ui convert` as a
// project's own TSX is: each converted, and its Python rendered against its
// TSX, the same page to the character. Its showcases on every preset, the
// canvas of its create page; and its examples of each component on one preset
// of each base, whose examples are fetched: a style is the same parts in other
// classes, which the twins compare.
import { act, createElement, Fragment, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { beforeAll, describe, expect, it } from "vitest"

import * as tooltip from "@/components/ui/tooltip"

const highlighter = import.meta.glob<{ loadHighlighter: (language: string) => Promise<unknown> }>("@/lib/highlighter.tsx")

// Each language of shiki that the lib lists, loaded before the pages: the first
// page to ask for one renders before it has loaded, the next ones after.
beforeAll(async () => {
  for (const load of Object.values(highlighter)) {
    const { loadHighlighter } = await load()

    await Promise.all(["bash", "css", "diff", "html", "javascript", "json", "jsx", "markdown", "python", "sql", "tsx", "typescript", "yaml"].map(loadHighlighter))
  }
})

// The provider the application's root holds tooltips in, where the preset has one.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

// What the libraries ask of the page and jsdom does not have.
Object.assign(Element.prototype, { scrollIntoView() {}, hasPointerCapture: () => false, releasePointerCapture() {}, getAnimations: () => [] })
;(globalThis as { CSS?: object }).CSS ??= { escape: (value: string) => value.replace(/[^\w-]/g, "\\$&") }
for (const name of ["ResizeObserver", "IntersectionObserver"]) {
  ;(globalThis as Record<string, unknown>)[name] ??= class {
    observe() {}
    unobserve() {}
    disconnect() {}
  }
}
window.matchMedia ??= (() => ({ matches: false, addEventListener() {}, removeEventListener() {} })) as never
document.elementFromPoint ??= () => null
let seed = 1
Math.random = () => (seed = (seed * 16807) % 2147483647) / 2147483647

const tsx = import.meta.glob(["@/examples/*/*-example.tsx", "@/previews/*/page.tsx"])
const py = import.meta.glob(["@/examples/*/*_example.py", "@/previews/*/page.py"])

// input-otp marks the selection of the second input it sees, whichever renders it.
function numbered(page: string) {
  const ids = new Map<string, number>()

  return page
    .replace(/_r_[0-9a-z]+_|\bDnd\w+-\d+|\breact-aria-description-\d+/g, (id) => {
      if (!ids.has(id)) ids.set(id, ids.size)
      return `_id${ids.get(id)}_`
    })
    .replace(/ data-input-otp-ms[se]="\d+"/g, "")
}

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

const examples = Object.keys(tsx).map((path) => [path.split("/").at(-2)!, path] as const)

describe.each(examples)("%s", (name, path) => {
  it("is converted, and renders as the TSX one does", async () => {
    const converted = path.replace(/[^/]+$/, (file) => file.replace(/-/g, "_").replace(/\.tsx$/, ".py"))

    expect(Object.keys(py), `${name} converted to Python`).toContain(converted)

    // Its default export, or the one component it exports: component-example's.
    const tsxModule = (await tsx[path]()) as Record<string, ComponentType>
    const Page = tsxModule.default ?? Object.values(tsxModule)[0]
    const pyModule = (await py[converted]()) as Record<string, ComponentType>
    const expected = await html(Page)
    const got = await html(pyModule[Page.name])
    let at = 0

    while (at < expected.length && expected[at] === got[at]) at++
    // Where the two first part, with what leads to it.
    expect(got.slice(Math.max(0, at - 80), at + 80)).toBe(expected.slice(Math.max(0, at - 80), at + 80))
  })
})
