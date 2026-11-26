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


def NavMain(items=None, **_):
    return t"""
        <{SidebarGroup}>
            <{SidebarGroupLabel}>Platform</{SidebarGroupLabel}>
            <{SidebarMenu}>
                {[t'''
                    <{Collapsible} key={item["title"]} asChild defaultOpen={item.get("isActive")}>
                        <{SidebarMenuItem}>
                            <{SidebarMenuButton} asChild tooltip={item["title"]}>
                                <a href={item["url"]}>
                                    {item["icon"]}
                                    <span>{item["title"]}</span>
                                </a>
                            </{SidebarMenuButton}>
                            {t"""
                                <{CollapsibleTrigger} asChild>
                                    <{SidebarMenuAction} class="data-[state=open]:rotate-90">
                                        <{ChevronRightIcon} />
                                        <span class="sr-only">Toggle</span>
                                    </{SidebarMenuAction}>
                                </{CollapsibleTrigger}>
                                <{CollapsibleContent}>
                                    <{SidebarMenuSub}>
                                        {[t'''
                                            <{SidebarMenuSubItem} key={sub_item["title"]}>
                                                <{SidebarMenuSubButton} asChild>
                                                    <a href={sub_item["url"]}>
                                                        <span>{sub_item["title"]}</span>
                                                    </a>
                                                </{SidebarMenuSubButton}>
                                            </{SidebarMenuSubItem}>
                                        ''' for sub_item in item.get("items")]}
                                    </{SidebarMenuSub}>
                                </{CollapsibleContent}>
                            """ if (len(item.get("items")) if item.get("items") else None) else None}
                        </{SidebarMenuItem}>
                    </{Collapsible}>
                ''' for item in items]}
            </{SidebarMenu}>
        </{SidebarGroup}>
    """
