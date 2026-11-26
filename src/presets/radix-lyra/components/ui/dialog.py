from utils import cn
from button import Button

__js__ = {"radix-ui": ["Dialog as DialogPrimitive"], "lucide-react": ["XIcon"]}


def Dialog(**props):
    return t'<{DialogPrimitive.Root} data-slot="dialog" ...{props} />'


def DialogTrigger(**props):
    return t'<{DialogPrimitive.Trigger} data-slot="dialog-trigger" ...{props} />'


def DialogPortal(**props):
    return t'<{DialogPrimitive.Portal} data-slot="dialog-portal" ...{props} />'


def DialogClose(**props):
    return t'<{DialogPrimitive.Close} data-slot="dialog-close" ...{props} />'


def DialogOverlay(className=None, **props):
    return t"""
        <{DialogPrimitive.Overlay}
            data-slot="dialog-overlay"
            class={cn("fixed inset-0 isolate z-50 bg-black/10 duration-100 supports-backdrop-filter:backdrop-blur-xs data-open:animate-in data-open:fade-in-0 data-closed:animate-out data-closed:fade-out-0", className)}
            ...{props}
        />
    """


def DialogContent(className=None, children=None, showCloseButton=True, **props):
    close = t"""
        <{DialogPrimitive.Close} data-slot="dialog-close" asChild>
            <{Button} variant="ghost" class="absolute top-2 right-2" size="icon-sm">
                <{XIcon} />
                <span class="sr-only">Close</span>
            </{Button}>
        </{DialogPrimitive.Close}>
    """

    return t"""
        <{DialogPortal}>
            <{DialogOverlay} />
            <{DialogPrimitive.Content}
                data-slot="dialog-content"
                class={cn("fixed top-1/2 left-1/2 z-50 grid w-full max-w-[calc(100%-2rem)] -translate-x-1/2 -translate-y-1/2 gap-4 rounded-none bg-popover p-4 text-xs/relaxed text-popover-foreground ring-1 ring-foreground/10 duration-100 outline-none sm:max-w-sm data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                ...{props}
            >
                {children}
                {showCloseButton and close}
            </{DialogPrimitive.Content}>
        </{DialogPortal}>
    """


def DialogHeader(className=None, **props):
    return t'<div data-slot="dialog-header" class={cn("flex flex-col gap-1 text-left", className)} ...{props} />'


def DialogFooter(className=None, showCloseButton=False, children=None, **props):
    close = t"""
        <{DialogPrimitive.Close} asChild>
            <{Button} variant="outline">Close</{Button}>
        </{DialogPrimitive.Close}>
    """

    return t"""
        <div
            data-slot="dialog-footer"
            class={cn("flex flex-col-reverse gap-2 sm:flex-row sm:justify-end", className)}
            ...{props}
        >
            {children}
            {showCloseButton and close}
        </div>
    """


def DialogTitle(className=None, **props):
    return t"""
        <{DialogPrimitive.Title}
            data-slot="dialog-title"
            class={cn("font-heading text-sm font-medium", className)}
            ...{props}
        />
    """


def DialogDescription(className=None, **props):
    return t"""
        <{DialogPrimitive.Description}
            data-slot="dialog-description"
            class={cn("text-xs/relaxed text-muted-foreground *:[a]:underline *:[a]:underline-offset-3 *:[a]:hover:text-foreground", className)}
            ...{props}
        />
    """
