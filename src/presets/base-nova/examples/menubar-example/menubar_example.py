from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from menubar import (
    Menubar,
    MenubarCheckboxItem,
    MenubarContent,
    MenubarGroup,
    MenubarItem,
    MenubarLabel,
    MenubarMenu,
    MenubarRadioGroup,
    MenubarRadioItem,
    MenubarSeparator,
    MenubarShortcut,
    MenubarSub,
    MenubarSubContent,
    MenubarSubTrigger,
    MenubarTrigger,
)

__js__ = {
    "lucide-react": [
        "FileIcon",
        "FolderIcon",
        "SaveIcon",
        "CircleDashedIcon",
        "BoldIcon",
        "ItalicIcon",
        "UnderlineIcon",
        "ImageIcon",
        "LinkIcon",
        "TableIcon",
        "SearchIcon",
        "CheckIcon",
        "TrashIcon",
        "UserIcon",
        "SettingsIcon",
        "LogOutIcon",
        "CopyIcon",
        "ScissorsIcon",
        "ClipboardPasteIcon",
    ],
}


def MenubarExample():
    return t"""
        <{ExampleWrapper}>
            <{MenubarBasic} />
            <{MenubarWithSubmenu} />
            <{MenubarSides} />
            <{MenubarWithCheckboxes} />
            <{MenubarWithRadio} />
            <{MenubarWithIcons} />
            <{MenubarWithShortcuts} />
            <{MenubarFormat} />
            <{MenubarInsert} />
            <{MenubarDestructive} />
            <{MenubarInDialog} />
            <{MenubarWithInset} />
        </{ExampleWrapper}>
    """


