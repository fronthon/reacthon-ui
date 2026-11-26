import { Fragment, lazy, StrictMode, Suspense, useEffect, useState, type ComponentType } from "react"
import { createRoot } from "react-dom/client"

import "./index.css"
import { page } from "./blocks.ts"
import { ThemeProvider } from "./components/theme-provider.tsx"
import { Toaster } from "@/components/ui/sonner"
import * as tooltip from "@/components/ui/tooltip"

// The components' page, written with Radix's parts, loaded when it is shown:
// a block's page opens on any preset.
const App = lazy(() => import("./App.py").then((module) => ({ default: module.App as ComponentType })))

// The provider the application's root holds tooltips in, where the preset has one.
const TooltipProvider = ("TooltipProvider" in tooltip ? tooltip.TooltipProvider : Fragment) as ComponentType<{ children: React.ReactNode }>

// `#/sidebar-07` shows that block's page in Python, `#/sidebar-07/tsx` its TSX
// twin, anything else the components.
const shown = () => /^#\/([\w-]+?)(\/tsx)?$/.exec(location.hash)

function Shown() {
  const [hash, setHash] = useState(location.hash)
  const [Page, setPage] = useState<{ hash: string; Page: ComponentType } | null>(null)

  useEffect(() => {
    const changed = () => setHash(location.hash)

    addEventListener("hashchange", changed)
    return () => removeEventListener("hashchange", changed)
  }, [])

  useEffect(() => {
    const found = shown()

    if (found) page(found[1], found[2] ? "tsx" : "python").then((one) => setPage({ hash, Page: one }))
  }, [hash])

  if (!shown()) {
    return (
      <Suspense fallback={null}>
        <App />
      </Suspense>
    )
  }
  return Page?.hash === hash ? <Page.Page /> : null
}

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
