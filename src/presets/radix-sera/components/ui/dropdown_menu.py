from utils import cn

__js__ = {"radix-ui": ["DropdownMenu as DropdownMenuPrimitive"], "lucide-react": ["CheckIcon", "ChevronRightIcon"]}


def DropdownMenu(**props):
    return t'<{DropdownMenuPrimitive.Root} data-slot="dropdown-menu" ...{props} />'


def DropdownMenuPortal(**props):
    return t'<{DropdownMenuPrimitive.Portal} data-slot="dropdown-menu-portal" ...{props} />'


def DropdownMenuTrigger(**props):
    return t'<{DropdownMenuPrimitive.Trigger} data-slot="dropdown-menu-trigger" ...{props} />'


def DropdownMenuContent(className=None, align="start", sideOffset=4, **props):
    return t"""
        <{DropdownMenuPrimitive.Portal}>
            <{DropdownMenuPrimitive.Content}
                data-slot="dropdown-menu-content"
                sideOffset={sideOffset}
                align={align}
                class={cn("z-50 max-h-(--radix-dropdown-menu-content-available-height) w-(--radix-dropdown-menu-trigger-width) min-w-48 origin-(--radix-dropdown-menu-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-none bg-popover p-1.5 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-[state=closed]:overflow-hidden data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                ...{props}
            />
        </{DropdownMenuPrimitive.Portal}>
    """


def DropdownMenuGroup(**props):
    return t'<{DropdownMenuPrimitive.Group} data-slot="dropdown-menu-group" ...{props} />'


def DropdownMenuItem(className=None, inset=None, variant="default", **props):
    return t"""
        <{DropdownMenuPrimitive.Item}
            data-slot="dropdown-menu-item"
            data-inset={inset}
            data-variant={variant}
            class={cn("group/dropdown-menu-item relative flex cursor-default items-center gap-2.5 rounded-none px-3 py-2 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-9.5 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5 data-[variant=destructive]:*:[svg]:text-destructive", className)}
            ...{props}
        />
    """


def DropdownMenuCheckboxItem(className=None, children=None, checked=None, inset=None, **props):
    return t"""
        <{DropdownMenuPrimitive.CheckboxItem}
            data-slot="dropdown-menu-checkbox-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2.5 rounded-none py-2 pr-8 pl-3 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-9.5 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            checked={checked}
            ...{props}
        >
            <span
                class="pointer-events-none absolute right-2 flex items-center justify-center"
                data-slot="dropdown-menu-checkbox-item-indicator"
            >
                <{DropdownMenuPrimitive.ItemIndicator}>
                    <{CheckIcon} />
                </{DropdownMenuPrimitive.ItemIndicator}>
            </span>
            {children}
        </{DropdownMenuPrimitive.CheckboxItem}>
    """


def DropdownMenuRadioGroup(**props):
    return t'<{DropdownMenuPrimitive.RadioGroup} data-slot="dropdown-menu-radio-group" ...{props} />'


def DropdownMenuRadioItem(className=None, children=None, inset=None, **props):
    return t"""
        <{DropdownMenuPrimitive.RadioItem}
            data-slot="dropdown-menu-radio-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2.5 rounded-none py-2 pr-8 pl-3 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-9.5 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            <span
                class="pointer-events-none absolute right-2 flex items-center justify-center"
                data-slot="dropdown-menu-radio-item-indicator"
            >
                <{DropdownMenuPrimitive.ItemIndicator}>
                    <{CheckIcon} />
                </{DropdownMenuPrimitive.ItemIndicator}>
            </span>
            {children}
        </{DropdownMenuPrimitive.RadioItem}>
    """


def DropdownMenuLabel(className=None, inset=None, **props):
    return t"""
        <{DropdownMenuPrimitive.Label}
            data-slot="dropdown-menu-label"
            data-inset={inset}
            class={cn("px-3 py-2 text-xs font-semibold tracking-wider text-muted-foreground uppercase data-inset:pl-9.5", className)}
            ...{props}
        />
    """


def DropdownMenuSeparator(className=None, **props):
    return t"""
        <{DropdownMenuPrimitive.Separator}
            data-slot="dropdown-menu-separator"
            class={cn("-mx-1.5 my-1.5 h-px bg-border/50", className)}
            ...{props}
        />
    """


def DropdownMenuShortcut(className=None, **props):
    return t"""
        <span
            data-slot="dropdown-menu-shortcut"
            class={cn("ml-auto text-xs tracking-widest text-muted-foreground group-focus/dropdown-menu-item:text-accent-foreground", className)}
            ...{props}
        />
    """


def DropdownMenuSub(**props):
    return t'<{DropdownMenuPrimitive.Sub} data-slot="dropdown-menu-sub" ...{props} />'


def DropdownMenuSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{DropdownMenuPrimitive.SubTrigger}
            data-slot="dropdown-menu-sub-trigger"
            data-inset={inset}
            class={cn("flex cursor-default items-center gap-2 rounded-none px-3 py-2 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-9.5 data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            {children}
            <{ChevronRightIcon} class="ml-auto" />
        </{DropdownMenuPrimitive.SubTrigger}>
    """


def DropdownMenuSubContent(className=None, **props):
    return t"""
        <{DropdownMenuPrimitive.SubContent}
            data-slot="dropdown-menu-sub-content"
            class={cn("z-50 min-w-36 origin-(--radix-dropdown-menu-content-transform-origin) overflow-hidden rounded-none bg-popover p-1.5 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
            ...{props}
        />
    """
