from javascript import Math
from reacthon import use_state
from nav_user import NavUser
from label import Label
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarFooter,
    SidebarGroup,
    SidebarGroupContent,
    SidebarHeader,
    SidebarInput,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    use_sidebar,
)
from switch import Switch
from utils import sort

__js__ = {"lucide-react": ["InboxIcon", "FileIcon", "SendIcon", "ArchiveXIcon", "Trash2Icon", "TerminalIcon"]}

data = {
    "user": {"name": "shadcn", "email": "m@example.com", "avatar": "/avatars/shadcn.jpg"},
    "navMain": [
        {"title": "Inbox", "url": "#", "icon": t"<{InboxIcon} />", "isActive": True},
        {"title": "Drafts", "url": "#", "icon": t"<{FileIcon} />", "isActive": False},
        {"title": "Sent", "url": "#", "icon": t"<{SendIcon} />", "isActive": False},
        {"title": "Junk", "url": "#", "icon": t"<{ArchiveXIcon} />", "isActive": False},
        {"title": "Trash", "url": "#", "icon": t"<{Trash2Icon} />", "isActive": False},
    ],
    "mails": [
        {
            "name": "William Smith",
            "email": "williamsmith@example.com",
            "subject": "Meeting Tomorrow",
            "date": "09:34 AM",
            "teaser": "Hi team, just a reminder about our meeting tomorrow at 10 AM.\nPlease come prepared with your project updates.",
        },
        {
            "name": "Alice Smith",
            "email": "alicesmith@example.com",
            "subject": "Re: Project Update",
            "date": "Yesterday",
            "teaser": "Thanks for the update. The progress looks great so far.\nLet's schedule a call to discuss the next steps.",
        },
        {
            "name": "Bob Johnson",
            "email": "bobjohnson@example.com",
            "subject": "Weekend Plans",
            "date": "2 days ago",
            "teaser": "Hey everyone! I'm thinking of organizing a team outing this weekend.\nWould you be interested in a hiking trip or a beach day?",
        },
        {
            "name": "Emily Davis",
            "email": "emilydavis@example.com",
            "subject": "Re: Question about Budget",
            "date": "2 days ago",
            "teaser": "I've reviewed the budget numbers you sent over.\nCan we set up a quick call to discuss some potential adjustments?",
        },
        {
            "name": "Michael Wilson",
            "email": "michaelwilson@example.com",
            "subject": "Important Announcement",
            "date": "1 week ago",
            "teaser": "Please join us for an all-hands meeting this Friday at 3 PM.\nWe have some exciting news to share about the company's future.",
        },
        {
            "name": "Sarah Brown",
            "email": "sarahbrown@example.com",
            "subject": "Re: Feedback on Proposal",
            "date": "1 week ago",
            "teaser": "Thank you for sending over the proposal. I've reviewed it and have some thoughts.\nCould we schedule a meeting to discuss my feedback in detail?",
        },
        {
            "name": "David Lee",
            "email": "davidlee@example.com",
            "subject": "New Project Idea",
            "date": "1 week ago",
            "teaser": "I've been brainstorming and came up with an interesting project concept.\nDo you have time this week to discuss its potential impact and feasibility?",
        },
        {
            "name": "Olivia Wilson",
            "email": "oliviawilson@example.com",
            "subject": "Vacation Plans",
            "date": "1 week ago",
            "teaser": "Just a heads up that I'll be taking a two-week vacation next month.\nI'll make sure all my projects are up to date before I leave.",
        },
        {
            "name": "James Martin",
            "email": "jamesmartin@example.com",
            "subject": "Re: Conference Registration",
            "date": "1 week ago",
            "teaser": "I've completed the registration for the upcoming tech conference.\nLet me know if you need any additional information from my end.",
        },
        {
            "name": "Sophia White",
            "email": "sophiawhite@example.com",
            "subject": "Team Dinner",
            "date": "1 week ago",
            "teaser": "To celebrate our recent project success, I'd like to organize a team dinner.\nAre you available next Friday evening? Please let me know your preferences.",
        },
    ],
}


