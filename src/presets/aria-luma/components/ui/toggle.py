from utils import cn, cva

__js__ = {"react-aria-components": ["ToggleButton as TogglePrimitive"]}

toggle_variants = cva(
    "group/toggle inline-flex items-center justify-center gap-1 rounded-3xl text-sm font-medium whitespace-nowrap transition-colors outline-none hover:bg-muted hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/30 disabled:pointer-events-none disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-destructive/20 aria-pressed:bg-muted dark:aria-invalid:ring-destructive/40 data-selected:bg-muted [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
    {
        "variant": {"default": "bg-transparent", "outline": "border border-input bg-transparent hover:bg-muted"},
        "size": {
            "default": "h-9 min-w-9 px-3 has-data-[icon=inline-end]:pr-2.5 has-data-[icon=inline-start]:pl-2.5",
            "sm": "h-8 min-w-8 px-3 has-data-[icon=inline-end]:pr-2 has-data-[icon=inline-start]:pl-2",
            "lg": "h-10 min-w-10 px-4 has-data-[icon=inline-end]:pr-3 has-data-[icon=inline-start]:pl-3",
        },
    },
    {"variant": "default", "size": "default"},
)


def Toggle(className=None, variant="default", size="default", **props):
    return t"""
        <{TogglePrimitive}
            data-slot="toggle"
            class={cn(toggle_variants(variant=variant, size=size, className=className))}
            ...{props}
        />
    """
