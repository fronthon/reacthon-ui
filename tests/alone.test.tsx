// @vitest-environment jsdom
// Every component of src/components/ui written in Python, rendered alone with
// one child, against shadcn/ui's own: where the TSX one renders by itself, the
// same page, to the character.
import { act, createElement, type ComponentType } from "react"
import { createRoot } from "react-dom/client"
import { describe, expect, it } from "vitest"

;(globalThis as { IS_REACT_ACT_ENVIRONMENT?: boolean }).IS_REACT_ACT_ENVIRONMENT = true

// What Radix, embla and the media queries ask of the page and jsdom does not have.
Object.assign(Element.prototype, { scrollIntoView() {}, hasPointerCapture: () => false, releasePointerCapture() {} })
;(globalThis as { ResizeObserver?: unknown }).ResizeObserver ??= class {
  observe() {}
  unobserve() {}
  disconnect() {}
}
window.matchMedia ??= (() => ({ matches: false, addEventListener() {}, removeEventListener() {} })) as never
// The sidebar's skeleton draws its width at random.
Math.random = () => 0.5

const tsx = import.meta.glob("/src/components/ui/*.tsx")
const py = import.meta.glob("/src/components/ui/*.py")

// React's ids count every root the page has rendered: each one is named by the
// order it first appears in. input-otp marks the selection of the second input
// it sees, whichever renders it.
function numbered(page: string) {
  const ids = new Map<string, number>()

  return page
    .replace(/_r_[0-9a-z]+_/g, (id) => {
      if (!ids.has(id)) ids.set(id, ids.size)
      return `_id${ids.get(id)}_`
    })
    .replace(/ data-input-otp-ms[se]="\d+"/g, "")
}

async function html(Comp: ComponentType) {
  const container = document.createElement("div")
  let failed: unknown = null
  const root = createRoot(container, { onUncaughtError: (error) => (failed = error), onCaughtError: (error) => (failed = error) })
  const quiet = console.error

  console.error = () => {}
  document.body.append(container)
  try {
    await act(() => root.render(createElement(Comp, null, "x")))
    if (failed) throw failed
    return numbered(document.body.innerHTML)
  } finally {
    await act(() => root.unmount())
    container.remove()
    document.body.innerHTML = ""
    console.error = quiet
  }
}

const files = Object.keys(py).map((path) => [path.split("/").pop()!.replace(/\.py$/, ""), path])

describe.each(files)("%s", (name, path) => {
  it("renders each component alone as the TSX one does", async () => {
    const pyModule = (await py[path]()) as Record<string, ComponentType>
    const tsxModule = (await tsx[`/src/components/ui/${name.replace(/_/g, "-")}.tsx`]()) as Record<string, ComponentType>

    for (const [key, Comp] of Object.entries(tsxModule)) {
      if (!/^[A-Z]/.test(key) || typeof Comp !== "function") continue

      let expected: string

      try {
        expected = await html(Comp)
      } catch {
        // It needs its context, in TSX as well: the twin renders it inside.
        continue
      }
      expect(await html(pyModule[key]), key).toBe(expected)
    }
  })
})
