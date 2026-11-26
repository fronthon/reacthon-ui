from nav_documents import NavDocuments
from nav_main import NavMain
from nav_secondary import NavSecondary
from nav_user import NavUser
from sidebar import (
    Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarMenu, SidebarMenuButton, SidebarMenuItem,
)

__js__ = {
    "lucide-react": [
        "LayoutDashboardIcon",
        "ListIcon",
        "ChartBarIcon",
        "FolderIcon",
        "UsersIcon",
        "CameraIcon",
        "FileTextIcon",
        "Settings2Icon",
        "CircleHelpIcon",
        "SearchIcon",
        "DatabaseIcon",
        "FileChartColumnIcon",
        "FileIcon",
        "CommandIcon",
    ],
}

data = {
    "user": {"name": "shadcn", "email": "m@example.com", "avatar": "/avatars/shadcn.jpg"},
    "navMain": [
        {"title": "Dashboard", "url": "#", "icon": t"<{LayoutDashboardIcon} />"},
        {"title": "Lifecycle", "url": "#", "icon": t"<{ListIcon} />"},
        {"title": "Analytics", "url": "#", "icon": t"<{ChartBarIcon} />"},
        {"title": "Projects", "url": "#", "icon": t"<{FolderIcon} />"},
        {"title": "Team", "url": "#", "icon": t"<{UsersIcon} />"},
    ],
    "navClouds": [
        {
            "title": "Capture",
            "icon": t"<{CameraIcon} />",
            "isActive": True,
            "url": "#",
            "items": [{"title": "Active Proposals", "url": "#"}, {"title": "Archived", "url": "#"}],
        },
        {
            "title": "Proposal",
            "icon": t"<{FileTextIcon} />",
            "url": "#",
            "items": [{"title": "Active Proposals", "url": "#"}, {"title": "Archived", "url": "#"}],
        },
        {
            "title": "Prompts",
            "icon": t"<{FileTextIcon} />",
            "url": "#",
            "items": [{"title": "Active Proposals", "url": "#"}, {"title": "Archived", "url": "#"}],
        },
    ],
    "navSecondary": [
        {"title": "Settings", "url": "#", "icon": t"<{Settings2Icon} />"},
        {"title": "Get Help", "url": "#", "icon": t"<{CircleHelpIcon} />"},
        {"title": "Search", "url": "#", "icon": t"<{SearchIcon} />"},
    ],
    "documents": [
        {"name": "Data Library", "url": "#", "icon": t"<{DatabaseIcon} />"},
        {"name": "Reports", "url": "#", "icon": t"<{FileChartColumnIcon} />"},
        {"name": "Word Assistant", "url": "#", "icon": t"<{FileIcon} />"},
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} collapsible="offcanvas" ...{props}>
            <{SidebarHeader}>
                <{SidebarMenu}>
                    <{SidebarMenuItem}>
                        <{SidebarMenuButton} class="data-[slot=sidebar-menu-button]:p-1.5!" render={t'<a href="#" />'}>
                            <{CommandIcon} class="size-5!" />
                            <span class="text-base font-semibold">Acme Inc.</span>
                        </{SidebarMenuButton}>
                    </{SidebarMenuItem}>
                </{SidebarMenu}>
            </{SidebarHeader}>
            <{SidebarContent}>
                <{NavMain} items={data["navMain"]} />
                <{NavDocuments} items={data["documents"]} />
                <{NavSecondary} items={data["navSecondary"]} class="mt-auto" />
            </{SidebarContent}>
            <{SidebarFooter}>
                <{NavUser} user={data["user"]} />
            </{SidebarFooter}>
        </{Sidebar}>
    """
