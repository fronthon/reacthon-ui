from utils import cn


def Skeleton(className=None, **props):
    return t'<div data-slot="skeleton" class={cn("animate-pulse rounded-2xl bg-muted", className)} ...{props} />'
