from browser import document, window

from button import button_variants
from button_group import ButtonGroup
from native_select import NativeSelect, NativeSelectOptGroup, NativeSelectOption

__js__ = {
    "./components/theme-provider.tsx": ["useTheme"],
    "lucide-react": ["MoonIcon", "SunIcon"],
}

STYLES = ["vega", "nova", "maia", "lyra", "mira", "luma", "rhea", "sera"]
BASES = {"radix": "Radix", "base": "Base UI", "aria": "React Aria"}
# Each page's group, by the first word of its name, in shadcn's order.
GROUPS = {"preview": "Showcases", "dashboard": "Dashboard", "sidebar": "Sidebars", "login": "Logins", "signup": "Signups"}

LOGO = t"""
    <svg viewBox="0 0 256 256" class="size-6 shrink-0 rounded-[min(var(--radius-sm),6px)]" aria-hidden="true">
        <rect width="256" height="256" fill="#3776AB" />
        <g fill="none" stroke="#FFD343" strokeLinecap="round" strokeWidth="32">
            <line x1="192" y1="40" x2="40" y2="192" />
            <line x1="208" y1="128" x2="128" y2="208" />
        </g>
    </svg>
"""


def label(name):
    if name.startswith("preview"):
        return "Showcase 2" if name == "preview-02" else "Showcase"
    word, _, number = name.partition("-")
    return f"{word.capitalize()} {number}"


# The demo's toolbar, over each page: the page, its preset's style and base,
# each preset a build of its own beside the others, its colors, shadcn's grays
# and colors, painted at once, its Python or its TSX twin, and the theme.
def Toolbar(page, side, pages, preset, color, colors, onColor, presets=None):
    base, style = preset.split("-")
    theme = useTheme()
    dark = document.documentElement.classList.contains("dark")
    groups = {}

    for name in pages:
        groups.setdefault(GROUPS[name.split("-")[0]], []).append(name)

    def show(name, shown):
        window.location.hash = f"#/{name}/tsx" if shown == "tsx" else f"#/{name}"

    def to(chosen):
        window.location.href = f"../{chosen}/{window.location.hash}"

    def toggle(shown):
        return t"""
            <button
                data-slot="button"
                class={button_variants(variant="default" if side == shown else "outline", size="sm")}
                aria-pressed={side == shown}
                onClick={(lambda: show(page, shown))}
            >
                {"Python" if shown == "python" else "TSX"}
            </button>
        """

    one_build = "One preset a build: DEMO_PRESET=base-rhea npm run dev" if presets is None else None

    return t"""
        <div
            data-demo-toolbar
            class="fixed bottom-4 left-1/2 z-50 flex w-max max-w-[calc(100vw-2rem)] -translate-x-1/2 flex-wrap items-center justify-center gap-2 rounded-xl border bg-background/80 p-2 shadow-lg backdrop-blur-md"
        >
            <a href="https://github.com/fronthon/reacthon-ui" class="flex items-center gap-2 px-1 text-sm font-medium">
                {LOGO}
                Reacthon UI
            </a>
            <{NativeSelect} size="sm" aria-label="Page" value={page} onChange={(lambda event: show(event.target.value, side))}>
                {[t'''
                    <{NativeSelectOptGroup} key={group} label={group}>
                        {[t"<{NativeSelectOption} key={name} value={name}>{label(name)}</{NativeSelectOption}>" for name in names]}
                    </{NativeSelectOptGroup}>
                ''' for group, names in groups.items()]}
            </{NativeSelect}>
            <{NativeSelect}
                size="sm"
                aria-label="Style"
                title={one_build}
                disabled={presets is None}
                value={style}
                onChange={(lambda event: to(f"{base}-{event.target.value}"))}
            >
                {[t"<{NativeSelectOption} key={one} value={one}>{one.capitalize()}</{NativeSelectOption}>" for one in STYLES]}
            </{NativeSelect}>
            <{NativeSelect}
                size="sm"
                aria-label="Base"
                title={one_build}
                disabled={presets is None}
                value={base}
                onChange={(lambda event: to(f"{event.target.value}-{style}"))}
            >
                {[t"<{NativeSelectOption} key={one} value={one}>{named}</{NativeSelectOption}>" for one, named in BASES.items()]}
            </{NativeSelect}>
            <{NativeSelect} size="sm" aria-label="Color" value={color} onChange={(lambda event: onColor(event.target.value))}>
                {[t'''
                    <{NativeSelectOptGroup} key={group} label={group}>
                        {[t"<{NativeSelectOption} key={one['name']} value={one['name']}>{one['title']}</{NativeSelectOption}>" for one in colors if one["gray"] == gray]}
                    </{NativeSelectOptGroup}>
                ''' for group, gray in [("Grays", True), ("Colors", False)]]}
            </{NativeSelect}>
            <{ButtonGroup} aria-label="Language">
                {toggle("python")}
                {toggle("tsx")}
            </{ButtonGroup}>
            <button
                data-slot="button"
                class={button_variants(variant="ghost", size="icon-sm")}
                aria-label="Theme"
                onClick={(lambda: theme.setTheme("light" if dark else "dark"))}
            >
                {t"<{SunIcon} />" if dark else t"<{MoonIcon} />"}
            </button>
        </div>
    """
