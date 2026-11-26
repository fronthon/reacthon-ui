from utils import cn
from button import Button

__js__ = {
    "@base-ui/react/toast": ["Toast as ToastPrimitive"],
    "lucide-react": ["XIcon", "CircleCheckIcon", "InfoIcon", "TriangleAlertIcon", "OctagonXIcon", "Loader2Icon"],
}

toast = ToastPrimitive.createToastManager()


def ToastProvider(**props):
    return t"<{ToastPrimitive.Provider} ...{props} />"


def ToastPortal(**props):
    return t'<{ToastPrimitive.Portal} data-slot="toast-portal" ...{props} />'


def ToastViewport(className=None, **props):
    return t"""
        <{ToastPrimitive.Viewport}
            data-slot="toast-viewport"
            class={cn("pointer-events-none fixed inset-x-4 bottom-4 z-50 mx-auto w-auto max-w-sm outline-none sm:right-4 sm:left-auto sm:mx-0 sm:w-full", className)}
            ...{props}
        />
    """


def Toast(className=None, **props):
    return t"""
        <{ToastPrimitive.Root}
            data-slot="toast"
            class={cn(
                "group/toast pointer-events-auto absolute right-0 bottom-0 z-[calc(1000-var(--toast-index))] w-full origin-bottom rounded-2xl border bg-popover text-popover-foreground shadow-lg will-change-transform outline-none select-none focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50",
                "[--gap:0.75rem] [--height:var(--toast-frontmost-height,var(--toast-height))] [--offset-y:calc(var(--toast-offset-y)*-1+calc(var(--toast-index)*var(--gap)*-1)+var(--toast-swipe-movement-y))] [--peek:0.75rem] [--scale:calc(max(0,1-(var(--toast-index)*0.1)))] [--shrink:calc(1-var(--scale))]",
                "h-(--height) [transform:translateX(var(--toast-swipe-movement-x))_translateY(calc(var(--toast-swipe-movement-y)-(var(--toast-index)*var(--peek))-(var(--shrink)*var(--height))))_scale(var(--scale))] [transition:transform_500ms_cubic-bezier(0.22,1,0.36,1),opacity_500ms,height_150ms]",
                "after:absolute after:top-full after:left-0 after:h-[calc(var(--gap)+1px)] after:w-full after:content-['']",
                "data-expanded:h-(--toast-height) data-expanded:[transform:translateX(var(--toast-swipe-movement-x))_translateY(var(--offset-y))]",
                "data-limited:opacity-0 data-starting-style:[transform:translateY(150%)]",
                "[&[data-ending-style]:not([data-limited]):not([data-swipe-direction])]:[transform:translateY(150%)]",
                "data-ending-style:data-[swipe-direction=down]:[transform:translateY(calc(var(--toast-swipe-movement-y)+150%))]",
                "data-ending-style:data-[swipe-direction=left]:[transform:translateX(calc(var(--toast-swipe-movement-x)-150%))_translateY(var(--offset-y))]",
                "data-ending-style:data-[swipe-direction=right]:[transform:translateX(calc(var(--toast-swipe-movement-x)+150%))_translateY(var(--offset-y))]",
                "data-ending-style:data-[swipe-direction=up]:[transform:translateY(calc(var(--toast-swipe-movement-y)-150%))]",
                "data-expanded:data-ending-style:data-[swipe-direction=down]:[transform:translateY(calc(var(--toast-swipe-movement-y)+150%))]",
                "data-expanded:data-ending-style:data-[swipe-direction=left]:[transform:translateX(calc(var(--toast-swipe-movement-x)-150%))_translateY(var(--offset-y))]",
                "data-expanded:data-ending-style:data-[swipe-direction=right]:[transform:translateX(calc(var(--toast-swipe-movement-x)+150%))_translateY(var(--offset-y))]",
                "data-expanded:data-ending-style:data-[swipe-direction=up]:[transform:translateY(calc(var(--toast-swipe-movement-y)-150%))]",
                className,
            )}
            ...{props}
        />
    """


def ToastContent(className=None, **props):
    return t"""
        <{ToastPrimitive.Content}
            data-slot="toast-content"
            class={cn("flex h-full items-center gap-3 overflow-hidden p-4 transition-opacity duration-250 ease-[cubic-bezier(0.22,1,0.36,1)] data-behind:opacity-0 data-expanded:opacity-100", className)}
            ...{props}
        />
    """


def ToastTitle(className=None, **props):
    return t'<{ToastPrimitive.Title} data-slot="toast-title" class={cn("text-sm font-medium", className)} ...{props} />'


def ToastDescription(className=None, **props):
    return t"""
        <{ToastPrimitive.Description}
            data-slot="toast-description"
            class={cn("text-sm text-muted-foreground", className)}
            ...{props}
        />
    """


def ToastAction(className=None, render=t'<{Button} variant="outline" size="sm" />', **props):
    return t"""
        <{ToastPrimitive.Action}
            data-slot="toast-action"
            render={render}
            class={cn("shrink-0", className)}
            ...{props}
        />
    """


def ToastClose(className=None, children=None, render=t'<{Button} variant="ghost" size="icon-sm" />', **props):
    return t"""
        <{ToastPrimitive.Close}
            data-slot="toast-close"
            aria-label="Close toast"
            render={render}
            class={cn("relative shrink-0 text-muted-foreground after:absolute after:-inset-2 after:content-[''] hover:text-foreground", className)}
            ...{props}
        >
            {children if children is not None else t'<{XIcon} aria-hidden="true" />'}
        </{ToastPrimitive.Close}>
    """


def ToastIcon(type=None):
    icon = None

    if type == "success":
        icon = t'<{CircleCheckIcon} aria-hidden="true" />'

    if type == "info":
        icon = t'<{InfoIcon} aria-hidden="true" />'

    if type == "warning":
        icon = t'<{TriangleAlertIcon} aria-hidden="true" />'

    if type == "error":
        icon = t'<{OctagonXIcon} class="text-destructive" aria-hidden="true" />'

    if type == "loading":
        icon = t'<{Loader2Icon} class="animate-spin" aria-hidden="true" />'

    if not icon:
        return None

    return t"""
        <span
            data-slot="toast-icon"
            class="shrink-0 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4"
        >
            {icon}
        </span>
    """


def ToastList():
    toasts = ToastPrimitive.useToastManager().toasts

    return [t"""
        <{Toast} key={toast_item["id"]} toast={toast_item}>
            <{ToastContent}>
                <{ToastIcon} type={toast_item.get("type")} />
                <div class="flex min-w-0 flex-1 flex-col gap-1">
                    <{ToastTitle} />
                    <{ToastDescription} />
                </div>
                <{ToastAction} />
                <{ToastClose} />
            </{ToastContent}>
        </{Toast}>
    """ for toast_item in toasts]


def Toaster(children=None, toastManager=toast, **props):
    return t"""
        <{ToastProvider} toastManager={toastManager} ...{props}>
            {children}
            <{ToastPortal}>
                <{ToastViewport}>
                    <{ToastList} />
                </{ToastViewport}>
            </{ToastPortal}>
        </{ToastProvider}>
    """


create_toast_manager = ToastPrimitive.createToastManager

use_toast_manager = ToastPrimitive.useToastManager
