from utils import cn
from button import Button

__js__ = {"lucide-react": ["ChevronLeftIcon", "ChevronRightIcon", "MoreHorizontalIcon"]}


def Pagination(className=None, **props):
    return t"""
        <nav
            role="navigation"
            aria-label="pagination"
            data-slot="pagination"
            class={cn("mx-auto flex w-full justify-center", className)}
            ...{props}
        />
    """


def PaginationContent(className=None, **props):
    return t'<ul data-slot="pagination-content" class={cn("flex items-center gap-1", className)} ...{props} />'


def PaginationItem(**props):
    return t'<li data-slot="pagination-item" ...{props} />'


def PaginationLink(className=None, isActive=None, size="icon", **props):
    return t"""
        <{Button} asChild variant={"outline" if isActive else "ghost"} size={size} class={cn(className)}>
            <a aria-current={"page" if isActive else None} data-slot="pagination-link" data-active={isActive} ...{props} />
        </{Button}>
    """


def PaginationPrevious(className=None, text="Previous", **props):
    return t"""
        <{PaginationLink} aria-label="Go to previous page" size="default" class={cn("pl-1.5!", className)} ...{props}>
            <{ChevronLeftIcon} data-icon="inline-start" />
            <span class="hidden sm:block">{text}</span>
        </{PaginationLink}>
    """


def PaginationNext(className=None, text="Next", **props):
    return t"""
        <{PaginationLink} aria-label="Go to next page" size="default" class={cn("pr-1.5!", className)} ...{props}>
            <span class="hidden sm:block">{text}</span>
            <{ChevronRightIcon} data-icon="inline-end" />
        </{PaginationLink}>
    """


def PaginationEllipsis(className=None, **props):
    return t"""
        <span
            aria-hidden
            data-slot="pagination-ellipsis"
            class={cn("flex size-8 items-center justify-center [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <{MoreHorizontalIcon} />
            <span class="sr-only">More pages</span>
        </span>
    """
