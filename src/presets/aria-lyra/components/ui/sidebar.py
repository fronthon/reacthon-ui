from browser import document, window
from javascript import Math, NULL
from reacthon import create_context, use_callback, use_context, use_effect, use_memo, use_state
from utils import cn, cva
from button import Button
from input import Input
from separator import Separator
from sheet import Sheet, SheetDescription, SheetHeader, SheetTitle
from skeleton import Skeleton
from tooltip import Tooltip, TooltipTrigger

__js__ = {
    "react-aria-components": ["Button as ButtonPrimitive", "Link as LinkPrimitive"],
    "@/hooks/use-mobile": ["useIsMobile"],
    "lucide-react": ["PanelLeftIcon"],
}

SIDEBAR_COOKIE_NAME = "sidebar_state"

SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7

SIDEBAR_WIDTH = "16rem"

SIDEBAR_WIDTH_MOBILE = "18rem"

SIDEBAR_WIDTH_ICON = "3rem"

SIDEBAR_KEYBOARD_SHORTCUT = "b"

SidebarContext = create_context(NULL)


def use_sidebar():
    context = use_context(SidebarContext)
    if not context:
        raise RuntimeError("useSidebar must be used within a SidebarProvider.")

    return context


def SidebarProvider(defaultOpen=True, open=None, onOpenChange=None, className=None, style=None, children=None, **props):
    open_prop = open
    set_open_prop = onOpenChange

    is_mobile = useIsMobile()
    open_mobile, set_open_mobile = use_state(False)

    # This is the internal state of the sidebar.
    # We use openProp and setOpenProp for control from outside the component.
    _open, _set_open = use_state(defaultOpen)
    open_ = open_prop if open_prop not in (None, NULL) else _open

    def set_open(value):
        open_state = value(open_) if callable(value) else value
        if set_open_prop:
            set_open_prop(open_state)
        else:
            _set_open(open_state)

        # This sets the cookie to keep the sidebar state.
        document.cookie = f"{SIDEBAR_COOKIE_NAME}={str(open_state).lower()}; path=/; max-age={SIDEBAR_COOKIE_MAX_AGE}"

    set_open = use_callback(set_open, [set_open_prop, open_])

    # Helper to toggle the sidebar.
    toggle_sidebar = use_callback(
        lambda: set_open_mobile(lambda open_: not open_) if is_mobile else set_open(lambda open_: not open_),
        [is_mobile, set_open, set_open_mobile],
    )

    # Adds a keyboard shortcut to toggle the sidebar.
    def effect():
        def handle_key_down(event):
            if event.key == SIDEBAR_KEYBOARD_SHORTCUT and (event.metaKey or event.ctrlKey):
                event.preventDefault()
                toggle_sidebar()

        window.addEventListener("keydown", handle_key_down)
        return lambda: window.removeEventListener("keydown", handle_key_down)

    use_effect(effect, [toggle_sidebar])

    # We add a state so that we can do data-state="expanded" or "collapsed".
    # This makes it easier to style the sidebar with Tailwind classes.
    state = "expanded" if open_ else "collapsed"

    context_value = use_memo(
        lambda: {
            "state": state,
            "open": open_,
            "setOpen": set_open,
            "isMobile": is_mobile,
            "openMobile": open_mobile,
            "setOpenMobile": set_open_mobile,
            "toggleSidebar": toggle_sidebar,
        },
        [state, open_, set_open, is_mobile, open_mobile, set_open_mobile, toggle_sidebar],
    )

    return t"""
        <{SidebarContext.Provider} value={context_value}>
            <div
                data-slot="sidebar-wrapper"
                style={ {
                    "--sidebar-width": SIDEBAR_WIDTH,
                    "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
                    **(style or {}),
                } }
                class={cn("group/sidebar-wrapper flex min-h-svh w-full has-data-[variant=inset]:bg-sidebar", className)}
                ...{props}
            >
                {children}
            </div>
        </{SidebarContext.Provider}>
    """


