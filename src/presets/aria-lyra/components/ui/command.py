from utils import cn
from dialog import Dialog, DialogDescription, DialogHeader, DialogTitle
from input_group import InputGroup, InputGroupAddon

__js__ = {
    "react-aria-components": [
        "Autocomplete",
        "Collection",
        "composeRenderProps",
        "Header",
        "Input",
        "Menu",
        "MenuItem",
        "MenuSection",
        "SearchField",
        "Separator",
        "useFilter",
    ],
    "lucide-react": ["SearchIcon", "CheckIcon"],
}


def Command(className=None, dir=None, style=None, **props):
    contains = useFilter({"sensitivity": "base"}).contains
    return t"""
        <div
            data-slot="command"
            dir={dir}
            class={cn("flex size-full flex-col overflow-hidden rounded-none bg-popover text-popover-foreground", className)}
            style={style}
        >
            <{Autocomplete} ...{props} filter={props.get("filter") or contains}>{props["children"]}</{Autocomplete}>
        </div>
    """


def CommandDialog(title="Command Palette", description="Search for a command to run...", children=None, open=None, onOpenChange=None, className=None, showCloseButton=False, **props):
    return t"""
        <{Dialog}
            isOpen={open}
            onOpenChange={onOpenChange}
            class={cn("top-1/3 translate-y-0 overflow-hidden rounded-none p-0", className)}
            showCloseButton={showCloseButton}
            isDismissable
            ...{props}
        >
            <{DialogHeader} class="sr-only">
                <{DialogTitle}>{title}</{DialogTitle}>
                <{DialogDescription}>{description}</{DialogDescription}>
            </{DialogHeader}>
            {children}
        </{Dialog}>
    """


def CommandInput(className=None, **props):
    return t"""
        <{SearchField}
            autoFocus
            aria-label={props.get("placeholder") or "Search"}
            data-slot="command-input-wrapper"
            class="border-b pb-0"
        >
            <{InputGroup} class="h-8 border-none border-input/30 bg-input/30 shadow-none! *:data-[slot=input-group-addon]:pl-2!">
                <{Input}
                    ...{props}
                    data-slot="command-input"
                    class={cn("w-full text-xs outline-hidden disabled:cursor-not-allowed disabled:opacity-50 [&::-webkit-search-cancel-button]:hidden", className)}
                />
                <{InputGroupAddon}>
                    <{SearchIcon} class="size-4 shrink-0 opacity-50" />
                </{InputGroupAddon}>
            </{InputGroup}>
        </{SearchField}>
    """


def CommandList(className=None, **props):
    return t"""
        <{Menu}
            ...{props}
            data-slot="command-list"
            class={cn("no-scrollbar max-h-72 scroll-py-0 overflow-x-hidden overflow-y-auto outline-none", className)}
        />
    """


def CommandEmpty(className=None, **props):
    return t'<div data-slot="command-empty" class={cn("py-6 text-center text-xs", className)} ...{props} />'


def CommandGroup(className=None, children=None, items=None, heading=None, **props):
    return t"""
        <{MenuSection}
            data-slot="command-group"
            class={cn("overflow-hidden text-foreground **:[[cmdk-group-heading]]:px-2 **:[[cmdk-group-heading]]:py-1.5 **:[[cmdk-group-heading]]:text-xs **:[[cmdk-group-heading]]:text-muted-foreground", className)}
            ...{props}
        >
            {heading and t'<{Header} cmdk-group-heading="">{heading}</{Header}>'}
            <{Collection} items={items}>{children}</{Collection}>
        </{MenuSection}>
    """


def CommandSeparator(className=None, **props):
    return t'<{Separator} data-slot="command-separator" class={cn("-mx-1 h-px bg-border", className)} ...{props} />'


def CommandItem(className=None, children=None, textValue=None, **props):
    return t"""
        <{MenuItem}
            ...{props}
            data-slot="command-item"
            class={cn("group/command-item relative flex cursor-default items-center gap-2 rounded-none px-2 py-2 text-xs outline-hidden select-none in-data-[slot=dialog-content]:rounded-none! data-focused:bg-muted data-focused:text-foreground data-[disabled=true]:pointer-events-none data-[disabled=true]:opacity-50 data-selected:bg-muted data-selected:text-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 data-focused:*:[svg]:text-foreground data-selected:*:[svg]:text-foreground", className)}
            textValue={textValue or (children if isinstance(children, str) else None)}
        >
            {composeRenderProps(children, lambda children: t'''
                {children}
                <{CheckIcon} class="ml-auto opacity-0 group-has-data-[slot=command-shortcut]/command-item:hidden group-data-[checked=true]/command-item:opacity-100" />
            ''')}
        </{MenuItem}>
    """


def CommandShortcut(className=None, **props):
    return t"""
        <span
            data-slot="command-shortcut"
            class={cn("ml-auto text-xs tracking-widest text-muted-foreground group-data-focused/command-item:text-foreground group-data-selected/command-item:text-foreground", className)}
            ...{props}
        />
    """
