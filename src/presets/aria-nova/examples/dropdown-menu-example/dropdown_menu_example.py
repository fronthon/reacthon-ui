from browser import window
from reacthon import use_state
from example import Example, ExampleWrapper
from avatar import Avatar, AvatarFallback, AvatarImage
from button import Button
from dialog import Dialog, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
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

__js__ = {
    "lucide-react": [
        "UserIcon",
        "CreditCardIcon",
        "SettingsIcon",
        "LogOutIcon",
        "LayoutIcon",
        "ActivityIcon",
        "PanelLeftIcon",
        "ArrowUpIcon",
        "ArrowDownIcon",
        "ArrowRightIcon",
        "MailIcon",
        "MessageSquareIcon",
        "BellIcon",
        "WalletIcon",
        "Building2Icon",
        "PencilIcon",
        "ShareIcon",
        "ArchiveIcon",
        "TrashIcon",
        "BadgeCheckIcon",
        "ChevronsUpDownIcon",
        "CopyIcon",
        "ScissorsIcon",
        "ClipboardPasteIcon",
        "UsersIcon",
        "PlusCircleIcon",
        "HelpCircleIcon",
    ],
}


def DropdownMenuExample():
    return t"""
        <{ExampleWrapper}>
            <{DropdownMenuBasic} />
            <{DropdownMenuComplex} />
            <{DropdownMenuSides} />
            <{DropdownMenuWithIcons} />
            <{DropdownMenuWithShortcuts} />
            <{DropdownMenuWithSubmenu} />
            <{DropdownMenuWithCheckboxes} />
            <{DropdownMenuWithCheckboxesIcons} />
            <{DropdownMenuWithRadio} />
            <{DropdownMenuWithRadioIcons} />
            <{DropdownMenuWithDestructive} />
            <{DropdownMenuWithAvatar} />
            <{DropdownMenuInDialog} />
            <{DropdownMenuWithInset} />
        </{ExampleWrapper}>
    """


