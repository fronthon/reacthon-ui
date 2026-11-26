from utils import cn, cva


def Empty(className=None, **props):
    return t"""
        <div
            data-slot="empty"
            class={cn("flex w-full min-w-0 flex-1 flex-col items-center justify-center gap-4 rounded-xl border-dashed p-6 text-center text-balance", className)}
            ...{props}
        />
    """


def EmptyHeader(className=None, **props):
    return t"""
        <div
            data-slot="empty-header"
            class={cn("flex max-w-sm flex-col items-center gap-1", className)}
            ...{props}
        />
    """


empty_media_variants = cva(
    "mb-2 flex shrink-0 items-center justify-center [&_svg]:pointer-events-none [&_svg]:shrink-0",
    {
        "variant": {
            "default": "bg-transparent",
            "icon": "flex size-8 shrink-0 items-center justify-center rounded-md bg-muted text-foreground [&_svg:not([class*='size-'])]:size-4",
        },
    },
    {"variant": "default"},
)


def EmptyMedia(className=None, variant="default", **props):
    return t"""
        <div
            data-slot="empty-icon"
            data-variant={variant}
            class={cn(empty_media_variants(variant=variant, className=className))}
            ...{props}
        />
    """


def EmptyTitle(className=None, **props):
    return t"""
        <div
            data-slot="empty-title"
            class={cn("font-heading text-sm font-medium tracking-tight", className)}
            ...{props}
        />
    """


def EmptyDescription(className=None, **props):
    return t"""
        <div
            data-slot="empty-description"
            class={cn("text-xs/relaxed text-muted-foreground [&>a]:underline [&>a]:underline-offset-4 [&>a:hover]:text-primary", className)}
            ...{props}
        />
    """


def EmptyContent(className=None, **props):
    return t"""
        <div
            data-slot="empty-content"
            class={cn("flex w-full max-w-sm min-w-0 flex-col items-center gap-2 text-xs/relaxed text-balance", className)}
            ...{props}
        />
    """
