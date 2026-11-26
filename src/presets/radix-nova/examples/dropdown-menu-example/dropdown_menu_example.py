from reacthon import use_state
from example import Example, ExampleWrapper
from avatar import Avatar, AvatarFallback, AvatarImage
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuPortal,
    DropdownMenuRadioGroup,
    DropdownMenuRadioItem,
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
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Open</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>My Account</{DropdownMenuLabel}>
                        <{DropdownMenuItem}>Profile</{DropdownMenuItem}>
                        <{DropdownMenuItem}>Billing</{DropdownMenuItem}>
                        <{DropdownMenuItem}>Settings</{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>GitHub</{DropdownMenuItem}>
                        <{DropdownMenuItem} disabled>API</{DropdownMenuItem}>
                        <{DropdownMenuItem}>Support</{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Open</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent}>
                    <{DropdownMenuGroup}>
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
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem} variant="destructive">
                            <{LogOutIcon} />
                            Log out
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithShortcuts():
    return t"""
        <{Example} title="With Shortcuts">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Open</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent}>
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
                            Shortcuts
                            <{DropdownMenuShortcut}>⌘K</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>
                            Log out
                            <{DropdownMenuShortcut}>⇧⌘Q</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithSubmenu():
    return t"""
        <{Example} title="With Submenu">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Open</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>Team</{DropdownMenuItem}>
                        <{DropdownMenuSub}>
                            <{DropdownMenuSubTrigger}>Invite users</{DropdownMenuSubTrigger}>
                            <{DropdownMenuPortal}>
                                <{DropdownMenuSubContent}>
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuItem}>Email</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Message</{DropdownMenuItem}>
                                    </{DropdownMenuGroup}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuItem}>More...</{DropdownMenuItem}>
                                    </{DropdownMenuGroup}>
                                </{DropdownMenuSubContent}>
                            </{DropdownMenuPortal}>
                        </{DropdownMenuSub}>
                        <{DropdownMenuItem}>
                            New Team
                            <{DropdownMenuShortcut}>⌘+T</{DropdownMenuShortcut}>
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithCheckboxes():
    show_status_bar, set_show_status_bar = use_state(True)
    show_activity_bar, set_show_activity_bar = use_state(False)
    show_panel, set_show_panel = use_state(False)

    return t"""
        <{Example} title="With Checkboxes">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Checkboxes</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent} class="min-w-40">
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>Appearance</{DropdownMenuLabel}>
                        <{DropdownMenuCheckboxItem} checked={show_status_bar} onCheckedChange={set_show_status_bar}>
                            <{LayoutIcon} />
                            Status Bar
                        </{DropdownMenuCheckboxItem}>
                        <{DropdownMenuCheckboxItem}
                            checked={show_activity_bar}
                            onCheckedChange={set_show_activity_bar}
                            disabled
                        >
                            <{ActivityIcon} />
                            Activity Bar
                        </{DropdownMenuCheckboxItem}>
                        <{DropdownMenuCheckboxItem} checked={show_panel} onCheckedChange={set_show_panel}>
                            <{PanelLeftIcon} />
                            Panel
                        </{DropdownMenuCheckboxItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithRadio():
    position, set_position = use_state("bottom")

    return t"""
        <{Example} title="With Radio Group">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Radio Group</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>Panel Position</{DropdownMenuLabel}>
                        <{DropdownMenuRadioGroup} value={position} onValueChange={set_position}>
                            <{DropdownMenuRadioItem} value="top">
                                <{ArrowUpIcon} />
                                Top
                            </{DropdownMenuRadioItem}>
                            <{DropdownMenuRadioItem} value="bottom">
                                <{ArrowDownIcon} />
                                Bottom
                            </{DropdownMenuRadioItem}>
                            <{DropdownMenuRadioItem} value="right" disabled>
                                <{ArrowRightIcon} />
                                Right
                            </{DropdownMenuRadioItem}>
                        </{DropdownMenuRadioGroup}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithCheckboxesIcons():
    notifications, set_notifications = use_state({"email": True, "sms": False, "push": True})

    return t"""
        <{Example} title="Checkboxes with Icons">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Notifications</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent} class="min-w-56">
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>Notification Preferences</{DropdownMenuLabel}>
                        <{DropdownMenuCheckboxItem}
                            checked={notifications["email"]}
                            onCheckedChange={(lambda checked: set_notifications({
                                **notifications,
                                "email": checked == True,
                            }))}
                        >
                            <{MailIcon} />
                            Email notifications
                        </{DropdownMenuCheckboxItem}>
                        <{DropdownMenuCheckboxItem}
                            checked={notifications["sms"]}
                            onCheckedChange={(lambda checked: set_notifications({
                                **notifications,
                                "sms": checked == True,
                            }))}
                        >
                            <{MessageSquareIcon} />
                            SMS notifications
                        </{DropdownMenuCheckboxItem}>
                        <{DropdownMenuCheckboxItem}
                            checked={notifications["push"]}
                            onCheckedChange={(lambda checked: set_notifications({
                                **notifications,
                                "push": checked == True,
                            }))}
                        >
                            <{BellIcon} />
                            Push notifications
                        </{DropdownMenuCheckboxItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithRadioIcons():
    payment_method, set_payment_method = use_state("card")

    return t"""
        <{Example} title="Radio with Icons">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline">Payment Method</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent} class="min-w-56">
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>Select Payment Method</{DropdownMenuLabel}>
                        <{DropdownMenuRadioGroup} value={payment_method} onValueChange={set_payment_method}>
                            <{DropdownMenuRadioItem} value="card">
                                <{CreditCardIcon} />
                                Credit Card
                            </{DropdownMenuRadioItem}>
                            <{DropdownMenuRadioItem} value="paypal">
                                <{WalletIcon} />
                                PayPal
                            </{DropdownMenuRadioItem}>
                            <{DropdownMenuRadioItem} value="bank">
                                <{Building2Icon} />
                                Bank Transfer
                            </{DropdownMenuRadioItem}>
                        </{DropdownMenuRadioGroup}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuWithDestructive():
    return t"""
        <{Example} title="With Destructive Items">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Actions</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent}>
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>
                            <{PencilIcon} />
                            Edit
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem}>
                            <{ShareIcon} />
                            Share
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuItem}>
                            <{ArchiveIcon} />
                            Archive
                        </{DropdownMenuItem}>
                        <{DropdownMenuItem} variant="destructive">
                            <{TrashIcon} />
                            Delete
                        </{DropdownMenuItem}>
                    </{DropdownMenuGroup}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
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
        <{DropdownMenuGroup}>
            <{DropdownMenuItem}>
                <{LogOutIcon} />
                Sign Out
            </{DropdownMenuItem}>
        </{DropdownMenuGroup}>
    """

    return t"""
        <{Example} title="With Avatar">
            <div class="flex items-center justify-between gap-4">
                <{DropdownMenu}>
                    <{DropdownMenuTrigger} asChild>
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
                    </{DropdownMenuTrigger}>
                    <{DropdownMenuContent} class="w-(--radix-dropdown-menu-trigger-width) min-w-56">
                        {menu_content}
                    </{DropdownMenuContent}>
                </{DropdownMenu}>
                <{DropdownMenu}>
                    <{DropdownMenuTrigger} asChild>
                        <{Button} variant="ghost" size="icon" class="rounded-full">
                            <{Avatar}>
                                <{AvatarImage} src="https://github.com/shadcn.png" alt="shadcn" />
                                <{AvatarFallback}>LR</{AvatarFallback}>
                            </{Avatar}>
                        </{Button}>
                    </{DropdownMenuTrigger}>
                    <{DropdownMenuContent} align="end" side="top">{menu_content}</{DropdownMenuContent}>
                </{DropdownMenu}>
            </div>
        </{Example}>
    """


def DropdownMenuInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Open Dialog</{Button}>
                </{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Dropdown Menu Example</{DialogTitle}>
                        <{DialogDescription}>Click the button below to see the dropdown menu.</{DialogDescription}>
                    </{DialogHeader}>
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} asChild>
                            <{Button} variant="outline" class="w-fit">Open Menu</{Button}>
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent}>
                            <{DropdownMenuGroup}>
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
                            </{DropdownMenuGroup}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuSub}>
                                <{DropdownMenuSubTrigger}>More Options</{DropdownMenuSubTrigger}>
                                <{DropdownMenuPortal}>
                                    <{DropdownMenuSubContent}>
                                        <{DropdownMenuGroup}>
                                            <{DropdownMenuItem}>Save Page...</{DropdownMenuItem}>
                                            <{DropdownMenuItem}>Create Shortcut...</{DropdownMenuItem}>
                                            <{DropdownMenuItem}>Name Window...</{DropdownMenuItem}>
                                        </{DropdownMenuGroup}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuGroup}>
                                            <{DropdownMenuItem}>Developer Tools</{DropdownMenuItem}>
                                        </{DropdownMenuGroup}>
                                    </{DropdownMenuSubContent}>
                                </{DropdownMenuPortal}>
                            </{DropdownMenuSub}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuGroup}>
                                <{DropdownMenuItem} variant="destructive">
                                    <{TrashIcon} />
                                    Delete
                                </{DropdownMenuItem}>
                            </{DropdownMenuGroup}>
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