def AppSidebar(**props):
    # Note: I'm using state to show active item.
    # IRL you should use the url/router.
    active_item, set_active_item = use_state(data["navMain"][0])
    mails, set_mails = use_state(data["mails"])
    set_open = use_sidebar().get("setOpen")

    def render_item(item):
        def on_click():
            set_active_item(item)
            mail = sort(data["mails"], lambda *_: Math.random() - 0.5)
            set_mails(mail[0:Math.max(5, Math.floor(Math.random() * 10) + 1)])
            set_open(True)

        return t"""
            <{SidebarMenuItem} key={item["title"]}>
                <{SidebarMenuButton}
                    tooltip={ {
                        "children": item["title"],
                        "hidden": False,
                    } }
                    onClick={on_click}
                    isActive={active_item["title"] == item["title"]}
                    class="px-2.5 md:px-2"
                >
                    {item["icon"]}
                    <span>{item["title"]}</span>
                </{SidebarMenuButton}>
            </{SidebarMenuItem}>
        """

    return t"""
        <{Sidebar} collapsible="icon" class="overflow-hidden *:data-[sidebar=sidebar]:flex-row" ...{props}>
            <{Sidebar} collapsible="none" class="w-[calc(var(--sidebar-width-icon)+1px)]! border-r">
                <{SidebarHeader}>
                    <{SidebarMenu}>
                        <{SidebarMenuItem}>
                            <{SidebarMenuButton} size="lg" class="md:h-8 md:p-0" render={t'<a href="#" />'}>
                                <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                                    <{TerminalIcon} class="size-4" />
                                </div>
                                <div class="grid flex-1 text-left text-sm leading-tight">
                                    <span class="truncate font-medium">Acme Inc</span>
                                    <span class="truncate text-xs">Enterprise</span>
                                </div>
                            </{SidebarMenuButton}>
                        </{SidebarMenuItem}>
                    </{SidebarMenu}>
                </{SidebarHeader}>
                <{SidebarContent}>
                    <{SidebarGroup}>
                        <{SidebarGroupContent} class="px-1.5 md:px-0">
                            <{SidebarMenu}>{[render_item(item) for item in data["navMain"]]}</{SidebarMenu}>
                        </{SidebarGroupContent}>
                    </{SidebarGroup}>
                </{SidebarContent}>
                <{SidebarFooter}>
                    <{NavUser} user={data["user"]} />
                </{SidebarFooter}>
            </{Sidebar}>
            <{Sidebar} collapsible="none" class="hidden flex-1 md:flex">
                <{SidebarHeader} class="gap-3.5 border-b p-4">
                    <div class="flex w-full items-center justify-between">
                        <div class="text-base font-medium text-foreground">{active_item["title"]}</div>
                        <{Label} class="flex items-center gap-2 text-sm">
                            <span>Unreads</span>
                            <{Switch} class="shadow-none" />
                        </{Label}>
                    </div>
                    <{SidebarInput} placeholder="Type to search..." />
                </{SidebarHeader}>
                <{SidebarContent}>
                    <{SidebarGroup} class="px-0">
                        <{SidebarGroupContent}>
                            {[t'''
                                <a
                                    href="#"
                                    key={mail["email"]}
                                    class="flex flex-col items-start gap-2 border-b p-4 text-sm leading-tight whitespace-nowrap last:border-b-0 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
                                >
                                    <div class="flex w-full items-center gap-2">
                                        <span>{mail["name"]}</span>
                                        {" "}
                                        <span class="ml-auto text-xs">{mail["date"]}</span>
                                    </div>
                                    <span class="font-medium">{mail["subject"]}</span>
                                    <span class="line-clamp-2 w-[260px] text-xs whitespace-break-spaces">
                                        {mail["teaser"]}
                                    </span>
                                </a>
                            ''' for mail in mails]}
                        </{SidebarGroupContent}>
                    </{SidebarGroup}>
                </{SidebarContent}>
            </{Sidebar}>
        </{Sidebar}>
    """
