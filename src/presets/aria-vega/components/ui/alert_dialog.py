from utils import cn
from button import Button

__js__ = {
    "react-aria-components": [
        "Dialog as AlertDialogPrimitive",
        "DialogTrigger as AlertDialogTriggerPrimitive",
        "Heading",
        "ModalOverlay as ModalOverlayPrimitive",
        "Modal as ModalPrimitive",
    ],
}


def AlertDialogTrigger(**props):
    return t'<{AlertDialogTriggerPrimitive} data-slot="alert-dialog-trigger" ...{props} />'


def AlertDialogOverlay(className=None, children=None, **props):
    return t"""
        <{ModalOverlayPrimitive}
            data-slot="alert-dialog-overlay"
            class={cn("fixed inset-0 isolate z-50 bg-black/10 duration-100 data-entering:animate-in data-entering:fade-in-0 data-exiting:animate-out data-exiting:fade-out-0 supports-backdrop-filter:backdrop-blur-xs", className)}
            ...{props}
        >
            {children}
        </{ModalOverlayPrimitive}>
    """


def AlertDialog(className=None, size="default", children=None, **props):
    return t"""
        <{AlertDialogOverlay} ...{props}>
            <{ModalPrimitive}
                data-slot="alert-dialog-content"
                data-size={size}
                class={cn("group/alert-dialog-content fixed top-1/2 left-1/2 z-50 grid w-full -translate-x-1/2 -translate-y-1/2 gap-6 rounded-xl bg-popover p-6 text-popover-foreground ring-1 ring-foreground/10 duration-100 outline-none data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[size=default]:max-w-xs data-[size=sm]:max-w-xs data-[size=default]:sm:max-w-lg", className)}
            >
                <{AlertDialogPrimitive}
                    data-slot="alert-dialog"
                    role="alertdialog"
                    class="[display:inherit] [gap:inherit] outline-none"
                >
                    {children}
                </{AlertDialogPrimitive}>
            </{ModalPrimitive}>
        </{AlertDialogOverlay}>
    """


def AlertDialogContent(className=None, size="default", children=None, **props):
    return t"<{AlertDialog} class={className} size={size} ...{props}>{children}</{AlertDialog}>"


def AlertDialogHeader(className=None, **props):
    return t"""
        <div
            data-slot="alert-dialog-header"
            class={cn("grid grid-rows-[auto_1fr] place-items-center gap-1.5 text-center has-data-[slot=alert-dialog-media]:grid-rows-[auto_auto_1fr] has-data-[slot=alert-dialog-media]:gap-x-6 sm:group-data-[size=default]/alert-dialog-content:place-items-start sm:group-data-[size=default]/alert-dialog-content:text-left sm:group-data-[size=default]/alert-dialog-content:has-data-[slot=alert-dialog-media]:grid-rows-[auto_1fr]", className)}
            ...{props}
        />
    """


def AlertDialogFooter(className=None, **props):
    return t"""
        <div
            data-slot="alert-dialog-footer"
            class={cn("flex flex-col-reverse gap-2 group-data-[size=sm]/alert-dialog-content:grid group-data-[size=sm]/alert-dialog-content:grid-cols-2 sm:flex-row sm:justify-end", className)}
            ...{props}
        />
    """


def AlertDialogMedia(className=None, **props):
    return t"""
        <div
            data-slot="alert-dialog-media"
            class={cn("mb-2 inline-flex size-16 items-center justify-center rounded-md bg-muted sm:group-data-[size=default]/alert-dialog-content:row-span-2 *:[svg:not([class*='size-'])]:size-8", className)}
            ...{props}
        />
    """


def AlertDialogTitle(className=None, **props):
    return t"""
        <{Heading}
            slot="title"
            data-slot="alert-dialog-title"
            class={cn("font-heading text-lg font-medium sm:group-data-[size=default]/alert-dialog-content:group-has-data-[slot=alert-dialog-media]/alert-dialog-content:col-start-2", className)}
            ...{props}
        />
    """


def AlertDialogDescription(className=None, **props):
    return t"""
        <div
            data-slot="alert-dialog-description"
            class={cn("text-sm text-balance text-muted-foreground md:text-pretty *:[a]:underline *:[a]:underline-offset-3 *:[a]:hover:text-foreground", className)}
            ...{props}
        />
    """


def AlertDialogAction(className=None, **props):
    return t'<{Button} slot="close" data-slot="alert-dialog-action" class={cn(className)} ...{props} />'


def AlertDialogCancel(className=None, variant="outline", size="default", **props):
    return t"""
        <{Button}
            slot="close"
            data-slot="alert-dialog-cancel"
            class={cn(className)}
            variant={variant}
            size={size}
            ...{props}
        />
    """
