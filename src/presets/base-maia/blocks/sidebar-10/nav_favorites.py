from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from sidebar import (
    SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction, SidebarMenuButton, SidebarMenuItem, use_sidebar,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon", "StarOffIcon", "LinkIcon", "ArrowUpRightIcon", "Trash2Icon"]}


def NavFavorites(favorites=None, **_):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup} class="group-data-[collapsible=icon]:hidden">
            <{SidebarGroupLabel}>Favorites</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{SidebarMenuItem} key={item["name"]}>
                        <{SidebarMenuButton} render={t"<a href={item["url"]} title={item["name"]} />"}>
                            <span>{item["emoji"]}</span>
                            <span>{item["name"]}</span>
                        </{SidebarMenuButton}>
                        <{DropdownMenu}>
                            <{DropdownMenuTrigger} render={t"""<{SidebarMenuAction} showOnHover class="aria-expanded:bg-muted" />"""}>
                                <{MoreHorizontalIcon} />
                                <span class="sr-only">More</span>
                            </{DropdownMenuTrigger}>
                            <{DropdownMenuContent}
                                class="w-56 rounded-lg"
                                side={"bottom" if is_mobile else "right"}
                                align={"end" if is_mobile else "start"}
                            >
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem}>
                                        <{StarOffIcon} class="text-muted-foreground" />
                                        <span>Remove from Favorites</span>
                                    </{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
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
                                </{DropdownMenuGroup}>
                            </{DropdownMenuContent}>
                        </{DropdownMenu}>
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
