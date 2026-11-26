from javascript import NULL
from utils import cn, cva
from button import Button

__js__ = {"radix-ui": ["Slot"]}

attachment_variants = cva(
    "group/attachment relative flex w-fit max-w-full min-w-0 shrink-0 flex-wrap rounded-2xl border bg-card text-card-foreground transition-colors focus-within:ring-1 focus-within:ring-ring/50 has-[>a,>button]:hover:bg-muted/50 data-[state=error]:border-destructive/30 data-[state=idle]:border-dashed",
    {
        "size": {
            "default": "gap-2 text-sm has-data-[slot=attachment-content]:px-2.5 has-data-[slot=attachment-content]:py-2 has-data-[slot=attachment-media]:p-2",
            "sm": "gap-2.5 text-xs has-data-[slot=attachment-content]:px-2 has-data-[slot=attachment-content]:py-1.5 has-data-[slot=attachment-media]:p-1.5",
            "xs": "gap-1.5 rounded-xl text-xs has-data-[slot=attachment-content]:px-1.5 has-data-[slot=attachment-content]:py-1 has-data-[slot=attachment-media]:p-1",
        },
        "orientation": {
            "horizontal": "min-w-40 items-center",
            "vertical": "w-24 flex-col has-data-[slot=attachment-content]:w-30",
        },
    },
)


def Attachment(className=None, state="done", size="default", orientation="horizontal", **props):
    return t"""
        <div
            data-slot="attachment"
            data-state={state}
            data-size={size}
            data-orientation={orientation}
            class={cn(attachment_variants(size=size, orientation=orientation), className)}
            ...{props}
        />
    """


attachment_media_variants = cva(
    "relative flex aspect-square w-10 shrink-0 items-center justify-center overflow-hidden rounded-xl bg-muted text-foreground group-data-[orientation=vertical]/attachment:w-full group-data-[size=sm]/attachment:w-8 group-data-[size=xs]/attachment:w-7 group-data-[size=xs]/attachment:rounded-lg group-data-[state=error]/attachment:bg-destructive/10 group-data-[state=error]/attachment:text-destructive group-data-[orientation=vertical]/attachment:*:data-[slot=spinner]:size-6! [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 group-data-[orientation=vertical]/attachment:[&_svg:not([class*='size-'])]:size-6 group-data-[size=xs]/attachment:[&_svg:not([class*='size-'])]:size-3.5",
    {
        "variant": {
            "icon": "",
            "image": "opacity-60 group-data-[state=done]/attachment:opacity-100 group-data-[state=idle]/attachment:opacity-100 *:[img]:aspect-square *:[img]:w-full *:[img]:object-cover",
        },
    },
    {"variant": "icon"},
)


def AttachmentMedia(className=None, variant="icon", **props):
    return t"""
        <div
            data-slot="attachment-media"
            data-variant={variant}
            class={cn(attachment_media_variants(variant=variant), className)}
            ...{props}
        />
    """


def AttachmentContent(className=None, **props):
    return t"""
        <div
            data-slot="attachment-content"
            class={cn("max-w-full min-w-0 flex-1 leading-tight group-data-[orientation=vertical]/attachment:px-1", className)}
            ...{props}
        />
    """


def AttachmentTitle(className=None, **props):
    return t"""
        <span
            data-slot="attachment-title"
            class={cn("block max-w-full min-w-0 truncate font-medium group-data-[state=processing]/attachment:shimmer group-data-[state=uploading]/attachment:shimmer", className)}
            ...{props}
        />
    """


def AttachmentDescription(className=None, **props):
    return t"""
        <span
            data-slot="attachment-description"
            class={cn("mt-0.5 block min-w-0 truncate text-xs text-muted-foreground group-data-[state=error]/attachment:text-destructive/80", "max-w-full", className)}
            ...{props}
        />
    """


def AttachmentActions(className=None, **props):
    return t"""
        <div
            data-slot="attachment-actions"
            class={cn("relative z-20 flex shrink-0 items-center group-data-[orientation=vertical]/attachment:absolute group-data-[orientation=vertical]/attachment:top-3 group-data-[orientation=vertical]/attachment:right-3 group-data-[orientation=vertical]/attachment:gap-1", className)}
            ...{props}
        />
    """


def AttachmentAction(className=None, variant=None, size="icon-xs", **props):
    return t"""
        <{Button}
            data-slot="attachment-action"
            variant={variant if variant not in (None, NULL) else "ghost"}
            size={size}
            class={cn(className)}
            ...{props}
        />
    """


def AttachmentTrigger(className=None, asChild=False, type=None, **props):
    Comp = Slot.Root if asChild else "button"

    return t"""
        <{Comp}
            data-slot="attachment-trigger"
            type={None if asChild else type if type not in (None, NULL) else "button"}
            class={cn("absolute inset-0 z-10 outline-none", className)}
            ...{props}
        />
    """


def AttachmentGroup(className=None, **props):
    return t"""
        <div
            data-slot="attachment-group"
            class={cn("flex min-w-0 scroll-fade-x snap-x snap-mandatory scroll-px-1 scrollbar-none gap-3 overflow-x-auto overscroll-x-contain py-1 *:data-[slot=attachment]:flex-none *:data-[slot=attachment]:snap-start", className)}
            ...{props}
        />
    """
