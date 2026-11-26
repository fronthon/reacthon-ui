from utils import cn, cva

__js__ = {"radix-ui": ["NavigationMenu as NavigationMenuPrimitive"], "lucide-react": ["ChevronDownIcon"]}


def NavigationMenu(className=None, children=None, viewport=True, **props):
    return t"""
        <{NavigationMenuPrimitive.Root}
            data-slot="navigation-menu"
            data-viewport={viewport}
            class={cn("group/navigation-menu relative flex max-w-max flex-1 items-center justify-center", className)}
            ...{props}
        >
            {children}
            {viewport and t'<{NavigationMenuViewport} />'}
        </{NavigationMenuPrimitive.Root}>
    """


def NavigationMenuList(className=None, **props):
    return t"""
        <{NavigationMenuPrimitive.List}
            data-slot="navigation-menu-list"
            class={cn("group flex flex-1 list-none items-center justify-center gap-0", className)}
            ...{props}
        />
    """


def NavigationMenuItem(className=None, **props):
    return t"""
        <{NavigationMenuPrimitive.Item}
            data-slot="navigation-menu-item"
            class={cn("relative", className)}
            ...{props}
        />
    """


navigation_menu_trigger_style = cva(
    "group/navigation-menu-trigger inline-flex h-9 w-max items-center justify-center rounded-2xl px-4.5 py-2.5 text-sm font-medium transition-all outline-none hover:bg-muted focus:bg-muted focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 disabled:pointer-events-none disabled:opacity-50 data-popup-open:bg-muted/50 data-popup-open:hover:bg-muted data-open:bg-muted/50 data-open:hover:bg-muted data-open:focus:bg-muted",
)


def NavigationMenuTrigger(className=None, children=None, **props):
    return t"""
        <{NavigationMenuPrimitive.Trigger}
            data-slot="navigation-menu-trigger"
            class={cn(navigation_menu_trigger_style(), "group", className)}
            ...{props}
        >
            {children}
            {" "}
            <{ChevronDownIcon}
                class="relative top-px ml-1 size-3 transition duration-300 group-data-popup-open/navigation-menu-trigger:rotate-180 group-data-open/navigation-menu-trigger:rotate-180"
                aria-hidden="true"
            />
        </{NavigationMenuPrimitive.Trigger}>
    """


def NavigationMenuContent(className=None, **props):
    return t"""
        <{NavigationMenuPrimitive.Content}
            data-slot="navigation-menu-content"
            class={cn("top-0 left-0 isolate z-50 w-full p-2.5 pr-3 ease-[cubic-bezier(0.22,1,0.36,1)] group-data-[viewport=false]/navigation-menu:top-full group-data-[viewport=false]/navigation-menu:mt-1.5 group-data-[viewport=false]/navigation-menu:overflow-hidden group-data-[viewport=false]/navigation-menu:rounded-2xl group-data-[viewport=false]/navigation-menu:bg-popover group-data-[viewport=false]/navigation-menu:text-popover-foreground group-data-[viewport=false]/navigation-menu:shadow-2xl group-data-[viewport=false]/navigation-menu:ring-1 group-data-[viewport=false]/navigation-menu:ring-foreground/5 group-data-[viewport=false]/navigation-menu:duration-300 data-[motion=from-end]:slide-in-from-right-52 data-[motion=from-start]:slide-in-from-left-52 data-[motion=to-end]:slide-out-to-right-52 data-[motion=to-start]:slide-out-to-left-52 data-[motion^=from-]:animate-in data-[motion^=from-]:fade-in data-[motion^=to-]:animate-out data-[motion^=to-]:fade-out **:data-[slot=navigation-menu-link]:focus:ring-0 **:data-[slot=navigation-menu-link]:focus:outline-none md:absolute md:w-auto group-data-[viewport=false]/navigation-menu:data-open:animate-in group-data-[viewport=false]/navigation-menu:data-open:fade-in-0 group-data-[viewport=false]/navigation-menu:data-open:zoom-in-95 group-data-[viewport=false]/navigation-menu:data-closed:animate-out group-data-[viewport=false]/navigation-menu:data-closed:fade-out-0 group-data-[viewport=false]/navigation-menu:data-closed:zoom-out-95", className)}
            ...{props}
        />
    """


def NavigationMenuViewport(className=None, **props):
    return t"""
        <div class={cn("absolute top-full left-0 isolate z-50 flex justify-center")}>
            <{NavigationMenuPrimitive.Viewport}
                data-slot="navigation-menu-viewport"
                class={cn("origin-top-center relative mt-1.5 h-(--radix-navigation-menu-viewport-height) w-full overflow-hidden rounded-2xl bg-popover text-popover-foreground shadow-2xl ring-1 ring-foreground/5 duration-100 md:w-(--radix-navigation-menu-viewport-width) data-open:animate-in data-open:zoom-in-90 data-closed:animate-out data-closed:zoom-out-90", className)}
                ...{props}
            />
        </div>
    """


def NavigationMenuLink(className=None, **props):
    return t"""
        <{NavigationMenuPrimitive.Link}
            data-slot="navigation-menu-link"
            class={cn("flex items-center gap-1.5 rounded-2xl p-3 text-sm transition-all outline-none hover:bg-muted focus:bg-muted focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 in-data-[slot=navigation-menu-content]:rounded-xl data-[active=true]:bg-muted/50 data-[active=true]:hover:bg-muted data-[active=true]:focus:bg-muted [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        />
    """


def NavigationMenuIndicator(className=None, **props):
    return t"""
        <{NavigationMenuPrimitive.Indicator}
            data-slot="navigation-menu-indicator"
            class={cn("top-full z-1 flex h-1.5 items-end justify-center overflow-hidden data-[state=hidden]:animate-out data-[state=hidden]:fade-out data-[state=visible]:animate-in data-[state=visible]:fade-in", className)}
            ...{props}
        >
            <div class="relative top-[60%] h-2 w-2 rotate-45 rounded-tl-sm bg-border shadow-md" />
        </{NavigationMenuPrimitive.Indicator}>
    """
