from utils import cn
from button import Button

__js__ = {"@base-ui/react/dialog": ["Dialog as SheetPrimitive"], "lucide-react": ["XIcon"]}


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
        <{SheetPrimitive.Backdrop}
            data-slot="sheet-overlay"
            class={cn("fixed inset-0 z-50 bg-black/20 transition-opacity duration-150 data-ending-style:opacity-0 data-starting-style:opacity-0 supports-backdrop-filter:backdrop-blur-sm", className)}
            ...{props}
        />
    """


def SheetContent(className=None, children=None, side="right", showCloseButton=True, **props):
    close = t"""
        <{SheetPrimitive.Close}
            data-slot="sheet-close"
            render={t'''
                <{Button}
                    variant="ghost"
                    class="absolute top-4 right-4 bg-secondary"
                    size="icon-sm"
                />
            '''}
        >
            <{XIcon} />
            <span class="sr-only">Close</span>
        </{SheetPrimitive.Close}>
    """

    return t"""
        <{SheetPortal}>
            <{SheetOverlay} />
            <{SheetPrimitive.Popup}
                data-slot="sheet-content"
                data-side={side}
                class={cn("fixed z-50 flex flex-col bg-popover bg-clip-padding text-sm text-popover-foreground shadow-md transition duration-200 ease-in-out data-ending-style:opacity-0 data-starting-style:opacity-0 data-[side=bottom]:inset-x-0 data-[side=bottom]:bottom-0 data-[side=bottom]:h-auto data-[side=bottom]:border-t data-[side=bottom]:data-ending-style:translate-y-[2.5rem] data-[side=bottom]:data-starting-style:translate-y-[2.5rem] data-[side=left]:inset-y-0 data-[side=left]:left-0 data-[side=left]:h-full data-[side=left]:w-3/4 data-[side=left]:border-r data-[side=left]:data-ending-style:translate-x-[-2.5rem] data-[side=left]:data-starting-style:translate-x-[-2.5rem] data-[side=right]:inset-y-0 data-[side=right]:right-0 data-[side=right]:h-full data-[side=right]:w-3/4 data-[side=right]:border-l data-[side=right]:data-ending-style:translate-x-[2.5rem] data-[side=right]:data-starting-style:translate-x-[2.5rem] data-[side=top]:inset-x-0 data-[side=top]:top-0 data-[side=top]:h-auto data-[side=top]:border-b data-[side=top]:data-ending-style:translate-y-[-2.5rem] data-[side=top]:data-starting-style:translate-y-[-2.5rem] data-[side=left]:sm:max-w-sm data-[side=right]:sm:max-w-sm", className)}
                ...{props}
            >
                {children}
                {showCloseButton and close}
            </{SheetPrimitive.Popup}>
        </{SheetPortal}>
    """


def SheetHeader(className=None, **props):
    return t'<div data-slot="sheet-header" class={cn("flex flex-col gap-1.5 p-8", className)} ...{props} />'


def SheetFooter(className=None, **props):
    return t'<div data-slot="sheet-footer" class={cn("mt-auto flex flex-col gap-2 p-8", className)} ...{props} />'


def SheetTitle(className=None, **props):
    return t"""
        <{SheetPrimitive.Title}
            data-slot="sheet-title"
            class={cn("font-heading text-lg font-semibold tracking-wider text-foreground uppercase", className)}
            ...{props}
        />
    """


def SheetDescription(className=None, **props):
    return t"""
        <{SheetPrimitive.Description}
            data-slot="sheet-description"
            class={cn("mt-0.5 text-sm leading-relaxed text-muted-foreground", className)}
            ...{props}
        />
    """
