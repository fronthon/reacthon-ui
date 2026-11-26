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
                        defaultOpen={item.get("isActive")}
                        class="group/collapsible"
                        render={t"<{SidebarMenuItem} />"}
                    >
                        <{CollapsibleTrigger} render={t"<{SidebarMenuButton} tooltip={item["title"]} />"}>
                            {item.get("icon")}
                            <span>{item["title"]}</span>
                            <{ChevronRightIcon} class="ml-auto transition-transform duration-200 group-data-open/collapsible:rotate-90" />
                        </{CollapsibleTrigger}>
                        <{CollapsibleContent}>
                            <{SidebarMenuSub}>
                                {[t"""
                                    <{SidebarMenuSubItem} key={sub_item["title"]}>
                                        <{SidebarMenuSubButton} render={t'<a href={sub_item["url"]} />'}>
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
