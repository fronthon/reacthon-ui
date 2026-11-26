from utils import cn


def Card(className=None, size="default", **props):
    return t"""
        <div
            data-slot="card"
            data-size={size}
            class={cn("group/card flex flex-col gap-(--card-spacing) overflow-hidden rounded-2xl bg-card py-(--card-spacing) text-sm text-card-foreground ring-1 ring-foreground/10 [--card-spacing:--spacing(6)] has-[>img:first-child]:pt-0 data-[size=sm]:[--card-spacing:--spacing(4)] *:[img:first-child]:rounded-t-xl *:[img:last-child]:rounded-b-xl", className)}
            ...{props}
        />
    """


def CardHeader(className=None, **props):
    return t"""
        <div
            data-slot="card-header"
            class={cn("group/card-header @container/card-header grid auto-rows-min items-start gap-2 rounded-t-xl px-(--card-spacing) has-data-[slot=card-action]:grid-cols-[1fr_auto] has-data-[slot=card-description]:grid-rows-[auto_auto] [.border-b]:pb-(--card-spacing)", className)}
            ...{props}
        />
    """


def CardTitle(className=None, **props):
    return t'<div data-slot="card-title" class={cn("font-heading text-base font-medium", className)} ...{props} />'


def CardDescription(className=None, **props):
    return t'<div data-slot="card-description" class={cn("text-sm text-muted-foreground", className)} ...{props} />'


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
            class={cn("flex items-center rounded-b-xl px-(--card-spacing) [.border-t]:pt-(--card-spacing)", className)}
            ...{props}
        />
    """