def Sidebar(side="left", variant="sidebar", collapsible="offcanvas", className=None, children=None, dir=None, **props):
    sidebar = use_sidebar()
    is_mobile, state, open_mobile, set_open_mobile = sidebar.get("isMobile"), sidebar.get("state"), sidebar.get("openMobile"), sidebar.get("setOpenMobile")

    if collapsible == "none":
        return t"""
            <div
                data-slot="sidebar"
                class={cn("flex h-full w-(--sidebar-width) flex-col bg-sidebar text-sidebar-foreground", className)}
                ...{props}
            >
                {children}
            </div>
        """

    if is_mobile:
        return t"""
            <{Sheet}
                isOpen={open_mobile}
                onOpenChange={set_open_mobile}
                dir={dir}
                data-sidebar="sidebar"
                data-slot="sidebar"
                data-mobile="true"
                class="w-(--sidebar-width) bg-sidebar p-0 text-sidebar-foreground [&>button]:hidden"
                style={ {
                    "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
                } }
                side={side}
                ...{props}
            >
                <{SheetHeader} class="sr-only">
                    <{SheetTitle}>Sidebar</{SheetTitle}>
                    <{SheetDescription}>Displays the mobile sidebar.</{SheetDescription}>
                </{SheetHeader}>
                <div class="flex h-full w-full flex-col">{children}</div>
            </{Sheet}>
        """

    return t"""
        <div
            class="group peer hidden text-sidebar-foreground md:block"
            data-state={state}
            data-collapsible={collapsible if state == "collapsed" else ""}
            data-variant={variant}
            data-side={side}
            data-slot="sidebar"
        >
            <div
                data-slot="sidebar-gap"
                class={cn(
                    "relative w-(--sidebar-width) bg-transparent transition-[width] duration-200 ease-linear",
                    "group-data-[collapsible=offcanvas]:w-0",
                    "group-data-[side=right]:rotate-180",
                    "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+(--spacing(4)))]" if variant == "floating" or variant == "inset" else "group-data-[collapsible=icon]:w-(--sidebar-width-icon)",
                )}
            />
            <div
                data-slot="sidebar-container"
                data-side={side}
                class={cn(
                    "fixed inset-y-0 z-10 hidden h-svh w-(--sidebar-width) transition-[left,right,width] duration-200 ease-linear data-[side=left]:left-0 data-[side=left]:group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)] data-[side=right]:right-0 data-[side=right]:group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)] md:flex",
                    "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)+(--spacing(4))+2px)]" if variant == "floating" or variant == "inset" else "group-data-[collapsible=icon]:w-(--sidebar-width-icon) group-data-[side=left]:border-r group-data-[side=right]:border-l",
                    className,
                )}
                ...{props}
            >
                <div
                    data-sidebar="sidebar"
                    data-slot="sidebar-inner"
                    class="flex size-full flex-col bg-sidebar group-data-[variant=floating]:rounded-none group-data-[variant=floating]:shadow-sm group-data-[variant=floating]:ring-1 group-data-[variant=floating]:ring-sidebar-border"
                >
                    {children}
                </div>
            </div>
        </div>
    """


def SidebarTrigger(className=None, onPress=None, **props):
    toggle_sidebar = use_sidebar().get("toggleSidebar")

    def on_press(event):
        if onPress:
            onPress(event)
        toggle_sidebar()

    return t"""
        <{Button}
            data-sidebar="trigger"
            data-slot="sidebar-trigger"
            variant="ghost"
            size="icon-sm"
            class={cn(className)}
            onPress={on_press}
            ...{props}
        >
            <{PanelLeftIcon} />
            <span class="sr-only">Toggle Sidebar</span>
        </{Button}>
    """


def SidebarRail(className=None, **props):
    toggle_sidebar = use_sidebar().get("toggleSidebar")

    return t"""
        <button
            data-sidebar="rail"
            data-slot="sidebar-rail"
            aria-label="Toggle Sidebar"
            tabIndex={-1}
            onClick={toggle_sidebar}
            title="Toggle Sidebar"
            class={cn(
                "absolute inset-y-0 z-20 hidden w-4 transition-all ease-linear group-data-[side=left]:-right-4 group-data-[side=right]:left-0 after:absolute after:inset-y-0 after:start-1/2 after:w-[2px] hover:after:bg-sidebar-border sm:flex ltr:-translate-x-1/2 rtl:-translate-x-1/2",
                "in-data-[side=left]:cursor-w-resize in-data-[side=right]:cursor-e-resize",
                "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
                "group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full hover:group-data-[collapsible=offcanvas]:bg-sidebar",
                "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
                "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
                className,
            )}
            ...{props}
        />
    """


def SidebarInset(className=None, **props):
    return t"""
        <main
            data-slot="sidebar-inset"
            class={cn("relative flex w-full flex-1 flex-col bg-background md:peer-data-[variant=inset]:m-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-none md:peer-data-[variant=inset]:shadow-sm md:peer-data-[variant=inset]:peer-data-[state=collapsed]:ml-2", className)}
            ...{props}
        />
    """


def SidebarInput(className=None, **props):
    return t"""
        <{Input}
            data-slot="sidebar-input"
            data-sidebar="input"
            class={cn("h-8 w-full bg-background shadow-none", className)}
            ...{props}
        />
    """


