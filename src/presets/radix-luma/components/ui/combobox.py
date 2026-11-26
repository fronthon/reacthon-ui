from reacthon import use_ref
from utils import cn
from button import Button
from input_group import InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput

__js__ = {
    "@base-ui/react": ["Combobox as ComboboxPrimitive"],
    "lucide-react": ["ChevronDownIcon", "XIcon", "CheckIcon"],
}

Combobox = ComboboxPrimitive.Root


def ComboboxValue(**props):
    return t'<{ComboboxPrimitive.Value} data-slot="combobox-value" ...{props} />'


def ComboboxTrigger(className=None, children=None, **props):
    return t"""
        <{ComboboxPrimitive.Trigger}
            data-slot="combobox-trigger"
            class={cn("[&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{ChevronDownIcon} class="pointer-events-none size-4 text-muted-foreground" />
        </{ComboboxPrimitive.Trigger}>
    """


def ComboboxClear(className=None, **props):
    return t"""
        <{ComboboxPrimitive.Clear}
            data-slot="combobox-clear"
            render={t'<{InputGroupButton} variant="ghost" size="icon-xs" />'}
            class={cn(className)}
            ...{props}
        >
            <{XIcon} class="pointer-events-none" />
        </{ComboboxPrimitive.Clear}>
    """


def ComboboxInput(className=None, children=None, disabled=False, showTrigger=True, showClear=False, **props):
    input_group_button = t"""
        <{InputGroupButton}
            size="icon-xs"
            variant="ghost"
            asChild
            data-slot="input-group-button"
            class="group-has-data-[slot=combobox-clear]/input-group:hidden data-pressed:bg-transparent"
            disabled={disabled}
        >
            <{ComboboxTrigger} />
        </{InputGroupButton}>
    """

    return t"""
        <{InputGroup} class={cn("w-auto", className)}>
            <{ComboboxPrimitive.Input} render={t'<{InputGroupInput} disabled={disabled} />'} ...{props} />
            <{InputGroupAddon} align="inline-end">
                {showTrigger and input_group_button}
                {showClear and t'<{ComboboxClear} disabled={disabled} />'}
            </{InputGroupAddon}>
            {children}
        </{InputGroup}>
    """


def ComboboxContent(className=None, side="bottom", sideOffset=6, align="start", alignOffset=0, anchor=None, **props):
    return t"""
        <{ComboboxPrimitive.Portal}>
            <{ComboboxPrimitive.Positioner}
                side={side}
                sideOffset={sideOffset}
                align={align}
                alignOffset={alignOffset}
                anchor={anchor}
                class="isolate z-50"
            >
                <{ComboboxPrimitive.Popup}
                    data-slot="combobox-content"
                    data-chips={bool(anchor)}
                    class={cn("group/combobox-content relative max-h-(--available-height) w-(--anchor-width) max-w-(--available-width) min-w-[calc(var(--anchor-width)+--spacing(7))] origin-(--transform-origin) overflow-hidden rounded-3xl bg-popover text-popover-foreground shadow-lg ring-1 ring-foreground/5 duration-100 data-[chips=true]:min-w-(--anchor-width) data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 *:data-[slot=input-group]:m-1.5 *:data-[slot=input-group]:mb-0 *:data-[slot=input-group]:h-8 *:data-[slot=input-group]:border-input/30 *:data-[slot=input-group]:bg-input/50 *:data-[slot=input-group]:shadow-none dark:ring-foreground/10 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                    ...{props}
                />
            </{ComboboxPrimitive.Positioner}>
        </{ComboboxPrimitive.Portal}>
    """


def ComboboxList(className=None, **props):
    return t"""
        <{ComboboxPrimitive.List}
            data-slot="combobox-list"
            class={cn("no-scrollbar max-h-[min(calc(--spacing(72)---spacing(9)),calc(var(--available-height)---spacing(9)))] scroll-py-1.5 overflow-y-auto overscroll-contain p-1.5 data-empty:p-0", className)}
            ...{props}
        />
    """


