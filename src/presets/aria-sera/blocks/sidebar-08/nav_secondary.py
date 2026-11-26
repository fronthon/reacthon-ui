from sidebar import SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuButton, SidebarMenuItem


def NavSecondary(items=None, **props):
    return t"""
        <{SidebarGroup} ...{props}>
            <{SidebarGroupContent}>
                <{SidebarMenu}>
                    {[t'''
                        <{SidebarMenuItem} key={item["title"]}>
                            <{SidebarMenuButton} href={item["url"]} size="sm">
                                {item["icon"]}
                                <span>{item["title"]}</span>
                            </{SidebarMenuButton}>
                        </{SidebarMenuItem}>
                    ''' for item in items]}
                </{SidebarMenu}>
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
