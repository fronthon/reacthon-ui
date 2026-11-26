from reacthon import use_state
from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuTrigger
from item import Item, ItemActions, ItemContent, ItemDescription, ItemTitle
from label import Label
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
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

__js__ = {"lucide-react": ["ChevronsUpDownIcon", "CheckIcon", "SearchIcon"]}


def SidebarExample():
    data = {
        "versions": ["1.0.1", "1.1.0-alpha", "2.0.0-beta1"],
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

    selected_version, set_selected_version = use_state(data["versions"][0])

    def render_version(version):
        return t"""
            <{DropdownMenuItem}
                key={version}
                onAction={(lambda: set_selected_version(version))}
            >
                v{version}
                {" "}
                {version == selected_version and t'<{CheckIcon} class="ml-auto" />'}
            </{DropdownMenuItem}>
        """

    return t"""
        <{SidebarProvider}>
            <{Sidebar}>
                <{SidebarHeader}>
                    <{SidebarMenu}>
                        <{SidebarMenuItem}>
                            <{DropdownMenuTrigger}>
                                <{SidebarMenuButton}
                                    size="lg"
                                    class="aria-expanded:bg-sidebar-accent aria-expanded:text-sidebar-accent-foreground"
                                >
                                    <{Item} class="p-0" size="xs">
                                        <{ItemContent}>
                                            <{ItemTitle} class="text-sm">Documentation</{ItemTitle}>
                                            <{ItemDescription}>v{selected_version}</{ItemDescription}>
                                        </{ItemContent}>
                                        <{ItemActions}>
                                            <{ChevronsUpDownIcon} />
                                        </{ItemActions}>
                                    </{Item}>
                                </{SidebarMenuButton}>
                                <{DropdownMenu}>
                                    {[render_version(version) for version in data["versions"]]}
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{SidebarMenuItem}>
                    </{SidebarMenu}>
                    <form>
                        <{SidebarGroup} class="py-0">
                            <{SidebarGroupContent} class="relative">
                                <{Label} for="search" class="sr-only">Search</{Label}>
                                <{SidebarInput} id="search" placeholder="Search the docs..." class="pl-8" />
                                <{SearchIcon} class="pointer-events-none absolute top-1/2 left-2 size-4 -translate-y-1/2 opacity-50 select-none" />
                            </{SidebarGroupContent}>
                        </{SidebarGroup}>
                    </form>
                </{SidebarHeader}>
                <{SidebarContent}>
                    {[t'''
                        <{SidebarGroup} key={item["title"]}>
                            <{SidebarGroupLabel}>{item["title"]}</{SidebarGroupLabel}>
                            <{SidebarGroupContent}>
                                <{SidebarMenu}>
                                    {[t"""
                                        <{SidebarMenuItem} key={sub_item["title"]}>
                                            <{SidebarMenuButton}
                                                href={sub_item["url"]}
                                                isActive={sub_item.get("isActive", False)}
                                            >
                                                {sub_item["title"]}
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                    """ for sub_item in item["items"]]}
                                </{SidebarMenu}>
                            </{SidebarGroupContent}>
                        </{SidebarGroup}>
                    ''' for item in data["navMain"]]}
                </{SidebarContent}>
                <{SidebarRail} />
            </{Sidebar}>
            <{SidebarInset}>
                <header class="flex h-16 shrink-0 items-center gap-2 px-4">
                    <{SidebarTrigger} class="-ml-1" />
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4">
                    <div class="grid auto-rows-min gap-4 md:grid-cols-3">
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                    </div>
                    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
                </div>
            </{SidebarInset}>
        </{SidebarProvider}>
    """
