from avatar import Avatar, AvatarFallback, AvatarImage
from dropdown_menu import (
    DropdownMenu, DropdownMenuGroup, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger,
)
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {"lucide-react": ["EllipsisVerticalIcon", "CircleUserRoundIcon", "CreditCardIcon", "BellIcon", "LogOutIcon"]}


def NavUser(user=None):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenuTrigger}>
                    <{SidebarMenuButton} size="lg" class="aria-expanded:bg-muted">
                        <{Avatar} class="size-8 rounded-lg grayscale">
                            <{AvatarImage} src={user["avatar"]} alt={user["name"]} />
                            <{AvatarFallback} class="rounded-lg">CN</{AvatarFallback}>
                        </{Avatar}>
                        <div class="grid flex-1 text-left text-sm leading-tight">
                            <span class="truncate font-medium">{user["name"]}</span>
                            <span class="truncate text-xs text-foreground/70">{user["email"]}</span>
                        </div>
                        <{EllipsisVerticalIcon} class="ml-auto size-4" />
                    </{SidebarMenuButton}>
                    <{DropdownMenu} class="min-w-56" placement={"bottom end" if is_mobile else "right bottom"} offset={4}>
                        <{DropdownMenuGroup}>
                            <{DropdownMenuLabel} class="p-0 font-normal">
                                <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                                    <{Avatar} class="size-8">
                                        <{AvatarImage} src={user["avatar"]} alt={user["name"]} />
                                        <{AvatarFallback} class="rounded-lg">CN</{AvatarFallback}>
                                    </{Avatar}>
                                    <div class="grid flex-1 text-left text-sm leading-tight">
                                        <span class="truncate font-medium">{user["name"]}</span>
                                        <span class="truncate text-xs text-muted-foreground">{user["email"]}</span>
                                    </div>
                                </div>
                            </{DropdownMenuLabel}>
                        </{DropdownMenuGroup}>
                        <{DropdownMenuSeparator} />
                        <{DropdownMenuGroup}>
                            <{DropdownMenuItem}>
                                <{CircleUserRoundIcon} />
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
                            Log out
                        </{DropdownMenuItem}>
                    </{DropdownMenu}>
                </{DropdownMenuTrigger}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
