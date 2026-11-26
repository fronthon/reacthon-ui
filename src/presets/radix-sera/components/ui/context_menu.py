from utils import cn

__js__ = {"radix-ui": ["ContextMenu as ContextMenuPrimitive"], "lucide-react": ["ChevronRightIcon", "CheckIcon"]}


def ContextMenu(**props):
    return t'<{ContextMenuPrimitive.Root} data-slot="context-menu" ...{props} />'


def ContextMenuTrigger(className=None, **props):
    return t"""
        <{ContextMenuPrimitive.Trigger}
            data-slot="context-menu-trigger"
            class={cn("select-none", className)}
            ...{props}
        />
    """


def ContextMenuGroup(**props):
    return t'<{ContextMenuPrimitive.Group} data-slot="context-menu-group" ...{props} />'


def ContextMenuPortal(**props):
    return t'<{ContextMenuPrimitive.Portal} data-slot="context-menu-portal" ...{props} />'


def ContextMenuSub(**props):
    return t'<{ContextMenuPrimitive.Sub} data-slot="context-menu-sub" ...{props} />'


def ContextMenuRadioGroup(**props):
    return t'<{ContextMenuPrimitive.RadioGroup} data-slot="context-menu-radio-group" ...{props} />'


def ContextMenuContent(className=None, **props):
    return t"""
        <{ContextMenuPrimitive.Portal}>
            <{ContextMenuPrimitive.Content}
                data-slot="context-menu-content"
                class={cn("z-50 max-h-(--radix-context-menu-content-available-height) min-w-48 origin-(--radix-context-menu-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-none bg-popover p-1.5 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                ...{props}
            />
        </{ContextMenuPrimitive.Portal}>
    """


def ContextMenuItem(className=None, inset=None, variant="default", **props):
    return t"""
        <{ContextMenuPrimitive.Item}
            data-slot="context-menu-item"
            data-inset={inset}
            data-variant={variant}
            class={cn("group/context-menu-item relative flex cursor-default items-center gap-2.5 rounded-none px-3 py-2 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-9.5 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5 focus:*:[svg]:text-accent-foreground data-[variant=destructive]:*:[svg]:text-destructive", className)}
            ...{props}
        />
    """


def ContextMenuSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{ContextMenuPrimitive.SubTrigger}
            data-slot="context-menu-sub-trigger"
            data-inset={inset}
            class={cn("flex cursor-default items-center rounded-none px-3 py-2 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-9.5 data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            {children}
            <{ChevronRightIcon} class="ml-auto" />
        </{ContextMenuPrimitive.SubTrigger}>
    """


def ContextMenuSubContent(className=None, **props):
    return t"""
        <{ContextMenuPrimitive.SubContent}
            data-slot="context-menu-sub-content"
            class={cn("z-50 min-w-32 origin-(--radix-context-menu-content-transform-origin) overflow-hidden rounded-none bg-popover p-1.5 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
            ...{props}
        />
    """


def ContextMenuCheckboxItem(className=None, children=None, checked=None, inset=None, **props):
    return t"""
        <{ContextMenuPrimitive.CheckboxItem}
            data-slot="context-menu-checkbox-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2.5 rounded-none py-2 pr-8 pl-3 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-9.5 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            checked={checked}
            ...{props}
        >
            <span class="pointer-events-none absolute right-2">
                <{ContextMenuPrimitive.ItemIndicator}>
                    <{CheckIcon} />
                </{ContextMenuPrimitive.ItemIndicator}>
            </span>
            {children}
        </{ContextMenuPrimitive.CheckboxItem}>
    """


def ContextMenuRadioItem(className=None, children=None, inset=None, **props):
    return t"""
        <{ContextMenuPrimitive.RadioItem}
            data-slot="context-menu-radio-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2.5 rounded-none py-2 pr-8 pl-3 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-9.5 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            <span class="pointer-events-none absolute right-2">
                <{ContextMenuPrimitive.ItemIndicator}>
                    <{CheckIcon} />
                </{ContextMenuPrimitive.ItemIndicator}>
            </span>
            {children}
        </{ContextMenuPrimitive.RadioItem}>
    """


def ContextMenuLabel(className=None, inset=None, **props):
    return t"""
        <{ContextMenuPrimitive.Label}
            data-slot="context-menu-label"
            data-inset={inset}
            class={cn("px-3 py-2 text-xs font-semibold tracking-wider text-muted-foreground uppercase data-inset:pl-9.5", className)}
            ...{props}
        />
    """


def ContextMenuSeparator(className=None, **props):
    return t"""
        <{ContextMenuPrimitive.Separator}
            data-slot="context-menu-separator"
            class={cn("-mx-1.5 my-1.5 h-px bg-border/50", className)}
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
