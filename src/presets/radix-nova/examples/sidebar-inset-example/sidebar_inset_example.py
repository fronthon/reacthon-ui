from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarInset,
    SidebarMenu,
    SidebarMenuAction,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
    SidebarProvider,
    SidebarRail,
    SidebarTrigger,
)

__js__ = {
    "lucide-react": [
        "HomeIcon",
        "ChartLineIcon",
        "ShoppingBagIcon",
        "ShoppingCartIcon",
        "FileIcon",
        "UserIcon",
        "Settings2Icon",
        "LifeBuoy",
        "Send",
        "ChevronRightIcon",
    ],
}


def SidebarInsetExample():
    data = {
        "navMain": [
            {
                "title": "Dashboard",
                "url": "#",
                "icon": t"<{HomeIcon} />",
                "isActive": True,
                "items": [{"title": "Overview", "url": "#"}, {"title": "Analytics", "url": "#"}],
            },
            {
                "title": "Analytics",
                "url": "#",
                "icon": t"<{ChartLineIcon} />",
                "items": [{"title": "Reports", "url": "#"}, {"title": "Metrics", "url": "#"}],
            },
            {
                "title": "Orders",
                "url": "#",
                "icon": t"<{ShoppingBagIcon} />",
                "items": [
                    {"title": "All Orders", "url": "#"},
                    {"title": "Pending", "url": "#"},
                    {"title": "Completed", "url": "#"},
                ],
            },
            {
                "title": "Products",
                "url": "#",
                "icon": t"<{ShoppingCartIcon} />",
                "items": [{"title": "All Products", "url": "#"}, {"title": "Categories", "url": "#"}],
            },
            {"title": "Invoices", "url": "#", "icon": t"<{FileIcon} />"},
            {"title": "Customers", "url": "#", "icon": t"<{UserIcon} />"},
            {"title": "Settings", "url": "#", "icon": t"<{Settings2Icon} />"},
        ],
        "navSecondary": [
            {"title": "Support", "url": "#", "icon": t"<{LifeBuoy} />"},
            {"title": "Feedback", "url": "#", "icon": t"<{Send} />"},
        ],
    }

    return t"""
        <{SidebarProvider}>
            <{Sidebar} variant="inset">
                <{SidebarContent}>
                    <{SidebarGroup}>
                        <{SidebarGroupLabel}>Dashboard</{SidebarGroupLabel}>
                        <{SidebarMenu}>
                            {[t'''
                                <{Collapsible} key={item["title"]} asChild defaultOpen={item.get("isActive")}>
                                    <{SidebarMenuItem}>
                                        <{SidebarMenuButton}
                                            asChild
                                            tooltip={item["title"]}
                                            isActive={item.get("isActive", False)}
                                        >
                                            <a href={item["url"]}>
                                                {item["icon"]}
                                                <span>{item["title"]}</span>
                                            </a>
                                        </{SidebarMenuButton}>
                                        {t"""
                                            <{CollapsibleTrigger} asChild>
                                                <{SidebarMenuAction} class="data-[state=open]:rotate-90">
                                                    <{ChevronRightIcon} />
                                                    <span class="sr-only">Toggle</span>
                                                </{SidebarMenuAction}>
                                            </{CollapsibleTrigger}>
                                            <{CollapsibleContent}>
                                                <{SidebarMenuSub}>
                                                    {[t'''
                                                        <{SidebarMenuSubItem} key={sub_item["title"]}>
                                                            <{SidebarMenuSubButton} asChild>
                                                                <a href={sub_item["url"]}>
                                                                    <span>{sub_item["title"]}</span>
                                                                </a>
                                                            </{SidebarMenuSubButton}>
                                                        </{SidebarMenuSubItem}>
                                                    ''' for sub_item in item["items"]]}
                                                </{SidebarMenuSub}>
                                            </{CollapsibleContent}>
                                        """ if (len(item.get("items")) if item.get("items") else None) else None}
                                    </{SidebarMenuItem}>
                                </{Collapsible}>
                            ''' for item in data["navMain"]]}
                        </{SidebarMenu}>
                    </{SidebarGroup}>
                    <{SidebarGroup} class="mt-auto">
                        <{SidebarGroupContent}>
                            <{SidebarMenu}>
                                {[t'''
                                    <{SidebarMenuItem} key={item["title"]}>
                                        <{SidebarMenuButton} asChild size="sm">
                                            <a href={item["url"]}>
                                                {item["icon"]}
                                                <span>{item["title"]}</span>
                                            </a>
                                        </{SidebarMenuButton}>
                                    </{SidebarMenuItem}>
                                ''' for item in data["navSecondary"]]}
                            </{SidebarMenu}>
                        </{SidebarGroupContent}>
                    </{SidebarGroup}>
                </{SidebarContent}>
                <{SidebarRail} />
            </{Sidebar}>
            <{SidebarInset}>
                <header class="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
