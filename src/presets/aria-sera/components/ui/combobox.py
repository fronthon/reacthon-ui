from javascript import NULL
from reacthon import use_context, use_ref
from utils import cn
from button import Button
from input_group import InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput

__js__ = {
    "react-aria-components": [
        "Button as ButtonPrimitive",
        "Collection",
        "ComboBox as ComboBoxPrimitive",
        "ComboBoxStateContext",
        "ComboBoxValue as ComboBoxValuePrimitive",
        "composeRenderProps",
        "Group",
        "Header as HeaderPrimitive",
        "Input as InputPrimitive",
        "ListBoxItem as ListBoxItemPrimitive",
        "ListBox as ListBoxPrimitive",
        "ListBoxSection as ListBoxSectionPrimitive",
        "Popover as PopoverPrimitive",
        "Separator as SeparatorPrimitive",
        "TagGroup as TagGroupPrimitive",
        "TagList as TagListPrimitive",
        "Tag as TagPrimitive",
    ],
    "lucide-react": ["ChevronDownIcon", "XIcon", "CheckIcon"],
}


def ComboboxValue(**props):
    return t'<{ComboBoxValuePrimitive} data-slot="combobox-value" ...{props} />'


def ComboboxTrigger(className=None, children=None, **props):
    return t"""
        <{ButtonPrimitive}
            data-slot="combobox-trigger"
            class={cn("[&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            {children}
            <{ChevronDownIcon} class="pointer-events-none size-3.5 text-muted-foreground" />
        </{ButtonPrimitive}>
    """


def ComboboxClear(className=None, **props):
    state = use_context(ComboBoxStateContext)
    if (state.inputValue if state else None) == "":
        return None

    def on_press():
        if state:
            state.setValue(None)

    return t"""
        <{InputGroupButton}
            data-slot="combobox-clear"
            variant="ghost"
            size="icon-xs"
            aria-label="Clear"
            class={cn(className)}
            onPress={on_press}
            slot={None}
            ...{props}
        >
            <{XIcon} class="pointer-events-none" />
        </{InputGroupButton}>
    """


def ComboboxInput(className=None, children=None, disabled=False, showTrigger=True, showClear=False, **props):
    input_group_button = t"""
        <{InputGroupButton}
            size="icon-xs"
            variant="ghost"
            data-slot="combobox-trigger"
            class="group-has-data-[slot=combobox-clear]/input-group:hidden data-pressed:bg-transparent [&_svg:not([class*='size-'])]:size-3.5"
            isDisabled={disabled}
        >
            <{ChevronDownIcon} class="pointer-events-none size-3.5 text-muted-foreground" />
        </{InputGroupButton}>
    """

    return t"""
        <{InputGroup} class={cn("w-auto", className)}>
            <{InputGroupInput} disabled={disabled} ...{props} />
            <{InputGroupAddon} align="inline-end">
                {showTrigger and input_group_button}
                {showClear and t'<{ComboboxClear} isDisabled={disabled} />'}
            </{InputGroupAddon}>
            {children}
        </{InputGroup}>
    """


def ComboboxContent(className=None, placement="bottom", offset=6, crossOffset=0, anchor=None, **props):
    return t"""
        <{PopoverPrimitive}
            data-slot="combobox-content"
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            triggerRef={anchor}
            class={cn("relative isolate z-50 max-h-72 w-(--trigger-width) min-w-36 origin-(--trigger-anchor-point) overflow-hidden rounded-none bg-popover text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2 **:data-[slot$=-item]:data-focused:bg-foreground/10 *:data-[slot=input-group]:m-1.5 *:data-[slot=input-group]:mb-0 *:data-[slot=input-group]:h-8 *:data-[slot=input-group]:border-transparent *:data-[slot=input-group]:bg-transparent *:data-[slot=input-group]:px-2.5 *:data-[slot=input-group]:focus-within:border-transparent", className)}
            ...{props}
        />
    """


def ComboboxList(className=None, **props):
    return t"""
        <{ListBoxPrimitive}
            data-slot="combobox-list"
            class={cn("group/combobox-content no-scrollbar max-h-[inherit] scroll-py-1.5 overflow-y-auto overscroll-contain p-1.5 data-empty:p-0", className)}
            ...{props}
        />
    """


