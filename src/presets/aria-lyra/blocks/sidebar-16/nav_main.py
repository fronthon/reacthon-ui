from collapsible import Collapsible, CollapsibleContent
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
                    <{Collapsible}
                        key={item["title"]}
                        defaultExpanded={item.get("isActive")}
                        render={(lambda props: t"<{SidebarMenuItem} ...{props} />")}
                    >
                        <{SidebarMenuButton} href={item["url"]} tooltip={item["title"]}>
                            {item["icon"]}
                            <span>{item["title"]}</span>
                        </{SidebarMenuButton}>
                        {t"""
                            <{SidebarMenuAction} slot="trigger" class="aria-expanded:rotate-90">
                                <{ChevronRightIcon} />
                                <span class="sr-only">Toggle</span>
                            </{SidebarMenuAction}>
                            <{CollapsibleContent}>
                                <{SidebarMenuSub}>
                                    {[t'''
                                        <{SidebarMenuSubItem} key={sub_item["title"]}>
                                            <{SidebarMenuSubButton} href={sub_item["url"]}>
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
