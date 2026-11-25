from button import Button
from sidebar import SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuButton, SidebarMenuItem

__js__ = {"lucide-react": ["CirclePlusIcon", "MailIcon"]}


def NavMain(items=None):
    return t"""
        <{SidebarGroup}>
            <{SidebarGroupContent} class="flex flex-col gap-2">
                <{SidebarMenu}>
                    <{SidebarMenuItem} class="flex items-center gap-2">
                        <{SidebarMenuButton}
                            tooltip="Quick Create"
                            class="min-w-8 bg-primary text-primary-foreground duration-200 ease-linear hover:bg-primary/90 hover:text-primary-foreground active:bg-primary/90 active:text-primary-foreground"
                        >
                            <{CirclePlusIcon} />
                            <span>Quick Create</span>
                        </{SidebarMenuButton}>
                        <{Button} size="icon" class="size-8 group-data-[collapsible=icon]:opacity-0" variant="outline">
                            <{MailIcon} />
                            <span class="sr-only">Inbox</span>
                        </{Button}>
                    </{SidebarMenuItem}>
                </{SidebarMenu}>
                <{SidebarMenu}>
                    {[t'''
                        <{SidebarMenuItem} key={item["title"]}>
                            <{SidebarMenuButton} tooltip={item["title"]}>
                                {item.get("icon")}
                                <span>{item["title"]}</span>
                            </{SidebarMenuButton}>
                        </{SidebarMenuItem}>
                    ''' for item in items]}
                </{SidebarMenu}>
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
