from browser import window
from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from context_menu import (
    ContextMenu,
    ContextMenuGroup,
    ContextMenuItem,
    ContextMenuLabel,
    ContextMenuSeparator,
    ContextMenuShortcut,
    ContextMenuSub,
    ContextMenuSubContent,
    ContextMenuSubTrigger,
    ContextMenuTrigger,
)
from dialog import Dialog, DialogDescription, DialogHeader, DialogTitle, DialogTrigger

__js__ = {
    "react-aria-components": ["Pressable"],
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
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>Back</{ContextMenuItem}>
                        <{ContextMenuItem} isDisabled>Forward</{ContextMenuItem}>
                        <{ContextMenuItem}>Reload</{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
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
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithShortcuts():
    return t"""
        <{Example} title="With Shortcuts">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
                    <{ContextMenuGroup}>
                        <{ContextMenuItem}>
                            Back
                            <{ContextMenuShortcut}>⌘[</{ContextMenuShortcut}>
                        </{ContextMenuItem}>
                        <{ContextMenuItem} isDisabled>
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
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithSubmenu():
    return t"""
        <{Example} title="With Submenu">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
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
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithGroups():
    return t"""
        <{Example} title="With Groups, Labels & Separators">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
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
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithCheckboxes():
    selected_keys, set_selected_keys = use_state(window.Set.new(["bookmarks-bar", "developer-tools"]))

    return t"""
        <{Example} title="With Checkboxes">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
                    <{ContextMenuGroup}
                        selectionMode="multiple"
                        selectedKeys={selected_keys}
                        onSelectionChange={set_selected_keys}
                    >
                        <{ContextMenuItem} id="bookmarks-bar">Show Bookmarks Bar</{ContextMenuItem}>
                        <{ContextMenuItem}>Show Full URLs</{ContextMenuItem}>
                        <{ContextMenuItem} id="developer-tools">Show Developer Tools</{ContextMenuItem}>
                    </{ContextMenuGroup}>
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithRadio():
    user, set_user = use_state("pedro")
    theme, set_theme = use_state("light")

    def on_selection_change(keys):
        return set_user("pedro" if keys == "all" else keys.values().next().value)

    def on_selection_change_2(keys):
        return set_theme("light" if keys == "all" else keys.values().next().value)

    return t"""
        <{Example} title="With Radio Group">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>People</{ContextMenuLabel}>
                        <{ContextMenuGroup}
                            selectionMode="single"
                            selectedKeys={[user]}
                            onSelectionChange={on_selection_change}
                        >
                            <{ContextMenuItem} id="pedro">Pedro Duarte</{ContextMenuItem}>
                            <{ContextMenuItem} id="colm">Colm Tuite</{ContextMenuItem}>
                        </{ContextMenuGroup}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}>
                        <{ContextMenuLabel}>Theme</{ContextMenuLabel}>
                        <{ContextMenuGroup}
                            selectionMode="single"
                            selectedKeys={theme}
                            onSelectionChange={on_selection_change_2}
                        >
                            <{ContextMenuItem} id="light">Light</{ContextMenuItem}>
                            <{ContextMenuItem} id="dark">Dark</{ContextMenuItem}>
                            <{ContextMenuItem} id="system">System</{ContextMenuItem}>
                        </{ContextMenuGroup}>
                    </{ContextMenuGroup}>
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithDestructive():
    return t"""
        <{Example} title="With Destructive Items">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu}>
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
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """


def ContextMenuWithSides():
    return t"""
        <{Example} title="With Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap justify-center gap-2">
                {[t'''
                    <{ContextMenuTrigger} key={item["placement"]}>
                        <{Pressable}>
                            <div
                                role="button"
                                class="flex aspect-[2/0.5] items-center justify-center rounded-lg border p-4 text-sm capitalize"
                            >
                                {item["label"]}
                            </div>
                        </{Pressable}>
                        <{ContextMenu} placement={item["placement"]}>
                            <{ContextMenuGroup}>
                                <{ContextMenuItem}>Back</{ContextMenuItem}>
                                <{ContextMenuItem}>Forward</{ContextMenuItem}>
                                <{ContextMenuItem}>Reload</{ContextMenuItem}>
                            </{ContextMenuGroup}>
                        </{ContextMenu}>
                    </{ContextMenuTrigger}>
                ''' for item in [{"label": "start", "placement": "start top"}, {"label": "left", "placement": "left top"}, {"label": "top", "placement": "top start"}, {"label": "bottom", "placement": "bottom start"}, {"label": "right", "placement": "right top"}, {"label": "end", "placement": "end top"}]]}
            </div>
        </{Example}>
    """


def ContextMenuInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{DialogTrigger}>
                <{Button} variant="outline">Open Dialog</{Button}>
                <{Dialog}>
                    <{DialogHeader}>
                        <{DialogTitle}>Context Menu Example</{DialogTitle}>
                        <{DialogDescription}>
                            Right click on the area below to see the context menu.
                        </{DialogDescription}>
                    </{DialogHeader}>
                    <{ContextMenuTrigger}>
                        <{Pressable}>
                            <div
                                role="button"
                                class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                            >
                                Right click here
                            </div>
                        </{Pressable}>
                        <{ContextMenu}>
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
                        </{ContextMenu}>
                    </{ContextMenuTrigger}>
                </{Dialog}>
            </{DialogTrigger}>
        </{Example}>
    """


def ContextMenuWithInset():
    selected_keys, set_selected_keys = use_state(window.Set.new(["bookmarks"]))
    theme, set_theme = use_state("system")

    def on_selection_change(keys):
        return set_theme("system" if keys == "all" else keys.values().next().value)

    return t"""
        <{Example} title="With Inset">
            <{ContextMenuTrigger}>
                <{Pressable}>
                    <div
                        role="button"
                        class="flex aspect-[2/0.5] w-full items-center justify-center rounded-lg border text-sm"
                    >
                        Right click here
                    </div>
                </{Pressable}>
                <{ContextMenu} class="w-44">
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
                    <{ContextMenuGroup}
                        selectionMode="multiple"
                        selectedKeys={selected_keys}
                        onSelectionChange={set_selected_keys}
                    >
                        <{ContextMenuLabel} inset>Appearance</{ContextMenuLabel}>
                        <{ContextMenuItem} inset id="bookmarks">Bookmarks</{ContextMenuItem}>
                        <{ContextMenuItem} inset id="urls">Full URLs</{ContextMenuItem}>
                    </{ContextMenuGroup}>
                    <{ContextMenuSeparator} />
                    <{ContextMenuGroup}
                        selectionMode="single"
                        selectedKeys={[theme]}
                        onSelectionChange={on_selection_change}
                    >
                        <{ContextMenuLabel} inset>Theme</{ContextMenuLabel}>
                        <{ContextMenuItem} inset id="light">Light</{ContextMenuItem}>
                        <{ContextMenuItem} inset id="dark">Dark</{ContextMenuItem}>
                        <{ContextMenuItem} inset id="system">System</{ContextMenuItem}>
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
                </{ContextMenu}>
            </{ContextMenuTrigger}>
        </{Example}>
    """
