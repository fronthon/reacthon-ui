from utils import cn
from button import Button

__js__ = {
    "react-aria-components": [
        "Heading",
        "ModalOverlay as ModalOverlayPrimitive",
        "Modal as ModalPrimitive",
        "Dialog as SheetPrimitive",
        "DialogTrigger as SheetTriggerPrimitive",
    ],
    "lucide-react": ["XIcon"],
}


def SheetTrigger(**props):
    return t'<{SheetTriggerPrimitive} data-slot="sheet-trigger" ...{props} />'


def SheetClose(className=None, variant="outline", size="default", **props):
    return t"""
        <{Button}
            slot="close"
            data-slot="sheet-close"
            variant={variant}
            size={size}
            class={cn(className)}
            ...{props}
        />
    """


def SheetOverlay(className=None, children=None, **props):
    return t"""
        <{ModalOverlayPrimitive}
            data-slot="sheet-overlay"
            isDismissable
            class={cn("fixed inset-0 z-50 bg-black/30 transition-opacity duration-150 data-entering:opacity-0 data-exiting:opacity-0 supports-backdrop-filter:backdrop-blur-sm", className)}
            ...{props}
        >
            {children}
        </{ModalOverlayPrimitive}>
    """


def Sheet(className=None, children=None, side="right", showCloseButton=True, **props):
    sheet_close = t"""
        <{SheetClose} variant="ghost" class="absolute top-4 right-4 bg-secondary" size="icon-sm">
            <{XIcon} />
            <span class="sr-only">Close</span>
        </{SheetClose}>
    """

    return t"""
        <{SheetOverlay} ...{props}>
            <{ModalPrimitive}
                data-slot="sheet-content"
                data-side={side}
                class={cn("fixed z-50 flex flex-col bg-popover bg-clip-padding text-sm text-popover-foreground shadow-xl transition duration-200 ease-in-out data-entering:opacity-0 data-exiting:opacity-0 data-[side=bottom]:inset-x-0 data-[side=bottom]:bottom-0 data-[side=bottom]:h-auto data-[side=bottom]:border-t data-[side=bottom]:data-entering:translate-y-[2.5rem] data-[side=bottom]:data-exiting:translate-y-[2.5rem] data-[side=left]:inset-y-0 data-[side=left]:left-0 data-[side=left]:h-full data-[side=left]:w-3/4 data-[side=left]:border-r data-[side=left]:data-entering:translate-x-[-2.5rem] data-[side=left]:data-exiting:translate-x-[-2.5rem] data-[side=right]:inset-y-0 data-[side=right]:right-0 data-[side=right]:h-full data-[side=right]:w-3/4 data-[side=right]:border-l data-[side=right]:data-entering:translate-x-[2.5rem] data-[side=right]:data-exiting:translate-x-[2.5rem] data-[side=top]:inset-x-0 data-[side=top]:top-0 data-[side=top]:h-auto data-[side=top]:border-b data-[side=top]:data-entering:translate-y-[-2.5rem] data-[side=top]:data-exiting:translate-y-[-2.5rem] data-[side=left]:sm:max-w-sm data-[side=right]:sm:max-w-sm", className)}
            >
                <{SheetPrimitive}
                    data-slot="sheet"
                    class="[display:inherit] h-full max-h-[inherit] [flex-direction:inherit] [gap:inherit] outline-none"
                >
                    {children}
                    {showCloseButton and sheet_close}
                </{SheetPrimitive}>
            </{ModalPrimitive}>
        </{SheetOverlay}>
    """


def SheetContent(className=None, children=None, side="right", showCloseButton=True, **props):
    return t"<{Sheet} class={className} side={side} showCloseButton={showCloseButton} ...{props}>{children}</{Sheet}>"


def SheetHeader(className=None, **props):
    return t'<div data-slot="sheet-header" class={cn("flex flex-col gap-1.5 p-6", className)} ...{props} />'


def SheetFooter(className=None, **props):
    return t'<div data-slot="sheet-footer" class={cn("mt-auto flex flex-col gap-2 p-6", className)} ...{props} />'


def SheetTitle(className=None, **props):
    return t"""
        <{Heading}
            slot="title"
            data-slot="sheet-title"
            class={cn("font-heading text-base font-medium text-foreground", className)}
            ...{props}
        />
    """


def SheetDescription(className=None, **props):
    return t'<div data-slot="sheet-description" class={cn("text-sm text-muted-foreground", className)} ...{props} />'
