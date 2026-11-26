import { Fragment, StrictMode, useEffect, useState, type ComponentType } from "react"
import { createRoot } from "react-dom/client"

import "./index.css"
import { choices, paint, saved } from "./colors.ts"
import { page, pages } from "./pages.ts"
import { ThemeProvider } from "./components/theme-provider.tsx"
import { Toolbar } from "./toolbar.py"
import { Toaster } from "@/components/ui/sonner"
import * as tooltip from "@/components/ui/tooltip"

// The preset this build is of, and the presets built beside it, which the
// toolbar switches between, or none in development, one preset a server.
declare const __DEMO_PRESET__: string
declare const __DEMO_PRESETS__: string[] | null

// The provider the application's root holds tooltips in, where the preset has one.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType<{ children: React.ReactNode }>

// `#/sidebar-07` shows that page in Python, `#/sidebar-07/tsx` its TSX twin,
// and anything else shadcn's first showcase.
function route() {
  const [, name, tsx] = /^#\/([\w-]+?)(\/tsx)?$/.exec(location.hash) ?? []

  return { name: pages.includes(name) ? name : pages[0], side: tsx ? ("tsx" as const) : ("python" as const) }
}

function Shown() {
  const [hash, setHash] = useState(location.hash)
  const [shown, setShown] = useState<{ hash: string; Page: ComponentType } | null>(null)
  const [color, setColor] = useState(saved)
  const { name, side } = route()

  useEffect(() => paint(color), [color])

  useEffect(() => {
    const changed = () => setHash(location.hash)

    addEventListener("hashchange", changed)
    return () => removeEventListener("hashchange", changed)
  }, [])

  useEffect(() => {
    page(name, side).then((Page) => setShown({ hash, Page }))
    document.title = `${name} · Reacthon UI`
  }, [hash, name, side])

  // The page shown, once it is, which a reader of the page waits for.
  useEffect(() => {
    if (shown) document.documentElement.dataset.shown = shown.hash
  }, [shown])

  return (
    <>
      {shown?.hash === hash ? <shown.Page /> : null}
      <Toolbar
        page={name}
        side={side}
        pages={pages}
        preset={__DEMO_PRESET__}
        presets={__DEMO_PRESETS__ ?? undefined}
        color={color}
        colors={choices}
        onColor={setColor}
      />
    </>
  )
}

// The color kept from the last page, painted before the first.
paint(saved())

// The root of an application: its theme, its tooltips and its toasts.
createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ThemeProvider>
      <TooltipProvider>
        <Shown />
        <Toaster />
      </TooltipProvider>
    </ThemeProvider>
  </StrictMode>
)
