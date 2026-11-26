from utils import cn


def Card(className=None, size="default", **props):
    return t"""
        <div
            data-slot="card"
            data-size={size}
            class={cn("group/card flex flex-col gap-(--card-spacing) overflow-hidden bg-card py-(--card-spacing) text-sm text-card-foreground shadow-sm ring-1 ring-foreground/5 [--card-spacing:--spacing(8)] has-[>img:first-child]:pt-0 data-[size=sm]:[--card-spacing:--spacing(5)] *:[img:first-child]:rounded-none *:[img:last-child]:rounded-none", className)}
            ...{props}
        />
    """


def CardHeader(className=None, **props):
    return t"""
        <div
            data-slot="card-header"
            class={cn("group/card-header @container/card-header grid auto-rows-min items-start gap-1.5 rounded-none px-(--card-spacing) has-data-[slot=card-action]:grid-cols-[1fr_auto] has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-(--card-spacing)", className)}
            ...{props}
        />
    """


def CardTitle(className=None, **props):
    return t"""
        <div
            data-slot="card-title"
            class={cn("font-heading text-lg font-semibold tracking-wider uppercase", className)}
            ...{props}
        />
    """


def CardDescription(className=None, **props):
    return t"""
        <div
            data-slot="card-description"
            class={cn("text-sm leading-relaxed text-muted-foreground", className)}
            ...{props}
        />
    """


def CardAction(className=None, **props):
    return t"""
        <div
            data-slot="card-action"
            class={cn("col-start-2 row-span-2 row-start-1 self-start justify-self-end", className)}
            ...{props}
        />
    """


def CardContent(className=None, **props):
    return t'<div data-slot="card-content" class={cn("px-(--card-spacing)", className)} ...{props} />'


def CardFooter(className=None, **props):
    return t"""
        <div
            data-slot="card-footer"
            class={cn("flex items-center px-(--card-spacing) [.border-t]:pt-(--card-spacing)", className)}
            ...{props}
        />
    """
