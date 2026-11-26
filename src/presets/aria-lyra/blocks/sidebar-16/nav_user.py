from avatar import Avatar, AvatarFallback, AvatarImage
from dropdown_menu import (
    DropdownMenu, DropdownMenuGroup, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger,
)
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {
    "lucide-react": [
        "ChevronsUpDownIcon",
        "SparklesIcon",
        "BadgeCheckIcon",
        "CreditCardIcon",
        "BellIcon",
        "LogOutIcon",
    ],
}


def NavUser(user=None):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenuTrigger}>
                    <{SidebarMenuButton} size="lg" class="aria-expanded:bg-muted aria-expanded:text-foreground">
                        <{Avatar}>
                            <{AvatarImage} src={user["avatar"]} alt={user["name"]} />
                            <{AvatarFallback}>CN</{AvatarFallback}>
                        </{Avatar}>
                        <div class="grid flex-1 text-left text-sm leading-tight">
                            <span class="truncate font-medium">{user["name"]}</span>
                            <span class="truncate text-xs">{user["email"]}</span>
                        </div>
                        <{ChevronsUpDownIcon} class="ml-auto size-4" />
                    </{SidebarMenuButton}>
                    <{DropdownMenu}
                        class="min-w-56 rounded-lg"
                        placement={"bottom end" if is_mobile else "right bottom"}
                        offset={4}
                    >
                        <{DropdownMenuGroup}>
                            <{DropdownMenuLabel} class="p-0 font-normal">
                                <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                                    <{Avatar}>
                                        <{AvatarImage} src={user["avatar"]} alt={user["name"]} />
                                        <{AvatarFallback}>CN</{AvatarFallback}>
                                    </{Avatar}>
                                    <div class="grid flex-1 text-left text-sm leading-tight">
                                        <span class="truncate font-medium">{user["name"]}</span>
                                        <span class="truncate text-xs">{user["email"]}</span>
                                    </div>
                                </div>
                            </{DropdownMenuLabel}>
                        </{DropdownMenuGroup}>
                        <{DropdownMenuSeparator} />
                        <{DropdownMenuGroup}>
                            <{DropdownMenuItem}>
                                <{SparklesIcon} />
                                Upgrade to Pro
                            </{DropdownMenuItem}>
                        </{DropdownMenuGroup}>
                        <{DropdownMenuSeparator} />
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
                                Log out
                            </{DropdownMenuItem}>
                        </{DropdownMenuGroup}>
                    </{DropdownMenu}>
                </{DropdownMenuTrigger}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
