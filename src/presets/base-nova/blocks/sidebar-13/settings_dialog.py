from reacthon import use_state
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogTitle, DialogTrigger
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarProvider,
)

__js__ = {
    "lucide-react": [
        "BellIcon",
        "MenuIcon",
        "HomeIcon",
        "PaintbrushIcon",
        "MessageCircleIcon",
        "GlobeIcon",
        "KeyboardIcon",
        "CheckIcon",
        "VideoIcon",
        "LinkIcon",
        "LockIcon",
        "SettingsIcon",
    ],
}

data = {
    "nav": [
        {"name": "Notifications", "icon": t"<{BellIcon} />"},
        {"name": "Navigation", "icon": t"<{MenuIcon} />"},
        {"name": "Home", "icon": t"<{HomeIcon} />"},
        {"name": "Appearance", "icon": t"<{PaintbrushIcon} />"},
        {"name": "Messages & media", "icon": t"<{MessageCircleIcon} />"},
        {"name": "Language & region", "icon": t"<{GlobeIcon} />"},
        {"name": "Accessibility", "icon": t"<{KeyboardIcon} />"},
        {"name": "Mark as read", "icon": t"<{CheckIcon} />"},
        {"name": "Audio & video", "icon": t"<{VideoIcon} />"},
        {"name": "Connected accounts", "icon": t"<{LinkIcon} />"},
        {"name": "Privacy & visibility", "icon": t"<{LockIcon} />"},
        {"name": "Advanced", "icon": t"<{SettingsIcon} />"},
    ],
}


def SettingsDialog():
    open, set_open = use_state(True)
    return t"""
        <{Dialog} open={open} onOpenChange={set_open}>
            <{DialogTrigger} render={t'<{Button} size="sm" />'}>Open Dialog</{DialogTrigger}>
            <{DialogContent} class="overflow-hidden p-0 md:max-h-[500px] md:max-w-[700px] lg:max-w-[800px]">
                <{DialogTitle} class="sr-only">Settings</{DialogTitle}>
                <{DialogDescription} class="sr-only">Customize your settings here.</{DialogDescription}>
                <{SidebarProvider} class="items-start">
                    <{Sidebar} collapsible="none" class="hidden md:flex">
                        <{SidebarContent}>
                            <{SidebarGroup}>
                                <{SidebarGroupContent}>
                                    <{SidebarMenu}>
                                        {[t'''
                                            <{SidebarMenuItem} key={item["name"]}>
                                                <{SidebarMenuButton}
                                                    isActive={item["name"] == "Messages & media"}
                                                    render={t"""<a href="#" />"""}
                                                >
                                                    {item["icon"]}
                                                    <span>{item["name"]}</span>
                                                </{SidebarMenuButton}>
                                            </{SidebarMenuItem}>
                                        ''' for item in data["nav"]]}
                                    </{SidebarMenu}>
                                </{SidebarGroupContent}>
                            </{SidebarGroup}>
                        </{SidebarContent}>
                    </{Sidebar}>
                    <main class="flex h-[480px] flex-1 flex-col overflow-hidden">
                        <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
                            <div class="flex items-center gap-2 px-4">
                                <{Breadcrumb}>
                                    <{BreadcrumbList}>
                                        <{BreadcrumbItem} class="hidden md:block">
                                            <{BreadcrumbLink} href="#">Settings</{BreadcrumbLink}>
                                        </{BreadcrumbItem}>
                                        <{BreadcrumbSeparator} class="hidden md:block" />
                                        <{BreadcrumbItem}>
                                            <{BreadcrumbPage}>Messages & media</{BreadcrumbPage}>
                                        </{BreadcrumbItem}>
                                    </{BreadcrumbList}>
                                </{Breadcrumb}>
                            </div>
                        </header>
                        <div class="flex flex-1 flex-col gap-4 overflow-y-auto p-4 pt-0">
                            {[t'<div key={i} class="aspect-video max-w-3xl rounded-xl bg-muted/50" />' for i in range(10)]}
                        </div>
                    </main>
                </{SidebarProvider}>
            </{DialogContent}>
        </{Dialog}>
    """
