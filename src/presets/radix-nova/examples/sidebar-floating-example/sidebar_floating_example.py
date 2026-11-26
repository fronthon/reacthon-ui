from button import Button
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
from dropdown_menu import DropdownMenu, DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuTrigger
from field import Field
from item import Item, ItemContent, ItemDescription, ItemTitle
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarHeader,
    SidebarInput,
    SidebarInset,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarProvider,
    SidebarRail,
    SidebarTrigger,
)

__js__ = {"lucide-react": ["MoreHorizontalIcon"]}


def SidebarFloatingExample():
    data = {
        "navMain": [
            {
                "title": "Getting Started",
                "url": "#",
                "items": [{"title": "Installation", "url": "#"}, {"title": "Project Structure", "url": "#"}],
            },
            {
                "title": "Build Your Application",
                "url": "#",
                "items": [
                    {"title": "Routing", "url": "#"},
                    {"title": "Data Fetching", "url": "#", "isActive": True},
                    {"title": "Rendering", "url": "#"},
                    {"title": "Caching", "url": "#"},
                    {"title": "Styling", "url": "#"},
                    {"title": "Optimizing", "url": "#"},
                    {"title": "Configuring", "url": "#"},
                    {"title": "Testing", "url": "#"},
                    {"title": "Authentication", "url": "#"},
                    {"title": "Deploying", "url": "#"},
                    {"title": "Upgrading", "url": "#"},
                    {"title": "Examples", "url": "#"},
                ],
            },
            {
                "title": "API Reference",
                "url": "#",
                "items": [
                    {"title": "Components", "url": "#"},
                    {"title": "File Conventions", "url": "#"},
                    {"title": "Functions", "url": "#"},
                    {"title": "next.config.js Options", "url": "#"},
                    {"title": "CLI", "url": "#"},
                    {"title": "Edge Runtime", "url": "#"},
                ],
            },
            {
                "title": "Architecture",
                "url": "#",
                "items": [
                    {"title": "Accessibility", "url": "#"},
                    {"title": "Fast Refresh", "url": "#"},
                    {"title": "Next.js Compiler", "url": "#"},
                    {"title": "Supported Browsers", "url": "#"},
                    {"title": "Turbopack", "url": "#"},
                ],
            },
        ],
    }

    return t"""
        <{SidebarProvider} class="bg-background">
            <{Sidebar} variant="floating">
                <{SidebarHeader}>
                    <{SidebarMenu}>
                        <{SidebarMenuItem}>
                            <{SidebarMenuButton} size="lg" asChild>
                                <a href="#">
                                    <{Item} class="p-0" size="xs">
                                        <{ItemContent}>
                                            <{ItemTitle} class="text-sm">Documentation</{ItemTitle}>
                                            <{ItemDescription}>v1.0.0</{ItemDescription}>
                                        </{ItemContent}>
                                    </{Item}>
                                </a>
                            </{SidebarMenuButton}>
                        </{SidebarMenuItem}>
                    </{SidebarMenu}>
                </{SidebarHeader}>
                <{SidebarContent}>
                    <{SidebarGroup}>
                        <{SidebarMenu}>
                            {[t'''
                                <{DropdownMenu} key={item["title"]}>
                                    <{SidebarMenuItem}>
                                        <{DropdownMenuTrigger} asChild>
                                            <{SidebarMenuButton} class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground">
                                                {item["title"]}
                                                {" "}
                                                <{MoreHorizontalIcon} class="ml-auto" />
                                            </{SidebarMenuButton}>
                                        </{DropdownMenuTrigger}>
                                        {t"""
                                            <{DropdownMenuContent} side="right" align="start">
                                                <{DropdownMenuGroup}>
                                                    {[t'''
                                                        <{DropdownMenuItem} asChild key={sub_item["title"]}>
                                                            <a href={sub_item["url"]}>{sub_item["title"]}</a>
                                                        </{DropdownMenuItem}>
                                                    ''' for sub_item in item["items"]]}
                                                </{DropdownMenuGroup}>
                                            </{DropdownMenuContent}>
                                        """ if len(item["items"]) else None}
                                    </{SidebarMenuItem}>
                                </{DropdownMenu}>
                            ''' for item in data["navMain"]]}
                        </{SidebarMenu}>
                    </{SidebarGroup}>
                </{SidebarContent}>
                <{SidebarFooter}>
                    <{SidebarGroup} class="pb-1">
                        <{Card} size="sm" class="-mx-1">
                            <{CardHeader}>
                                <{CardTitle} class="text-sm">Subscribe to our newsletter</{CardTitle}>
                                <{CardDescription}>
                                    Opt-in to receive updates and news about the sidebar.
                                </{CardDescription}>
                            </{CardHeader}>
                            <{CardContent}>
                                <form>
                                    <{Field}>
                                        <{SidebarInput} type="email" placeholder="Email" />
                                        <{Button}
                                            class="w-full bg-sidebar-primary text-sidebar-primary-foreground"
                                            size="sm"
                                        >
                                            Subscribe
                                        </{Button}>
                                    </{Field}>
                                </form>
                            </{CardContent}>
                        </{Card}>
                    </{SidebarGroup}>
                </{SidebarFooter}>
                <{SidebarRail} />
            </{Sidebar}>
            <{SidebarInset}>
                <header class="flex h-16 shrink-0 items-center gap-2 px-4">
                    <{SidebarTrigger} class="-ml-1" />
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
                    <div class="grid auto-rows-min gap-4 md:grid-cols-3">
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                    </div>
                    <div class="min-h-screen flex-1 rounded-xl bg-muted/50 md:min-h-min" />
                </div>
            </{SidebarInset}>
        </{SidebarProvider}>
    """