def SidebarHeader(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-header"
            data-sidebar="header"
            class={cn("flex flex-col gap-2 p-2", className)}
            ...{props}
        />
    """


def SidebarFooter(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-footer"
            data-sidebar="footer"
            class={cn("flex flex-col gap-2 p-2", className)}
            ...{props}
        />
    """


def SidebarSeparator(className=None, **props):
    return t"""
        <{Separator}
            data-slot="sidebar-separator"
            data-sidebar="separator"
            class={cn("mx-2 w-auto bg-sidebar-border", className)}
            ...{props}
        />
    """


def SidebarContent(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-content"
            data-sidebar="content"
            class={cn("no-scrollbar flex min-h-0 flex-1 flex-col gap-0 overflow-auto group-data-[collapsible=icon]:overflow-hidden", className)}
            ...{props}
        />
    """


def SidebarGroup(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-group"
            data-sidebar="group"
            class={cn("relative flex w-full min-w-0 flex-col p-2", className)}
            ...{props}
        />
    """


def SidebarGroupLabel(className=None, elementType="div", **props):
    Element = elementType

    return t"""
        <{Element}
            data-slot="sidebar-group-label"
            data-sidebar="group-label"
            class={cn("flex h-8 shrink-0 items-center rounded-none px-2 text-xs text-sidebar-foreground/70 ring-sidebar-ring outline-hidden transition-[margin,opacity] duration-200 ease-linear group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0 focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0", className)}
            ...{props}
        />
    """


def SidebarGroupAction(className=None, **props):
    return t"""
        <button
            data-slot="sidebar-group-action"
            data-sidebar="group-action"
            class={cn("absolute top-3.5 right-3 flex aspect-square w-5 items-center justify-center rounded-none p-0 text-sidebar-foreground ring-sidebar-ring outline-hidden transition-transform group-data-[collapsible=icon]:hidden after:absolute after:-inset-2 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 md:after:hidden [&>svg]:size-4 [&>svg]:shrink-0", className)}
            ...{props}
        />
    """


def SidebarGroupContent(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-group-content"
            data-sidebar="group-content"
            class={cn("w-full text-xs", className)}
            ...{props}
        />
    """


def SidebarMenu(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-menu"
            data-sidebar="menu"
            class={cn("flex w-full min-w-0 flex-col gap-0", className)}
            ...{props}
        />
    """


def SidebarMenuItem(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-menu-item"
            data-sidebar="menu-item"
            class={cn("group/menu-item relative", className)}
            ...{props}
        />
    """


sidebar_menu_button_variants = cva(
    "peer/menu-button group/menu-button flex w-full items-center gap-2 overflow-hidden rounded-none p-2 text-left text-xs ring-sidebar-ring outline-hidden transition-[width,height,padding] group-has-data-[sidebar=menu-action]/menu-item:pr-8 group-data-[collapsible=icon]:size-8! group-data-[collapsible=icon]:p-2! hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 aria-expanded:hover:bg-sidebar-accent aria-expanded:hover:text-sidebar-accent-foreground data-open:hover:bg-sidebar-accent data-open:hover:text-sidebar-accent-foreground data-active:bg-sidebar-accent data-active:font-medium data-active:text-sidebar-accent-foreground [&_svg]:size-4 [&_svg]:shrink-0 [&>span:last-child]:truncate",
    {
        "variant": {
            "default": "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
            "outline": "bg-background shadow-[0_0_0_1px_var(--sidebar-border)] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_var(--sidebar-accent)]",
        },
        "size": {
            "default": "h-8 text-xs",
            "sm": "h-7 text-xs",
            "lg": "h-12 text-xs group-data-[collapsible=icon]:p-0!",
        },
    },
    {"variant": "default", "size": "default"},
)


def SidebarMenuButton(isActive=False, variant="default", size="default", tooltip=None, className=None, **props):
    sidebar = use_sidebar()
    is_mobile, state = sidebar.get("isMobile"), sidebar.get("state")
    link_primitive = t"""
        <{LinkPrimitive}
            data-slot="sidebar-menu-button"
            data-sidebar="menu-button"
            data-size={size}
            data-active={isActive}
            class={cn(sidebar_menu_button_variants(variant=variant, size=size), className)}
            ...{props}
        />
    """

    button_primitive = t"""
        <{ButtonPrimitive}
            data-slot="sidebar-menu-button"
            data-sidebar="menu-button"
            data-size={size}
            data-active={isActive}
            class={cn(sidebar_menu_button_variants(variant=variant, size=size), className)}
            ...{props}
        />
    """

    comp = link_primitive if props.get("href") is not None else button_primitive

    if not tooltip:
        return comp

    if isinstance(tooltip, str):
        tooltip = {"children": tooltip}

    return t"""
        <{TooltipTrigger} isDisabled={state != "collapsed" or is_mobile}>
            {comp}
            <{Tooltip} placement="right" ...{tooltip} />
        </{TooltipTrigger}>
    """


def SidebarMenuAction(className=None, showOnHover=False, **props):
    return t"""
        <{ButtonPrimitive}
            data-slot="sidebar-menu-action"
            data-sidebar="menu-action"
            class={cn(
                "absolute top-1.5 right-1 flex aspect-square w-5 items-center justify-center rounded-none p-0 text-sidebar-foreground ring-sidebar-ring outline-hidden transition-transform group-data-[collapsible=icon]:hidden peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[size=default]/menu-button:top-1.5 peer-data-[size=lg]/menu-button:top-2.5 peer-data-[size=sm]/menu-button:top-1 after:absolute after:-inset-2 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 md:after:hidden [&>svg]:size-4 [&>svg]:shrink-0",
                showOnHover and "group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 peer-data-active/menu-button:text-sidebar-accent-foreground aria-expanded:opacity-100 md:opacity-0",
                className,
            )}
            ...{props}
        />
    """


def SidebarMenuBadge(className=None, **props):
    return t"""
        <div
            data-slot="sidebar-menu-badge"
            data-sidebar="menu-badge"
            class={cn("pointer-events-none absolute right-1 flex h-5 min-w-5 items-center justify-center rounded-none px-1 text-xs font-medium text-sidebar-foreground tabular-nums select-none group-data-[collapsible=icon]:hidden peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[size=default]/menu-button:top-1.5 peer-data-[size=lg]/menu-button:top-2.5 peer-data-[size=sm]/menu-button:top-1 peer-data-active/menu-button:text-sidebar-accent-foreground", className)}
            ...{props}
        />
    """


def SidebarMenuSkeleton(className=None, showIcon=False, **props):
    # Random width between 50 to 90%.
    width = use_state(lambda: f"{Math.floor(Math.random() * 40) + 50}%")[0]

    return t"""
        <div
            data-slot="sidebar-menu-skeleton"
            data-sidebar="menu-skeleton"
            class={cn("flex h-8 items-center gap-2 rounded-none px-2", className)}
            ...{props}
        >
            {showIcon and t'<{Skeleton} class="size-4 rounded-none" data-sidebar="menu-skeleton-icon" />'}
            <{Skeleton}
                class="h-4 max-w-(--skeleton-width) flex-1"
                data-sidebar="menu-skeleton-text"
                style={ {
                    "--skeleton-width": width,
                } }
            />
        </div>
    """


def SidebarMenuSub(className=None, **props):
    return t"""
        <ul
            data-slot="sidebar-menu-sub"
            data-sidebar="menu-sub"
            class={cn("mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-l border-sidebar-border px-2.5 py-0.5 group-data-[collapsible=icon]:hidden", className)}
            ...{props}
        />
    """


def SidebarMenuSubItem(className=None, **props):
    return t"""
        <li
            data-slot="sidebar-menu-sub-item"
            data-sidebar="menu-sub-item"
            class={cn("group/menu-sub-item relative", className)}
            ...{props}
        />
    """


def SidebarMenuSubButton(size="md", isActive=False, className=None, **props):
    link_primitive = t"""
        <{LinkPrimitive}
            data-slot="sidebar-menu-sub-button"
            data-sidebar="menu-sub-button"
            data-size={size}
            data-active={isActive}
            class={cn("flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-none px-2 text-sidebar-foreground ring-sidebar-ring outline-hidden group-data-[collapsible=icon]:hidden hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[size=md]:text-xs data-[size=sm]:text-xs data-active:bg-sidebar-accent data-active:text-sidebar-accent-foreground [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0 [&>svg]:text-sidebar-accent-foreground", className)}
            ...{props}
        />
    """

    button_primitive = t"""
        <{ButtonPrimitive}
            data-slot="sidebar-menu-sub-button"
            data-sidebar="menu-sub-button"
            data-size={size}
            data-active={isActive}
            class={cn("flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-none px-2 text-sidebar-foreground ring-sidebar-ring outline-hidden group-data-[collapsible=icon]:hidden hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[size=md]:text-xs data-[size=sm]:text-xs data-active:bg-sidebar-accent data-active:text-sidebar-accent-foreground [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0 [&>svg]:text-sidebar-accent-foreground", className)}
            ...{props}
        />
    """

    return link_primitive if props.get("href") is not None else button_primitive
