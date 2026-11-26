from utils import cn
from button import Button

__js__ = {"radix-ui": ["Dialog as SheetPrimitive"], "lucide-react": ["XIcon"]}


def Sheet(**props):
    return t'<{SheetPrimitive.Root} data-slot="sheet" ...{props} />'


def SheetTrigger(**props):
    return t'<{SheetPrimitive.Trigger} data-slot="sheet-trigger" ...{props} />'


def SheetClose(**props):
    return t'<{SheetPrimitive.Close} data-slot="sheet-close" ...{props} />'


def SheetPortal(**props):
    return t'<{SheetPrimitive.Portal} data-slot="sheet-portal" ...{props} />'


def SheetOverlay(className=None, **props):
    return t"""
        <{SheetPrimitive.Overlay}
            data-slot="sheet-overlay"
            class={cn("fixed inset-0 z-50 bg-black/10 duration-100 supports-backdrop-filter:backdrop-blur-xs data-open:animate-in data-open:fade-in-0 data-closed:animate-out data-closed:fade-out-0", className)}
            ...{props}
        />
    """


def SheetContent(className=None, children=None, side="right", showCloseButton=True, **props):
    close = t"""
        <{SheetPrimitive.Close} data-slot="sheet-close" asChild>
            <{Button} variant="ghost" class="absolute top-4 right-4" size="icon-sm">
                <{XIcon} />
                <span class="sr-only">Close</span>
            </{Button}>
        </{SheetPrimitive.Close}>
    """

    return t"""
        <{SheetPortal}>
            <{SheetOverlay} />
            <{SheetPrimitive.Content}
                data-slot="sheet-content"
                data-side={side}
                class={cn("fixed z-50 flex flex-col gap-4 bg-popover bg-clip-padding text-sm text-popover-foreground shadow-lg transition duration-200 ease-in-out data-[side=bottom]:inset-x-0 data-[side=bottom]:bottom-0 data-[side=bottom]:h-auto data-[side=bottom]:border-t data-[side=left]:inset-y-0 data-[side=left]:left-0 data-[side=left]:h-full data-[side=left]:w-3/4 data-[side=left]:border-r data-[side=right]:inset-y-0 data-[side=right]:right-0 data-[side=right]:h-full data-[side=right]:w-3/4 data-[side=right]:border-l data-[side=top]:inset-x-0 data-[side=top]:top-0 data-[side=top]:h-auto data-[side=top]:border-b data-[side=left]:sm:max-w-sm data-[side=right]:sm:max-w-sm data-open:animate-in data-open:fade-in-0 data-[side=bottom]:data-open:slide-in-from-bottom-10 data-[side=left]:data-open:slide-in-from-left-10 data-[side=right]:data-open:slide-in-from-right-10 data-[side=top]:data-open:slide-in-from-top-10 data-closed:animate-out data-closed:fade-out-0 data-[side=bottom]:data-closed:slide-out-to-bottom-10 data-[side=left]:data-closed:slide-out-to-left-10 data-[side=right]:data-closed:slide-out-to-right-10 data-[side=top]:data-closed:slide-out-to-top-10", className)}
                ...{props}
            >
                {children}
                {showCloseButton and close}
            </{SheetPrimitive.Content}>
        </{SheetPortal}>
    """


def SheetHeader(className=None, **props):
    return t'<div data-slot="sheet-header" class={cn("flex flex-col gap-1.5 p-4", className)} ...{props} />'


def SheetFooter(className=None, **props):
    return t'<div data-slot="sheet-footer" class={cn("mt-auto flex flex-col gap-2 p-4", className)} ...{props} />'


def SheetTitle(className=None, **props):
    return t"""
        <{SheetPrimitive.Title}
            data-slot="sheet-title"
            class={cn("font-heading font-medium text-foreground", className)}
            ...{props}
        />
    """


def SheetDescription(className=None, **props):
    return t"""
        <{SheetPrimitive.Description}
            data-slot="sheet-description"
            class={cn("text-sm text-muted-foreground", className)}
            ...{props}
        />
    """
