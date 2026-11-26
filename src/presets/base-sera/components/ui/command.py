from utils import cn
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle
from input_group import InputGroup, InputGroupAddon

__js__ = {"cmdk": ["Command as CommandPrimitive"], "lucide-react": ["SearchIcon", "CheckIcon"]}


def Command(className=None, **props):
    return t"""
        <{CommandPrimitive}
            data-slot="command"
            class={cn("flex size-full flex-col overflow-hidden bg-popover text-popover-foreground", className)}
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
                class={cn("top-1/3 translate-y-0 overflow-hidden p-0", className)}
                showCloseButton={showCloseButton}
            >
                {children}
            </{DialogContent}>
        </{Dialog}>
    """


def CommandInput(className=None, **props):
    return t"""
        <div data-slot="command-input-wrapper" class="p-1">
            <{InputGroup} class="border-transparent border-b-input bg-transparent px-3">
                <{CommandPrimitive.Input}
                    data-slot="command-input"
                    class={cn("w-full px-2 text-sm outline-hidden disabled:cursor-not-allowed disabled:opacity-50", className)}
                    ...{props}
                />
                <{InputGroupAddon}>
                    <{SearchIcon} class="size-3.5 shrink-0 opacity-50" />
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
            class={cn("overflow-hidden p-1.5 text-foreground **:[[cmdk-group-heading]]:px-3 **:[[cmdk-group-heading]]:py-2 **:[[cmdk-group-heading]]:text-xs **:[[cmdk-group-heading]]:font-semibold **:[[cmdk-group-heading]]:tracking-wider **:[[cmdk-group-heading]]:text-muted-foreground **:[[cmdk-group-heading]]:uppercase", className)}
            ...{props}
        />
    """


def CommandSeparator(className=None, **props):
    return t"""
        <{CommandPrimitive.Separator}
            data-slot="command-separator"
            class={cn("-mx-1.5 my-1.5 h-px bg-border/50", className)}
            ...{props}
        />
    """


def CommandItem(className=None, children=None, **props):
    return t"""
        <{CommandPrimitive.Item}
            data-slot="command-item"
            class={cn("group/command-item relative flex cursor-default items-center gap-2 rounded-none px-3 py-2 text-sm outline-hidden select-none in-data-[slot=dialog-content]:rounded-none data-[disabled=true]:pointer-events-none data-[disabled=true]:opacity-50 data-selected:bg-muted data-selected:text-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5 data-selected:*:[svg]:text-foreground", className)}
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
