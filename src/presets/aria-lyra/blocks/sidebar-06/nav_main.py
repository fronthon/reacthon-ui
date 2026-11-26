from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuTrigger
from sidebar import SidebarGroup, SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {"lucide-react": ["MoreHorizontalIcon"]}


def NavMain(items=None, **_):
    is_mobile = use_sidebar().get("isMobile")
    return t"""
        <{SidebarGroup}>
            <{SidebarMenu}>
                {[t'''
                    <{SidebarMenuItem} key={item["title"]}>
                        <{DropdownMenuTrigger}>
                            <{SidebarMenuButton} class="aria-expanded:bg-muted">
                                {item["title"]}
                                {" "}
                                <{MoreHorizontalIcon} class="ml-auto" />
                            </{SidebarMenuButton}>
                            {t"""
                                <{DropdownMenu}
                                    placement={"bottom end" if is_mobile else "right top"}
                                    class="min-w-56 rounded-lg"
                                >
                                    {[t'''
                                        <{DropdownMenuItem}
                                            key={item["title"]}
                                            href={item["url"]}
                                        >
                                            {item["title"]}
                                        </{DropdownMenuItem}>
                                    ''' for item in item.get("items")]}
                                </{DropdownMenu}>
                            """ if (len(item.get("items")) if item.get("items") else None) else None}
                        </{DropdownMenuTrigger}>
                    </{SidebarMenuItem}>
                ''' for item in items]}
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
