from javascript import NULL
from reacthon import create_context, use_context, use_memo
from utils import cn

__js__ = {"@base-ui/react/drawer": ["Drawer as DrawerPrimitive"]}

DrawerContext = create_context(None)


def use_drawer():
    context = use_context(DrawerContext)

    if not context:
        raise RuntimeError("useDrawer must be used within a Drawer.")

    return context


def Drawer(modal=True, showSwipeHandle=False, snapPoints=None, swipeDirection="down", **props):
    has_snap_points = snapPoints not in (None, NULL) and len(snapPoints) > 0
    context_value = use_memo(
        lambda: {
            "hasSnapPoints": has_snap_points,
            "modal": modal,
            "showSwipeHandle": showSwipeHandle,
            "swipeDirection": swipeDirection,
        },
        [has_snap_points, modal, showSwipeHandle, swipeDirection],
    )

    return t"""
        <{DrawerContext.Provider} value={context_value}>
            <{DrawerPrimitive.Root}
                data-slot="drawer"
                modal={modal}
                snapPoints={snapPoints}
                swipeDirection={swipeDirection}
                ...{props}
            />
        </{DrawerContext.Provider}>
    """


def DrawerTrigger(**props):
    return t'<{DrawerPrimitive.Trigger} data-slot="drawer-trigger" ...{props} />'


def DrawerPortal(**props):
    return t'<{DrawerPrimitive.Portal} data-slot="drawer-portal" ...{props} />'


def DrawerClose(**props):
    return t'<{DrawerPrimitive.Close} data-slot="drawer-close" ...{props} />'


def DrawerOverlay(className=None, **props):
    return t"""
        <{DrawerPrimitive.Backdrop}
            data-slot="drawer-overlay"
            class={cn("fixed inset-0 z-50 min-h-dvh bg-black/10 opacity-[max(var(--drawer-overlay-min-opacity,0),calc(1-var(--drawer-swipe-progress)))] transition-opacity duration-450 ease-[cubic-bezier(0.32,0.72,0,1)] select-none data-ending-style:pointer-events-none data-ending-style:opacity-0 data-ending-style:duration-[calc(var(--drawer-swipe-strength)*400ms)] data-snap-points:[--drawer-overlay-min-opacity:0.5] data-starting-style:opacity-0 data-swiping:duration-0 supports-backdrop-filter:backdrop-blur-xs supports-[-webkit-touch-callout:none]:absolute", className)}
            ...{props}
        />
    """


def DrawerSwipeHandle(className=None, **props):
    return t"""
        <div
            data-slot="drawer-swipe-handle"
            aria-hidden="true"
            class={cn("relative z-10 flex shrink-0 cursor-grab transition-opacity duration-200 group-data-nested-drawer-open/drawer-popup:opacity-0 group-data-nested-drawer-swiping/drawer-popup:opacity-100 group-data-[swipe-axis=x]/drawer-popup:h-full group-data-[swipe-axis=x]/drawer-popup:w-3 group-data-[swipe-axis=x]/drawer-popup:items-center group-data-[swipe-axis=y]/drawer-popup:h-3 group-data-[swipe-axis=y]/drawer-popup:w-full group-data-[swipe-axis=y]/drawer-popup:justify-center group-data-[swipe-direction=down]/drawer-popup:items-end group-data-[swipe-direction=left]/drawer-popup:order-last group-data-[swipe-direction=left]/drawer-popup:justify-start group-data-[swipe-direction=right]/drawer-popup:justify-end group-data-[swipe-direction=up]/drawer-popup:order-last group-data-[swipe-direction=up]/drawer-popup:items-start after:block after:shrink-0 after:rounded-full after:bg-muted group-data-[swipe-axis=x]/drawer-popup:after:h-24 group-data-[swipe-axis=x]/drawer-popup:after:w-1 group-data-[swipe-axis=y]/drawer-popup:after:h-1 group-data-[swipe-axis=y]/drawer-popup:after:w-24 active:cursor-grabbing", className)}
            ...{props}
        />
    """


