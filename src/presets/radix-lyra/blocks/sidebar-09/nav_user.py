from avatar import Avatar, AvatarFallback, AvatarImage
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
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


def NavUser(user=None, **_):
    is_mobile = use_sidebar().get("isMobile")

    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenu}>
                    <{DropdownMenuTrigger} asChild>
                        <{SidebarMenuButton}
                            size="lg"
                            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground md:h-8 md:p-0"
                        >
                            <{Avatar} class="h-8 w-8 rounded-lg">
                                <{AvatarImage} src={user["avatar"]} alt={user["name"]} />
                                <{AvatarFallback} class="rounded-lg">CN</{AvatarFallback}>
                            </{Avatar}>
                            <div class="grid flex-1 text-left text-sm leading-tight">
                                <span class="truncate font-medium">{user["name"]}</span>
                                <span class="truncate text-xs">{user["email"]}</span>
                            </div>
                            <{ChevronsUpDownIcon} class="ml-auto size-4" />
                        </{SidebarMenuButton}>
                    </{DropdownMenuTrigger}>
                    <{DropdownMenuContent}
                        class="w-(--radix-dropdown-menu-trigger-width) min-w-56 rounded-lg"
                        side={"bottom" if is_mobile else "right"}
                        align="end"
                        sideOffset={4}
                    >
                        <{DropdownMenuLabel} class="p-0 font-normal">
                            <div class="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
                                <{Avatar} class="h-8 w-8 rounded-lg">
                                    <{AvatarImage} src={user["avatar"]} alt={user["name"]} />
                                    <{AvatarFallback} class="rounded-lg">CN</{AvatarFallback}>
                                </{Avatar}>
                                <div class="grid flex-1 text-left text-sm leading-tight">
                                    <span class="truncate font-medium">{user["name"]}</span>
                                    <span class="truncate text-xs">{user["email"]}</span>
                                </div>
                            </div>
                        </{DropdownMenuLabel}>
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
                        <{DropdownMenuItem}>
                            <{LogOutIcon} />
                            Log out
                        </{DropdownMenuItem}>
                    </{DropdownMenuContent}>
                </{DropdownMenu}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
