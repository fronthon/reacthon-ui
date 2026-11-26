from utils import cn
from button import Button

__js__ = {"@base-ui/react/alert-dialog": ["AlertDialog as AlertDialogPrimitive"]}


def AlertDialog(**props):
    return t'<{AlertDialogPrimitive.Root} data-slot="alert-dialog" ...{props} />'


def AlertDialogTrigger(**props):
    return t'<{AlertDialogPrimitive.Trigger} data-slot="alert-dialog-trigger" ...{props} />'


def AlertDialogPortal(**props):
    return t'<{AlertDialogPrimitive.Portal} data-slot="alert-dialog-portal" ...{props} />'


def AlertDialogOverlay(className=None, **props):
    return t"""
        <{AlertDialogPrimitive.Backdrop}
            data-slot="alert-dialog-overlay"
            class={cn("fixed inset-0 isolate z-50 bg-black/10 duration-100 supports-backdrop-filter:backdrop-blur-xs data-open:animate-in data-open:fade-in-0 data-closed:animate-out data-closed:fade-out-0", className)}
            ...{props}
        />
    """


def AlertDialogContent(className=None, size="default", **props):
    return t"""
        <{AlertDialogPortal}>
            <{AlertDialogOverlay} />
            <{AlertDialogPrimitive.Popup}
                data-slot="alert-dialog-content"
                data-size={size}
                class={cn("group/alert-dialog-content fixed top-1/2 left-1/2 z-50 grid w-full -translate-x-1/2 -translate-y-1/2 gap-4 rounded-none bg-popover p-4 text-popover-foreground ring-1 ring-foreground/10 duration-100 outline-none data-[size=default]:max-w-xs data-[size=sm]:max-w-xs data-[size=default]:sm:max-w-sm data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                ...{props}
            />
        </{AlertDialogPortal}>
    """


def AlertDialogHeader(className=None, **props):
    return t"""
        <div
            data-slot="alert-dialog-header"
            class={cn("grid grid-rows-[auto_1fr] place-items-center gap-1.5 text-center has-data-[slot=alert-dialog-media]:grid-rows-[auto_auto_1fr] has-data-[slot=alert-dialog-media]:gap-x-4 sm:group-data-[size=default]/alert-dialog-content:place-items-start sm:group-data-[size=default]/alert-dialog-content:text-left sm:group-data-[size=default]/alert-dialog-content:has-data-[slot=alert-dialog-media]:grid-rows-[auto_1fr]", className)}
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
            class={cn("mb-2 inline-flex size-10 items-center justify-center rounded-none bg-muted sm:group-data-[size=default]/alert-dialog-content:row-span-2 *:[svg:not([class*='size-'])]:size-6", className)}
            ...{props}
        />
    """


def AlertDialogTitle(className=None, **props):
    return t"""
        <{AlertDialogPrimitive.Title}
            data-slot="alert-dialog-title"
            class={cn("font-heading text-sm font-medium sm:group-data-[size=default]/alert-dialog-content:group-has-data-[slot=alert-dialog-media]/alert-dialog-content:col-start-2", className)}
            ...{props}
        />
    """


def AlertDialogDescription(className=None, **props):
    return t"""
        <{AlertDialogPrimitive.Description}
            data-slot="alert-dialog-description"
            class={cn("text-xs/relaxed text-balance text-muted-foreground md:text-pretty *:[a]:underline *:[a]:underline-offset-3 *:[a]:hover:text-foreground", className)}
            ...{props}
        />
    """


def AlertDialogAction(className=None, **props):
    return t'<{Button} data-slot="alert-dialog-action" class={cn(className)} ...{props} />'


def AlertDialogCancel(className=None, variant="outline", size="default", **props):
    return t"""
        <{AlertDialogPrimitive.Close}
            data-slot="alert-dialog-cancel"
            class={cn(className)}
            render={t'<{Button} variant={variant} size={size} />'}
            ...{props}
        />
    """
