from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from sidebar import (
    SidebarGroup, SidebarGroupLabel, SidebarMenu, SidebarMenuAction, SidebarMenuButton, SidebarMenuItem, use_sidebar,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon", "FolderIcon", "ShareIcon", "Trash2Icon"]}


def NavProjects(projects=None):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup} class="group-data-[collapsible=icon]:hidden">
            <{SidebarGroupLabel}>Projects</{SidebarGroupLabel}>
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
                                class="w-48"
                                side={"bottom" if is_mobile else "right"}
                                align={"end" if is_mobile else "start"}
                            >
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
                            </{DropdownMenuContent}>
                        </{DropdownMenu}>
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
