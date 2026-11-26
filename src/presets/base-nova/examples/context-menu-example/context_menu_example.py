from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from context_menu import (
    ContextMenu,
    ContextMenuCheckboxItem,
    ContextMenuContent,
    ContextMenuGroup,
    ContextMenuItem,
    ContextMenuLabel,
    ContextMenuRadioGroup,
    ContextMenuRadioItem,
    ContextMenuSeparator,
    ContextMenuShortcut,
    ContextMenuSub,
    ContextMenuSubContent,
    ContextMenuSubTrigger,
    ContextMenuTrigger,
)
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger

__js__ = {
    "lucide-react": [
        "CopyIcon",
        "ScissorsIcon",
        "ClipboardPasteIcon",
        "TrashIcon",
        "PencilIcon",
        "ShareIcon",
        "ArchiveIcon",
    ],
}


def ContextMenuExample():
    return t"""
        <{ExampleWrapper}>
            <{ContextMenuBasic} />
            <{ContextMenuWithIcons} />
            <{ContextMenuWithSides} />
            <{ContextMenuWithShortcuts} />
            <{ContextMenuWithSubmenu} />
            <{ContextMenuWithGroups} />
            <{ContextMenuWithCheckboxes} />
            <{ContextMenuWithRadio} />
            <{ContextMenuWithDestructive} />
            <{ContextMenuInDialog} />
            <{ContextMenuWithInset} />
        </{ExampleWrapper}>
    """


def ContextMenuBasic():
    return t"""
        <{Example} title="Basic">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>Back</{ContextMenuItem}>
                        <{ContextMenuItem} disabled>Forward</{ContextMenuItem}>
                        <{ContextMenuItem}>Reload</{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            <{CopyIcon} />
                            Copy
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            <{ScissorsIcon} />
                            Cut
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            <{ClipboardPasteIcon} />
                            Paste
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuItem} variant="destructive">
                            <{TrashIcon} />
                            Delete
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithShortcuts():
    return t"""
        <{Example} title="With Shortcuts">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            Back
                            <{ContextMenuShortcut}>⌘[</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem} disabled>
                            Forward
                            <{ContextMenuShortcut}>⌘]</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Reload
                            <{ContextMenuShortcut}>⌘R</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            Save
                            <{ContextMenuShortcut}>⌘S</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Save As...
                            <{ContextMenuShortcut}>⇧⌘S</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithSubmenu():
    return t"""
        <{Example} title="With Submenu">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            Copy
                            <{ContextMenuShortcut}>⌘C</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Cut
                            <{ContextMenuShortcut}>⌘X</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSub}>
                        <{ContextMenuSubTrigger}>More Tools</{ContextMenuSubTrigger}>
                        <{ContextMenuSubContent}>
                            <{ContextMenuGroup}>
                                <{ContextMenuItem}>Save Page...</{ContextMenuItem}>
                                <{ContextMenuItem}>Create Shortcut...</{ContextMenuItem}>
                                <{ContextMenuItem}>Name Window...</{ContextMenuItem}>
                            </{ContextMenuGroup}>
                            <{ContextMenuSeparator} />
                            <{ContextMenuGroup}>
                                <{ContextMenuItem}>Developer Tools</{ContextMenuItem}>
                            </{ContextMenuGroup}>
                            <{ContextMenuSeparator} />
                            <{ContextMenuGroup}>
                                <{ContextMenuItem} variant="destructive">Delete</{ContextMenuItem}>
                            </{ContextMenuGroup}>
                        </{ContextMenuSubContent}>
                    </{ContextMenuSub}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithGroups():
    return t"""
        <{Example} title="With Groups, Labels & Separators">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>File</{ContextMenuLabel}>
                        <{ContextMenuItem}>
                            New File
                            <{ContextMenuShortcut}>⌘N</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Open File
                            <{ContextMenuShortcut}>⌘O</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Save
                            <{ContextMenuShortcut}>⌘S</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>Edit</{ContextMenuLabel}>
                        <{ContextMenuItem}>
                            Undo
                            <{ContextMenuShortcut}>⌘Z</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Redo
                            <{ContextMenuShortcut}>⇧⌘Z</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            Cut
                            <{ContextMenuShortcut}>⌘X</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Copy
                            <{ContextMenuShortcut}>⌘C</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            Paste
                            <{ContextMenuShortcut}>⌘V</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuItem} variant="destructive">
                            Delete
                            <{ContextMenuShortcut}>⌫</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithCheckboxes():
    return t"""
        <{Example} title="With Checkboxes">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuCheckboxItem} defaultChecked>Show Bookmarks Bar</{ContextMenuCheckboxItem}>
                        <{ContextMenuCheckboxItem}>Show Full URLs</{ContextMenuCheckboxItem}>
                        <{ContextMenuCheckboxItem} defaultChecked>Show Developer Tools</{ContextMenuCheckboxItem}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithRadio():
    user, set_user = use_state("pedro")
    theme, set_theme = use_state("light")

    return t"""
        <{Example} title="With Radio Group">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>People</{ContextMenuLabel}>
                        <{ContextMenuRadioGroup} value={user} onValueChange={set_user}>
                            <{ContextMenuRadioItem} value="pedro">Pedro Duarte</{ContextMenuRadioItem}>
                            <{ContextMenuRadioItem} value="colm">Colm Tuite</{ContextMenuRadioItem}>
                        </{ContextMenuRadioGroup}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>Theme</{ContextMenuLabel}>
                        <{ContextMenuRadioGroup} value={theme} onValueChange={set_theme}>
                            <{ContextMenuRadioItem} value="light">Light</{ContextMenuRadioItem}>
                            <{ContextMenuRadioItem} value="dark">Dark</{ContextMenuRadioItem}>
                            <{ContextMenuRadioItem} value="system">System</{ContextMenuRadioItem}>
                        </{ContextMenuRadioGroup}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithDestructive():
    return t"""
        <{Example} title="With Destructive Items">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            <{PencilIcon} />
                            Edit
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            <{ShareIcon} />
                            Share
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            <{ArchiveIcon} />
                            Archive
                        </{ContextMenuItem}>
                        <{ContextMenuItem} variant="destructive">
                            <{TrashIcon} />
                            Delete
                        </{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """


