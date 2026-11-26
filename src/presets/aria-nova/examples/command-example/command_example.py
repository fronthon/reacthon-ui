from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from card import Card, CardContent
from command import (
    Command,
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
    CommandSeparator,
    CommandShortcut,
)

__js__ = {
    "lucide-react": [
        "CalendarIcon",
        "SmileIcon",
        "CalculatorIcon",
        "UserIcon",
        "CreditCardIcon",
        "SettingsIcon",
        "HomeIcon",
        "InboxIcon",
        "FileTextIcon",
        "FolderIcon",
        "PlusIcon",
        "FolderPlusIcon",
        "CopyIcon",
        "ScissorsIcon",
        "ClipboardPasteIcon",
        "TrashIcon",
        "LayoutGridIcon",
        "ListIcon",
        "ZoomInIcon",
        "ZoomOutIcon",
        "BellIcon",
        "HelpCircleIcon",
        "ImageIcon",
        "CodeIcon",
    ],
}


def CommandExample():
    return t"""
        <{ExampleWrapper}>
            <{CommandInline} />
            <{CommandBasic} />
            <{CommandWithShortcuts} />
            <{CommandWithGroups} />
            <{CommandManyItems} />
        </{ExampleWrapper}>
    """


def CommandInline():
    return t"""
        <{Example} title="Inline">
            <{Card} class="w-full p-0">
                <{CardContent} class="p-0">
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList} renderEmptyState={(lambda: t'<{CommandEmpty}>No results found.</{CommandEmpty}>')}>
                            <{CommandGroup} heading="Suggestions">
                                <{CommandItem} textValue="Calendar">
                                    <{CalendarIcon} />
                                    <span>Calendar</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Search Emoji">
                                    <{SmileIcon} />
                                    <span>Search Emoji</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Calculator">
                                    <{CalculatorIcon} />
                                    <span>Calculator</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Settings">
                                <{CommandItem} textValue="Profile">
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Billing">
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Settings">
                                    <{SettingsIcon} />
                                    <span>Settings</span>
                                    <{CommandShortcut}>⌘S</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                        </{CommandList}>
                    </{Command}>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CommandBasic():
    open_, set_open = use_state(False)

    return t"""
        <{Example} title="Basic">
            <div class="flex flex-col gap-4">
                <{Button} onPress={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList} renderEmptyState={(lambda: t'<{CommandEmpty}>No results found.</{CommandEmpty}>')}>
                            <{CommandGroup} heading="Suggestions">
                                <{CommandItem}>Calendar</{CommandItem}>
                                <{CommandItem}>Search Emoji</{CommandItem}>
                                <{CommandItem}>Calculator</{CommandItem}>
                            </{CommandGroup}>
                        </{CommandList}>
                    </{Command}>
                </{CommandDialog}>
            </div>
        </{Example}>
    """


def CommandWithShortcuts():
    open_, set_open = use_state(False)

    return t"""
        <{Example} title="With Shortcuts">
            <div class="flex flex-col gap-4">
                <{Button} onPress={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList} renderEmptyState={(lambda: t'<{CommandEmpty}>No results found.</{CommandEmpty}>')}>
                            <{CommandGroup} heading="Settings">
                                <{CommandItem} textValue="Profile">
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Billing">
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Settings">
                                    <{SettingsIcon} />
                                    <span>Settings</span>
                                    <{CommandShortcut}>⌘S</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                        </{CommandList}>
                    </{Command}>
                </{CommandDialog}>
            </div>
        </{Example}>
    """


def CommandWithGroups():
    open_, set_open = use_state(False)

    return t"""
        <{Example} title="With Groups">
            <div class="flex flex-col gap-4">
                <{Button} onPress={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList} renderEmptyState={(lambda: t'<{CommandEmpty}>No results found.</{CommandEmpty}>')}>
                            <{CommandGroup} heading="Suggestions">
                                <{CommandItem} textValue="Calendar">
                                    <{CalendarIcon} />
                                    <span>Calendar</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Search Emoji">
                                    <{SmileIcon} />
                                    <span>Search Emoji</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Calculator">
                                    <{CalculatorIcon} />
                                    <span>Calculator</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Settings">
                                <{CommandItem} textValue="Profile">
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Billing">
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Settings">
                                    <{SettingsIcon} />
                                    <span>Settings</span>
                                    <{CommandShortcut}>⌘S</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                        </{CommandList}>
                    </{Command}>
                </{CommandDialog}>
            </div>
        </{Example}>
    """


def CommandManyItems():
    open_, set_open = use_state(False)

    return t"""
        <{Example} title="Many Groups & Items">
            <div class="flex flex-col gap-4">
                <{Button} onPress={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList} renderEmptyState={(lambda: t'<{CommandEmpty}>No results found.</{CommandEmpty}>')}>
                            <{CommandGroup} heading="Navigation">
                                <{CommandItem} textValue="Home">
                                    <{HomeIcon} />
                                    <span>Home</span>
                                    <{CommandShortcut}>⌘H</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Inbox">
                                    <{InboxIcon} />
                                    <span>Inbox</span>
                                    <{CommandShortcut}>⌘I</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Documents">
                                    <{FileTextIcon} />
                                    <span>Documents</span>
                                    <{CommandShortcut}>⌘D</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Folders">
                                    <{FolderIcon} />
                                    <span>Folders</span>
                                    <{CommandShortcut}>⌘F</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Actions">
                                <{CommandItem} textValue="New File">
                                    <{PlusIcon} />
                                    <span>New File</span>
                                    <{CommandShortcut}>⌘N</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="New Folder">
                                    <{FolderPlusIcon} />
                                    <span>New Folder</span>
                                    <{CommandShortcut}>⇧⌘N</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Copy">
                                    <{CopyIcon} />
                                    <span>Copy</span>
                                    <{CommandShortcut}>⌘C</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Cut">
                                    <{ScissorsIcon} />
                                    <span>Cut</span>
                                    <{CommandShortcut}>⌘X</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Paste">
                                    <{ClipboardPasteIcon} />
                                    <span>Paste</span>
                                    <{CommandShortcut}>⌘V</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Delete">
                                    <{TrashIcon} />
                                    <span>Delete</span>
                                    <{CommandShortcut}>⌫</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="View">
                                <{CommandItem} textValue="Grid View">
                                    <{LayoutGridIcon} />
                                    <span>Grid View</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="List View">
                                    <{ListIcon} />
                                    <span>List View</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Zoom In">
                                    <{ZoomInIcon} />
                                    <span>Zoom In</span>
                                    <{CommandShortcut}>⌘+</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Zoom Out">
                                    <{ZoomOutIcon} />
                                    <span>Zoom Out</span>
                                    <{CommandShortcut}>⌘-</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Account">
                                <{CommandItem} textValue="Profile">
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Billing">
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Settings">
                                    <{SettingsIcon} />
                                    <span>Settings</span>
                                    <{CommandShortcut}>⌘S</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem} textValue="Notifications">
                                    <{BellIcon} />
                                    <span>Notifications</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Help & Support">
                                    <{HelpCircleIcon} />
                                    <span>Help & Support</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Tools">
                                <{CommandItem} textValue="Calculator">
                                    <{CalculatorIcon} />
                                    <span>Calculator</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Calendar">
                                    <{CalendarIcon} />
                                    <span>Calendar</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Image Editor">
                                    <{ImageIcon} />
                                    <span>Image Editor</span>
                                </{CommandItem}>
                                <{CommandItem} textValue="Code Editor">
                                    <{CodeIcon} />
                                    <span>Code Editor</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                        </{CommandList}>
                    </{Command}>
                </{CommandDialog}>
            </div>
        </{Example}>
    """