def ComboboxItem(className=None, children=None, **props):
    span = t'<span class="pointer-events-none absolute right-2 flex size-4 items-center justify-center" />'

    return t"""
        <{ComboboxPrimitive.Item}
            data-slot="combobox-item"
            class={cn("relative flex w-full cursor-default items-center gap-2.5 rounded-2xl py-2 pr-8 pl-3 text-sm font-medium outline-hidden select-none data-highlighted:bg-accent data-highlighted:text-accent-foreground not-data-[variant=destructive]:data-highlighted:**:text-accent-foreground data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{ComboboxPrimitive.ItemIndicator} render={span}>
                <{CheckIcon} class="pointer-events-none" />
            </{ComboboxPrimitive.ItemIndicator}>
        </{ComboboxPrimitive.Item}>
    """


def ComboboxGroup(className=None, **props):
    return t'<{ComboboxPrimitive.Group} data-slot="combobox-group" class={cn(className)} ...{props} />'


def ComboboxLabel(className=None, **props):
    return t"""
        <{ComboboxPrimitive.GroupLabel}
            data-slot="combobox-label"
            class={cn("px-3 py-2.5 text-xs text-muted-foreground", className)}
            ...{props}
        />
    """


def ComboboxCollection(**props):
    return t'<{ComboboxPrimitive.Collection} data-slot="combobox-collection" ...{props} />'


def ComboboxEmpty(className=None, **props):
    return t"""
        <{ComboboxPrimitive.Empty}
            data-slot="combobox-empty"
            class={cn("hidden w-full justify-center py-2 text-center text-sm text-muted-foreground group-data-empty/combobox-content:flex", className)}
            ...{props}
        />
    """


def ComboboxSeparator(className=None, **props):
    return t"""
        <{ComboboxPrimitive.Separator}
            data-slot="combobox-separator"
            class={cn("-mx-1.5 my-1.5 h-px bg-border", className)}
            ...{props}
        />
    """


def ComboboxChips(className=None, **props):
    return t"""
        <{ComboboxPrimitive.Chips}
            data-slot="combobox-chips"
            class={cn("flex min-h-9 flex-wrap items-center gap-1.5 rounded-3xl border border-transparent bg-input/50 bg-clip-padding px-3 py-1.5 text-sm transition-[color,box-shadow,background-color] focus-within:border-ring focus-within:ring-3 focus-within:ring-ring/30 has-aria-invalid:border-destructive has-aria-invalid:ring-3 has-aria-invalid:ring-destructive/20 has-data-[slot=combobox-chip]:px-1.5 dark:has-aria-invalid:border-destructive/50 dark:has-aria-invalid:ring-destructive/40", className)}
            ...{props}
        />
    """


def ComboboxChip(className=None, children=None, showRemove=True, **props):
    chip_remove = t"""
        <{ComboboxPrimitive.ChipRemove}
            render={t'<{Button} variant="ghost" size="icon-xs" />'}
            class="-ml-1 opacity-50 hover:opacity-100"
            data-slot="combobox-chip-remove"
        >
            <{XIcon} class="pointer-events-none" />
        </{ComboboxPrimitive.ChipRemove}>
    """

    return t"""
        <{ComboboxPrimitive.Chip}
            data-slot="combobox-chip"
            class={cn("flex h-[calc(--spacing(5.5))] w-fit items-center justify-center gap-1 rounded-3xl bg-input px-2 text-xs font-medium whitespace-nowrap text-foreground has-disabled:pointer-events-none has-disabled:cursor-not-allowed has-disabled:opacity-50 has-data-[slot=combobox-chip-remove]:pr-0 dark:bg-input/60", className)}
            ...{props}
        >
            {children}
            {showRemove and chip_remove}
        </{ComboboxPrimitive.Chip}>
    """


def ComboboxChipsInput(className=None, **props):
    return t"""
        <{ComboboxPrimitive.Input}
            data-slot="combobox-chip-input"
            class={cn("min-w-16 flex-1 outline-none", className)}
            ...{props}
        />
    """


def use_combobox_anchor():
    return use_ref(None)
