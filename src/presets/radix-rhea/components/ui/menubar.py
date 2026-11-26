from utils import cn

__js__ = {"radix-ui": ["Menubar as MenubarPrimitive"], "lucide-react": ["CheckIcon", "ChevronRightIcon"]}


def Menubar(className=None, **props):
    return t"""
        <{MenubarPrimitive.Root}
            data-slot="menubar"
            class={cn("flex h-8 items-center rounded-2xl border p-[3px]", className)}
            ...{props}
        />
    """


def MenubarMenu(**props):
    return t'<{MenubarPrimitive.Menu} data-slot="menubar-menu" ...{props} />'


def MenubarGroup(**props):
    return t'<{MenubarPrimitive.Group} data-slot="menubar-group" ...{props} />'


def MenubarPortal(**props):
    return t'<{MenubarPrimitive.Portal} data-slot="menubar-portal" ...{props} />'


def MenubarRadioGroup(**props):
    return t'<{MenubarPrimitive.RadioGroup} data-slot="menubar-radio-group" ...{props} />'


def MenubarTrigger(className=None, **props):
    return t"""
        <{MenubarPrimitive.Trigger}
            data-slot="menubar-trigger"
            class={cn("flex items-center rounded-2xl px-1.5 py-[2px] text-sm font-medium outline-hidden select-none hover:bg-muted aria-expanded:bg-muted", className)}
            ...{props}
        />
    """


def MenubarContent(className=None, align="start", alignOffset=-4, sideOffset=8, **props):
    return t"""
        <{MenubarPortal}>
            <{MenubarPrimitive.Content}
                data-slot="menubar-content"
                align={align}
                alignOffset={alignOffset}
                sideOffset={sideOffset}
                class={cn("z-50 min-w-36 origin-(--radix-menubar-content-transform-origin) overflow-hidden rounded-2xl bg-popover p-1 text-popover-foreground shadow-lg ring-1 ring-foreground/5 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 dark:ring-foreground/10 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95", className)}
                ...{props}
            />
        </{MenubarPortal}>
    """


def MenubarItem(className=None, inset=None, variant="default", **props):
    return t"""
        <{MenubarPrimitive.Item}
            data-slot="menubar-item"
            data-inset={inset}
            data-variant={variant}
            class={cn("group/menubar-item relative flex min-h-7 cursor-default items-center gap-2 rounded-xl px-2 py-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-7 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 data-[variant=destructive]:*:[svg]:text-destructive!", className)}
            ...{props}
        />
    """


def MenubarCheckboxItem(className=None, children=None, checked=None, inset=None, **props):
    return t"""
        <{MenubarPrimitive.CheckboxItem}
            data-slot="menubar-checkbox-item"
            data-inset={inset}
            class={cn("relative flex min-h-7 cursor-default items-center gap-2 rounded-xl py-1.5 pr-1.5 pl-7 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-7 data-disabled:pointer-events-none [&_svg]:pointer-events-none [&_svg]:shrink-0", className)}
            checked={checked}
            ...{props}
        >
            <span class="pointer-events-none absolute left-1.5 flex size-4 items-center justify-center [&_svg:not([class*='size-'])]:size-4">
                <{MenubarPrimitive.ItemIndicator}>
                    <{CheckIcon} />
                </{MenubarPrimitive.ItemIndicator}>
            </span>
            {children}
        </{MenubarPrimitive.CheckboxItem}>
    """


def MenubarRadioItem(className=None, children=None, inset=None, **props):
    return t"""
        <{MenubarPrimitive.RadioItem}
            data-slot="menubar-radio-item"
            data-inset={inset}
            class={cn("relative flex min-h-7 cursor-default items-center gap-2 rounded-xl py-1.5 pr-1.5 pl-7 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-7 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <span class="pointer-events-none absolute left-1.5 flex size-4 items-center justify-center [&_svg:not([class*='size-'])]:size-4">
                <{MenubarPrimitive.ItemIndicator}>
                    <{CheckIcon} />
                </{MenubarPrimitive.ItemIndicator}>
            </span>
            {children}
        </{MenubarPrimitive.RadioItem}>
    """


def MenubarLabel(className=None, inset=None, **props):
    return t"""
        <{MenubarPrimitive.Label}
            data-slot="menubar-label"
            data-inset={inset}
            class={cn("px-2 py-1 text-sm text-muted-foreground data-inset:pl-7", className)}
            ...{props}
        />
    """


def MenubarSeparator(className=None, **props):
    return t"""
        <{MenubarPrimitive.Separator}
            data-slot="menubar-separator"
            class={cn("-mx-1 my-1 h-px bg-border/50", className)}
            ...{props}
        />
    """


def MenubarShortcut(className=None, **props):
    return t"""
        <span
            data-slot="menubar-shortcut"
            class={cn("ml-auto text-xs tracking-widest text-muted-foreground group-focus/menubar-item:text-accent-foreground", className)}
            ...{props}
        />
    """


def MenubarSub(**props):
    return t'<{MenubarPrimitive.Sub} data-slot="menubar-sub" ...{props} />'


def MenubarSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{MenubarPrimitive.SubTrigger}
            data-slot="menubar-sub-trigger"
            data-inset={inset}
            class={cn("flex min-h-7 cursor-default items-center gap-2 rounded-xl px-2 py-1.5 text-sm outline-none select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-7 data-open:bg-accent data-open:text-accent-foreground [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{ChevronRightIcon} class="ml-auto size-4" />
        </{MenubarPrimitive.SubTrigger}>
    """


def MenubarSubContent(className=None, **props):
    return t"""
        <{MenubarPrimitive.SubContent}
            data-slot="menubar-sub-content"
            class={cn("z-50 min-w-32 origin-(--radix-menubar-content-transform-origin) overflow-hidden rounded-2xl bg-popover p-1 text-popover-foreground shadow-lg ring-1 ring-foreground/5 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 dark:ring-foreground/10 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
            ...{props}
        />
    """
