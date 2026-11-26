from search_form import SearchForm
from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
    SidebarRail,
)

__js__ = {"lucide-react": ["GalleryVerticalEndIcon", "PlusIcon", "MinusIcon"]}

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
        {"title": "Community", "url": "#", "items": [{"title": "Contribution Guide", "url": "#"}]},
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} ...{props}>
            <{SidebarHeader}>
                <{SidebarMenu}>
                    <{SidebarMenuItem}>
                        <{SidebarMenuButton} size="lg" render={t'<a href="#" />'}>
                            <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                                <{GalleryVerticalEndIcon} class="size-4" />
                            </div>
                            <div class="flex flex-col gap-0.5 leading-none">
                                <span class="font-medium">Documentation</span>
                                <span class="">v1.0.0</span>
                            </div>
                        </{SidebarMenuButton}>
                    </{SidebarMenuItem}>
                </{SidebarMenu}>
                <{SearchForm} />
            </{SidebarHeader}>
            <{SidebarContent}>
                <{SidebarGroup}>
                    <{SidebarMenu}>
                        {[t'''
                            <{Collapsible} key={item["title"]} defaultOpen={index == 1} class="group/collapsible">
                                <{SidebarMenuItem}>
                                    <{SidebarMenuButton} render={t"<{CollapsibleTrigger} />"}>
                                        {item["title"]}
                                        {" "}
                                        <{PlusIcon} class="ml-auto group-aria-expanded/menu-button:hidden" />
                                        <{MinusIcon} class="ml-auto hidden group-aria-expanded/menu-button:block" />
                                    </{SidebarMenuButton}>
                                    {t"""
                                        <{CollapsibleContent}>
                                            <{SidebarMenuSub}>
                                                {[t'''
                                                    <{SidebarMenuSubItem} key={item["title"]}>
                                                        <{SidebarMenuSubButton}
                                                            isActive={item.get("isActive", False)}
                                                            render={t"<a href={item["url"]} />"}
                                                        >
                                                            {item["title"]}
                                                        </{SidebarMenuSubButton}>
                                                    </{SidebarMenuSubItem}>
                                                ''' for item in item["items"]]}
                                            </{SidebarMenuSub}>
                                        </{CollapsibleContent}>
                                    """ if len(item["items"]) else None}
                                </{SidebarMenuItem}>
                            </{Collapsible}>
                        ''' for index, item in enumerate(data["navMain"])]}
                    </{SidebarMenu}>
                </{SidebarGroup}>
            </{SidebarContent}>
            <{SidebarRail} />
        </{Sidebar}>
    """
