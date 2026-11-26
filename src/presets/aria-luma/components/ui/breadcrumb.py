from utils import cn

__js__ = {
    "react-aria-components": [
        "Breadcrumb as BreadcrumbPrimitive",
        "Breadcrumbs as BreadcrumbsPrimitive",
        "composeRenderProps",
        "Link as LinkPrimitive",
    ],
    "lucide-react": ["ChevronRightIcon", "MoreHorizontalIcon"],
}


def Breadcrumb(className=None, **props):
    return t'<nav aria-label="breadcrumb" data-slot="breadcrumb" class={cn(className)} ...{props} />'


def BreadcrumbList(className=None, **props):
    return t"""
        <{BreadcrumbsPrimitive}
            data-slot="breadcrumb-list"
            class={cn("flex flex-wrap items-center gap-1.5 text-sm wrap-break-word text-muted-foreground sm:gap-2.5", className)}
            ...{props}
        />
    """


def BreadcrumbItem(className=None, children=None, separatorClassName=None, **props):
    def callback(children, props):
        is_current = props.get("isCurrent")

        span = t"""
            <span
                data-slot="breadcrumb-separator"
                role="presentation"
                aria-hidden="true"
                class={cn("[&>svg]:size-3.5", separatorClassName)}
            >
                <{ChevronRightIcon} />
            </span>
        """

        return t"{children}{not is_current and span}"

    return t"""
        <{BreadcrumbPrimitive}
            data-slot="breadcrumb-item"
            class={cn("inline-flex items-center gap-1.5", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{BreadcrumbPrimitive}>
    """


def BreadcrumbLink(className=None, render=None, **props):
    return t"""
        <{LinkPrimitive}
            data-slot="breadcrumb-link"
            class={cn("transition-colors hover:text-foreground", className)}
            render={render}
            ...{props}
        />
    """


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


def BreadcrumbEllipsis(className=None, **props):
    return t"""
        <span
            data-slot="breadcrumb-ellipsis"
            role="presentation"
            aria-hidden="true"
            class={cn("flex size-5 items-center justify-center [&>svg]:size-4", className)}
            ...{props}
        >
            <{MoreHorizontalIcon} />
            <span class="sr-only">More</span>
        </span>
    """
