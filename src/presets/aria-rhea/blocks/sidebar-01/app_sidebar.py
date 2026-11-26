from search_form import SearchForm
from version_switcher import VersionSwitcher
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


def AppSidebar(**props):
    return t"""
        <{Sidebar} ...{props}>
            <{SidebarHeader}>
                <{VersionSwitcher} versions={data["versions"]} defaultVersion={data["versions"][0]} />
                <{SearchForm} />
            </{SidebarHeader}>
            <{SidebarContent}>
                {[t'''
                    <{SidebarGroup} key={item["title"]}>
                        <{SidebarGroupLabel}>{item["title"]}</{SidebarGroupLabel}>
                        <{SidebarGroupContent}>
                            <{SidebarMenu}>
                                {[t"""
                                    <{SidebarMenuItem} key={item["title"]}>
                                        <{SidebarMenuButton} href={item["url"]} isActive={item.get("isActive", False)}>
                                            {item["title"]}
                                        </{SidebarMenuButton}>
                                    </{SidebarMenuItem}>
                                """ for item in item["items"]]}
                            </{SidebarMenu}>
                        </{SidebarGroupContent}>
                    </{SidebarGroup}>
                ''' for item in data["navMain"]]}
            </{SidebarContent}>
            <{SidebarRail} />
        </{Sidebar}>
    """
