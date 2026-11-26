from reacthon import use_state
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuTrigger,
)
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem

__js__ = {"lucide-react": ["ChevronDownIcon", "PlusIcon"]}


def TeamSwitcher(teams=None, **_):
    active_team, set_active_team = use_state(teams[0])
    if not active_team:
        return None
    sidebar_menu_button = t"""
        <{SidebarMenuButton} class="w-fit px-1.5 aria-expanded:bg-muted aria-expanded:text-foreground" />
    """

    def render_team(team, index):
        return t"""
            <{DropdownMenuItem} key={team["name"]} onClick={(lambda: set_active_team(team))} class="gap-2 p-2">
                <div class="flex size-6 items-center justify-center rounded-xs border">{team["logo"]}</div>
                {team["name"]}
                <{DropdownMenuShortcut}>⌘{index + 1}</{DropdownMenuShortcut}>
            </{DropdownMenuItem}>
        """

    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenu}>
                    <{DropdownMenuTrigger} render={sidebar_menu_button}>
                        <div class="flex aspect-square size-5 items-center justify-center rounded-md bg-sidebar-primary text-sidebar-primary-foreground">
                            {active_team["logo"]}
                        </div>
                        <span class="truncate font-medium">{active_team["name"]}</span>
                        <{ChevronDownIcon} class="opacity-50" />
                    </{DropdownMenuTrigger}>
                    <{DropdownMenuContent} class="w-64 rounded-lg" align="start" side="bottom" sideOffset={4}>
                        <{DropdownMenuGroup}>
                            <{DropdownMenuLabel} class="text-xs text-muted-foreground">Teams</{DropdownMenuLabel}>
                            {[render_team(team, index) for index, team in enumerate(teams)]}
                        </{DropdownMenuGroup}>
                        <{DropdownMenuSeparator} />
                        <{DropdownMenuGroup}>
                            <{DropdownMenuItem} class="gap-2 p-2">
                                <div class="flex size-6 items-center justify-center rounded-md border bg-background">
                                    <{PlusIcon} class="size-4" />
                                </div>
                                <div class="font-medium text-muted-foreground">Add team</div>
                            </{DropdownMenuItem}>
                        </{DropdownMenuGroup}>
                    </{DropdownMenuContent}>
                </{DropdownMenu}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
