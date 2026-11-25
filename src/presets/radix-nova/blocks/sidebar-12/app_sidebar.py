from calendars import Calendars
from date_picker import DatePicker
from nav_user import NavUser
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarRail,
    SidebarSeparator,
)

__js__ = {"lucide-react": ["PlusIcon"]}

data = {
    "user": {"name": "shadcn", "email": "m@example.com", "avatar": "/avatars/shadcn.jpg"},
    "calendars": [
        {"name": "My Calendars", "items": ["Personal", "Work", "Family"]},
        {"name": "Favorites", "items": ["Holidays", "Birthdays"]},
        {"name": "Other", "items": ["Travel", "Reminders", "Deadlines"]},
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} ...{props}>
            <{SidebarHeader} class="h-16 border-b border-sidebar-border">
                <{NavUser} user={data["user"]} />
            </{SidebarHeader}>
            <{SidebarContent}>
                <{DatePicker} />
                <{SidebarSeparator} class="mx-0" />
                <{Calendars} calendars={data["calendars"]} />
            </{SidebarContent}>
            <{SidebarFooter}>
                <{SidebarMenu}>
                    <{SidebarMenuItem}>
                        <{SidebarMenuButton}>
                            <{PlusIcon} />
                            <span>New Calendar</span>
                        </{SidebarMenuButton}>
                    </{SidebarMenuItem}>
                </{SidebarMenu}>
            </{SidebarFooter}>
            <{SidebarRail} />
        </{Sidebar}>
    """
