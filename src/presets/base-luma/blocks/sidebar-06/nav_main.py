from dropdown_menu import DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger
from sidebar import SidebarGroup, SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {"lucide-react": ["MoreHorizontalIcon"]}


def NavMain(items=None):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup}>
            <{SidebarMenu}>
                {[t'''
                    <{DropdownMenu} key={item["title"]}>
                        <{SidebarMenuItem}>
                            <{DropdownMenuTrigger} render={t"""<{SidebarMenuButton} class="aria-expanded:bg-muted" />"""}>
                                {item["title"]}
                                {" "}
                                <{MoreHorizontalIcon} class="ml-auto" />
                            </{DropdownMenuTrigger}>
                            {t"""
                                <{DropdownMenuContent}
                                    side={"bottom" if is_mobile else "right"}
                                    align={"end" if is_mobile else "start"}
                                    class="min-w-56 rounded-lg"
                                >
                                    {[t'''
                                        <{DropdownMenuItem}
                                            key={item["title"]}
                                            render={t"<a href={item["url"]} />"}
                                        >
                                            {item["title"]}
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
