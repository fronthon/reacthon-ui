// A headless Chrome of its own, driven through its DevTools protocol: what a
// page shows once laid out, which jsdom lays out not at all. Chrome is the one
// `CHROME` names, `google-chrome` otherwise, as GitHub's runners have it.
import { spawn } from "node:child_process"
import { existsSync, mkdtempSync, readFileSync, rmSync } from "node:fs"
import { tmpdir } from "node:os"
import { join } from "node:path"
import { setTimeout as sleep } from "node:timers/promises"

type Message = { id?: number; method?: string; params?: Record<string, any>; result?: Record<string, any> }

async function until<T>(found: () => T | false | Promise<T | false>, ms = 20_000): Promise<T> {
  for (const start = Date.now(); Date.now() - start < ms; await sleep(50)) {
    const one = await found()

    if (one) return one
  }
  throw new Error("timeout")
}

export async function chrome() {
  const profile = mkdtempSync(join(tmpdir(), "reacthon-ui-chrome-"))
  const child = spawn(
    process.env.CHROME ?? "google-chrome",
    ["--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check", `--user-data-dir=${profile}`, "--remote-debugging-port=0", "about:blank"],
    { stdio: "ignore" },
  )
  const portFile = join(profile, "DevToolsActivePort")
  const port = await until(() => existsSync(portFile) && readFileSync(portFile, "utf8").split("\n")[0])
  const target = await (await fetch(`http://127.0.0.1:${port}/json/new?about:blank`, { method: "PUT" })).json()
  const socket = new WebSocket(target.webSocketDebuggerUrl)
  const pending = new Map<number, (message: Message) => void>()
  // What the page throws, which a test reads and empties.
  const thrown: string[] = []
  let id = 0

  await new Promise((resolve, reject) => {
    socket.onopen = resolve
    socket.onerror = reject
  })
  socket.onmessage = (event) => {
    const message: Message = JSON.parse(String(event.data))

    if (message.method === "Runtime.exceptionThrown") thrown.push(message.params!.exceptionDetails.exception?.description?.split("\n")[0])
    if (message.id !== undefined) pending.get(message.id)?.(message)
    pending.delete(message.id!)
  }

  const send = (method: string, params: Record<string, unknown> = {}) =>
    new Promise<Message>((resolve) => {
      pending.set(++id, resolve)
      socket.send(JSON.stringify({ id, method, params }))
    })
  const evaluate = async (expression: string) => {
    const reply = await send("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true })

    if (reply.result?.exceptionDetails) throw new Error(reply.result.exceptionDetails.exception?.description)
    return reply.result?.result?.value
  }
  const close = async () => {
    socket.close()
    child.kill()
    await sleep(300)
    rmSync(profile, { recursive: true, force: true })
  }

  await send("Runtime.enable")
  await send("Page.enable")
  return { send, evaluate, close, thrown }
}
