from utils import cn, cva

__js__ = {"radix-ui": ["Slot"]}

marker_variants = cva(
    "group/marker relative flex min-h-4 w-full items-center gap-2 text-left text-xs/relaxed text-muted-foreground [&_svg:not([class*='size-'])]:size-3.5 [a]:underline [a]:underline-offset-3 [a]:hover:text-foreground",
    {
        "variant": {
            "default": "",
            "separator": "before:mr-1 before:h-px before:min-w-0 before:flex-1 before:bg-border after:ml-1 after:h-px after:min-w-0 after:flex-1 after:bg-border",
            "border": "border-b border-border pb-2",
        },
    },
)


def Marker(className=None, variant="default", asChild=False, **props):
    Comp = Slot.Root if asChild else "div"

    return t"""
        <{Comp}
            data-slot="marker"
            data-variant={variant}
            class={cn(marker_variants(variant=variant, className=className))}
            ...{props}
        />
    """


def MarkerIcon(className=None, **props):
    return t"""
        <span
            data-slot="marker-icon"
            aria-hidden="true"
            class={cn("size-3.5 shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        />
    """


def MarkerContent(className=None, **props):
    return t"""
        <span
            data-slot="marker-content"
            class={cn("min-w-0 wrap-break-word group-data-[variant=separator]/marker:flex-none group-data-[variant=separator]/marker:text-center *:[a]:underline *:[a]:underline-offset-3 *:[a]:hover:text-foreground", className)}
            ...{props}
        />
    """
