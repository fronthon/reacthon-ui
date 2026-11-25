from utils import cn

__js__ = {"vaul": ["Drawer as DrawerPrimitive"]}


def Drawer(**props):
    return t'<{DrawerPrimitive.Root} data-slot="drawer" ...{props} />'


def DrawerTrigger(**props):
    return t'<{DrawerPrimitive.Trigger} data-slot="drawer-trigger" ...{props} />'


def DrawerPortal(**props):
    return t'<{DrawerPrimitive.Portal} data-slot="drawer-portal" ...{props} />'


def DrawerClose(**props):
    return t'<{DrawerPrimitive.Close} data-slot="drawer-close" ...{props} />'


def DrawerOverlay(className=None, **props):
    return t"""
        <{DrawerPrimitive.Overlay}
            data-slot="drawer-overlay"
            class={cn("fixed inset-0 z-50 bg-black/10 supports-backdrop-filter:backdrop-blur-xs data-open:animate-in data-open:fade-in-0 data-closed:animate-out data-closed:fade-out-0", className)}
            ...{props}
        />
    """


def DrawerContent(className=None, children=None, **props):
    return t"""
        <{DrawerPortal} data-slot="drawer-portal">
            <{DrawerOverlay} />
            <{DrawerPrimitive.Content}
                data-slot="drawer-content"
                class={cn("group/drawer-content fixed z-50 flex h-auto flex-col bg-popover text-sm text-popover-foreground data-[vaul-drawer-direction=bottom]:inset-x-0 data-[vaul-drawer-direction=bottom]:bottom-0 data-[vaul-drawer-direction=bottom]:mt-24 data-[vaul-drawer-direction=bottom]:max-h-[80vh] data-[vaul-drawer-direction=bottom]:rounded-t-xl data-[vaul-drawer-direction=bottom]:border-t data-[vaul-drawer-direction=left]:inset-y-0 data-[vaul-drawer-direction=left]:left-0 data-[vaul-drawer-direction=left]:w-3/4 data-[vaul-drawer-direction=left]:rounded-r-xl data-[vaul-drawer-direction=left]:border-r data-[vaul-drawer-direction=right]:inset-y-0 data-[vaul-drawer-direction=right]:right-0 data-[vaul-drawer-direction=right]:w-3/4 data-[vaul-drawer-direction=right]:rounded-l-xl data-[vaul-drawer-direction=right]:border-l data-[vaul-drawer-direction=top]:inset-x-0 data-[vaul-drawer-direction=top]:top-0 data-[vaul-drawer-direction=top]:mb-24 data-[vaul-drawer-direction=top]:max-h-[80vh] data-[vaul-drawer-direction=top]:rounded-b-xl data-[vaul-drawer-direction=top]:border-b data-[vaul-drawer-direction=left]:sm:max-w-sm data-[vaul-drawer-direction=right]:sm:max-w-sm", className)}
                ...{props}
            >
                <div class="mx-auto mt-4 hidden h-1 w-[100px] shrink-0 rounded-full bg-muted group-data-[vaul-drawer-direction=bottom]/drawer-content:block" />
                {children}
            </{DrawerPrimitive.Content}>
        </{DrawerPortal}>
    """


def DrawerHeader(className=None, **props):
    return t"""
        <div
            data-slot="drawer-header"
            class={cn("flex flex-col gap-0.5 p-4 group-data-[vaul-drawer-direction=bottom]/drawer-content:text-center group-data-[vaul-drawer-direction=top]/drawer-content:text-center md:gap-0.5 md:text-left", className)}
            ...{props}
        />
    """


def DrawerFooter(className=None, **props):
    return t'<div data-slot="drawer-footer" class={cn("mt-auto flex flex-col gap-2 p-4", className)} ...{props} />'


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
            class={cn("text-sm text-muted-foreground", className)}
            ...{props}
        />
    """
