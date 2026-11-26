from search_form import SearchForm
from version_switcher import VersionSwitcher
from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarRail,
)

__js__ = {"lucide-react": ["ChevronRightIcon"]}

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
        {"title": "Community", "url": "#", "items": [{"title": "Contribution Guide", "url": "#"}]},
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} ...{props}>
            <{SidebarHeader}>
                <{VersionSwitcher} versions={data["versions"]} defaultVersion={data["versions"][0]} />
                <{SearchForm} />
            </{SidebarHeader}>
            <{SidebarContent} class="gap-0">
                {[t'''
                    <{Collapsible} key={item["title"]} title={item["title"]} defaultOpen class="group/collapsible">
                        <{SidebarGroup}>
                            <{SidebarGroupLabel}
                                class="group/label text-sm text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
                                render={t"<{CollapsibleTrigger} />"}
                            >
                                {item["title"]}
                                {" "}
                                <{ChevronRightIcon} class="ml-auto transition-transform group-data-open/collapsible:rotate-90" />
                            </{SidebarGroupLabel}>
                            <{CollapsibleContent}>
                                <{SidebarGroupContent}>
                                    <{SidebarMenu}>
                                        {[t"""
                                            <{SidebarMenuItem} key={item["title"]}>
                                                <{SidebarMenuButton}
                                                    isActive={item.get("isActive", False)}
                                                    render={t'<a href={item["url"]} />'}
                                                >
                                                    {item["title"]}
                                                </{SidebarMenuButton}>
                                            </{SidebarMenuItem}>
                                        """ for item in item["items"]]}
                                    </{SidebarMenu}>
                                </{SidebarGroupContent}>
                            </{CollapsibleContent}>
                        </{SidebarGroup}>
                    </{Collapsible}>
                ''' for item in data["navMain"]]}
            </{SidebarContent}>
            <{SidebarRail} />
        </{Sidebar}>
    """
