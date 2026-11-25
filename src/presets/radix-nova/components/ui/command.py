from utils import cn
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle
from input_group import InputGroup, InputGroupAddon

__js__ = {"cmdk": ["Command as CommandPrimitive"], "lucide-react": ["SearchIcon", "CheckIcon"]}


def Command(className=None, **props):
    return t"""
        <{CommandPrimitive}
            data-slot="command"
            class={cn("flex size-full flex-col overflow-hidden rounded-xl! bg-popover p-1 text-popover-foreground", className)}
            ...{props}
        />
    """


def CommandDialog(title="Command Palette", description="Search for a command to run...", children=None, className=None, showCloseButton=False, **props):
    return t"""
        <{Dialog} ...{props}>
            <{DialogHeader} class="sr-only">
                <{DialogTitle}>{title}</{DialogTitle}>
                <{DialogDescription}>{description}</{DialogDescription}>
            </{DialogHeader}>
            <{DialogContent}
                class={cn("top-1/3 translate-y-0 overflow-hidden rounded-xl! p-0", className)}
                showCloseButton={showCloseButton}
            >
                {children}
            </{DialogContent}>
        </{Dialog}>
    """


def CommandInput(className=None, **props):
    return t"""
        <div data-slot="command-input-wrapper" class="p-1 pb-0">
            <{InputGroup} class="h-8! rounded-lg! border-input/30 bg-input/30 shadow-none! *:data-[slot=input-group-addon]:pl-2!">
                <{CommandPrimitive.Input}
                    data-slot="command-input"
                    class={cn("w-full text-sm outline-hidden disabled:cursor-not-allowed disabled:opacity-50", className)}
                    ...{props}
                />
                <{InputGroupAddon}>
                    <{SearchIcon} class="size-4 shrink-0 opacity-50" />
                </{InputGroupAddon}>
            </{InputGroup}>
        </div>
    """


def CommandList(className=None, **props):
    return t"""
        <{CommandPrimitive.List}
            data-slot="command-list"
            class={cn("no-scrollbar max-h-72 scroll-py-1 overflow-x-hidden overflow-y-auto outline-none", className)}
            ...{props}
        />
    """


def CommandEmpty(className=None, **props):
    return t"""
        <{CommandPrimitive.Empty}
            data-slot="command-empty"
            class={cn("py-6 text-center text-sm", className)}
            ...{props}
        />
    """


def CommandGroup(className=None, **props):
    return t"""
        <{CommandPrimitive.Group}
            data-slot="command-group"
            class={cn("overflow-hidden p-1 text-foreground **:[[cmdk-group-heading]]:px-2 **:[[cmdk-group-heading]]:py-1.5 **:[[cmdk-group-heading]]:text-xs **:[[cmdk-group-heading]]:font-medium **:[[cmdk-group-heading]]:text-muted-foreground", className)}
            ...{props}
        />
    """


def CommandSeparator(className=None, **props):
    return t"""
        <{CommandPrimitive.Separator}
            data-slot="command-separator"
            class={cn("-mx-1 h-px bg-border", className)}
            ...{props}
        />
    """


def CommandItem(className=None, children=None, **props):
    return t"""
        <{CommandPrimitive.Item}
            data-slot="command-item"
            class={cn("group/command-item relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none in-data-[slot=dialog-content]:rounded-lg! data-[disabled=true]:pointer-events-none data-[disabled=true]:opacity-50 data-selected:bg-muted data-selected:text-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 data-selected:*:[svg]:text-foreground", className)}
            ...{props}
        >
            {children}
            <{CheckIcon} class="ml-auto opacity-0 group-has-data-[slot=command-shortcut]/command-item:hidden group-data-[checked=true]/command-item:opacity-100" />
        </{CommandPrimitive.Item}>
    """


def CommandShortcut(className=None, **props):
    return t"""
        <span
            data-slot="command-shortcut"
            class={cn("ml-auto text-xs tracking-widest text-muted-foreground group-data-selected/command-item:text-foreground", className)}
            ...{props}
        />
    """
