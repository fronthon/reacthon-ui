from nav_main import NavMain
from nav_projects import NavProjects
from nav_user import NavUser
from team_switcher import TeamSwitcher
from sidebar import Sidebar, SidebarContent, SidebarFooter, SidebarHeader, SidebarRail

__js__ = {
    "lucide-react": [
        "GalleryVerticalEndIcon",
        "AudioLinesIcon",
        "TerminalIcon",
        "TerminalSquareIcon",
        "BotIcon",
        "BookOpenIcon",
        "Settings2Icon",
        "FrameIcon",
        "PieChartIcon",
        "MapIcon",
    ],
}

data = {
    "user": {"name": "shadcn", "email": "m@example.com", "avatar": "/avatars/shadcn.jpg"},
    "teams": [
        {"name": "Acme Inc", "logo": t"<{GalleryVerticalEndIcon} />", "plan": "Enterprise"},
        {"name": "Acme Corp.", "logo": t"<{AudioLinesIcon} />", "plan": "Startup"},
        {"name": "Evil Corp.", "logo": t"<{TerminalIcon} />", "plan": "Free"},
    ],
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
    "projects": [
        {"name": "Design Engineering", "url": "#", "icon": t"<{FrameIcon} />"},
        {"name": "Sales & Marketing", "url": "#", "icon": t"<{PieChartIcon} />"},
        {"name": "Travel", "url": "#", "icon": t"<{MapIcon} />"},
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} collapsible="icon" ...{props}>
            <{SidebarHeader}>
                <{TeamSwitcher} teams={data["teams"]} />
            </{SidebarHeader}>
            <{SidebarContent}>
                <{NavMain} items={data["navMain"]} />
                <{NavProjects} projects={data["projects"]} />
            </{SidebarContent}>
            <{SidebarFooter}>
                <{NavUser} user={data["user"]} />
            </{SidebarFooter}>
            <{SidebarRail} />
        </{Sidebar}>
    """
