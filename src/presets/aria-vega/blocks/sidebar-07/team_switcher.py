from reacthon import use_state
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuTrigger,
)
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {"lucide-react": ["ChevronsUpDownIcon", "PlusIcon"]}


def TeamSwitcher(teams=None):
    is_mobile = use_sidebar().get("isMobile")
    active_team, set_active_team = use_state(teams[0])
    if not active_team:
        return None
    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenuTrigger}>
                    <{SidebarMenuButton}
                        size="lg"
                        class="aria-expanded:bg-sidebar-accent aria-expanded:text-sidebar-accent-foreground"
                    >
                        <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                            {active_team["logo"]}
                        </div>
                        <div class="grid flex-1 text-left text-sm leading-tight">
                            <span class="truncate font-medium">{active_team["name"]}</span>
                            <span class="truncate text-xs">{active_team["plan"]}</span>
                        </div>
                        <{ChevronsUpDownIcon} class="ml-auto" />
                    </{SidebarMenuButton}>
                    <{DropdownMenu} class="w-fit" placement={"bottom start" if is_mobile else "right top"} offset={4}>
                        <{DropdownMenuGroup}>
                            <{DropdownMenuLabel} class="text-xs text-muted-foreground">Teams</{DropdownMenuLabel}>
                            {[t'''
                                <{DropdownMenuItem}
                                    key={team["name"]}
                                    onAction={(lambda: set_active_team(team))}
                                    class="gap-2 p-2"
                                >
                                    <div class="flex size-6 items-center justify-center rounded-md border">
                                        {team["logo"]}
                                    </div>
                                    {team["name"]}
                                    <{DropdownMenuShortcut}>⌘{index + 1}</{DropdownMenuShortcut}>
                                </{DropdownMenuItem}>
                            ''' for index, team in enumerate(teams)]}
                        </{DropdownMenuGroup}>
                        <{DropdownMenuSeparator} />
                        <{DropdownMenuGroup}>
                            <{DropdownMenuItem} class="gap-2 p-2">
                                <div class="flex size-6 items-center justify-center rounded-md border bg-transparent">
                                    <{PlusIcon} class="size-4" />
                                </div>
                                <div class="font-medium text-muted-foreground">Add team</div>
                            </{DropdownMenuItem}>
                        </{DropdownMenuGroup}>
                    </{DropdownMenu}>
                </{DropdownMenuTrigger}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
