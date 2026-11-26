from utils import cn

__js__ = {"@base-ui/react/menu": ["Menu as MenuPrimitive"], "lucide-react": ["ChevronRightIcon", "CheckIcon"]}


def DropdownMenu(**props):
    return t'<{MenuPrimitive.Root} data-slot="dropdown-menu" ...{props} />'


def DropdownMenuPortal(**props):
    return t'<{MenuPrimitive.Portal} data-slot="dropdown-menu-portal" ...{props} />'


def DropdownMenuTrigger(**props):
    return t'<{MenuPrimitive.Trigger} data-slot="dropdown-menu-trigger" ...{props} />'


def DropdownMenuContent(align="start", alignOffset=0, side="bottom", sideOffset=4, className=None, **props):
    return t"""
        <{MenuPrimitive.Portal}>
            <{MenuPrimitive.Positioner}
                class="isolate z-50 outline-none"
                align={align}
                alignOffset={alignOffset}
                side={side}
                sideOffset={sideOffset}
            >
                <{MenuPrimitive.Popup}
                    data-slot="dropdown-menu-content"
                    class={cn("z-50 max-h-(--available-height) w-(--anchor-width) min-w-32 origin-(--transform-origin) overflow-x-hidden overflow-y-auto rounded-none bg-popover text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 outline-none data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:overflow-hidden data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                    ...{props}
                />
            </{MenuPrimitive.Positioner}>
        </{MenuPrimitive.Portal}>
    """


def DropdownMenuGroup(**props):
    return t'<{MenuPrimitive.Group} data-slot="dropdown-menu-group" ...{props} />'


def DropdownMenuLabel(className=None, inset=None, **props):
    return t"""
        <{MenuPrimitive.GroupLabel}
            data-slot="dropdown-menu-label"
            data-inset={inset}
            class={cn("px-2 py-2 text-xs text-muted-foreground data-inset:pl-7", className)}
            ...{props}
        />
    """


def DropdownMenuItem(className=None, inset=None, variant="default", **props):
    return t"""
        <{MenuPrimitive.Item}
            data-slot="dropdown-menu-item"
            data-inset={inset}
            data-variant={variant}
            class={cn("group/dropdown-menu-item relative flex cursor-default items-center gap-2 rounded-none px-2 py-2 text-xs outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-7 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 data-[variant=destructive]:*:[svg]:text-destructive", className)}
            ...{props}
        />
    """


def DropdownMenuSub(**props):
    return t'<{MenuPrimitive.SubmenuRoot} data-slot="dropdown-menu-sub" ...{props} />'


def DropdownMenuSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{MenuPrimitive.SubmenuTrigger}
            data-slot="dropdown-menu-sub-trigger"
            data-inset={inset}
            class={cn("flex cursor-default items-center gap-2 rounded-none px-2 py-2 text-xs outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-7 data-popup-open:bg-accent data-popup-open:text-accent-foreground data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{ChevronRightIcon} class="ml-auto" />
        </{MenuPrimitive.SubmenuTrigger}>
    """


def DropdownMenuSubContent(align="start", alignOffset=-3, side="right", sideOffset=0, className=None, **props):
    return t"""
        <{DropdownMenuContent}
            data-slot="dropdown-menu-sub-content"
            class={cn("w-auto min-w-[96px] rounded-none bg-popover text-popover-foreground shadow-lg ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
            align={align}
            alignOffset={alignOffset}
            side={side}
            sideOffset={sideOffset}
            ...{props}
        />
    """


def DropdownMenuCheckboxItem(className=None, children=None, checked=None, inset=None, **props):
    return t"""
        <{MenuPrimitive.CheckboxItem}
            data-slot="dropdown-menu-checkbox-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2 rounded-none py-2 pr-8 pl-2 text-xs outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-7 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            checked={checked}
            ...{props}
        >
            <span
                class="pointer-events-none absolute right-2 flex items-center justify-center"
                data-slot="dropdown-menu-checkbox-item-indicator"
            >
                <{MenuPrimitive.CheckboxItemIndicator}>
                    <{CheckIcon} />
                </{MenuPrimitive.CheckboxItemIndicator}>
            </span>
            {children}
        </{MenuPrimitive.CheckboxItem}>
    """


def DropdownMenuRadioGroup(**props):
    return t'<{MenuPrimitive.RadioGroup} data-slot="dropdown-menu-radio-group" ...{props} />'


def DropdownMenuRadioItem(className=None, children=None, inset=None, **props):
    return t"""
        <{MenuPrimitive.RadioItem}
            data-slot="dropdown-menu-radio-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2 rounded-none py-2 pr-8 pl-2 text-xs outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-7 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <span
                class="pointer-events-none absolute right-2 flex items-center justify-center"
                data-slot="dropdown-menu-radio-item-indicator"
            >
                <{MenuPrimitive.RadioItemIndicator}>
                    <{CheckIcon} />
                </{MenuPrimitive.RadioItemIndicator}>
            </span>
            {children}
        </{MenuPrimitive.RadioItem}>
    """


def DropdownMenuSeparator(className=None, **props):
    return t"""
        <{MenuPrimitive.Separator}
            data-slot="dropdown-menu-separator"
            class={cn("-mx-1 h-px bg-border", className)}
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
