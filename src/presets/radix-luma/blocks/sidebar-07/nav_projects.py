from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
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
                        <{SidebarMenuButton} asChild>
                            <a href={item["url"]}>
                                {item["icon"]}
                                <span>{item["name"]}</span>
                            </a>
                        </{SidebarMenuButton}>
                        <{DropdownMenu}>
                            <{DropdownMenuTrigger} asChild>
                                <{SidebarMenuAction} showOnHover class="aria-expanded:bg-muted">
                                    <{MoreHorizontalIcon} />
                                    <span class="sr-only">More</span>
                                </{SidebarMenuAction}>
                            </{DropdownMenuTrigger}>
                            <{DropdownMenuContent}
                                class="w-fit"
                                side={"bottom" if is_mobile else "right"}
                                align={"end" if is_mobile else "start"}
                            >
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
                            </{DropdownMenuContent}>
                        </{DropdownMenu}>
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
