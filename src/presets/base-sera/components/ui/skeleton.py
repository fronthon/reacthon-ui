from utils import cn


def Skeleton(className=None, **props):
    return t'<div data-slot="skeleton" class={cn("animate-pulse bg-muted", className)} ...{props} />'
