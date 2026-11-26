from utils import cn

__js__ = {
    "@base-ui/react/context-menu": ["ContextMenu as ContextMenuPrimitive"],
    "lucide-react": ["ChevronRightIcon", "CheckIcon"],
}


def ContextMenu(**props):
    return t'<{ContextMenuPrimitive.Root} data-slot="context-menu" ...{props} />'


def ContextMenuPortal(**props):
    return t'<{ContextMenuPrimitive.Portal} data-slot="context-menu-portal" ...{props} />'


def ContextMenuTrigger(className=None, **props):
    return t"""
        <{ContextMenuPrimitive.Trigger}
            data-slot="context-menu-trigger"
            class={cn("select-none", className)}
            ...{props}
        />
    """


def ContextMenuContent(className=None, align="start", alignOffset=4, side="right", sideOffset=0, **props):
    return t"""
        <{ContextMenuPrimitive.Portal}>
            <{ContextMenuPrimitive.Positioner}
                class="isolate z-50 outline-none"
                align={align}
                alignOffset={alignOffset}
                side={side}
                sideOffset={sideOffset}
            >
                <{ContextMenuPrimitive.Popup}
                    data-slot="context-menu-content"
                    class={cn("z-50 max-h-(--available-height) min-w-36 origin-(--transform-origin) overflow-x-hidden overflow-y-auto rounded-md bg-popover p-1 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 outline-none data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                    ...{props}
                />
            </{ContextMenuPrimitive.Positioner}>
        </{ContextMenuPrimitive.Portal}>
    """


def ContextMenuGroup(**props):
    return t'<{ContextMenuPrimitive.Group} data-slot="context-menu-group" ...{props} />'


def ContextMenuLabel(className=None, inset=None, **props):
    return t"""
        <{ContextMenuPrimitive.GroupLabel}
            data-slot="context-menu-label"
            data-inset={inset}
            class={cn("px-2 py-1.5 text-xs font-medium text-muted-foreground data-inset:pl-8", className)}
            ...{props}
        />
    """


def ContextMenuItem(className=None, inset=None, variant="default", **props):
    return t"""
        <{ContextMenuPrimitive.Item}
            data-slot="context-menu-item"
            data-inset={inset}
            data-variant={variant}
            class={cn("group/context-menu-item relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 focus:*:[svg]:text-accent-foreground data-[variant=destructive]:*:[svg]:text-destructive", className)}
            ...{props}
        />
    """


def ContextMenuSub(**props):
    return t'<{ContextMenuPrimitive.SubmenuRoot} data-slot="context-menu-sub" ...{props} />'


def ContextMenuSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{ContextMenuPrimitive.SubmenuTrigger}
            data-slot="context-menu-sub-trigger"
            data-inset={inset}
            class={cn("flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{ChevronRightIcon} class="ml-auto" />
        </{ContextMenuPrimitive.SubmenuTrigger}>
    """


def ContextMenuSubContent(**props):
    return t'<{ContextMenuContent} data-slot="context-menu-sub-content" class="shadow-lg" side="right" ...{props} />'


def ContextMenuCheckboxItem(className=None, children=None, checked=None, inset=None, **props):
    return t"""
        <{ContextMenuPrimitive.CheckboxItem}
            data-slot="context-menu-checkbox-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            checked={checked}
            ...{props}
        >
            <span class="pointer-events-none absolute right-2">
                <{ContextMenuPrimitive.CheckboxItemIndicator}>
                    <{CheckIcon} />
                </{ContextMenuPrimitive.CheckboxItemIndicator}>
            </span>
            {children}
        </{ContextMenuPrimitive.CheckboxItem}>
    """


def ContextMenuRadioGroup(**props):
    return t'<{ContextMenuPrimitive.RadioGroup} data-slot="context-menu-radio-group" ...{props} />'


def ContextMenuRadioItem(className=None, children=None, inset=None, **props):
    return t"""
        <{ContextMenuPrimitive.RadioItem}
            data-slot="context-menu-radio-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <span class="pointer-events-none absolute right-2">
                <{ContextMenuPrimitive.RadioItemIndicator}>
                    <{CheckIcon} />
                </{ContextMenuPrimitive.RadioItemIndicator}>
            </span>
            {children}
        </{ContextMenuPrimitive.RadioItem}>
    """


def ContextMenuSeparator(className=None, **props):
    return t"""
        <{ContextMenuPrimitive.Separator}
            data-slot="context-menu-separator"
            class={cn("-mx-1 my-1 h-px bg-border", className)}
            ...{props}
        />
    """


def ContextMenuShortcut(className=None, **props):
    return t"""
        <span
            data-slot="context-menu-shortcut"
            class={cn("ml-auto text-xs tracking-widest text-muted-foreground group-focus/context-menu-item:text-accent-foreground", className)}
            ...{props}
        />
    """
