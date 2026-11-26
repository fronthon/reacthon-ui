from dropdown_menu import DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger
from sidebar import SidebarGroup, SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {"lucide-react": ["MoreHorizontalIcon"]}


def NavMain(items=None, **_):
    is_mobile = use_sidebar().get("isMobile")

    return t"""
        <{SidebarGroup}>
            <{SidebarMenu}>
                {[t'''
                    <{DropdownMenu} key={item["title"]}>
                        <{SidebarMenuItem}>
                            <{DropdownMenuTrigger} asChild>
                                <{SidebarMenuButton} class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground">
                                    {item["title"]}
                                    {" "}
                                    <{MoreHorizontalIcon} class="ml-auto" />
                                </{SidebarMenuButton}>
                            </{DropdownMenuTrigger}>
                            {t"""
                                <{DropdownMenuContent}
                                    side={"bottom" if is_mobile else "right"}
                                    align={"end" if is_mobile else "start"}
                                    class="min-w-56 rounded-lg"
                                >
                                    {[t'''
                                        <{DropdownMenuItem} asChild key={item["title"]}>
                                            <a href={item["url"]}>{item["title"]}</a>
                                        </{DropdownMenuItem}>
                                    ''' for item in item.get("items")]}
                                </{DropdownMenuContent}>
                            """ if (len(item.get("items")) if item.get("items") else None) else None}
                        </{SidebarMenuItem}>
                    </{DropdownMenu}>
                ''' for item in items]}
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
