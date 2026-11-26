from reacthon import use_state
from avatar import Avatar, AvatarFallback, AvatarImage
from button import button_variants
from collapsible import Collapsible, CollapsibleContent
from dropdown_menu import (
    DropdownMenu, DropdownMenuGroup, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger,
)
from item import Item, ItemContent, ItemDescription, ItemMedia, ItemTitle
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupLabel,
    SidebarHeader,
    SidebarInset,
    SidebarMenu,
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
        "TerminalSquareIcon",
        "BotIcon",
        "BookOpen",
        "Settings2Icon",
        "FrameIcon",
        "PieChartIcon",
        "MapIcon",
        "ChevronsUpDownIcon",
        "ChevronRightIcon",
    ],
}


def SidebarIconExample():
    data = {
        "user": {"name": "shadcn", "email": "m@example.com", "avatar": "/avatars/shadcn.jpg"},
        "teams": [
            {"name": "Acme Inc", "plan": "Enterprise"},
            {"name": "Acme Corp.", "plan": "Startup"},
            {"name": "Evil Corp.", "plan": "Free"},
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
                "icon": t"<{BookOpen} />",
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

    active_team, set_active_team = use_state(data["teams"][0])

    def render_team(team):
        return t"""
            <{DropdownMenuItem}
                key={team["name"]}
                onAction={(lambda: set_active_team(team))}
            >
                {team["name"]}
            </{DropdownMenuItem}>
        """

    return t"""
        <{SidebarProvider}>
            <{Sidebar} collapsible="icon">
                <{SidebarHeader}>
                    <{SidebarMenu}>
                        <{SidebarMenuItem}>
                            <{DropdownMenuTrigger}>
                                <{SidebarMenuButton}
                                    size="lg"
                                    class="aria-expanded:bg-sidebar-accent aria-expanded:text-sidebar-accent-foreground"
                                >
                                    <span data-slot="button" class={button_variants(size="icon-sm", className="size-8")}>
                                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
                                            <rect width="256" height="256" fill="none"></rect>
                                            <line
                                                x1="208"
                                                y1="128"
                                                x2="128"
                                                y2="208"
                                                fill="none"
                                                stroke="currentColor"
                                                strokeLinecap="round"
                                                strokeLinejoin="round"
                                                strokeWidth="32"
                                            ></line>
                                            <line
                                                x1="192"
                                                y1="40"
                                                x2="40"
                                                y2="192"
                                                fill="none"
                                                stroke="currentColor"
                                                strokeLinecap="round"
                                                strokeLinejoin="round"
                                                strokeWidth="32"
                                            ></line>
                                        </svg>
                                    </span>
                                    <div class="grid flex-1 text-left text-sm leading-tight">
                                        <span class="truncate font-medium">{active_team["name"]}</span>
                                        <span class="truncate text-xs">{active_team["plan"]}</span>
                                    </div>
                                    <{ChevronsUpDownIcon} />
                                </{SidebarMenuButton}>
                                <{DropdownMenu}>
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuLabel}>Teams</{DropdownMenuLabel}>
                                    </{DropdownMenuGroup}>
                                    <{DropdownMenuGroup}>
                                        {[render_team(team) for team in data["teams"]]}
                                    </{DropdownMenuGroup}>
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{SidebarMenuItem}>
                    </{SidebarMenu}>
                </{SidebarHeader}>
                <{SidebarContent}>
                    <{SidebarGroup}>
                        <{SidebarGroupLabel}>Platform</{SidebarGroupLabel}>
                        <{SidebarMenu}>
                            {[t'''
                                <{Collapsible}
                                    key={item["title"]}
                                    defaultExpanded={item.get("isActive")}
                                    class="group/collapsible"
                                >
                                    <{SidebarMenuItem}>
                                        <{SidebarMenuButton} slot="trigger" tooltip={item["title"]}>
                                            {item["icon"]}
                                            <span>{item["title"]}</span>
                                            <{ChevronRightIcon} class="ml-auto transition-transform duration-100 group-data-expanded/collapsible:rotate-90" />
                                        </{SidebarMenuButton}>
                                        <{CollapsibleContent}>
                                            <{SidebarMenuSub}>
                                                {[t"""
                                                    <{SidebarMenuSubItem} key={sub_item["title"]}>
                                                        <{SidebarMenuSubButton} href={sub_item["url"]}>
                                                            {sub_item["title"]}
                                                        </{SidebarMenuSubButton}>
                                                    </{SidebarMenuSubItem}>
                                                """ for sub_item in item["items"]]}
                                            </{SidebarMenuSub}>
                                        </{CollapsibleContent}>
                                    </{SidebarMenuItem}>
                                </{Collapsible}>
                            ''' for item in data["navMain"]]}
                        </{SidebarMenu}>
                    </{SidebarGroup}>
                    <{SidebarGroup} class="group-data-[collapsible=icon]:hidden">
                        <{SidebarGroupLabel}>Projects</{SidebarGroupLabel}>
                        <{SidebarMenu}>
                            {[t'''
                                <{SidebarMenuItem} key={item["name"]}>
                                    <{SidebarMenuButton} href={item["url"]}>
                                        {item["icon"]}
                                        {item["name"]}
                                    </{SidebarMenuButton}>
                                </{SidebarMenuItem}>
                            ''' for item in data["projects"]]}
                        </{SidebarMenu}>
                    </{SidebarGroup}>
                </{SidebarContent}>
                <{SidebarFooter}>
                    <{SidebarMenu}>
                        <{SidebarMenuItem}>
                            <{DropdownMenuTrigger}>
                                <{SidebarMenuButton}
                                    size="lg"
                                    class="aria-expanded:bg-sidebar-accent aria-expanded:text-sidebar-accent-foreground"
                                >
                                    <{Avatar}>
                                        <{AvatarImage} src={data["user"]["avatar"]} alt={data["user"]["name"]} />
                                        <{AvatarFallback} class="rounded-lg">CN</{AvatarFallback}>
                                    </{Avatar}>
                                    <div class="grid flex-1 text-left text-sm leading-tight">
                                        <span class="truncate font-medium">{data["user"]["name"]}</span>
                                        <span class="truncate text-xs">{data["user"]["email"]}</span>
                                    </div>
                                    <{ChevronsUpDownIcon} />
                                </{SidebarMenuButton}>
                                <{DropdownMenu}>
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuLabel}>
                                            <{Item} size="xs">
                                                <{ItemMedia}>
                                                    <{Avatar}>
                                                        <{AvatarImage}
                                                            src={data["user"]["avatar"]}
                                                            alt={data["user"]["name"]}
                                                        />
                                                        <{AvatarFallback}>CN</{AvatarFallback}>
                                                    </{Avatar}>
                                                </{ItemMedia}>
                                                <{ItemContent}>
                                                    <{ItemTitle}>{data["user"]["name"]}</{ItemTitle}>
                                                    <{ItemDescription}> {data["user"]["email"]}</{ItemDescription}>
                                                </{ItemContent}>
                                            </{Item}>
                                        </{DropdownMenuLabel}>
                                    </{DropdownMenuGroup}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuItem}>Account</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Billing</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Settings</{DropdownMenuItem}>
                                    </{DropdownMenuGroup}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuItem}>Log out</{DropdownMenuItem}>
                                    </{DropdownMenuGroup}>
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{SidebarMenuItem}>
                    </{SidebarMenu}>
                </{SidebarFooter}>
                <{SidebarRail} />
            </{Sidebar}>
            <{SidebarInset}>
                <header class="flex h-16 shrink-0 items-center gap-2 border-b transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
                    <div class="flex items-center gap-2 px-4">
                        <{SidebarTrigger} class="-ml-1" />
                    </div>
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
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
