from utils import cn
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuPortal,
    DropdownMenuRadioGroup,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuSub,
    DropdownMenuSubContent,
    DropdownMenuSubTrigger,
    DropdownMenuTrigger,
)

__js__ = {
    "@base-ui/react/menu": ["Menu as MenuPrimitive"],
    "@base-ui/react/menubar": ["Menubar as MenubarPrimitive"],
    "lucide-react": ["CheckIcon"],
}


def Menubar(className=None, **props):
    return t"""
        <{MenubarPrimitive}
            data-slot="menubar"
            class={cn("flex h-9 items-center gap-1 rounded-md border p-1 shadow-xs", className)}
            ...{props}
        />
    """


def MenubarMenu(**props):
    return t'<{DropdownMenu} data-slot="menubar-menu" ...{props} />'


def MenubarGroup(**props):
    return t'<{DropdownMenuGroup} data-slot="menubar-group" ...{props} />'


def MenubarPortal(**props):
    return t'<{DropdownMenuPortal} data-slot="menubar-portal" ...{props} />'


def MenubarTrigger(className=None, **props):
    return t"""
        <{DropdownMenuTrigger}
            data-slot="menubar-trigger"
            class={cn("flex items-center rounded-sm px-2 py-1 text-sm font-medium outline-hidden select-none hover:bg-muted aria-expanded:bg-muted", className)}
            ...{props}
        />
    """


def MenubarContent(className=None, align="start", alignOffset=-4, sideOffset=8, **props):
    return t"""
        <{DropdownMenuContent}
            data-slot="menubar-content"
            align={align}
            alignOffset={alignOffset}
            sideOffset={sideOffset}
            class={cn("min-w-36 rounded-md bg-popover p-1 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95", className)}
            ...{props}
        />
    """


def MenubarItem(className=None, inset=None, variant="default", **props):
    return t"""
        <{DropdownMenuItem}
            data-slot="menubar-item"
            data-inset={inset}
            data-variant={variant}
            class={cn("group/menubar-item gap-2 rounded-sm px-2 py-1.5 text-sm focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-8 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 data-disabled:opacity-50 [&_svg:not([class*='size-'])]:size-4 data-[variant=destructive]:*:[svg]:text-destructive!", className)}
            ...{props}
        />
    """


def MenubarCheckboxItem(className=None, children=None, checked=None, inset=None, **props):
    return t"""
        <{MenuPrimitive.CheckboxItem}
            data-slot="menubar-checkbox-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2 rounded-md py-1.5 pr-2 pl-8 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-8 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0", className)}
            checked={checked}
            ...{props}
        >
            <span class="pointer-events-none absolute left-2 flex size-4 items-center justify-center [&_svg:not([class*='size-'])]:size-4">
                <{MenuPrimitive.CheckboxItemIndicator}>
                    <{CheckIcon} />
                </{MenuPrimitive.CheckboxItemIndicator}>
            </span>
            {children}
        </{MenuPrimitive.CheckboxItem}>
    """


def MenubarRadioGroup(**props):
    return t'<{DropdownMenuRadioGroup} data-slot="menubar-radio-group" ...{props} />'


def MenubarRadioItem(className=None, children=None, inset=None, **props):
    return t"""
        <{MenuPrimitive.RadioItem}
            data-slot="menubar-radio-item"
            data-inset={inset}
            class={cn("relative flex cursor-default items-center gap-2 rounded-md py-1.5 pr-2 pl-8 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-8 data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <span class="pointer-events-none absolute left-2 flex size-4 items-center justify-center [&_svg:not([class*='size-'])]:size-4">
                <{MenuPrimitive.RadioItemIndicator}>
                    <{CheckIcon} />
                </{MenuPrimitive.RadioItemIndicator}>
            </span>
            {children}
        </{MenuPrimitive.RadioItem}>
    """


def MenubarLabel(className=None, inset=None, **props):
    return t"""
        <{DropdownMenuLabel}
            data-slot="menubar-label"
            data-inset={inset}
            class={cn("px-2 py-1.5 text-sm font-medium data-inset:pl-8", className)}
            ...{props}
        />
    """


def MenubarSeparator(className=None, **props):
    return t"""
        <{DropdownMenuSeparator}
            data-slot="menubar-separator"
            class={cn("-mx-1 my-1 h-px bg-border", className)}
            ...{props}
        />
    """


def MenubarShortcut(className=None, **props):
    return t"""
        <{DropdownMenuShortcut}
            data-slot="menubar-shortcut"
            class={cn("ml-auto text-xs tracking-widest text-muted-foreground group-focus/menubar-item:text-accent-foreground", className)}
            ...{props}
        />
    """


def MenubarSub(**props):
    return t'<{DropdownMenuSub} data-slot="menubar-sub" ...{props} />'


def MenubarSubTrigger(className=None, inset=None, **props):
    return t"""
        <{DropdownMenuSubTrigger}
            data-slot="menubar-sub-trigger"
            data-inset={inset}
            class={cn("gap-2 rounded-sm px-2 py-1.5 text-sm focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-open:bg-accent data-open:text-accent-foreground [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        />
    """


def MenubarSubContent(className=None, **props):
    return t"""
        <{DropdownMenuSubContent}
            data-slot="menubar-sub-content"
            class={cn("min-w-32 rounded-md bg-popover p-1 text-popover-foreground shadow-lg ring-1 ring-foreground/10 duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
            ...{props}
        />
    """
