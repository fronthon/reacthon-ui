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
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem

__js__ = {"lucide-react": ["ChevronDownIcon", "PlusIcon"]}


def TeamSwitcher(teams=None):
    active_team, set_active_team = use_state(teams[0])
    if not active_team:
        return None
    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenuTrigger}>
                    <{SidebarMenuButton} class="w-fit px-1.5 aria-expanded:bg-muted aria-expanded:text-foreground">
                        <div class="flex aspect-square size-5 items-center justify-center rounded-md bg-sidebar-primary text-sidebar-primary-foreground">
                            {active_team["logo"]}
                        </div>
                        <span class="truncate font-medium">{active_team["name"]}</span>
                        <{ChevronDownIcon} class="opacity-50" />
                    </{SidebarMenuButton}>
                    <{DropdownMenu} class="w-64 rounded-lg" placement="bottom start" offset={4}>
                        <{DropdownMenuGroup}>
                            <{DropdownMenuLabel} class="text-xs text-muted-foreground">Teams</{DropdownMenuLabel}>
                            {[t'''
                                <{DropdownMenuItem}
                                    key={team["name"]}
                                    onAction={(lambda: set_active_team(team))}
                                    class="gap-2 p-2"
                                >
                                    <div class="flex size-6 items-center justify-center rounded-xs border">
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
                                <div class="flex size-6 items-center justify-center rounded-md border bg-background">
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
