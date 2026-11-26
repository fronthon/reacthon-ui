from utils import cn
from button import Button

__js__ = {
    "react-aria-components": [
        "Dialog as DialogPrimitive",
        "DialogTrigger as DialogTriggerPrimitive",
        "Heading",
        "ModalOverlay as ModalOverlayPrimitive",
        "Modal as ModalPrimitive",
    ],
    "lucide-react": ["XIcon"],
}


def DialogTrigger(**props):
    return t'<{DialogTriggerPrimitive} data-slot="dialog-trigger" ...{props} />'


def DialogClose(className=None, variant="outline", size="default", **props):
    return t"""
        <{Button}
            slot="close"
            data-slot="dialog-close"
            variant={variant}
            size={size}
            class={cn(className)}
            ...{props}
        />
    """


def DialogOverlay(className=None, children=None, **props):
    return t"""
        <{ModalOverlayPrimitive}
            data-slot="dialog-overlay"
            class={cn("fixed inset-0 isolate z-50 bg-black/20 duration-100 data-entering:animate-in data-entering:fade-in-0 data-exiting:animate-out data-exiting:fade-out-0 supports-backdrop-filter:backdrop-blur-sm", className)}
            ...{props}
        >
            {children}
        </{ModalOverlayPrimitive}>
    """


def Dialog(className=None, children=None, showCloseButton=True, isDismissable=True, **props):
    dialog_close = t"""
        <{DialogClose} variant="ghost" class="absolute top-5 right-5 bg-secondary" size="icon-sm">
            <{XIcon} />
            <span class="sr-only">Close</span>
        </{DialogClose}>
    """

    return t"""
        <{DialogOverlay} isDismissable={isDismissable} ...{props}>
            <{ModalPrimitive}
                data-slot="dialog-content"
                class={cn("fixed top-1/2 left-1/2 z-50 grid w-full max-w-[calc(100%-2rem)] -translate-x-1/2 -translate-y-1/2 gap-6 rounded-none bg-popover p-6 text-sm text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 outline-none data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 sm:max-w-md", className)}
            >
                <{DialogPrimitive} data-slot="dialog" class="[display:inherit] [gap:inherit] outline-none">
                    {children}
                    {showCloseButton and dialog_close}
                </{DialogPrimitive}>
            </{ModalPrimitive}>
        </{DialogOverlay}>
    """


def DialogHeader(className=None, **props):
    return t'<div data-slot="dialog-header" class={cn("flex flex-col gap-2", className)} ...{props} />'


def DialogFooter(className=None, showCloseButton=False, children=None, **props):
    return t"""
        <div
            data-slot="dialog-footer"
            class={cn("flex flex-col-reverse gap-2 sm:flex-row sm:justify-end", className)}
            ...{props}
        >
            {children}
            {showCloseButton and t'<{DialogClose} variant="outline">Close</{DialogClose}>'}
        </div>
    """


def DialogTitle(className=None, **props):
    return t"""
        <{Heading}
            slot="title"
            data-slot="dialog-title"
            class={cn("font-heading text-lg leading-none font-semibold tracking-wider uppercase", className)}
            ...{props}
        />
    """


def DialogDescription(className=None, **props):
    return t"""
        <div
            data-slot="dialog-description"
            class={cn("mt-0.5 text-sm leading-relaxed text-muted-foreground *:[a]:underline *:[a]:underline-offset-3 *:[a]:hover:text-foreground", className)}
            ...{props}
        />
    """
