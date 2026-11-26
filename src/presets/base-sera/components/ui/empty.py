from utils import cn, cva


def Empty(className=None, **props):
    return t"""
        <div
            data-slot="empty"
            class={cn("flex w-full min-w-0 flex-1 flex-col items-center justify-center gap-4 border-dashed p-12 text-center text-balance", className)}
            ...{props}
        />
    """


def EmptyHeader(className=None, **props):
    return t"""
        <div
            data-slot="empty-header"
            class={cn("flex max-w-sm flex-col items-center gap-2", className)}
            ...{props}
        />
    """


empty_media_variants = cva(
    "mb-2 flex shrink-0 items-center justify-center [&_svg]:pointer-events-none [&_svg]:shrink-0",
    {
        "variant": {
            "default": "bg-transparent",
            "icon": "flex size-10 shrink-0 items-center justify-center rounded-none bg-muted text-foreground [&_svg:not([class*='size-'])]:size-5",
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
            class={cn("font-heading text-lg font-semibold tracking-wider uppercase", className)}
            ...{props}
        />
    """


def EmptyDescription(className=None, **props):
    return t"""
        <div
            data-slot="empty-description"
            class={cn("mt-0.5 text-sm/relaxed text-muted-foreground [&>a]:underline [&>a]:underline-offset-4 [&>a:hover]:text-primary", className)}
            ...{props}
        />
    """


def EmptyContent(className=None, **props):
    return t"""
        <div
            data-slot="empty-content"
            class={cn("flex w-full max-w-sm min-w-0 flex-col items-center gap-4 text-sm text-balance", className)}
            ...{props}
        />
    """
