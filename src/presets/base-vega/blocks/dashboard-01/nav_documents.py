from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from sidebar import (
    SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction, SidebarMenuButton, SidebarMenuItem, use_sidebar,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon", "FolderIcon", "ShareIcon", "Trash2Icon"]}


def NavDocuments(items=None):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup} class="group-data-[collapsible=icon]:hidden">
            <{SidebarGroupLabel}>Documents</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{SidebarMenuItem} key={item["name"]}>
                        <{SidebarMenuButton} render={t"<a href={item["url"]} />"}>
                            {item["icon"]}
                            <span>{item["name"]}</span>
                        </{SidebarMenuButton}>
                        <{DropdownMenu}>
                            <{DropdownMenuTrigger} render={t"""<{SidebarMenuAction} showOnHover class="aria-expanded:bg-muted" />"""}>
                                <{MoreHorizontalIcon} />
                                <span class="sr-only">More</span>
                            </{DropdownMenuTrigger}>
                            <{DropdownMenuContent}
                                class="w-24"
                                side={"bottom" if is_mobile else "right"}
                                align={"end" if is_mobile else "start"}
                            >
                                <{DropdownMenuItem}>
                                    <{FolderIcon} />
                                    <span>Open</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{ShareIcon} />
                                    <span>Share</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuItem} variant="destructive">
                                    <{Trash2Icon} />
                                    <span>Delete</span>
                                </{DropdownMenuItem}>
                            </{DropdownMenuContent}>
                        </{DropdownMenu}>
                    </{SidebarMenuItem}>
                ''' for item in items]}
                <{SidebarMenuItem}>
                    <{SidebarMenuButton} class="text-sidebar-foreground/70">
                        <{MoreHorizontalIcon} class="text-sidebar-foreground/70" />
                        <span>More</span>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
