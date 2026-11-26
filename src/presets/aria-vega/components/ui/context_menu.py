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


def ContextMenu(placement="bottom start", offset=4, crossOffset=0, className=None, children=None, **props):
    data_slot = props.pop("data-slot", "context-menu-content")

    return t"""
        <{PopoverPrimitive}
            data-slot={data_slot}
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            class={cn("z-50 w-(--trigger-width) min-w-36 origin-(--trigger-anchor-point) overflow-x-hidden overflow-y-auto rounded-md bg-popover p-1 text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 outline-none data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:overflow-hidden data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2 **:data-[slot$=-item]:data-focused:bg-foreground/10", className)}
        >
            <{MenuPrimitive} class="max-h-[inherit] overflow-x-hidden overflow-y-auto outline-hidden" ...{props}>
                {children}
            </{MenuPrimitive}>
        </{PopoverPrimitive}>
    """


def ContextMenuTrigger(**props):
    return t'<{MenuTriggerPrimitive} data-slot="context-menu" trigger="contextMenu" ...{props} />'


def ContextMenuGroup(**props):
    return t'<{MenuSectionPrimitive} data-slot="context-menu-group" ...{props} />'


def ContextMenuLabel(className=None, inset=None, **props):
    return t"""
        <{HeaderPrimitive}
            data-slot="context-menu-label"
            data-inset={inset}
            class={cn("px-2 py-1.5 text-xs font-medium text-muted-foreground data-inset:pl-8", className)}
            ...{props}
        />
    """


context_menu_item_variants = cva(
    "group/context-menu-item relative flex cursor-default items-center outline-hidden select-none data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0",
    {
        "selectionMode": {
            "none": "gap-2 rounded-sm px-2 py-1.5 text-sm focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-[variant=destructive]:text-destructive data-[variant=destructive]:focus:bg-destructive/10 data-[variant=destructive]:focus:text-destructive dark:data-[variant=destructive]:focus:bg-destructive/20 [&_svg:not([class*='size-'])]:size-4 focus:*:[svg]:text-accent-foreground data-[variant=destructive]:*:[svg]:text-destructive",
            "single": "gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm focus:bg-accent focus:text-accent-foreground data-inset:pl-8 [&_svg:not([class*='size-'])]:size-4",
            "multiple": "gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm focus:bg-accent focus:text-accent-foreground data-inset:pl-8 [&_svg:not([class*='size-'])]:size-4",
        },
    },
)


def ContextMenuItem(className=None, inset=None, variant="default", children=None, **props):
    def callback(class_name, props):
        selection_mode = props.get("selectionMode")

        return cn(context_menu_item_variants(selectionMode=selection_mode), class_name)

    def callback_2(children, props):
        is_selected, selection_mode = props.get("isSelected"), props.get("selectionMode")

        span = t"""
            <span
                class="pointer-events-none absolute right-2"
                data-slot={"context-menu-radio-item-indicator" if selection_mode == "single" else "context-menu-checkbox-item-indicator"}
            >
                {t'<{CheckIcon} />' if is_selected else None}
            </span>
        """

        return t"{span if selection_mode != "none" else None}{children}"

    return t"""
        <{MenuItemPrimitive}
            data-slot="context-menu-item"
            data-inset={inset}
            data-variant={variant}
            textValue={children if isinstance(children, str) else props.get("textValue")}
            class={composeRenderProps(className, callback)}
            ...{props}
        >
            {composeRenderProps(children, callback_2)}
        </{MenuItemPrimitive}>
    """


def ContextMenuSub(**props):
    return t'<{SubmenuTriggerPrimitive} data-slot="context-menu-sub" ...{props} />'


def ContextMenuSubTrigger(className=None, inset=None, children=None, **props):
    return t"""
        <{MenuItemPrimitive}
            data-slot="context-menu-sub-trigger"
            data-inset={inset}
            textValue={children if isinstance(children, str) else props.get("textValue")}
            class={cn("flex cursor-default items-center rounded-sm px-2 py-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground data-inset:pl-8 data-open:bg-accent data-open:text-accent-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {composeRenderProps(children, lambda children: t'''
                {children}
                <{ChevronRightIcon} class="ml-auto" />
            ''')}
        </{MenuItemPrimitive}>
    """


def ContextMenuSubContent(placement="end top", crossOffset=-3, offset=0, className=None, **props):
    return t"""
        <{ContextMenu}
            data-slot="context-menu-sub-content"
            class={cn("w-auto min-w-32 rounded-md border bg-popover p-1 text-popover-foreground shadow-lg duration-100", className)}
            placement={placement}
            crossOffset={crossOffset}
            offset={offset}
            ...{props}
        />
    """


def ContextMenuSeparator(className=None, **props):
    return t"""
        <{SeparatorPrimitive}
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
