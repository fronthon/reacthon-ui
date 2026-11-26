from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger
from sidebar import (
    SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction, SidebarMenuButton, SidebarMenuItem, use_sidebar,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon", "FolderIcon", "ShareIcon", "Trash2Icon"]}


def NavProjects(projects=None, **_):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup} class="group-data-[collapsible=icon]:hidden">
            <{SidebarGroupLabel}>Projects</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{SidebarMenuItem} key={item["name"]}>
                        <{SidebarMenuButton} href={item["url"]}>
                            {item["icon"]}
                            <span>{item["name"]}</span>
                        </{SidebarMenuButton}>
                        <{DropdownMenuTrigger}>
                            <{SidebarMenuAction} showOnHover class="aria-expanded:bg-muted">
                                <{MoreHorizontalIcon} />
                                <span class="sr-only">More</span>
                            </{SidebarMenuAction}>
                            <{DropdownMenu} class="w-48" placement={"bottom end" if is_mobile else "right top"}>
                                <{DropdownMenuItem}>
                                    <{FolderIcon} class="text-muted-foreground" />
                                    <span>View Project</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{ShareIcon} class="text-muted-foreground" />
                                    <span>Share Project</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuItem}>
                                    <{Trash2Icon} class="text-muted-foreground" />
                                    <span>Delete Project</span>
                                </{DropdownMenuItem}>
                            </{DropdownMenu}>
                        </{DropdownMenuTrigger}>
                    </{SidebarMenuItem}>
                ''' for item in projects]}
                <{SidebarMenuItem}>
                    <{SidebarMenuButton}>
                        <{MoreHorizontalIcon} />
                        <span>More</span>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
