from utils import cn, cva

marker_variants = cva(
    "group/marker relative flex min-h-4 w-full items-center gap-2 text-left text-xs tracking-wide text-muted-foreground uppercase [&_svg:not([class*='size-'])]:size-4 [a]:underline [a]:underline-offset-3 [a]:hover:text-foreground",
    {
        "variant": {
            "default": "",
            "separator": "before:mr-1 before:h-px before:min-w-0 before:flex-1 before:bg-border after:ml-1 after:h-px after:min-w-0 after:flex-1 after:bg-border",
            "border": "border-b border-border pb-2",
        },
    },
)


def Marker(className=None, variant="default", render=None, children=None, **props):
    if render:
        render_props = {
            **props,
            "data-slot": "marker",
            "data-variant": variant,
            "className": cn(marker_variants(variant=variant, className=className)),
            "children": children,
        }

        return render(render_props)

    return t"""
        <div
            ...{props}
            data-slot="marker"
            data-variant={variant}
            class={cn(marker_variants(variant=variant, className=className))}
        >
            {children}
        </div>
    """


def MarkerIcon(className=None, **props):
    return t"""
        <span
            data-slot="marker-icon"
            aria-hidden="true"
            class={cn("size-4 shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
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
