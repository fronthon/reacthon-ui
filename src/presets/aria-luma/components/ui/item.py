from utils import cn, cva
from separator import Separator

__js__ = {"react-aria-components": ["Link as LinkPrimitive"]}


def ItemGroup(className=None, **props):
    return t"""
        <div
            role="list"
            data-slot="item-group"
            class={cn("group/item-group flex w-full flex-col gap-4 has-data-[size=sm]:gap-2.5 has-data-[size=xs]:gap-2", className)}
            ...{props}
        />
    """


def ItemSeparator(className=None, **props):
    return t"""
        <{Separator}
            data-slot="item-separator"
            orientation="horizontal"
            class={cn("my-2", className)}
            ...{props}
        />
    """


item_variants = cva(
    "group/item flex w-full flex-wrap items-center rounded-2xl border text-sm transition-colors duration-100 outline-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 [a]:transition-colors [a]:hover:bg-muted",
    {
        "variant": {
            "default": "border-transparent",
            "outline": "border-border",
            "muted": "border-transparent bg-muted/50",
        },
        "size": {
            "default": "gap-3.5 px-4 py-3.5",
            "sm": "gap-3.5 px-3.5 py-3",
            "xs": "gap-2.5 px-3 py-2.5 in-data-[slot=dropdown-menu-content]:p-0",
        },
    },
    {"variant": "default", "size": "default"},
)


def Item(className=None, variant="default", size="default", **props):
    Element = LinkPrimitive if "href" in props else "div"
    return t"""
        <{Element}
            data-slot="item"
            data-variant={variant}
            data-size={size}
            class={cn(item_variants(variant=variant, size=size, className=className))}
            ...{props}
        />
    """


item_media_variants = cva(
    "flex shrink-0 items-center justify-center gap-2 group-has-data-[slot=item-description]/item:translate-y-0.5 group-has-data-[slot=item-description]/item:self-start [&_svg]:pointer-events-none",
    {
        "variant": {
            "default": "bg-transparent",
            "icon": "[&_svg:not([class*='size-'])]:size-4",
            "image": "size-10 overflow-hidden rounded-xl group-data-[size=sm]/item:size-8 group-data-[size=xs]/item:size-6 group-data-[size=xs]/item:rounded-lg [&_img]:size-full [&_img]:object-cover",
        },
    },
    {"variant": "default"},
)


def ItemMedia(className=None, variant="default", **props):
    return t"""
        <div
            data-slot="item-media"
            data-variant={variant}
            class={cn(item_media_variants(variant=variant, className=className))}
            ...{props}
        />
    """


def ItemContent(className=None, **props):
    return t"""
        <div
            data-slot="item-content"
            class={cn("flex flex-1 flex-col gap-1 group-data-[size=xs]/item:gap-0.5 [&+[data-slot=item-content]]:flex-none", className)}
            ...{props}
        />
    """


def ItemTitle(className=None, **props):
    return t"""
        <div
            data-slot="item-title"
            class={cn("line-clamp-1 flex w-fit items-center gap-2 text-sm leading-snug font-medium underline-offset-4", className)}
            ...{props}
        />
    """


def ItemDescription(className=None, **props):
    return t"""
        <p
            data-slot="item-description"
            class={cn("line-clamp-2 text-left text-sm font-normal text-muted-foreground [&>a]:underline [&>a]:underline-offset-4 [&>a:hover]:text-primary", className)}
            ...{props}
        />
    """


def ItemActions(className=None, **props):
    return t'<div data-slot="item-actions" class={cn("flex items-center gap-2", className)} ...{props} />'


def ItemHeader(className=None, **props):
    return t"""
        <div
            data-slot="item-header"
            class={cn("flex basis-full items-center justify-between gap-2", className)}
            ...{props}
        />
    """


def ItemFooter(className=None, **props):
    return t"""
        <div
            data-slot="item-footer"
            class={cn("flex basis-full items-center justify-between gap-2", className)}
            ...{props}
        />
    """
