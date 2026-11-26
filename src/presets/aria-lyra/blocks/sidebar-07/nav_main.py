from collapsible import Collapsible, CollapsibleContent
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
                        defaultExpanded={item.get("isActive")}
                        class="group/collapsible"
                        render={(lambda props: t"<{SidebarMenuItem} ...{props} />")}
                    >
                        <{SidebarMenuButton} slot="trigger" tooltip={item["title"]}>
                            {item.get("icon")}
                            <span>{item["title"]}</span>
                            <{ChevronRightIcon} class="ml-auto transition-transform duration-200 group-data-expanded/collapsible:rotate-90" />
                        </{SidebarMenuButton}>
                        <{CollapsibleContent}>
                            <{SidebarMenuSub}>
                                {[t"""
                                    <{SidebarMenuSubItem} key={sub_item["title"]}>
                                        <{SidebarMenuSubButton} href={sub_item["url"]}>
                                            <span>{sub_item["title"]}</span>
                                        </{SidebarMenuSubButton}>
                                    </{SidebarMenuSubItem}>
                                """ for sub_item in item.get("items")] if item.get("items") else None}
                            </{SidebarMenuSub}>
                        </{CollapsibleContent}>
                    </{Collapsible}>
                ''' for item in items]}
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
