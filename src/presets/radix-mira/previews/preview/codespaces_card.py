from browser import window
from reacthon import use_state
from button import Button
from card import Card, CardContent
from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle
from field import Field, FieldDescription, FieldLabel
from input_group import InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput
from item import Item, ItemActions, ItemContent, ItemDescription, ItemTitle
from separator import Separator
from spinner import Spinner
from tabs import Tabs, TabsContent, TabsList, TabsTrigger
from tooltip import Tooltip, TooltipContent, TooltipTrigger

__js__ = {
    "lucide-react": [
        "ContainerIcon",
        "CopyIcon",
        "DownloadIcon",
        "InfoIcon",
        "MonitorIcon",
        "MoreHorizontalIcon",
        "PlusIcon",
        "ServerIcon",
        "ShareIcon",
        "TerminalIcon",
        "ZapIcon",
    ],
}


def CodespacesCard():
    is_creating_codespace, set_is_creating_codespace = use_state(False)

    def on_click():
        set_is_creating_codespace(True)

        def callback():
            set_is_creating_codespace(False)

        window.setTimeout(callback, 2000)

    return t"""
        <{Card}>
            <{CardContent}>
                <{Tabs} defaultValue="codespaces">
                    <{TabsList} class="w-full">
                        <{TabsTrigger} value="codespaces">Codespaces</{TabsTrigger}>
                        <{TabsTrigger} value="local">Local</{TabsTrigger}>
                    </{TabsList}>
                    <{TabsContent} value="codespaces">
                        <{Item} size="sm" class="px-1 pt-2">
                            <{ItemContent}>
                                <{ItemTitle}>Codespaces</{ItemTitle}>
                                <{ItemDescription}>Your workspaces in the cloud</{ItemDescription}>
                            </{ItemContent}>
                            <{ItemActions}>
                                <{Tooltip}>
                                    <{TooltipTrigger} asChild>
                                        <{Button} variant="ghost" size="icon-sm">
                                            <{PlusIcon} />
                                        </{Button}>
                                    </{TooltipTrigger}>
                                    <{TooltipContent} side="bottom">Create a codespace on main</{TooltipContent}>
                                </{Tooltip}>
                                <{DropdownMenu}>
                                    <{DropdownMenuTrigger} asChild>
                                        <{Button} variant="ghost" size="icon-sm">
                                            <{MoreHorizontalIcon} />
                                        </{Button}>
                                    </{DropdownMenuTrigger}>
                                    <{DropdownMenuContent} align="end" class="w-56">
                                        <{DropdownMenuGroup}>
                                            <{DropdownMenuItem}>
                                                <{PlusIcon} />
                                                New with options...
                                            </{DropdownMenuItem}>
                                            <{DropdownMenuItem}>
                                                <{ContainerIcon} />
                                                Configure container
                                            </{DropdownMenuItem}>
                                            <{DropdownMenuItem}>
                                                <{ZapIcon} />
                                                Set up prebuilds
                                            </{DropdownMenuItem}>
                                        </{DropdownMenuGroup}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuGroup}>
                                            <{DropdownMenuItem}>
                                                <{ServerIcon} />
                                                Manage codespaces
                                            </{DropdownMenuItem}>
                                            <{DropdownMenuItem}>
                                                <{ShareIcon} />
                                                Share deep link
                                            </{DropdownMenuItem}>
                                            <{DropdownMenuItem}>
                                                <{InfoIcon} />
                                                What are codespaces?
                                            </{DropdownMenuItem}>
                                        </{DropdownMenuGroup}>
                                    </{DropdownMenuContent}>
                                </{DropdownMenu}>
                            </{ItemActions}>
                        </{Item}>
                        <{Separator} class="-mx-2 my-2 w-auto!" />
                        <{Empty} class="p-4">
                            <{EmptyHeader}>
                                <{EmptyMedia} variant="icon">
                                    <{ServerIcon} />
                                </{EmptyMedia}>
                                <{EmptyTitle}>No codespaces</{EmptyTitle}>
                                <{EmptyDescription}>
                                    You don't have any codespaces with this repository checked out
                                </{EmptyDescription}>
                            </{EmptyHeader}>
                            <{EmptyContent}>
                                <{Button} size="sm" onClick={on_click} disabled={is_creating_codespace}>
                                    {t'<{Spinner} data-icon="inline-start" />' if is_creating_codespace else ""}
                                    Create Codespace
                                </{Button}>
                                <a href="#learn-more" class="text-xs text-muted-foreground underline underline-offset-4">
                                    Learn more about codespaces
                                </a>
                            </{EmptyContent}>
                        </{Empty}>
                        <{Separator} class="-mx-2 my-2 w-auto!" />
                        <div class="p-1.5 text-xs text-muted-foreground">
                            Codespace usage for this repository is paid for by{" "}
                            <span class="font-medium">shadcn</span>.
                        </div>
                    </{TabsContent}>
                    <{TabsContent} value="local">
                        <{Item} size="sm" class="hidden p-0">
                            <{ItemContent}>
                                <{ItemTitle} class="gap-2">
                                    <{TerminalIcon} class="size-4" />
                                    Clone
                                </{ItemTitle}>
                            </{ItemContent}>
                            <{ItemActions}>
                                <{Tooltip}>
                                    <{TooltipTrigger} asChild>
                                        <{Button} variant="ghost" size="icon">
                                            <{InfoIcon} />
                                        </{Button}>
                                    </{TooltipTrigger}>
                                    <{TooltipContent} side="left">Which remote URL should I use?</{TooltipContent}>
                                </{Tooltip}>
                            </{ItemActions}>
                        </{Item}>
                        <{Tabs} defaultValue="https">
                            <{TabsList} variant="line" class="w-full justify-start border-b *:[button]:flex-0">
                                <{TabsTrigger} value="https">HTTPS</{TabsTrigger}>
                                <{TabsTrigger} value="ssh">SSH</{TabsTrigger}>
                                <{TabsTrigger} value="cli">GitHub CLI</{TabsTrigger}>
                            </{TabsList}>
                            <div class="rounded-md border bg-muted/30 p-2">
                                <{TabsContent} value="https">
                                    <{Field} class="gap-2">
                                        <{FieldLabel} for="https-url" class="sr-only">HTTPS URL</{FieldLabel}>
                                        <{InputGroup}>
                                            <{InputGroupAddon} align="inline-end">
                                                <{InputGroupButton} variant="ghost" size="icon-xs">
                                                    <{CopyIcon} />
                                                </{InputGroupButton}>
                                            </{InputGroupAddon}>
                                            <{InputGroupInput}
                                                id="https-url"
                                                defaultValue="https://github.com/shadcn-ui/ui.git"
                                                readOnly
                                            />
                                        </{InputGroup}>
                                        <{FieldDescription}>Clone using the web URL.</{FieldDescription}>
                                    </{Field}>
                                </{TabsContent}>
                                <{TabsContent} value="ssh">
                                    <{Field} class="gap-2">
                                        <{FieldLabel} for="ssh-url" class="sr-only">SSH URL</{FieldLabel}>
                                        <{InputGroup}>
                                            <{InputGroupAddon} align="inline-end">
                                                <{InputGroupButton} variant="ghost" size="icon-xs">
                                                    <{CopyIcon} />
                                                </{InputGroupButton}>
                                            </{InputGroupAddon}>
                                            <{InputGroupInput}
                                                id="ssh-url"
                                                defaultValue="git@github.com:shadcn-ui/ui.git"
                                                readOnly
                                            />
                                        </{InputGroup}>
                                        <{FieldDescription}>Use a password-protected SSH key.</{FieldDescription}>
                                    </{Field}>
                                </{TabsContent}>
                                <{TabsContent} value="cli">
                                    <{Field} class="gap-2">
                                        <{FieldLabel} for="cli-command" class="sr-only">CLI Command</{FieldLabel}>
                                        <{InputGroup}>
                                            <{InputGroupAddon} align="inline-end">
                                                <{InputGroupButton} variant="ghost" size="icon-xs">
                                                    <{CopyIcon} />
                                                </{InputGroupButton}>
                                            </{InputGroupAddon}>
                                            <{InputGroupInput}
                                                id="cli-command"
                                                defaultValue="gh repo clone shadcn-ui/ui"
                                                readOnly
                                            />
                                        </{InputGroup}>
                                        <{FieldDescription}>
                                            Work fast with our official CLI.{" "}
                                            <a href="#learn-more">Learn more</a>
                                        </{FieldDescription}>
                                    </{Field}>
                                </{TabsContent}>
                            </div>
                        </{Tabs}>
                        <{Separator} class="-mx-2 my-2 w-auto!" />
                        <div class="flex flex-col">
                            <{Button} variant="ghost" size="sm" class="justify-start gap-1.5">
                                <{MonitorIcon} data-icon="inline-start" />
                                Open with GitHub Desktop
                            </{Button}>
                            <{Button} variant="ghost" size="sm" class="justify-start gap-1.5">
                                <{DownloadIcon} data-icon="inline-start" />
                                Download ZIP
                            </{Button}>
                        </div>
                    </{TabsContent}>
                </{Tabs}>
            </{CardContent}>
        </{Card}>
    """
