from reacthon import use_effect, use_state
from button import Button
from popover import Popover, PopoverContent, PopoverTrigger
from sidebar import (
    Sidebar, SidebarContent, SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuButton, SidebarMenuItem,
)

__js__ = {
    "lucide-react": [
        "Settings2Icon",
        "FileTextIcon",
        "LinkIcon",
        "CopyIcon",
        "CornerUpRightIcon",
        "Trash2Icon",
        "CornerUpLeftIcon",
        "ChartLineIcon",
        "GalleryVerticalEndIcon",
        "TrashIcon",
        "BellIcon",
        "ArrowUpIcon",
        "ArrowDownIcon",
        "StarIcon",
        "MoreHorizontalIcon",
    ],
}

data = [
    [
        {"label": "Customize Page", "icon": t"<{Settings2Icon} />"},
        {"label": "Turn into wiki", "icon": t"<{FileTextIcon} />"},
    ],
    [
        {"label": "Copy Link", "icon": t"<{LinkIcon} />"},
        {"label": "Duplicate", "icon": t"<{CopyIcon} />"},
        {"label": "Move to", "icon": t"<{CornerUpRightIcon} />"},
        {"label": "Move to Trash", "icon": t"<{Trash2Icon} />"},
    ],
    [
        {"label": "Undo", "icon": t"<{CornerUpLeftIcon} />"},
        {"label": "View analytics", "icon": t"<{ChartLineIcon} />"},
        {"label": "Version History", "icon": t"<{GalleryVerticalEndIcon} />"},
        {"label": "Show delete pages", "icon": t"<{TrashIcon} />"},
        {"label": "Notifications", "icon": t"<{BellIcon} />"},
    ],
    [{"label": "Import", "icon": t"<{ArrowUpIcon} />"}, {"label": "Export", "icon": t"<{ArrowDownIcon} />"}],
]


def NavActions():
    is_open, set_is_open = use_state(False)

    def effect():
        set_is_open(True)

    use_effect(effect, [])

    return t"""
        <div class="flex items-center gap-2 text-sm">
            <div class="hidden font-medium text-muted-foreground md:inline-block">Edit Oct 08</div>
            <{Button} variant="ghost" size="icon" class="h-7 w-7">
                <{StarIcon} />
            </{Button}>
            <{Popover} open={is_open} onOpenChange={set_is_open}>
                <{PopoverTrigger} render={t'<{Button} variant="ghost" size="icon" class="h-7 w-7 data-open:bg-accent" />'}>
                    <{MoreHorizontalIcon} />
                </{PopoverTrigger}>
                <{PopoverContent} class="w-56 overflow-hidden rounded-lg p-0" align="end">
                    <{Sidebar} collapsible="none" class="bg-transparent">
                        <{SidebarContent}>
                            {[t'''
                                <{SidebarGroup} key={index} class="border-b last:border-none">
                                    <{SidebarGroupContent} class="gap-0">
                                        <{SidebarMenu}>
                                            {[t"""
                                                <{SidebarMenuItem} key={index}>
                                                    <{SidebarMenuButton}>
                                                        {item["icon"]} <span>{item["label"]}</span>
                                                    </{SidebarMenuButton}>
                                                </{SidebarMenuItem}>
                                            """ for index, item in enumerate(group)]}
                                        </{SidebarMenu}>
                                    </{SidebarGroupContent}>
                                </{SidebarGroup}>
                            ''' for index, group in enumerate(data)]}
                        </{SidebarContent}>
                    </{Sidebar}>
                </{PopoverContent}>
            </{Popover}>
        </div>
    """
