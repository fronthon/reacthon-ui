from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem


def NavMain(items=None, **_):
    return t"""
        <{SidebarMenu}>
            {[t'''
                <{SidebarMenuItem} key={item["title"]}>
                    <{SidebarMenuButton} href={item["url"]} isActive={item.get("isActive", False)}>
                        {item["icon"]}
                        <span>{item["title"]}</span>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            ''' for item in items]}
        </{SidebarMenu}>
    """
