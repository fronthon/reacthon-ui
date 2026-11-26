from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem


def NavMain(items=None, **_):
    return t"""
        <{SidebarMenu}>
            {[t'''
                <{SidebarMenuItem} key={item["title"]}>
                    <{SidebarMenuButton} asChild isActive={item.get("isActive", False)}>
                        <a href={item["url"]}>
                            {item["icon"]}
                            <span>{item["title"]}</span>
                        </a>
                    </{SidebarMenuButton}>
                </{SidebarMenuItem}>
            ''' for item in items]}
        </{SidebarMenu}>
    """
