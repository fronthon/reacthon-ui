from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    SidebarGroup,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
)

__js__ = {"lucide-react": ["ChevronRightIcon"]}


def NavMain(items=None, **_):
    return t"""
        <{SidebarGroup}>
            <{SidebarGroupLabel}>Platform</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{Collapsible}
                        key={item["title"]}
                        asChild
                        defaultOpen={item.get("isActive")}
                        class="group/collapsible"
                    >
                        <{SidebarMenuItem}>
                            <{CollapsibleTrigger} asChild>
                                <{SidebarMenuButton} tooltip={item["title"]}>
                                    {item.get("icon")}
                                    <span>{item["title"]}</span>
                                    <{ChevronRightIcon} class="ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
                                </{SidebarMenuButton}>
                            </{CollapsibleTrigger}>
                            <{CollapsibleContent}>
                                <{SidebarMenuSub}>
                                    {[t"""
                                        <{SidebarMenuSubItem} key={sub_item["title"]}>
                                            <{SidebarMenuSubButton} asChild>
                                                <a href={sub_item["url"]}>
                                                    <span>{sub_item["title"]}</span>
                                                </a>
                                            </{SidebarMenuSubButton}>
                                        </{SidebarMenuSubItem}>
                                    """ for sub_item in item.get("items")] if item.get("items") else None}
                                </{SidebarMenuSub}>
                            </{CollapsibleContent}>
                        </{SidebarMenuItem}>
                    </{Collapsible}>
                ''' for item in items]}
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
