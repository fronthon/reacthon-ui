from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger
from sidebar import (
    SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction, SidebarMenuButton, SidebarMenuItem, use_sidebar,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon", "FolderIcon", "ArrowRightIcon", "Trash2Icon"]}


def NavProjects(projects=None):
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
                            <{DropdownMenu} class="w-fit" placement={"bottom end" if is_mobile else "right top"}>
                                <{DropdownMenuItem}>
                                    <{FolderIcon} />
                                    <span>View Project</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{ArrowRightIcon} />
                                    <span>Share Project</span>
                                </{DropdownMenuItem}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuItem} variant="destructive">
                                    <{Trash2Icon} />
                                    <span>Delete Project</span>
                                </{DropdownMenuItem}>
                            </{DropdownMenu}>
                        </{DropdownMenuTrigger}>
                    </{SidebarMenuItem}>
                ''' for item in projects]}
                <{SidebarMenuItem}>
                    <{SidebarMenuButton} class="text-sidebar-foreground/70">
                        <{MoreHorizontalIcon} class="text-sidebar-foreground/70" />
                        <span>More</span>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
