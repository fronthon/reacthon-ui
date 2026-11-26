import { StrictMode, useEffect, useState, type ComponentType } from "react"
import { createRoot } from "react-dom/client"

import "./index.css"
import { App } from "./App.py"
import { page } from "./blocks.ts"
import { ThemeProvider } from "./components/theme-provider.tsx"
import { Toaster } from "@/components/ui/sonner"
import { TooltipProvider } from "@/components/ui/tooltip"

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

  if (!shown()) return <App />
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
