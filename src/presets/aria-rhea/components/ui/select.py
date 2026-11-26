from utils import cn
from input_group import InputGroup, InputGroupAddon, InputGroupInput

__js__ = {
    "react-aria-components": [
        "Button as ButtonPrimitive",
        "composeRenderProps",
        "Header as HeaderPrimitive",
        "ListBoxItem as ListBoxItemPrimitive",
        "ListBox as ListBoxPrimitive",
        "ListBoxSection as ListBoxSectionPrimitive",
        "Popover as PopoverPrimitive",
        "SearchField",
        "Select as SelectPrimitive",
        "SelectValue as SelectValuePrimitive",
        "Separator as SeparatorPrimitive",
    ],
    "lucide-react": ["ChevronDownIcon", "SearchIcon", "CheckIcon"],
}


def Select(className=None, **props):
    return t'<{SelectPrimitive} data-slot="select" class={cn("w-fit", className)} ...{props} />'


def SelectGroup(className=None, **props):
    return t"""
        <{ListBoxSectionPrimitive}
            data-slot="select-group"
            class={cn("scroll-my-1.5 p-1", className)}
            ...{props}
        />
    """


def SelectValue(className=None, children=None, **props):
    def callback(props_2):
        selected_items, selected_text, default_children = props_2.get("selectedItems"), props_2.get("selectedText"), props_2.get("defaultChildren")

        return selected_text if len(selected_items) > 1 else default_children

    return t"""
        <{SelectValuePrimitive}
            data-slot="select-value"
            class={cn("flex flex-1 text-left data-placeholder:text-muted-foreground", className)}
            ...{props}
        >
            {children if callable(children) else callback}
        </{SelectValuePrimitive}>
    """


def SelectTrigger(className=None, size="default", children=None, **props):
    return t"""
        <{ButtonPrimitive}
            data-slot="select-trigger"
            data-size={size}
            class={cn("flex w-full items-center justify-between gap-1.5 rounded-2xl border border-transparent bg-input/50 px-3 py-2 text-sm whitespace-nowrap transition-[color,box-shadow] duration-200 outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/30 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 data-placeholder:text-muted-foreground data-[size=default]:h-8 data-[size=sm]:h-7 *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-1.5 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{ChevronDownIcon} class="pointer-events-none size-4 text-muted-foreground" />
        </{ButtonPrimitive}>
    """


def SelectContent(className=None, children=None, placement="bottom", offset=4, crossOffset=0, **props):
    return t"""
        <{SelectPopover} class={className} placement={placement} offset={offset} crossOffset={crossOffset} ...{props}>
            <{SelectList}>{children}</{SelectList}>
        </{SelectPopover}>
    """


def SelectPopover(className=None, children=None, placement="bottom start", offset=4, crossOffset=0, **props):
    return t"""
        <{PopoverPrimitive}
            data-slot="select-content"
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            class={cn("relative isolate z-50 w-(--trigger-width) min-w-36 origin-(--trigger-anchor-point) overflow-hidden rounded-2xl bg-popover text-popover-foreground shadow-lg ring-1 ring-foreground/5 duration-100 data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2 **:data-[slot$=-item]:data-focused:bg-foreground/10 dark:ring-foreground/10", className)}
            ...{props}
        >
            {children}
        </{PopoverPrimitive}>
    """


def SelectList(className=None, **props):
    return t"""
        <{ListBoxPrimitive}
            data-slot="select-list"
            class={cn("group/select-list max-h-[inherit] overflow-x-hidden overflow-y-auto p-0 outline-hidden", className)}
            ...{props}
        />
    """


def SelectInput(className=None, **props):
    return t"""
        <{SearchField} ...{props} autoFocus data-slot="select-input-wrapper" class={cn("p-1 pb-0", className)}>
            <{InputGroup}>
                <{InputGroupInput} data-slot="select-input" class="[&::-webkit-search-cancel-button]:hidden" />
                <{InputGroupAddon}>
                    <{SearchIcon} class="size-4 shrink-0 opacity-50" />
                </{InputGroupAddon}>
            </{InputGroup}>
        </{SearchField}>
    """


def SelectLabel(className=None, **props):
    return t"""
        <{HeaderPrimitive}
            data-slot="select-label"
            class={cn("px-2 py-1 text-xs text-muted-foreground", className)}
            ...{props}
        />
    """


def SelectItem(className=None, children=None, **props):
    def callback(children, props_2):
        is_selected = props_2.get("isSelected")

        return t"""
            <span class="flex flex-1 shrink-0 gap-2 whitespace-nowrap">{children}</span>
            <span class="pointer-events-none absolute right-2 flex size-4 items-center justify-center">
                {t'<{CheckIcon} class="pointer-events-none" />' if is_selected else None}
            </span>
        """

    return t"""
        <{ListBoxItemPrimitive}
            data-slot="select-item"
            textValue={children if isinstance(children, str) else None}
            class={cn("relative flex min-h-7 w-full cursor-default items-center gap-2 rounded-xl py-1.5 pr-8 pl-2 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-focused:bg-accent data-focused:text-accent-foreground data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{ListBoxItemPrimitive}>
    """


def SelectSeparator(className=None, **props):
    return t"""
        <{SeparatorPrimitive}
            data-slot="select-separator"
            class={cn("pointer-events-none -mx-1 my-1 h-px bg-border", className)}
            ...{props}
        />
    """


def SelectEmpty(className=None, **props):
    return t"""
        <div
            data-slot="select-empty"
            class={cn("hidden w-full justify-center py-2 text-center text-sm text-muted-foreground group-data-empty/select-list:flex", className)}
            ...{props}
        />
    """
