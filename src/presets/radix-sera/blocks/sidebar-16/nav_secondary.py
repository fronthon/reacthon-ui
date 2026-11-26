from sidebar import SidebarGroup, SidebarGroupContent, SidebarMenu, SidebarMenuButton, SidebarMenuItem


def NavSecondary(items=None, **props):
    return t"""
        <{SidebarGroup} ...{props}>
            <{SidebarGroupContent}>
                <{SidebarMenu}>
                    {[t'''
                        <{SidebarMenuItem} key={item["title"]}>
                            <{SidebarMenuButton} asChild size="sm">
                                <a href={item["url"]}>
                                    {item["icon"]}
                                    <span>{item["title"]}</span>
                                </a>
                            </{SidebarMenuButton}>
                        </{SidebarMenuItem}>
                    ''' for item in items]}
                </{SidebarMenu}>
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