def ComboboxItem(className=None, children=None, **props):
    def callback(children, props):
        is_selected = props.get("isSelected")

        return t"""
            {children}
            <span class="pointer-events-none absolute right-2 flex size-4 items-center justify-center">
                {t'<{CheckIcon} class="pointer-events-none" />' if is_selected else None}
            </span>
        """

    return t"""
        <{ListBoxItemPrimitive}
            data-slot="combobox-item"
            textValue={children if isinstance(children, str) else None}
            class={cn("relative flex w-full cursor-default items-center gap-2.5 rounded-none py-2 pr-8 pl-3 text-sm outline-hidden select-none data-focused:bg-accent data-focused:text-accent-foreground not-data-[variant=destructive]:data-focused:**:text-accent-foreground data-highlighted:bg-accent data-highlighted:text-accent-foreground not-data-[variant=destructive]:data-highlighted:**:text-accent-foreground data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{ListBoxItemPrimitive}>
    """


def ComboboxGroup(className=None, **props):
    return t'<{ListBoxSectionPrimitive} data-slot="combobox-group" class={cn(className)} ...{props} />'


def ComboboxLabel(className=None, **props):
    return t"""
        <{HeaderPrimitive}
            data-slot="combobox-label"
            class={cn("px-3 py-2 text-xs font-semibold tracking-wider text-muted-foreground uppercase", className)}
            ...{props}
        />
    """


def ComboboxEmpty(className=None, **props):
    return t"""
        <div
            data-slot="combobox-empty"
            class={cn("hidden w-full justify-center py-2 text-center text-sm text-muted-foreground group-data-empty/combobox-content:flex", className)}
            ...{props}
        />
    """


def ComboboxSeparator(className=None, **props):
    return t"""
        <{SeparatorPrimitive}
            data-slot="combobox-separator"
            class={cn("-mx-1.5 my-1.5 h-px bg-border/50", className)}
            ...{props}
        />
    """


def ComboboxChips(children=None, className=None, **props):
    return t"""
        <{Group}
            data-slot="combobox-chips"
            class={cn("flex min-h-10 flex-wrap items-center gap-1.5 rounded-none border border-transparent border-b-input bg-transparent bg-clip-padding px-0 py-1.5 text-sm transition-[color,border-color] focus-within:border-b-ring has-aria-invalid:border-b-destructive has-data-[slot=combobox-chip]:px-0 dark:has-aria-invalid:border-b-destructive/50", className)}
            ...{props}
        >
            {children}
        </{Group}>
    """


def ComboboxChipList(className=None, **props):
    def callback(props):
        selected_items, state = props.get("selectedItems"), props.get("state")

        def on_remove(keys):
            if isinstance(state.value, list):
                state.setValue([k for k in state.value if not keys.has(k)])

        return t"""
            <{TagGroupPrimitive} data-slot="combobox-chip-list" class={cn("contents", className)} onRemove={on_remove}>
                <{TagListPrimitive}
                    class="contents"
                    items={[item for item in selected_items if item not in (None, NULL)]}
                    ...{props}
                />
            </{TagGroupPrimitive}>
        """

    return t'<{ComboBoxValuePrimitive} class="contents">{callback}</{ComboBoxValuePrimitive}>'


def ComboboxChip(className=None, children=None, showRemove=True, **props):
    button = t"""
        <{Button}
            slot="remove"
            variant="ghost"
            size="icon-xs"
            class="-ml-1 opacity-50 hover:opacity-100"
            data-slot="combobox-chip-remove"
        >
            <{XIcon} class="pointer-events-none" />
        </{Button}>
    """

    return t"""
        <{TagPrimitive}
            data-slot="combobox-chip"
            class={cn("flex h-[calc(--spacing(5.5))] w-fit items-center justify-center gap-1 rounded-none bg-muted px-2 text-xs font-medium whitespace-nowrap text-foreground has-disabled:pointer-events-none has-disabled:cursor-not-allowed has-disabled:opacity-50 has-data-[slot=combobox-chip-remove]:pr-0", className)}
            ...{props}
        >
            {children}
            {showRemove and button}
        </{TagPrimitive}>
    """


def ComboboxChipsInput(className=None, **props):
    state = use_context(ComboBoxStateContext)

    def on_key_down(e):
        if e.key == "Backspace" and e.currentTarget.value == "" and isinstance(state.value if state else None, list) and len(state.value) > 0:
            e.preventDefault()
            state.setValue(state.value[0:-1])

    return t"""
        <{InputPrimitive}
            data-slot="combobox-chip-input"
            class={cn("min-w-16 flex-1 outline-none", className)}
            onKeyDown={on_key_down}
            ...{props}
        />
    """


def use_combobox_anchor():
    return use_ref(None)


Combobox = ComboBoxPrimitive

ComboboxCollection = Collection
