from sidebar import SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuBadge, SidebarMenuButton, SidebarMenuItem


def NavSecondary(items=None, **props):
    return t"""
        <{SidebarGroup} ...{props}>
            <{SidebarGroupContent}>
                <{SidebarMenu}>
                    {[t'''
                        <{SidebarMenuItem} key={item["title"]}>
                            <{SidebarMenuButton} render={t"<a href={item["url"]} />"}>
                                {item["icon"]}
                                <span>{item["title"]}</span>
                            </{SidebarMenuButton}>
                            {item.get("badge") and t"<{SidebarMenuBadge}>{item.get("badge")}</{SidebarMenuBadge}>"}
                        </{SidebarMenuItem}>
                    ''' for item in items]}
                </{SidebarMenu}>
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
