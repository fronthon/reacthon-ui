// The demo's blocks in Chrome, where a page is laid out: each block's page in
// Python against its TSX twin, each loaded afresh with the same random draws,
// the same page as it loads and after each gesture of a mouse, and nothing
// thrown. jsdom renders neither recharts' tooltip, which it lays out by
// size, nor a drag, nor what a collapsed sidebar's tooltips show.
import { readdirSync, rmSync } from "node:fs"
import { tmpdir } from "node:os"
import { join } from "node:path"
import { setTimeout as sleep } from "node:timers/promises"
import { build, preview, type PreviewServer } from "vite"
import { afterAll, beforeAll, describe, expect, it } from "vitest"

import { chrome } from "./chrome"

// The preset the demo is built on, one of each base, as the project says.
const preset = process.env.DEMO_PRESET ?? "radix-nova"
const blocks = readdirSync(`src/presets/${preset}/blocks`).sort()
const outDir = join(tmpdir(), `reacthon-ui-demo-${preset}-${process.pid}`)
const SEEDED = "{ let seed = 1; Math.random = () => (seed = (seed * 16807) % 2147483647) / 2147483647 }"
// The page, its ids numbered as they first appear; the span recharts measures
// a text in holds the last it measured, which the order of its measures
// decides, and shows nothing.
const PAGE = `(() => {
  const ids = new Map()
  return document.body.innerHTML
    .replace(/(<span id="recharts_measurement_span"[^>]*>)[^<]*/, "$1")
    .replace(/_r_[0-9a-z]+_|\\bDnd\\w+-\\d+/g, (id) => {
      if (!ids.has(id)) ids.set(id, ids.size)
      return "_id" + ids.get(id) + "_"
    })
})()`

let server: PreviewServer
let page: Awaited<ReturnType<typeof chrome>>
let site = ""

// The point a gesture aims at, the element an expression finds scrolled into
// view, or null where the page has none.
const at = (find: string): Promise<[number, number] | null> =>
  page.evaluate(`(() => {
    const one = ${find}
    if (!one) return null
    one.scrollIntoView({ block: "center" })
    const box = one.getBoundingClientRect()
    return [box.x + box.width / 2, box.y + box.height / 2]
  })()`)
const mouse = (type: string, [x, y]: [number, number], buttons = 0) =>
  page.send("Input.dispatchMouseEvent", { type, x, y, button: type === "mouseMoved" ? "none" : "left", buttons, clickCount: 1 })
const handle = (n: number) => `[...document.querySelectorAll("button")].filter((one) => one.textContent.includes("Drag to reorder"))[${n}]`

const GESTURES: [string, string, (point: [number, number]) => Promise<unknown>][] = [
  ["collapse the sidebar", `document.querySelector("[data-slot=sidebar-trigger]")`, async (point) => {
    await mouse("mousePressed", point, 1)
    await mouse("mouseReleased", point)
  }],
  ["hover a menu's button", `document.querySelectorAll("[data-sidebar=menu-button]")[1]`, (point) => mouse("mouseMoved", point)],
  ["hover the chart", `document.querySelector("[data-slot=chart]")`, (point) => mouse("mouseMoved", point)],
  ["drag a row two down", handle(0), async (from) => {
    const to = (await at(handle(2)))!

    await mouse("mousePressed", from, 1)
    for (let step = 1; step <= 10; step++) await mouse("mouseMoved", [from[0], from[1] + ((to[1] - from[1] + 10) * step) / 10], 1)
    await mouse("mouseReleased", [from[0], to[1] + 10])
  }],
]

// The page held still: the same twice, a fifth of a second apart.
async function settled() {
  let before = ""

  for (let tries = 0; tries < 50; tries++) {
    await sleep(200)
    const now: string = await page.evaluate(PAGE).catch(() => "")

    if (now === before && now.includes("<")) return now
    before = now
  }
  return before
}

// A block's page loaded afresh, then after each gesture it has an element
// for, and what it threw.
async function played(hash: string) {
  await page.send("Page.navigate", { url: "about:blank" })
  await sleep(100)
  page.thrown.length = 0
  await page.send("Page.navigate", { url: `${site}${hash}` })

  const pages: [string, string][] = [["loaded", await settled()]]

  for (const [gesture, find, act] of GESTURES) {
    const point = await at(find)

    if (!point) continue
    await act(point)
    pages.push([`after ${gesture}`, await settled()])
  }
  return { pages, thrown: [...page.thrown] }
}

beforeAll(async () => {
  await build({ configFile: "vite.config.ts", logLevel: "silent", build: { outDir, emptyOutDir: true } })
  server = await preview({ configFile: "vite.config.ts", logLevel: "silent", build: { outDir }, preview: { port: 0 } })
  site = server.resolvedUrls!.local[0]
  page = await chrome()
  await page.send("Emulation.setDeviceMetricsOverride", { width: 1280, height: 800, deviceScaleFactor: 1, mobile: false })
  await page.send("Page.addScriptToEvaluateOnNewDocument", { source: SEEDED })
})

afterAll(async () => {
  await page?.close()
  await server?.close()
  rmSync(outDir, { recursive: true, force: true })
})

describe(`the demo's blocks in Chrome, on ${preset}`, () => {
  it.for(blocks)("%s is its TSX twin, loaded and after a mouse's gestures", async (name) => {
    const python = await played(`#/${name}`)
    const tsx = await played(`#/${name}/tsx`)

    expect(python.thrown, "thrown by the Python page").toEqual([])
    expect(tsx.thrown, "thrown by the TSX page").toEqual([])
    expect(python.pages.map(([step]) => step)).toEqual(tsx.pages.map(([step]) => step))
    tsx.pages.forEach(([step, expected], n) => {
      const got = python.pages[n][1]
      let from = 0

      while (from < expected.length && expected[from] === got[from]) from++
      // Where the two first part, with what leads to it.
      expect(got.slice(Math.max(0, from - 80), from + 80), step).toBe(expected.slice(Math.max(0, from - 80), from + 80))
    })
  })
})