def ContextMenuWithSides():
    return t"""
        <{Example} title="With Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap justify-center gap-2">
                {[t'''
                    <{ContextMenu} key={side}>
                        <{ContextMenuTrigger} class="flex aspect-[2/0.5] items-center justify-center rounded-lg border p-4 text-sm capitalize">
                            {side.replace("-", " ")}
                        </{ContextMenuTrigger}>
                        <{ContextMenuContent} side={side}>
                            <{ContextMenuGroup}>
                                <{ContextMenuItem}>Back</{ContextMenuItem}>
                                <{ContextMenuItem}>Forward</{ContextMenuItem}>
                                <{ContextMenuItem}>Reload</{ContextMenuItem}>
                            </{ContextMenuGroup}>
                        </{ContextMenuContent}>
                    </{ContextMenu}>
                ''' for side in ["inline-start", "left", "top", "bottom", "right", "inline-end"]]}
            </div>
        </{Example}>
    """


def ContextMenuInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open Dialog</{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Context Menu Example</{DialogTitle}>
                        <{DialogDescription}>
                            Right click on the area below to see the context menu.
                        </{DialogDescription}>
                    </{DialogHeader}>
                    <{ContextMenu}>
                        <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                            Right click here
                        </{ContextMenuTrigger}>
                        <{ContextMenuContent}>
                            <{ContextMenuGroup}>
                                <{ContextMenuItem}>
                                    <{CopyIcon} />
                                    Copy
                                </{ContextMenuItem}>
                                <{ContextMenuItem}>
                                    <{ScissorsIcon} />
                                    Cut
                                </{ContextMenuItem}>
                                <{ContextMenuItem}>
                                    <{ClipboardPasteIcon} />
                                    Paste
                                </{ContextMenuItem}>
                            </{ContextMenuGroup}>
                            <{ContextMenuSeparator} />
                            <{ContextMenuSub}>
                                <{ContextMenuSubTrigger}>More Options</{ContextMenuSubTrigger}>
                                <{ContextMenuSubContent}>
                                    <{ContextMenuGroup}>
                                        <{ContextMenuItem}>Save Page...</{ContextMenuItem}>
                                        <{ContextMenuItem}>Create Shortcut...</{ContextMenuItem}>
                                        <{ContextMenuItem}>Name Window...</{ContextMenuItem}>
                                    </{ContextMenuGroup}>
                                    <{ContextMenuSeparator} />
                                    <{ContextMenuGroup}>
                                        <{ContextMenuItem}>Developer Tools</{ContextMenuItem}>
                                    </{ContextMenuGroup}>
                                </{ContextMenuSubContent}>
                            </{ContextMenuSub}>
                            <{ContextMenuSeparator} />
                            <{ContextMenuGroup}>
                                <{ContextMenuItem} variant="destructive">
                                    <{TrashIcon} />
                                    Delete
                                </{ContextMenuItem}>
                            </{ContextMenuGroup}>
                        </{ContextMenuContent}>
                    </{ContextMenu}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


def ContextMenuWithInset():
    show_bookmarks, set_show_bookmarks = use_state(True)
    show_urls, set_show_urls = use_state(False)
    theme, set_theme = use_state("system")

    return t"""
        <{Example} title="With Inset">
            <{ContextMenu}>
                <{ContextMenuTrigger} class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm">
                    Right click here
                </{ContextMenuTrigger}>
                <{ContextMenuContent} class="w-44">
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>Actions</{ContextMenuLabel}>
                        <{ContextMenuItem}>
                            <{CopyIcon} />
                            Copy
                        </{ContextMenuItem}>
                        <{ContextMenuItem}>
                            <{ScissorsIcon} />
                            Cut
                        </{ContextMenuItem}>
                        <{ContextMenuItem} inset>Paste</{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel} inset>Appearance</{ContextMenuLabel}>
                        <{ContextMenuCheckboxItem} inset checked={show_bookmarks} onCheckedChange={set_show_bookmarks}>
                            Bookmarks
                        </{ContextMenuCheckboxItem}>
                        <{ContextMenuCheckboxItem} inset checked={show_urls} onCheckedChange={set_show_urls}>
                            Full URLs
                        </{ContextMenuCheckboxItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel} inset>Theme</{ContextMenuLabel}>
                        <{ContextMenuRadioGroup} value={theme} onValueChange={set_theme}>
                            <{ContextMenuRadioItem} inset value="light">Light</{ContextMenuRadioItem}>
                            <{ContextMenuRadioItem} inset value="dark">Dark</{ContextMenuRadioItem}>
                            <{ContextMenuRadioItem} inset value="system">System</{ContextMenuRadioItem}>
                        </{ContextMenuRadioGroup}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuSub}>
                        <{ContextMenuSubTrigger} inset>More Options</{ContextMenuSubTrigger}>
                        <{ContextMenuSubContent}>
                            <{ContextMenuGroup}>
                                <{ContextMenuItem}>Save Page...</{ContextMenuItem}>
                                <{ContextMenuItem}>Create Shortcut...</{ContextMenuItem}>
                            </{ContextMenuGroup}>
                        </{ContextMenuSubContent}>
                    </{ContextMenuSub}>
                </{ContextMenuContent}>
            </{ContextMenu}>
        </{Example}>
    """