def MenubarBasic():
    return t"""
        <{Example} title="Basic">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>File</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            New Tab <{MenubarShortcut}>⌘T</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            New Window <{MenubarShortcut}>⌘N</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem} disabled>New Incognito Window</{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>
                            Print... <{MenubarShortcut}>⌘P</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Edit</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            Undo <{MenubarShortcut}>⌘Z</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            Redo <{MenubarShortcut}>⇧⌘Z</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>Cut</{MenubarItem}>
                        <{MenubarItem}>Copy</{MenubarItem}>
                        <{MenubarItem}>Paste</{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarSides():
    return t"""
        <{Example} title="Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap justify-center gap-2">
                {[t'''
                    <{Menubar} key={side}>
                        <{MenubarMenu}>
                            <{MenubarTrigger} class="capitalize">{side.replace("-", " ")}</{MenubarTrigger}>
                            <{MenubarContent} side={side}>
                                <{MenubarGroup}>
                                    <{MenubarItem}>New Tab</{MenubarItem}>
                                    <{MenubarItem}>New Window</{MenubarItem}>
                                    <{MenubarItem}>New Incognito Window</{MenubarItem}>
                                </{MenubarGroup}>
                            </{MenubarContent}>
                        </{MenubarMenu}>
                    </{Menubar}>
                ''' for side in ["inline-start", "left", "top", "bottom", "right", "inline-end"]]}
            </div>
        </{Example}>
    """


def MenubarWithSubmenu():
    return t"""
        <{Example} title="With Submenu">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>File</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarSub}>
                            <{MenubarSubTrigger}>Share</{MenubarSubTrigger}>
                            <{MenubarSubContent}>
                                <{MenubarItem}>Email link</{MenubarItem}>
                                <{MenubarItem}>Messages</{MenubarItem}>
                                <{MenubarItem}>Notes</{MenubarItem}>
                            </{MenubarSubContent}>
                        </{MenubarSub}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>
                            Print... <{MenubarShortcut}>⌘P</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Edit</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            Undo <{MenubarShortcut}>⌘Z</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            Redo <{MenubarShortcut}>⇧⌘Z</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarSub}>
                            <{MenubarSubTrigger}>Find</{MenubarSubTrigger}>
                            <{MenubarSubContent}>
                                <{MenubarItem}>Find...</{MenubarItem}>
                                <{MenubarItem}>Find Next</{MenubarItem}>
                                <{MenubarItem}>Find Previous</{MenubarItem}>
                            </{MenubarSubContent}>
                        </{MenubarSub}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>Cut</{MenubarItem}>
                        <{MenubarItem}>Copy</{MenubarItem}>
                        <{MenubarItem}>Paste</{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarWithCheckboxes():
    return t"""
        <{Example} title="With Checkboxes">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>View</{MenubarTrigger}>
                    <{MenubarContent} class="w-64">
                        <{MenubarCheckboxItem}>Always Show Bookmarks Bar</{MenubarCheckboxItem}>
                        <{MenubarCheckboxItem} checked>Always Show Full URLs</{MenubarCheckboxItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem} inset>
                            Reload <{MenubarShortcut}>⌘R</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem} disabled inset>
                            Force Reload <{MenubarShortcut}>⇧⌘R</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Format</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarCheckboxItem} checked>Strikethrough</{MenubarCheckboxItem}>
                        <{MenubarCheckboxItem}>Code</{MenubarCheckboxItem}>
                        <{MenubarCheckboxItem}>Superscript</{MenubarCheckboxItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarWithRadio():
    user, set_user = use_state("benoit")
    theme, set_theme = use_state("system")

    return t"""
        <{Example} title="With Radio">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Profiles</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarRadioGroup} value={user} onValueChange={set_user}>
                            <{MenubarRadioItem} value="andy">Andy</{MenubarRadioItem}>
                            <{MenubarRadioItem} value="benoit">Benoit</{MenubarRadioItem}>
                            <{MenubarRadioItem} value="luis">Luis</{MenubarRadioItem}>
                        </{MenubarRadioGroup}>
                        <{MenubarSeparator} />
                        <{MenubarItem} inset>Edit...</{MenubarItem}>
                        <{MenubarItem} inset>Add Profile...</{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Theme</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarRadioGroup} value={theme} onValueChange={set_theme}>
                            <{MenubarRadioItem} value="light">Light</{MenubarRadioItem}>
                            <{MenubarRadioItem} value="dark">Dark</{MenubarRadioItem}>
                            <{MenubarRadioItem} value="system">System</{MenubarRadioItem}>
                        </{MenubarRadioGroup}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>File</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            <{FileIcon} />
                            New File <{MenubarShortcut}>⌘N</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{FolderIcon} />
                            Open Folder
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>
                            <{SaveIcon} />
                            Save <{MenubarShortcut}>⌘S</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>More</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarGroup}>
                            <{MenubarItem}>
                                <{CircleDashedIcon} />
                                Settings
                            </{MenubarItem}>
                            <{MenubarItem}>
                                <{CircleDashedIcon} />
                                Help
                            </{MenubarItem}>
                            <{MenubarSeparator} />
                            <{MenubarItem} variant="destructive">
                                <{CircleDashedIcon} />
                                Delete
                            </{MenubarItem}>
                        </{MenubarGroup}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarWithShortcuts():
    return t"""
        <{Example} title="With Shortcuts">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>File</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            New Tab <{MenubarShortcut}>⌘T</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            New Window <{MenubarShortcut}>⌘N</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            Print... <{MenubarShortcut}>⌘P</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Edit</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            Undo <{MenubarShortcut}>⌘Z</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            Redo <{MenubarShortcut}>⇧⌘Z</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>
                            Cut <{MenubarShortcut}>⌘X</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            Copy <{MenubarShortcut}>⌘C</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            Paste <{MenubarShortcut}>⌘V</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarFormat():
    return t"""
        <{Example} title="Format">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Format</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            <{BoldIcon} />
                            Bold <{MenubarShortcut}>⌘B</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{ItalicIcon} />
                            Italic <{MenubarShortcut}>⌘I</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{UnderlineIcon} />
                            Underline <{MenubarShortcut}>⌘U</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarCheckboxItem} checked>Strikethrough</{MenubarCheckboxItem}>
                        <{MenubarCheckboxItem}>Code</{MenubarCheckboxItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>View</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarCheckboxItem}>Show Ruler</{MenubarCheckboxItem}>
                        <{MenubarCheckboxItem} checked>Show Grid</{MenubarCheckboxItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem} inset>Zoom In</{MenubarItem}>
                        <{MenubarItem} inset>Zoom Out</{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarInsert():
    return t"""
        <{Example} title="Insert">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Insert</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarSub}>
                            <{MenubarSubTrigger}>
                                <{ImageIcon} />
                                Media
                            </{MenubarSubTrigger}>
                            <{MenubarSubContent}>
                                <{MenubarItem}>Image</{MenubarItem}>
                                <{MenubarItem}>Video</{MenubarItem}>
                                <{MenubarItem}>Audio</{MenubarItem}>
                            </{MenubarSubContent}>
                        </{MenubarSub}>
                        <{MenubarSeparator} />
                        <{MenubarItem}>
                            <{LinkIcon} />
                            Link <{MenubarShortcut}>⌘K</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{TableIcon} />
                            Table
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Tools</{MenubarTrigger}>
                    <{MenubarContent} class="w-44">
                        <{MenubarItem}>
                            <{SearchIcon} />
                            Find & Replace <{MenubarShortcut}>⌘F</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{CheckIcon} />
                            Spell Check
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarDestructive():
    return t"""
        <{Example} title="Destructive">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>File</{MenubarTrigger}>
                    <{MenubarContent} class="w-40">
                        <{MenubarItem}>
                            <{FileIcon} />
                            New File <{MenubarShortcut}>⌘N</{MenubarShortcut}>
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{FolderIcon} />
                            Open Folder
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem} variant="destructive">
                            <{TrashIcon} />
                            Delete File <{MenubarShortcut}>⌘⌫</{MenubarShortcut}>
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>Account</{MenubarTrigger}>
                    <{MenubarContent}>
                        <{MenubarItem}>
                            <{UserIcon} />
                            Profile
                        </{MenubarItem}>
                        <{MenubarItem}>
                            <{SettingsIcon} />
                            Settings
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem} variant="destructive">
                            <{LogOutIcon} />
                            Sign out
                        </{MenubarItem}>
                        <{MenubarSeparator} />
                        <{MenubarItem} variant="destructive">
                            <{TrashIcon} />
                            Delete
                        </{MenubarItem}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """


def MenubarInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open Dialog</{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Menubar Example</{DialogTitle}>
                        <{DialogDescription}>Use the menubar below to see the menu options.</{DialogDescription}>
                    </{DialogHeader}>
                    <{Menubar}>
                        <{MenubarMenu}>
                            <{MenubarTrigger}>File</{MenubarTrigger}>
                            <{MenubarContent}>
                                <{MenubarItem}>
                                    <{CopyIcon} />
                                    Copy
                                </{MenubarItem}>
                                <{MenubarItem}>
                                    <{ScissorsIcon} />
                                    Cut
                                </{MenubarItem}>
                                <{MenubarItem}>
                                    <{ClipboardPasteIcon} />
                                    Paste
                                </{MenubarItem}>
                                <{MenubarSeparator} />
                                <{MenubarSub}>
                                    <{MenubarSubTrigger}>More Options</{MenubarSubTrigger}>
                                    <{MenubarSubContent}>
                                        <{MenubarItem}>Save Page...</{MenubarItem}>
                                        <{MenubarItem}>Create Shortcut...</{MenubarItem}>
                                        <{MenubarItem}>Name Window...</{MenubarItem}>
                                        <{MenubarSeparator} />
                                        <{MenubarItem}>Developer Tools</{MenubarItem}>
                                    </{MenubarSubContent}>
                                </{MenubarSub}>
                                <{MenubarSeparator} />
                                <{MenubarItem} variant="destructive">
                                    <{TrashIcon} />
                                    Delete
                                </{MenubarItem}>
                            </{MenubarContent}>
                        </{MenubarMenu}>
                        <{MenubarMenu}>
                            <{MenubarTrigger}>Edit</{MenubarTrigger}>
                            <{MenubarContent}>
                                <{MenubarItem}>
                                    Undo <{MenubarShortcut}>⌘Z</{MenubarShortcut}>
                                </{MenubarItem}>
                                <{MenubarItem}>
                                    Redo <{MenubarShortcut}>⇧⌘Z</{MenubarShortcut}>
                                </{MenubarItem}>
                            </{MenubarContent}>
                        </{MenubarMenu}>
                    </{Menubar}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


def MenubarWithInset():
    show_bookmarks, set_show_bookmarks = use_state(True)
    show_urls, set_show_urls = use_state(False)
    theme, set_theme = use_state("system")

    return t"""
        <{Example} title="With Inset">
            <{Menubar}>
                <{MenubarMenu}>
                    <{MenubarTrigger}>View</{MenubarTrigger}>
                    <{MenubarContent} class="w-44">
                        <{MenubarGroup}>
                            <{MenubarLabel}>Actions</{MenubarLabel}>
                            <{MenubarItem}>
                                <{CopyIcon} />
                                Copy
                            </{MenubarItem}>
                            <{MenubarItem}>
                                <{ScissorsIcon} />
                                Cut
                            </{MenubarItem}>
                            <{MenubarItem} inset>Paste</{MenubarItem}>
                        </{MenubarGroup}>
                        <{MenubarSeparator} />
                        <{MenubarGroup}>
                            <{MenubarLabel} inset>Appearance</{MenubarLabel}>
                            <{MenubarCheckboxItem} inset checked={show_bookmarks} onCheckedChange={set_show_bookmarks}>
                                Bookmarks
                            </{MenubarCheckboxItem}>
                            <{MenubarCheckboxItem} inset checked={show_urls} onCheckedChange={set_show_urls}>
                                Full URLs
                            </{MenubarCheckboxItem}>
                        </{MenubarGroup}>
                        <{MenubarSeparator} />
                        <{MenubarGroup}>
                            <{MenubarLabel} inset>Theme</{MenubarLabel}>
                            <{MenubarRadioGroup} value={theme} onValueChange={set_theme}>
                                <{MenubarRadioItem} inset value="light">Light</{MenubarRadioItem}>
                                <{MenubarRadioItem} inset value="dark">Dark</{MenubarRadioItem}>
                                <{MenubarRadioItem} inset value="system">System</{MenubarRadioItem}>
                            </{MenubarRadioGroup}>
                        </{MenubarGroup}>
                        <{MenubarSeparator} />
                        <{MenubarSub}>
                            <{MenubarSubTrigger} inset>More Options</{MenubarSubTrigger}>
                            <{MenubarSubContent}>
                                <{MenubarGroup}>
                                    <{MenubarItem}>Save Page...</{MenubarItem}>
                                    <{MenubarItem}>Create Shortcut...</{MenubarItem}>
                                </{MenubarGroup}>
                            </{MenubarSubContent}>
                        </{MenubarSub}>
                    </{MenubarContent}>
                </{MenubarMenu}>
            </{Menubar}>
        </{Example}>
    """
