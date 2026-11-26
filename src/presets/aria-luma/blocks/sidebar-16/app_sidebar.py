from nav_main import NavMain
from nav_projects import NavProjects
from nav_secondary import NavSecondary
from nav_user import NavUser
from sidebar import (
    Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarMenu, SidebarMenuButton, SidebarMenuItem,
)

__js__ = {
    "lucide-react": [
        "TerminalSquareIcon",
        "BotIcon",
        "BookOpenIcon",
        "Settings2Icon",
        "LifeBuoyIcon",
        "SendIcon",
        "FrameIcon",
        "PieChartIcon",
        "MapIcon",
        "TerminalIcon",
    ],
}

data = {
    "user": {"name": "shadcn", "email": "m@example.com", "avatar": "/avatars/shadcn.jpg"},
    "navMain": [
        {
            "title": "Playground",
            "url": "#",
            "icon": t"<{TerminalSquareIcon} />",
            "isActive": True,
            "items": [
                {"title": "History", "url": "#"},
                {"title": "Starred", "url": "#"},
                {"title": "Settings", "url": "#"},
            ],
        },
        {
            "title": "Models",
            "url": "#",
            "icon": t"<{BotIcon} />",
            "items": [
                {"title": "Genesis", "url": "#"},
                {"title": "Explorer", "url": "#"},
                {"title": "Quantum", "url": "#"},
            ],
        },
        {
            "title": "Documentation",
            "url": "#",
            "icon": t"<{BookOpenIcon} />",
            "items": [
                {"title": "Introduction", "url": "#"},
                {"title": "Get Started", "url": "#"},
                {"title": "Tutorials", "url": "#"},
                {"title": "Changelog", "url": "#"},
            ],
        },
        {
            "title": "Settings",
            "url": "#",
            "icon": t"<{Settings2Icon} />",
            "items": [
                {"title": "General", "url": "#"},
                {"title": "Team", "url": "#"},
                {"title": "Billing", "url": "#"},
                {"title": "Limits", "url": "#"},
            ],
        },
    ],
    "navSecondary": [
        {"title": "Support", "url": "#", "icon": t"<{LifeBuoyIcon} />"},
        {"title": "Feedback", "url": "#", "icon": t"<{SendIcon} />"},
    ],
    "projects": [
        {"name": "Design Engineering", "url": "#", "icon": t"<{FrameIcon} />"},
        {"name": "Sales & Marketing", "url": "#", "icon": t"<{PieChartIcon} />"},
        {"name": "Travel", "url": "#", "icon": t"<{MapIcon} />"},
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} class="top-(--header-height) h-[calc(100svh-var(--header-height))]!" ...{props}>
            <{SidebarHeader}>
                <{SidebarMenu}>
                    <{SidebarMenuItem}>
                        <{SidebarMenuButton} href="#" size="lg">
                            <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                                <{TerminalIcon} class="size-4" />
                            </div>
                            <div class="grid flex-1 text-left text-sm leading-tight">
                                <span class="truncate font-medium">Acme Inc</span>
                                <span class="truncate text-xs">Enterprise</span>
                            </div>
                        </{SidebarMenuButton}>
                    </{SidebarMenuItem}>
                </{SidebarMenu}>
            </{SidebarHeader}>
            <{SidebarContent}>
                <{NavMain} items={data["navMain"]} />
                <{NavProjects} projects={data["projects"]} />
                <{NavSecondary} items={data["navSecondary"]} class="mt-auto" />
            </{SidebarContent}>
            <{SidebarFooter}>
                <{NavUser} user={data["user"]} />
            </{SidebarFooter}>
        </{Sidebar}>
    """