def DropdownMenuWithInset():
    show_bookmarks, set_show_bookmarks = use_state(True)
    show_urls, set_show_urls = use_state(False)
    theme, set_theme = use_state("system")

    return t"""
        <{Example} title="With Inset">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Open</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent} class="w-44">
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
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel} inset>Appearance</{DropdownMenuLabel}>
                        <{DropdownMenuCheckboxItem} inset checked={show_bookmarks} onCheckedChange={set_show_bookmarks}>
                            Bookmarks
                        </{DropdownMenuCheckboxItem}>
                        <{DropdownMenuCheckboxItem} inset checked={show_urls} onCheckedChange={set_show_urls}>
                            Full URLs
                        </{DropdownMenuCheckboxItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel} inset>Theme</{DropdownMenuLabel}>
                        <{DropdownMenuRadioGroup} value={theme} onValueChange={set_theme}>
                            <{DropdownMenuRadioItem} inset value="light">Light</{DropdownMenuRadioItem}>
                            <{DropdownMenuRadioItem} inset value="dark">Dark</{DropdownMenuRadioItem}>
                            <{DropdownMenuRadioItem} inset value="system">System</{DropdownMenuRadioItem}>
                        </{DropdownMenuRadioGroup}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuSub}>
                        <{DropdownMenuSubTrigger} inset>More Options</{DropdownMenuSubTrigger}>
                        <{DropdownMenuPortal}>
                            <{DropdownMenuSubContent}>
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem}>Save Page...</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Create Shortcut...</{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                            </{DropdownMenuSubContent}>
                        </{DropdownMenuPortal}>
                    </{DropdownMenuSub}>
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """


def DropdownMenuComplex():
    show_sidebar, set_show_sidebar = use_state(True)
    show_status_bar, set_show_status_bar = use_state(False)

    return t"""
        <{Example} title="Complex">
            <{DropdownMenu}>
                <{DropdownMenuTrigger} asChild>
                    <{Button} variant="outline" class="w-fit">Complex Menu</{Button}>
                </{DropdownMenuTrigger}>
                <{DropdownMenuContent} class="w-56">
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
                    <{DropdownMenuGroup}>
                        <{DropdownMenuLabel}>View</{DropdownMenuLabel}>
                        <{DropdownMenuCheckboxItem} checked={show_sidebar} onCheckedChange={set_show_sidebar}>
                            <{PanelLeftIcon} />
                            Sidebar
                        </{DropdownMenuCheckboxItem}>
                        <{DropdownMenuCheckboxItem} checked={show_status_bar} onCheckedChange={set_show_status_bar}>
                            <{LayoutIcon} />
                            Status Bar
                        </{DropdownMenuCheckboxItem}>
                    </{DropdownMenuGroup}>
                    <{DropdownMenuSeparator} />
                    <{DropdownMenuGroup}>
                        <{DropdownMenuSub}>
                            <{DropdownMenuSubTrigger}>
                                <{UsersIcon} />
                                Invite Users
                            </{DropdownMenuSubTrigger}>
                            <{DropdownMenuPortal}>
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
                            </{DropdownMenuPortal}>
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
                </{DropdownMenuContent}>
            </{DropdownMenu}>
        </{Example}>
    """
