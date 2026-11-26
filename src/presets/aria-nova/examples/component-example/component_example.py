from browser import window
from javascript import NULL
from reacthon import use_state
from example import Example, ExampleWrapper
from alert_dialog import (
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogMedia,
    AlertDialogTitle,
    AlertDialogTrigger,
)
from badge import Badge
from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from combobox import Combobox, ComboboxContent, ComboboxEmpty, ComboboxInput, ComboboxItem, ComboboxList
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuSub,
    DropdownMenuSubContent,
    DropdownMenuSubTrigger,
    DropdownMenuTrigger,
)
from field import Field, FieldGroup, FieldLabel
from input import Input
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from textarea import Textarea

__js__ = {
    "lucide-react": [
        "PlusIcon",
        "BluetoothIcon",
        "MoreVerticalIcon",
        "FileIcon",
        "FolderIcon",
        "FolderOpenIcon",
        "FileCodeIcon",
        "MoreHorizontalIcon",
        "FolderSearchIcon",
        "SaveIcon",
        "DownloadIcon",
        "EyeIcon",
        "LayoutIcon",
        "PaletteIcon",
        "SunIcon",
        "MoonIcon",
        "MonitorIcon",
        "UserIcon",
        "CreditCardIcon",
        "SettingsIcon",
        "KeyboardIcon",
        "LanguagesIcon",
        "BellIcon",
        "MailIcon",
        "ShieldIcon",
        "HelpCircleIcon",
        "FileTextIcon",
        "LogOutIcon",
    ],
}


def ComponentExample():
    return t"""
        <{ExampleWrapper}>
            <{CardExample} />
            <{FormExample} />
        </{ExampleWrapper}>
    """


