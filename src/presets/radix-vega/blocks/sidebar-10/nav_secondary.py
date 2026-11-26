from sidebar import SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuBadge, SidebarMenuButton, SidebarMenuItem


def NavSecondary(items=None, **props):
    return t"""
        <{SidebarGroup} ...{props}>
            <{SidebarGroupContent}>
                <{SidebarMenu}>
                    {[t'''
                        <{SidebarMenuItem} key={item["title"]}>
                            <{SidebarMenuButton} asChild>
                                <a href={item["url"]}>
                                    {item["icon"]}
                                    <span>{item["title"]}</span>
                                </a>
                            </{SidebarMenuButton}>
                            {item.get("badge") and t"<{SidebarMenuBadge}>{item.get("badge")}</{SidebarMenuBadge}>"}
                        </{SidebarMenuItem}>
                    ''' for item in items]}
                </{SidebarMenu}>
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
