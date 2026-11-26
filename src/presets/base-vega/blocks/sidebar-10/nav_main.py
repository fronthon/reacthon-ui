from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem


def NavMain(items=None, **_):
    return t"""
        <{SidebarMenu}>
            {[t'''
                <{SidebarMenuItem} key={item["title"]}>
                    <{SidebarMenuButton} isActive={item.get("isActive", False)} render={t"<a href={item["url"]} />"}>
                        {item["icon"]}
                        <span>{item["title"]}</span>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            ''' for item in items]}
        </{SidebarMenu}>
    """