def CardExample():
    return t"""
        <{Example} title="Card" class="items-center justify-center">
            <{Card} class="relative w-full max-w-sm overflow-hidden pt-0">
                <div class="absolute inset-0 z-30 aspect-video bg-primary opacity-50 mix-blend-color" />
                <img
                    src="https://images.unsplash.com/photo-1604076850742-4c7221f3101b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    alt="Photo by mymind on Unsplash"
                    title="Photo by mymind on Unsplash"
                    class="relative z-20 aspect-video w-full object-cover brightness-60 grayscale"
                />
                <{CardHeader}>
                    <{CardTitle}>Observability Plus is replacing Monitoring</{CardTitle}>
                    <{CardDescription}>
                        Switch to the improved way to explore your data, with natural language. Monitoring will no longer be available on the Pro plan in November, 2025
                    </{CardDescription}>
                </{CardHeader}>
                <{CardFooter}>
                    <{AlertDialogTrigger}>
                        <{Button}>
                            <{PlusIcon} data-icon="inline-start" />
                            Show Dialog
                        </{Button}>
                        <{AlertDialog} size="sm">
                            <{AlertDialogHeader}>
                                <{AlertDialogMedia}>
                                    <{BluetoothIcon} />
                                </{AlertDialogMedia}>
                                <{AlertDialogTitle}>Allow accessory to connect?</{AlertDialogTitle}>
                                <{AlertDialogDescription}>
                                    Do you want to allow the USB accessory to connect to this device?
                                </{AlertDialogDescription}>
                            </{AlertDialogHeader}>
                            <{AlertDialogFooter}>
                                <{AlertDialogCancel}>Don't allow</{AlertDialogCancel}>
                                <{AlertDialogAction}>Allow</{AlertDialogAction}>
                            </{AlertDialogFooter}>
                        </{AlertDialog}>
                    </{AlertDialogTrigger}>
                    <{Badge} variant="secondary" class="ml-auto">Warning</{Badge}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


frameworks = ["Next.js", "SvelteKit", "Nuxt.js", "Remix", "Astro"]

role_items = [
    {"label": "Developer", "value": "developer"},
    {"label": "Designer", "value": "designer"},
    {"label": "Manager", "value": "manager"},
    {"label": "Other", "value": "other"},
]


def FormExample():
    notifications, set_notifications = use_state(window.Set.new(["email", "push"]))
    view, set_view = use_state(window.Set.new(["sidebar"]))
    theme, set_theme = use_state("light")

    def on_selection_change(keys):
        return set_theme("system" if keys == "all" else keys.values().next().value)

    def render_empty_state():
        return t"<{ComboboxEmpty}>No frameworks found.</{ComboboxEmpty}>"

    return t"""
        <{Example} title="Form">
            <{Card} class="w-full max-w-md">
                <{CardHeader}>
                    <{CardTitle}>User Information</{CardTitle}>
                    <{CardDescription}>Please fill in your details below</{CardDescription}>
                    <{CardAction}>
                        <{DropdownMenuTrigger}>
                            <{Button} variant="ghost" size="icon">
                                <{MoreVerticalIcon} />
                                <span class="sr-only">More options</span>
                            </{Button}>
                            <{DropdownMenu} placement="bottom end" class="w-56">
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuLabel}>File</{DropdownMenuLabel}>
                                    <{DropdownMenuItem}>
                                        <{FileIcon} />
                                        New File
                                        <{DropdownMenuShortcut}>⌘N</{DropdownMenuShortcut}>
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuItem}>
                                        <{FolderIcon} />
                                        New Folder
                                        <{DropdownMenuShortcut}>⇧⌘N</{DropdownMenuShortcut}>
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuSub}>
                                        <{DropdownMenuSubTrigger}>
                                            <{FolderOpenIcon} />
                                            Open Recent
                                        </{DropdownMenuSubTrigger}>
                                        <{DropdownMenuSubContent}>
                                            <{DropdownMenuGroup}>
                                                <{DropdownMenuLabel}>Recent Projects</{DropdownMenuLabel}>
                                                <{DropdownMenuItem}>
                                                    <{FileCodeIcon} />
                                                    Project Alpha
                                                </{DropdownMenuItem}>
                                                <{DropdownMenuItem}>
                                                    <{FileCodeIcon} />
                                                    Project Beta
                                                </{DropdownMenuItem}>
                                                <{DropdownMenuSub}>
                                                    <{DropdownMenuSubTrigger}>
                                                        <{MoreHorizontalIcon} />
                                                        More Projects
                                                    </{DropdownMenuSubTrigger}>
                                                    <{DropdownMenuSubContent}>
                                                        <{DropdownMenuItem}>
                                                            <{FileCodeIcon} />
                                                            Project Gamma
                                                        </{DropdownMenuItem}>
                                                        <{DropdownMenuItem}>
                                                            <{FileCodeIcon} />
                                                            Project Delta
                                                        </{DropdownMenuItem}>
                                                    </{DropdownMenuSubContent}>
                                                </{DropdownMenuSub}>
                                            </{DropdownMenuGroup}>
                                            <{DropdownMenuSeparator} />
                                            <{DropdownMenuGroup}>
                                                <{DropdownMenuItem}>
                                                    <{FolderSearchIcon} />
                                                    Browse...
                                                </{DropdownMenuItem}>
                                            </{DropdownMenuGroup}>
                                        </{DropdownMenuSubContent}>
                                    </{DropdownMenuSub}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuItem}>
                                        <{SaveIcon} />
                                        Save
                                        <{DropdownMenuShortcut}>⌘S</{DropdownMenuShortcut}>
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuItem}>
                                        <{DownloadIcon} />
                                        Export
                                        <{DropdownMenuShortcut}>⇧⌘E</{DropdownMenuShortcut}>
                                    </{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}
                                    selectionMode="multiple"
                                    selectedKeys={notifications}
                                    onSelectionChange={set_notifications}
                                >
                                    <{DropdownMenuLabel}>View</{DropdownMenuLabel}>
                                    <{DropdownMenuItem} id="sidebar">
                                        <{EyeIcon} />
                                        Show Sidebar
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuItem} id="status-bar">
                                        <{LayoutIcon} />
                                        Show Status Bar
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuSub}>
                                        <{DropdownMenuSubTrigger}>
                                            <{PaletteIcon} />
                                            Theme
                                        </{DropdownMenuSubTrigger}>
                                        <{DropdownMenuSubContent}>
                                            <{DropdownMenuGroup}
                                                selectionMode="single"
                                                selectedKeys={[theme]}
                                                onSelectionChange={on_selection_change}
                                            >
                                                <{DropdownMenuLabel}>Appearance</{DropdownMenuLabel}>
                                                <{DropdownMenuItem} id="light">
                                                    <{SunIcon} />
                                                    Light
                                                </{DropdownMenuItem}>
                                                <{DropdownMenuItem} id="dark">
                                                    <{MoonIcon} />
                                                    Dark
                                                </{DropdownMenuItem}>
                                                <{DropdownMenuItem} id="system">
                                                    <{MonitorIcon} />
                                                    System
                                                </{DropdownMenuItem}>
                                            </{DropdownMenuGroup}>
                                        </{DropdownMenuSubContent}>
                                    </{DropdownMenuSub}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuLabel}>Account</{DropdownMenuLabel}>
                                    <{DropdownMenuItem}>
                                        <{UserIcon} />
                                        Profile
                                        <{DropdownMenuShortcut}>⇧⌘P</{DropdownMenuShortcut}>
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuItem}>
                                        <{CreditCardIcon} />
                                        Billing
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuSub}>
                                        <{DropdownMenuSubTrigger}>
                                            <{SettingsIcon} />
                                            Settings
                                        </{DropdownMenuSubTrigger}>
                                        <{DropdownMenuSubContent}>
                                            <{DropdownMenuGroup}>
                                                <{DropdownMenuLabel}>Preferences</{DropdownMenuLabel}>
                                                <{DropdownMenuItem}>
                                                    <{KeyboardIcon} />
                                                    Keyboard Shortcuts
                                                </{DropdownMenuItem}>
                                                <{DropdownMenuItem}>
                                                    <{LanguagesIcon} />
                                                    Language
                                                </{DropdownMenuItem}>
                                                <{DropdownMenuSub}>
                                                    <{DropdownMenuSubTrigger}>
                                                        <{BellIcon} />
                                                        Notifications
                                                    </{DropdownMenuSubTrigger}>
                                                    <{DropdownMenuSubContent}>
                                                        <{DropdownMenuGroup}
                                                            selectionMode="multiple"
                                                            selectedKeys={notifications}
                                                            onSelectionChange={set_notifications}
                                                        >
                                                            <{DropdownMenuLabel}>
                                                                Notification Types
                                                            </{DropdownMenuLabel}>
                                                            <{DropdownMenuItem} id="push">
                                                                <{BellIcon} />
                                                                Push Notifications
                                                            </{DropdownMenuItem}>
                                                            <{DropdownMenuItem} id="email">
                                                                <{MailIcon} />
                                                                Email Notifications
                                                            </{DropdownMenuItem}>
                                                        </{DropdownMenuGroup}>
                                                    </{DropdownMenuSubContent}>
                                                </{DropdownMenuSub}>
                                            </{DropdownMenuGroup}>
                                            <{DropdownMenuSeparator} />
                                            <{DropdownMenuGroup}>
                                                <{DropdownMenuItem}>
                                                    <{ShieldIcon} />
                                                    Privacy & Security
                                                </{DropdownMenuItem}>
                                            </{DropdownMenuGroup}>
                                        </{DropdownMenuSubContent}>
                                    </{DropdownMenuSub}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem}>
                                        <{HelpCircleIcon} />
                                        Help & Support
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuItem}>
                                        <{FileTextIcon} />
                                        Documentation
                                    </{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem} variant="destructive">
                                        <{LogOutIcon} />
                                        Sign Out
                                        <{DropdownMenuShortcut}>⇧⌘Q</{DropdownMenuShortcut}>
                                    </{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                            </{DropdownMenu}>
                        </{DropdownMenuTrigger}>
                    </{CardAction}>
                </{CardHeader}>
                <{CardContent}>
                    <form>
                        <{FieldGroup}>
                            <div class="grid grid-cols-2 gap-4">
                                <{Field}>
                                    <{FieldLabel} for="small-form-name">Name</{FieldLabel}>
                                    <{Input} id="small-form-name" placeholder="Enter your name" required />
                                </{Field}>
                                <{Field}>
                                    <{FieldLabel} for="small-form-role">Role</{FieldLabel}>
                                    <{Select} defaultValue={NULL}>
                                        <{SelectTrigger} id="small-form-role">
                                            <{SelectValue} />
                                        </{SelectTrigger}>
                                        <{SelectContent}>
                                            <{SelectGroup}>
                                                {[t'''
                                                    <{SelectItem}
                                                        key={item["value"]}
                                                        id={item["value"]}
                                                    >
                                                        {item["label"]}
                                                    </{SelectItem}>
                                                ''' for item in role_items]}
                                            </{SelectGroup}>
                                        </{SelectContent}>
                                    </{Select}>
                                </{Field}>
                            </div>
                            <{Field}>
                                <{FieldLabel} for="small-form-framework">Framework</{FieldLabel}>
                                <{Combobox} allowsEmptyCollection>
                                    <{ComboboxInput} id="small-form-framework" placeholder="Select a framework" required />
                                    <{ComboboxContent}>
                                        <{ComboboxList} renderEmptyState={render_empty_state}>
                                            {[t'''
                                                <{ComboboxItem}
                                                    key={item}
                                                    id={item}
                                                >
                                                    {item}
                                                </{ComboboxItem}>
                                            ''' for item in frameworks]}
                                        </{ComboboxList}>
                                    </{ComboboxContent}>
                                </{Combobox}>
                            </{Field}>
                            <{Field}>
                                <{FieldLabel} for="small-form-comments">Comments</{FieldLabel}>
                                <{Textarea} id="small-form-comments" placeholder="Add any additional comments" />
                            </{Field}>
                            <{Field} orientation="horizontal">
                                <{Button} type="submit">Submit</{Button}>
                                <{Button} variant="outline" type="button">Cancel</{Button}>
                            </{Field}>
                        </{FieldGroup}>
                    </form>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """
