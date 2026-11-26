from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from sidebar import (
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarSeparator,
)

__js__ = {"lucide-react": ["ChevronRightIcon", "CheckIcon"], "react": ["Fragment"]}


def Calendars(calendars=None, **_):
    return t"""
        {[t'''
            <{Fragment} key={calendar["name"]}>
                <{SidebarGroup} key={calendar["name"]}>
                    <{Collapsible} defaultOpen={index == 0} class="group/collapsible">
                        <{SidebarGroupLabel}
                            asChild
                            class="group/label w-full text-sm text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
                        >
                            <{CollapsibleTrigger}>
                                {calendar["name"]}
                                {" "}
                                <{ChevronRightIcon} class="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-90" />
                            </{CollapsibleTrigger}>
                        </{SidebarGroupLabel}>
                        <{CollapsibleContent}>
                            <{SidebarGroupContent}>
                                <{SidebarMenu}>
                                    {[t"""
                                        <{SidebarMenuItem} key={item}>
                                            <{SidebarMenuButton}>
                                                <div
                                                    data-active={index < 2}
                                                    class="group/calendar-item flex aspect-square size-4 shrink-0 items-center justify-center rounded-sm border border-sidebar-border text-sidebar-primary-foreground data-[active=true]:border-sidebar-primary data-[active=true]:bg-sidebar-primary"
                                                >
                                                    <{CheckIcon} class="hidden size-3 group-data-[active=true]/calendar-item:block" />
                                                </div>
                                                {item}
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                    """ for index, item in enumerate(calendar["items"])]}
                                </{SidebarMenu}>
                            </{SidebarGroupContent}>
                        </{CollapsibleContent}>
                    </{Collapsible}>
                </{SidebarGroup}>
                <{SidebarSeparator} class="mx-0" />
            </{Fragment}>
        ''' for index, calendar in enumerate(calendars)]}
    """
