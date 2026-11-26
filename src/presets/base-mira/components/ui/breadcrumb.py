from javascript import NULL
from utils import cn

__js__ = {
    "@base-ui/react/merge-props": ["mergeProps"],
    "@base-ui/react/use-render": ["useRender"],
    "lucide-react": ["ChevronRightIcon", "MoreHorizontalIcon"],
}


def Breadcrumb(className=None, **props):
    return t'<nav aria-label="breadcrumb" data-slot="breadcrumb" class={cn(className)} ...{props} />'


def BreadcrumbList(className=None, **props):
    return t"""
        <ol
            data-slot="breadcrumb-list"
            class={cn("flex flex-wrap items-center gap-1.5 text-xs/relaxed wrap-break-word text-muted-foreground", className)}
            ...{props}
        />
    """


def BreadcrumbItem(className=None, **props):
    return t'<li data-slot="breadcrumb-item" class={cn("inline-flex items-center gap-1", className)} ...{props} />'


def BreadcrumbLink(className=None, render=None, **props):
    return useRender(
        {
            "defaultTagName": "a",
            "props": mergeProps({"className": cn("transition-colors hover:text-foreground", className)}, props),
            "render": render,
            "state": {"slot": "breadcrumb-link"},
        },
    )


def BreadcrumbPage(className=None, **props):
    return t"""
        <span
            data-slot="breadcrumb-page"
            role="link"
            aria-disabled="true"
            aria-current="page"
            class={cn("font-normal text-foreground", className)}
            ...{props}
        />
    """


def BreadcrumbSeparator(children=None, className=None, **props):
    return t"""
        <li
            data-slot="breadcrumb-separator"
            role="presentation"
            aria-hidden="true"
            class={cn("[&>svg]:size-3.5", className)}
            ...{props}
        >
            {children if children not in (None, NULL) else t'<{ChevronRightIcon} />'}
        </li>
    """


def BreadcrumbEllipsis(className=None, **props):
    return t"""
        <span
            data-slot="breadcrumb-ellipsis"
            role="presentation"
            aria-hidden="true"
            class={cn("flex size-4 items-center justify-center [&>svg]:size-3.5", className)}
            ...{props}
        >
            <{MoreHorizontalIcon} />
            <span class="sr-only">More</span>
        </span>
    """
