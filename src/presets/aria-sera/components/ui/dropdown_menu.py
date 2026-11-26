from utils import cn, cva

__js__ = {
    "react-aria-components": [
        "composeRenderProps",
        "Header as HeaderPrimitive",
        "MenuItem as MenuItemPrimitive",
        "Menu as MenuPrimitive",
        "MenuSection as MenuSectionPrimitive",
        "MenuTrigger as MenuTriggerPrimitive",
        "Popover as PopoverPrimitive",
        "Separator as SeparatorPrimitive",
        "SubmenuTrigger as SubmenuTriggerPrimitive",
    ],
    "lucide-react": ["CheckIcon", "ChevronRightIcon"],
}


def DropdownMenuTrigger(**props):
    return t'<{MenuTriggerPrimitive} data-slot="dropdown-menu-trigger" ...{props} />'


def DropdownMenu(placement="bottom start", offset=4, crossOffset=0, className=None, children=None, **props):
    data_slot = props.pop("data-slot", "dropdown-menu-content")

    return t"""
        <{PopoverPrimitive}
            data-slot={data_slot}
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            class={cn("z-50 w-(--trigger-width) min-w-48 origin-(--trigger-anchor-point) overflow-x-hidden overflow-y-auto rounded-none bg-popover p-1.5 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 outline-none data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:overflow-hidden data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2 **:data-[slot$=-item]:data-focused:bg-foreground/10", className)}
        >
            <{MenuPrimitive} class="max-h-[inherit] overflow-x-hidden overflow-y-auto outline-hidden" ...{props}>
                {children}
            </{MenuPrimitive}>
        </{PopoverPrimitive}>
    """


def DropdownMenuGroup(**props):
    return t'<{MenuSectionPrimitive} data-slot="dropdown-menu-group" ...{props} />'


def DropdownMenuLabel(className=None, inset=None, **props):
    return t"""
        <{HeaderPrimitive}
            data-slot="dropdown-menu-label"
            data-inset={inset}
            class={cn("px-3 py-2 text-xs font-semibold tracking-wider text-muted-foreground uppercase data-inset:pl-9.5", className)}
            ...{props}
        />
    """


dropdown_menu_item_variants = cva(
    "group/dropdown-menu-item relative flex cursor-default items-center outline-hidden select-none data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0",
    {
        "selectionMode": {
            "none": "gap-2.5 rounded-none px-3 py-2 text-xs font-medium tracking-wider uppercase focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-9.5 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 [&_svg:not([class*='size-'])]:size-3.5 data-[variant=destructive]:*:[svg]:text-destructive",
            "single": "gap-2.5 rounded-none py-2 pr-8 pl-3 text-xs font-medium tracking-wider uppercase focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-9.5 [&_svg:not([class*='size-'])]:size-3.5",
            "multiple": "gap-2.5 rounded-none py-2 pr-8 pl-3 text-xs font-medium tracking-wider uppercase focus:bg-accent focus:text-accent-foreground focus:**:text-accent-foreground data-inset:pl-9.5 [&_svg:not([class*='size-'])]:size-3.5",
        },
    },
)


def DropdownMenuItem(className=None, inset=None, variant="default", children=None, **props):
    def callback(class_name, props_2):
        selection_mode = props_2.get("selectionMode")

        return cn(dropdown_menu_item_variants(selectionMode=selection_mode), class_name)

    def callback_2(children, props_2):
        is_selected, selection_mode = props_2.get("isSelected"), props_2.get("selectionMode")

        span = t"""
            <span
                class="pointer-events-none absolute right-2 flex items-center justify-center"
                data-slot={"dropdown-menu-radio-item-indicator" if selection_mode == "single" else "dropdown-menu-checkbox-item-indicator"}
            >
                {t'<{CheckIcon} />' if is_selected else None}
            </span>
        """

        return t"{span if selection_mode != "none" else None}{children}"

    return t"""
        <{MenuItemPrimitive}
            data-slot="dropdown-menu-item"
            data-inset={inset}
            data-variant={variant}
            textValue={children if isinstance(children, str) else props.get("textValue")}
            class={composeRenderProps(className, callback)}
            ...{props}
        >
            {composeRenderProps(children, callback_2)}
        </{MenuItemPrimitive}>
    """


def DropdownMenuSub(**props):
    return t'<{SubmenuTriggerPrimitive} data-slot="dropdown-menu-sub" ...{props} />'


def DropdownMenuSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{MenuItemPrimitive}
            data-slot="dropdown-menu-sub-trigger"
            data-inset={inset}
            textValue={children if isinstance(children, str) else props.get("textValue")}
            class={cn("flex cursor-default items-center gap-2 rounded-none px-3 py-2 text-xs font-medium tracking-wider uppercase outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-inset:pl-9.5 data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            {composeRenderProps(children, lambda children: t'''
                {children}
                <{ChevronRightIcon} class="ml-auto" />
            ''')}
        </{MenuItemPrimitive}>
    """


def DropdownMenuSubContent(placement="end top", crossOffset=-3, offset=0, className=None, **props):
    return t"""
        <{DropdownMenu}
            data-slot="dropdown-menu-sub-content"
            class={cn("w-auto min-w-36 rounded-none bg-popover p-1.5 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100", className)}
            placement={placement}
            crossOffset={crossOffset}
            offset={offset}
            ...{props}
        />
    """


def DropdownMenuSeparator(className=None, **props):
    return t"""
        <{SeparatorPrimitive}
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
