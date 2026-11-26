from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
    SidebarRail,
)

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
            <{SidebarContent}>
                <{SidebarGroup}>
                    <{SidebarGroupLabel}>Table of Contents</{SidebarGroupLabel}>
                    <{SidebarGroupContent}>
                        <{SidebarMenu}>
                            {[t'''
                                <{SidebarMenuItem} key={item["title"]}>
                                    <{SidebarMenuButton} asChild>
                                        <a href={item["url"]} class="font-medium">{item["title"]}</a>
                                    </{SidebarMenuButton}>
                                    {t"""
                                        <{SidebarMenuSub}>
                                            {[t'''
                                                <{SidebarMenuSubItem} key={item["title"]}>
                                                    <{SidebarMenuSubButton}
                                                        asChild
                                                        isActive={item.get("isActive", False)}
                                                    >
                                                        <a href={item["url"]}>{item["title"]}</a>
                                                    </{SidebarMenuSubButton}>
                                                </{SidebarMenuSubItem}>
                                            ''' for item in item["items"]]}
                                        </{SidebarMenuSub}>
                                    """ if len(item["items"]) else None}
                                </{SidebarMenuItem}>
                            ''' for item in data["navMain"]]}
                        </{SidebarMenu}>
                    </{SidebarGroupContent}>
                </{SidebarGroup}>
            </{SidebarContent}>
            <{SidebarRail} />
        </{Sidebar}>
    """
