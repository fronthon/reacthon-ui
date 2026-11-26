from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger
from sidebar import (
    SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction, SidebarMenuButton, SidebarMenuItem, use_sidebar,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon", "StarOffIcon", "LinkIcon", "ArrowUpRightIcon", "Trash2Icon"]}


def NavFavorites(favorites=None):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup} class="group-data-[collapsible=icon]:hidden">
            <{SidebarGroupLabel}>Favorites</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{SidebarMenuItem} key={item["name"]}>
                        <{SidebarMenuButton} href={item["url"]} tooltip={item["name"]}>
                            <span>{item["emoji"]}</span>
                            <span>{item["name"]}</span>
                        </{SidebarMenuButton}>
                        <{DropdownMenuTrigger}>
                            <{SidebarMenuAction} showOnHover class="aria-expanded:bg-muted">
                                <{MoreHorizontalIcon} />
                                <span class="sr-only">More</span>
                            </{SidebarMenuAction}>
                            <{DropdownMenu}
                                class="w-56 rounded-lg"
                                placement={"bottom end" if is_mobile else "right top"}
                            >
                                <{DropdownMenuItem}>
                                    <{StarOffIcon} class="text-muted-foreground" />
                                    <span>Remove from Favorites</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuItem}>
                                    <{LinkIcon} class="text-muted-foreground" />
                                    <span>Copy Link</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{ArrowUpRightIcon} class="text-muted-foreground" />
                                    <span>Open in New Tab</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuItem}>
                                    <{Trash2Icon} class="text-muted-foreground" />
                                    <span>Delete</span>
                                </{DropdownMenuItem}>
                            </{DropdownMenu}>
                        </{DropdownMenuTrigger}>
                    </{SidebarMenuItem}>
                ''' for item in favorites]}
                <{SidebarMenuItem}>
                    <{SidebarMenuButton} class="text-sidebar-foreground/70">
                        <{MoreHorizontalIcon} />
                        <span>More</span>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
