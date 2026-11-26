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
                        <{CommandList}>
                            <{CommandEmpty}>No results found.</{CommandEmpty}>
                            <{CommandGroup} heading="Suggestions">
                                <{CommandItem}>
                                    <{CalendarIcon} />
                                    <span>Calendar</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{SmileIcon} />
                                    <span>Search Emoji</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CalculatorIcon} />
                                    <span>Calculator</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Settings">
                                <{CommandItem}>
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
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
                <{Button} onClick={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList}>
                            <{CommandEmpty}>No results found.</{CommandEmpty}>
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
                <{Button} onClick={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList}>
                            <{CommandEmpty}>No results found.</{CommandEmpty}>
                            <{CommandGroup} heading="Settings">
                                <{CommandItem}>
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
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
                <{Button} onClick={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList}>
                            <{CommandEmpty}>No results found.</{CommandEmpty}>
                            <{CommandGroup} heading="Suggestions">
                                <{CommandItem}>
                                    <{CalendarIcon} />
                                    <span>Calendar</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{SmileIcon} />
                                    <span>Search Emoji</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CalculatorIcon} />
                                    <span>Calculator</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Settings">
                                <{CommandItem}>
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
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
                <{Button} onClick={(lambda: set_open(True))} variant="outline" class="w-fit">Open Menu</{Button}>
                <{CommandDialog} open={open_} onOpenChange={set_open}>
                    <{Command}>
                        <{CommandInput} placeholder="Type a command or search..." />
                        <{CommandList}>
                            <{CommandEmpty}>No results found.</{CommandEmpty}>
                            <{CommandGroup} heading="Navigation">
                                <{CommandItem}>
                                    <{HomeIcon} />
                                    <span>Home</span>
                                    <{CommandShortcut}>⌘H</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{InboxIcon} />
                                    <span>Inbox</span>
                                    <{CommandShortcut}>⌘I</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{FileTextIcon} />
                                    <span>Documents</span>
                                    <{CommandShortcut}>⌘D</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{FolderIcon} />
                                    <span>Folders</span>
                                    <{CommandShortcut}>⌘F</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Actions">
                                <{CommandItem}>
                                    <{PlusIcon} />
                                    <span>New File</span>
                                    <{CommandShortcut}>⌘N</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{FolderPlusIcon} />
                                    <span>New Folder</span>
                                    <{CommandShortcut}>⇧⌘N</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CopyIcon} />
                                    <span>Copy</span>
                                    <{CommandShortcut}>⌘C</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{ScissorsIcon} />
                                    <span>Cut</span>
                                    <{CommandShortcut}>⌘X</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{ClipboardPasteIcon} />
                                    <span>Paste</span>
                                    <{CommandShortcut}>⌘V</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{TrashIcon} />
                                    <span>Delete</span>
                                    <{CommandShortcut}>⌫</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="View">
                                <{CommandItem}>
                                    <{LayoutGridIcon} />
                                    <span>Grid View</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{ListIcon} />
                                    <span>List View</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{ZoomInIcon} />
                                    <span>Zoom In</span>
                                    <{CommandShortcut}>⌘+</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{ZoomOutIcon} />
                                    <span>Zoom Out</span>
                                    <{CommandShortcut}>⌘-</{CommandShortcut}>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Account">
                                <{CommandItem}>
                                    <{UserIcon} />
                                    <span>Profile</span>
                                    <{CommandShortcut}>⌘P</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CreditCardIcon} />
                                    <span>Billing</span>
                                    <{CommandShortcut}>⌘B</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{SettingsIcon} />
                                    <span>Settings</span>
                                    <{CommandShortcut}>⌘S</{CommandShortcut}>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{BellIcon} />
                                    <span>Notifications</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{HelpCircleIcon} />
                                    <span>Help & Support</span>
                                </{CommandItem}>
                            </{CommandGroup}>
                            <{CommandSeparator} />
                            <{CommandGroup} heading="Tools">
                                <{CommandItem}>
                                    <{CalculatorIcon} />
                                    <span>Calculator</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{CalendarIcon} />
                                    <span>Calendar</span>
                                </{CommandItem}>
                                <{CommandItem}>
                                    <{ImageIcon} />
                                    <span>Image Editor</span>
                                </{CommandItem}>
                                <{CommandItem}>
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