def DrawerContent(className=None, children=None, **props):
    drawer = use_drawer()
    has_snap_points, modal, show_swipe_handle, swipe_direction = drawer.get("hasSnapPoints"), drawer.get("modal"), drawer.get("showSwipeHandle"), drawer.get("swipeDirection")
    swipe_axis = "y" if swipe_direction == "down" or swipe_direction == "up" else "x"

    return t"""
        <{DrawerPortal} data-slot="drawer-portal">
            {modal == True and t'<{DrawerOverlay} data-snap-points={"" if has_snap_points else None} />'}
            <{DrawerPrimitive.Viewport}
                data-slot="drawer-viewport"
                data-modal={modal}
                class="pointer-events-none fixed inset-0 z-50 select-none data-[modal=true]:pointer-events-auto"
            >
                <{DrawerPrimitive.Popup}
                    data-slot="drawer-popup"
                    data-swipe-axis={swipe_axis}
                    data-snap-points={"" if has_snap_points else None}
                    class={cn(
                        "group/drawer-popup pointer-events-auto fixed z-50 m-(--drawer-inset,0px) flex h-(--drawer-content-height) max-h-(--drawer-content-max-height,none) min-h-0 w-(--drawer-content-width,auto) transform-[translate3d(var(--translate-x,0px),var(--translate-y,0px),0)_scale(var(--stack-scale))] flex-col bg-popover text-sm text-popover-foreground transition-[transform,height,opacity,filter] duration-450 ease-[cubic-bezier(0.22,1,0.36,1)] will-change-transform outline-none select-none [interpolate-size:allow-keywords] data-[swipe-direction=down]:rounded-t-xl data-[swipe-direction=down]:border-t data-[swipe-direction=left]:rounded-r-xl data-[swipe-direction=left]:border-r data-[swipe-direction=right]:rounded-l-xl data-[swipe-direction=right]:border-l data-[swipe-direction=up]:rounded-b-xl data-[swipe-direction=up]:border-b",
                        "data-nested-drawer-open:overflow-hidden data-nested-drawer-open:brightness-95",
                        "after:pointer-events-none after:absolute after:bg-(--drawer-bleed-background,var(--color-popover)) data-[swipe-axis=x]:after:inset-y-0 data-[swipe-axis=x]:after:w-(--bleed) data-[swipe-axis=y]:after:inset-x-0 data-[swipe-axis=y]:after:h-(--bleed) data-[swipe-direction=down]:after:top-full data-[swipe-direction=left]:after:right-full data-[swipe-direction=right]:after:left-full data-[swipe-direction=up]:after:bottom-full",
                        "[--drawer-content-height:var(--drawer-height,auto)] data-[swipe-axis=x]:[--drawer-content-width:75%] data-[swipe-axis=y]:[--drawer-content-max-height:calc(100dvh-6rem)] data-[swipe-axis=y]:data-snap-points:[--drawer-content-height:100dvh] data-[swipe-axis=x]:sm:[--drawer-content-width:24rem]",
                        "[--bleed:3rem] [--peek:1rem] [--stack-height:var(--drawer-frontmost-height,var(--drawer-height,0px))] [--stack-peek-offset:max(0px,calc((var(--nested-drawers)-var(--stack-progress))*var(--peek)))] [--stack-progress:clamp(0,var(--drawer-swipe-progress),1)] [--stack-scale-base:max(0,calc(1-(var(--nested-drawers)*var(--stack-step))))] [--stack-scale:clamp(0,calc(var(--stack-scale-base)+(var(--stack-step)*var(--stack-progress))),1)] [--stack-shrink:calc(1-var(--stack-scale))] [--stack-step:0.05]",
                        "data-ending-style:transform-(--closed-transform) data-ending-style:opacity-[0.9999] data-ending-style:duration-[calc(var(--drawer-swipe-strength)*400ms)] data-nested-drawer-swiping:duration-0 data-ending-style:data-nested-drawer-swiping:duration-[calc(var(--drawer-swipe-strength)*400ms)] data-starting-style:transform-(--closed-transform) data-swiping:duration-0 data-ending-style:data-swiping:duration-[calc(var(--drawer-swipe-strength)*400ms)]",
                        "data-[swipe-axis=y]:inset-x-0 data-[swipe-axis=y]:data-nested-drawer-open:h-(--stack-height)",
                        "data-[swipe-axis=x]:inset-y-0 data-[swipe-axis=x]:flex-row",
                        "data-[swipe-direction=down]:bottom-0 data-[swipe-direction=down]:origin-bottom data-[swipe-direction=down]:[--closed-transform:translate3d(0,calc(100%+var(--drawer-inset,0px)+2px),0)] data-[swipe-direction=down]:[--translate-y:calc(var(--drawer-snap-point-offset,0px)+var(--drawer-swipe-movement-y)-var(--stack-peek-offset)-(var(--stack-shrink)*var(--stack-height)))]",
                        "data-[swipe-direction=up]:top-0 data-[swipe-direction=up]:origin-top data-[swipe-direction=up]:[--closed-transform:translate3d(0,calc(-100%-var(--drawer-inset,0px)-2px),0)] data-[swipe-direction=up]:[--translate-y:calc(var(--drawer-snap-point-offset,0px)+var(--drawer-swipe-movement-y)+var(--stack-peek-offset)+(var(--stack-shrink)*var(--stack-height)))]",
                        "data-[swipe-direction=left]:left-0 data-[swipe-direction=left]:origin-left data-[swipe-direction=left]:[--closed-transform:translate3d(calc(-100%-var(--drawer-inset,0px)-2px),0,0)] data-[swipe-direction=left]:[--translate-x:calc(var(--drawer-swipe-movement-x)+var(--stack-peek-offset)+(var(--stack-shrink)*100%))]",
                        "data-[swipe-direction=right]:right-0 data-[swipe-direction=right]:origin-right data-[swipe-direction=right]:[--closed-transform:translate3d(calc(100%+var(--drawer-inset,0px)+2px),0,0)] data-[swipe-direction=right]:[--translate-x:calc(var(--drawer-swipe-movement-x)-var(--stack-peek-offset)-(var(--stack-shrink)*100%))]",
                        className,
                    )}
                    ...{props}
                >
                    {show_swipe_handle and t'<{DrawerSwipeHandle} />'}
                    <{DrawerPrimitive.Content}
                        data-slot="drawer-content"
                        class={cn("flex min-h-0 flex-1 flex-col overflow-hidden overscroll-contain rounded-[inherit] transition-opacity duration-300 ease-[cubic-bezier(0.45,1.005,0,1.005)] select-text group-data-nested-drawer-open/drawer-popup:opacity-0 group-data-nested-drawer-swiping/drawer-popup:opacity-100 group-data-swiping/drawer-popup:select-none")}
                    >
                        {children}
                    </{DrawerPrimitive.Content}>
                </{DrawerPrimitive.Popup}>
            </{DrawerPrimitive.Viewport}>
        </{DrawerPortal}>
    """


def DrawerHeader(className=None, **props):
    return t"""
        <div
            data-slot="drawer-header"
            class={cn("flex shrink-0 flex-col gap-0.5 p-4 pb-0 group-data-[swipe-axis=y]/drawer-popup:text-center md:gap-0.5 md:text-left", className)}
            ...{props}
        />
    """


def DrawerFooter(className=None, **props):
    return t"""
        <div
            data-slot="drawer-footer"
            class={cn("mt-auto flex shrink-0 flex-col gap-2 p-4 pt-0", className)}
            ...{props}
        />
    """


def DrawerTitle(className=None, **props):
    return t"""
        <{DrawerPrimitive.Title}
            data-slot="drawer-title"
            class={cn("font-heading text-base font-medium text-foreground", className)}
            ...{props}
        />
    """


def DrawerDescription(className=None, **props):
    return t"""
        <{DrawerPrimitive.Description}
            data-slot="drawer-description"
            class={cn("text-sm text-balance text-muted-foreground", className)}
            ...{props}
        />
    """
