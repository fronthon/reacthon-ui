from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    SidebarGroup,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuAction,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarMenuSubButton,
    SidebarMenuSubItem,
)

__js__ = {"lucide-react": ["ChevronRightIcon"]}


def NavMain(items=None):
    return t"""
        <{SidebarGroup}>
            <{SidebarGroupLabel}>Platform</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{Collapsible}
                        key={item["title"]}
                        defaultOpen={item.get("isActive")}
                        render={t"<{SidebarMenuItem} />"}
                    >
                        <{SidebarMenuButton} tooltip={item["title"]} render={t"<a href={item["url"]} />"}>
                            {item["icon"]}
                            <span>{item["title"]}</span>
                        </{SidebarMenuButton}>
                        {t"""
                            <{SidebarMenuAction} render={t'<{CollapsibleTrigger} />'} class="aria-expanded:rotate-90">
                                <{ChevronRightIcon} />
                                <span class="sr-only">Toggle</span>
                            </{SidebarMenuAction}>
                            <{CollapsibleContent}>
                                <{SidebarMenuSub}>
                                    {[t'''
                                        <{SidebarMenuSubItem} key={sub_item["title"]}>
                                            <{SidebarMenuSubButton} render={t"<a href={sub_item["url"]} />"}>
                                                <span>{sub_item["title"]}</span>
                                            </{SidebarMenuSubButton}>
                                        </{SidebarMenuSubItem}>
                                    ''' for sub_item in item.get("items")]}
                                </{SidebarMenuSub}>
                            </{CollapsibleContent}>
                        """ if (len(item.get("items")) if item.get("items") else None) else None}
                    </{Collapsible}>
                ''' for item in items]}
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