def DropdownMenuBasic():
    return t"""
        <{Example} title="Basic">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Open</{Button}>
                <{DropdownMenu}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>My Account</{DropdownMenuLabel}>
                        <{DropdownMenuItem}>Profile</{DropdownMenuItem}>
                        <{DropdownMenuItem}>Billing</{DropdownMenuItem}>
                        <{DropdownMenuItem}>Settings</{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuItem}>GitHub</{DropdownMenuItem}>
                    <{DropdownMenuItem}>Support</{DropdownMenuItem}>
                    <{DropdownMenuItem} isDisabled>API</{DropdownMenuItem}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuSides():
    return t"""
        <{Example} title="Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap justify-center gap-2">
                {[t'''
                    <{DropdownMenuTrigger} key={item["placement"]}>
                        <{Button} variant="outline" class="w-fit capitalize">{item["label"]}</{Button}>
                        <{DropdownMenu} placement={item["placement"]}>
                            <{DropdownMenuGroup}>
                                <{DropdownMenuItem}>Profile</{DropdownMenuItem}>
                                <{DropdownMenuItem}>Billing</{DropdownMenuItem}>
                                <{DropdownMenuItem}>Settings</{DropdownMenuItem}>
                            </{DropdownMenuGroup}>
                        </{DropdownMenu}>
                    </{DropdownMenuTrigger}>
                ''' for item in [{"label": "start", "placement": "start top"}, {"label": "left", "placement": "left top"}, {"label": "top", "placement": "top start"}, {"label": "bottom", "placement": "bottom start"}, {"label": "right", "placement": "right top"}, {"label": "end", "placement": "end top"}]]}
            </div>
        </{Example}>
    """


def DropdownMenuWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Open</{Button}>
                <{DropdownMenu}>
                    <{DropdownMenuItem}>
                        <{UserIcon} />
                        Profile
                    </{DropdownMenuItem}>
                    <{DropdownMenuItem}>
                        <{CreditCardIcon} />
                        Billing
                    </{DropdownMenuItem}>
                    <{DropdownMenuItem}>
                        <{SettingsIcon} />
                        Settings
                    </{DropdownMenuItem}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuItem} variant="destructive">
                        <{LogOutIcon} />
                        Log out
                    </{DropdownMenuItem}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithShortcuts():
    return t"""
        <{Example} title="With Shortcuts">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Open</{Button}>
                <{DropdownMenu}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>My Account</{DropdownMenuLabel}>
                        <{DropdownMenuItem}>
                            Profile
                            <{DropdownMenuShortcut}>⇧⌘P</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            Billing
                            <{DropdownMenuShortcut}>⌘B</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            Settings
                            <{DropdownMenuShortcut}>⌘S</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            Keyboard shortcuts
                            <{DropdownMenuShortcut}>⌘K</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuItem}>
                        Log out
                        <{DropdownMenuShortcut}>⇧⌘Q</{DropdownMenuShortcut}>
                    </{DropdownMenuItem}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithSubmenu():
    return t"""
        <{Example} title="With Submenu">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Open</{Button}>
                <{DropdownMenu}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>Team</{DropdownMenuItem}>
                        <{DropdownMenuSub}>
                            <{DropdownMenuSubTrigger}>Invite users</{DropdownMenuSubTrigger}>
                            <{DropdownMenuSubContent}>
                                <{DropdownMenuItem}>Email</{DropdownMenuItem}>
                                <{DropdownMenuItem}>Message</{DropdownMenuItem}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuItem}>More...</{DropdownMenuItem}>
                            </{DropdownMenuSubContent}>
                        </{DropdownMenuSub}>
                        <{DropdownMenuItem}>
                            New Team
                            <{DropdownMenuShortcut}>⌘+T</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithCheckboxes():
    selected_keys, set_selected_keys = use_state(window.Set.new(["status-bar"]))

    return t"""
        <{Example} title="With Checkboxes">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Checkboxes</{Button}>
                <{DropdownMenu} class="min-w-40">
                    <{DropdownMenuGroup}
                        selectionMode="multiple"
                        selectedKeys={selected_keys}
                        onSelectionChange={set_selected_keys}
                    >
                        <{DropdownMenuLabel}>Appearance</{DropdownMenuLabel}>
                        <{DropdownMenuItem} id="status-bar">
                            <{LayoutIcon} />
                            Status Bar
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="activity-bar" isDisabled>
                            <{ActivityIcon} />
                            Activity Bar
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="panel">
                            <{PanelLeftIcon} />
                            Panel
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithRadio():
    position, set_position = use_state("bottom")

    def on_selection_change(keys):
        return set_position("bottom" if keys == "all" else keys.values().next().value)

    return t"""
        <{Example} title="With Radio Group">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Radio Group</{Button}>
                <{DropdownMenu}>
                    <{DropdownMenuGroup}
                        selectionMode="single"
                        selectedKeys={[position]}
                        onSelectionChange={on_selection_change}
                    >
                        <{DropdownMenuLabel}>Panel Position</{DropdownMenuLabel}>
                        <{DropdownMenuItem} id="top">
                            <{ArrowUpIcon} />
                            Top
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="bottom">
                            <{ArrowDownIcon} />
                            Bottom
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="right" isDisabled>
                            <{ArrowRightIcon} />
                            Right
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithCheckboxesIcons():
    selected_keys, set_selected_keys = use_state(window.Set.new(["email", "push"]))

    return t"""
        <{Example} title="Checkboxes with Icons">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Notifications</{Button}>
                <{DropdownMenu} class="min-w-56">
                    <{DropdownMenuGroup}
                        selectionMode="multiple"
                        selectedKeys={selected_keys}
                        onSelectionChange={set_selected_keys}
                    >
                        <{DropdownMenuLabel}>Notification Preferences</{DropdownMenuLabel}>
                        <{DropdownMenuItem} id="email">
                            <{MailIcon} />
                            Email notifications
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="sms">
                            <{MessageSquareIcon} />
                            SMS notifications
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="push">
                            <{BellIcon} />
                            Push notifications
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithRadioIcons():
    payment_method, set_payment_method = use_state("card")

    def on_selection_change(keys):
        return set_payment_method("card" if keys == "all" else keys.values().next().value)

    return t"""
        <{Example} title="Radio with Icons">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Payment Method</{Button}>
                <{DropdownMenu} class="min-w-56">
                    <{DropdownMenuGroup}
                        selectionMode="single"
                        selectedKeys={[payment_method]}
                        onSelectionChange={on_selection_change}
                    >
                        <{DropdownMenuLabel}>Select Payment Method</{DropdownMenuLabel}>
                        <{DropdownMenuItem} id="card">
                            <{CreditCardIcon} />
                            Credit Card
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="paypal">
                            <{WalletIcon} />
                            PayPal
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="bank">
                            <{Building2Icon} />
                            Bank Transfer
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithDestructive():
    return t"""
        <{Example} title="With Destructive Items">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Actions</{Button}>
                <{DropdownMenu}>
                    <{DropdownMenuItem}>
                        <{PencilIcon} />
                        Edit
                    </{DropdownMenuItem}>
                    <{DropdownMenuItem}>
                        <{ShareIcon} />
                        Share
                    </{DropdownMenuItem}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuItem}>
                        <{ArchiveIcon} />
                        Archive
                    </{DropdownMenuItem}>
                    <{DropdownMenuItem} variant="destructive">
                        <{TrashIcon} />
                        Delete
                    </{DropdownMenuItem}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuWithAvatar():
    menu_content = t"""
        <{DropdownMenuGroup}>
            <{DropdownMenuItem}>
                <{BadgeCheckIcon} />
                Account
            </{DropdownMenuItem}>
            <{DropdownMenuItem}>
                <{CreditCardIcon} />
                Billing
            </{DropdownMenuItem}>
            <{DropdownMenuItem}>
                <{BellIcon} />
                Notifications
            </{DropdownMenuItem}>
        </{DropdownMenuGroup}>
        <{DropdownMenuSeparator} />
        <{DropdownMenuItem}>
            <{LogOutIcon} />
            Sign Out
        </{DropdownMenuItem}>
    """

    return t"""
        <{Example} title="With Avatar">
            <div class="flex items-center justify-between gap-4">
                <{DropdownMenuTrigger}>
                    <{Button}
                        variant="outline"
                        class="h-12 justify-start px-2 md:max-w-[200px] style-sera:font-normal style-sera:tracking-normal style-sera:normal-case"
                    >
                        <{Avatar}>
                            <{AvatarImage} src="https://github.com/shadcn.png" alt="Shadcn" />
                            <{AvatarFallback} class="rounded-lg">CN</{AvatarFallback}>
                        </{Avatar}>
                        <div class="grid flex-1 text-left text-sm leading-tight">
                            <span class="truncate font-semibold">shadcn</span>
                            <span class="truncate text-xs text-muted-foreground">shadcn@example.com</span>
                        </div>
                        <{ChevronsUpDownIcon} class="ml-auto text-muted-foreground" />
                    </{Button}>
                    <{DropdownMenu} class="w-(--anchor-width) min-w-56">{menu_content}</{DropdownMenu}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuTrigger}>
                    <{Button} variant="ghost" size="icon" class="rounded-full">
                        <{Avatar}>
                            <{AvatarImage} src="https://github.com/shadcn.png" alt="shadcn" />
                            <{AvatarFallback}>LR</{AvatarFallback}>
                        </{Avatar}>
                    </{Button}>
                    <{DropdownMenu} placement="top end">{menu_content}</{DropdownMenu}>
                </{DropdownMenuTrigger}>
            </div>
        </{Example}>
    """


def DropdownMenuInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{DialogTrigger}>
                <{Button} variant="outline">Open Dialog</{Button}>
                <{Dialog}>
                    <{DialogHeader}>
                        <{DialogTitle}>Dropdown Menu Example</{DialogTitle}>
                        <{DialogDescription}>Click the button below to see the dropdown menu.</{DialogDescription}>
                    </{DialogHeader}>
                    <{DropdownMenuTrigger}>
                        <{Button} variant="outline" class="w-fit">Open Menu</{Button}>
                        <{DropdownMenu}>
                            <{DropdownMenuItem}>
                                <{CopyIcon} />
                                Copy
                            </{DropdownMenuItem}>
                            <{DropdownMenuItem}>
                                <{ScissorsIcon} />
                                Cut
                            </{DropdownMenuItem}>
                            <{DropdownMenuItem}>
                                <{ClipboardPasteIcon} />
                                Paste
                            </{DropdownMenuItem}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuSub}>
                                <{DropdownMenuSubTrigger}>More Options</{DropdownMenuSubTrigger}>
                                <{DropdownMenuSubContent}>
                                    <{DropdownMenuItem}>Save Page...</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Create Shortcut...</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Name Window...</{DropdownMenuItem}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuItem}>Developer Tools</{DropdownMenuItem}>
                                </{DropdownMenuSubContent}>
                            </{DropdownMenuSub}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuItem} variant="destructive">
                                <{TrashIcon} />
                                Delete
                            </{DropdownMenuItem}>
                        </{DropdownMenu}>
                    </{DropdownMenuTrigger}>
                </{Dialog}>
            </{DialogTrigger}>
        </{Example}>
    """


def DropdownMenuWithInset():
    selected_keys, set_selected_keys = use_state(window.Set.new(["bookmarks"]))
    theme, set_theme = use_state("system")

    def on_selection_change(keys):
        return set_theme("system" if keys == "all" else keys.values().next().value)

    return t"""
        <{Example} title="With Inset">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Open</{Button}>
                <{DropdownMenu} class="w-44">
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>Actions</{DropdownMenuLabel}>
                        <{DropdownMenuItem}>
                            <{CopyIcon} />
                            Copy
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            <{ScissorsIcon} />
                            Cut
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} inset>Paste</{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}
                        selectionMode="multiple"
                        selectedKeys={selected_keys}
                        onSelectionChange={set_selected_keys}
                    >
                        <{DropdownMenuLabel} inset>Appearance</{DropdownMenuLabel}>
                        <{DropdownMenuItem} inset id="bookmarks">Bookmarks</{DropdownMenuItem}>
                        <{DropdownMenuItem} inset id="urls">Full URLs</{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}
                        selectionMode="single"
                        selectedKeys={[theme]}
                        onSelectionChange={on_selection_change}
                    >
                        <{DropdownMenuLabel} inset>Theme</{DropdownMenuLabel}>
                        <{DropdownMenuItem} inset id="light">Light</{DropdownMenuItem}>
                        <{DropdownMenuItem} inset id="dark">Dark</{DropdownMenuItem}>
                        <{DropdownMenuItem} inset id="system">System</{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuSub}>
                        <{DropdownMenuSubTrigger} inset>More Options</{DropdownMenuSubTrigger}>
                        <{DropdownMenuSubContent}>
                            <{DropdownMenuGroup}>
                                <{DropdownMenuItem}>Save Page...</{DropdownMenuItem}>
                                <{DropdownMenuItem}>Create Shortcut...</{DropdownMenuItem}>
                            </{DropdownMenuGroup}>
                        </{DropdownMenuSubContent}>
                    </{DropdownMenuSub}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """


def DropdownMenuComplex():
    selected_keys, set_selected_keys = use_state(window.Set.new(["sidebar"]))

    return t"""
        <{Example} title="Complex">
            <{DropdownMenuTrigger}>
                <{Button} variant="outline" class="w-fit">Complex Menu</{Button}>
                <{DropdownMenu} class="w-56">
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>My Account</{DropdownMenuLabel}>
                        <{DropdownMenuItem}>
                            <{UserIcon} />
                            Profile
                            <{DropdownMenuShortcut}>⇧⌘P</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            <{CreditCardIcon} />
                            Billing
                            <{DropdownMenuShortcut}>⌘B</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            <{SettingsIcon} />
                            Settings
                            <{DropdownMenuShortcut}>⌘S</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}
                        selectionMode="multiple"
                        selectedKeys={selected_keys}
                        onSelectionChange={set_selected_keys}
                    >
                        <{DropdownMenuLabel}>View</{DropdownMenuLabel}>
                        <{DropdownMenuItem} id="sidebar">
                            <{PanelLeftIcon} />
                            Sidebar
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} id="status-bar">
                            <{LayoutIcon} />
                            Status Bar
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuSub}>
                            <{DropdownMenuSubTrigger}>
                                <{UsersIcon} />
                                Invite Users
                            </{DropdownMenuSubTrigger}>
                            <{DropdownMenuSubContent}>
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem}>
                                        <{MailIcon} />
                                        Email
                                    </{DropdownMenuItem}>
                                    <{DropdownMenuItem}>
                                        <{MessageSquareIcon} />
                                        Message
                                    </{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem}>
                                        <{PlusCircleIcon} />
                                        More...
                                    </{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                            </{DropdownMenuSubContent}>
                        </{DropdownMenuSub}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>
                            <{HelpCircleIcon} />
                            Support
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} variant="destructive">
                            <{LogOutIcon} />
                            Sign Out
                            <{DropdownMenuShortcut}>⇧⌘Q</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenu}>
            </{DropdownMenuTrigger}>
        </{Example}>
    """
