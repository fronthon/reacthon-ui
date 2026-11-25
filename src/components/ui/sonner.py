__js__ = {
    "next-themes": ["useTheme"],
    "sonner": ["Toaster as Sonner"],
    "lucide-react": ["CircleCheckIcon", "InfoIcon", "TriangleAlertIcon", "OctagonXIcon", "Loader2Icon"],
}


def Toaster(**props):
    theme = useTheme().get("theme")
    if theme is None:
        theme = "system"

    return t"""
        <{Sonner}
            theme={theme}
            class="toaster group"
            icons={ {
                "success": t'<{CircleCheckIcon} class="size-4" />',
                "info": t'<{InfoIcon} class="size-4" />',
                "warning": t'<{TriangleAlertIcon} class="size-4" />',
                "error": t'<{OctagonXIcon} class="size-4" />',
                "loading": t'<{Loader2Icon} class="size-4 animate-spin" />',
            } }
            style={ {
                "--normal-bg": "var(--popover)",
                "--normal-text": "var(--popover-foreground)",
                "--normal-border": "var(--border)",
                "--border-radius": "var(--radius)",
            } }
            toastOptions={ {
                "classNames": {"toast": "cn-toast"},
            } }
            ...{props}
        />
    """
