from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuAction,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
)

__js__ = {"lucide-react": ["ChevronRightIcon", "PlusIcon", "MoreHorizontalIcon"]}


def NavWorkspaces(workspaces=None):
    return t"""
        <{SidebarGroup}>
            <{SidebarGroupLabel}>Workspaces</{SidebarGroupLabel}>
            <{SidebarGroupContent}>
                <{SidebarMenu}>
                    {[t'''
                        <{Collapsible} key={workspace["name"]}>
                            <{SidebarMenuItem}>
                                <{SidebarMenuButton} asChild>
                                    <a href="#">
                                        <span>{workspace["emoji"]}</span>
                                        <span>{workspace["name"]}</span>
                                    </a>
                                </{SidebarMenuButton}>
                                <{CollapsibleTrigger} asChild>
                                    <{SidebarMenuAction}
                                        class="left-2 bg-sidebar-accent text-sidebar-accent-foreground data-[state=open]:rotate-90"
                                        showOnHover
                                    >
                                        <{ChevronRightIcon} />
                                    </{SidebarMenuAction}>
                                </{CollapsibleTrigger}>
                                <{SidebarMenuAction} showOnHover>
                                    <{PlusIcon} />
                                </{SidebarMenuAction}>
                                <{CollapsibleContent}>
                                    <{SidebarMenuSub}>
                                        {[t"""
                                            <{SidebarMenuSubItem} key={page["name"]}>
                                                <{SidebarMenuSubButton} asChild>
                                                    <a href="#">
                                                        <span>{page["emoji"]}</span>
                                                        <span>{page["name"]}</span>
                                                    </a>
                                                </{SidebarMenuSubButton}>
                                            </{SidebarMenuSubItem}>
                                        """ for page in workspace["pages"]]}
                                    </{SidebarMenuSub}>
                                </{CollapsibleContent}>
                            </{SidebarMenuItem}>
                        </{Collapsible}>
                    ''' for workspace in workspaces]}
                    <{SidebarMenuItem}>
                        <{SidebarMenuButton} class="text-sidebar-foreground/70">
                            <{MoreHorizontalIcon} />
                            <span>More</span>
                        </{SidebarMenuButton}>
                    </{SidebarMenuItem}>
                </{SidebarMenu}>
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
