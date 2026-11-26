from reacthon import use_state
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuShortcut,
    DropdownMenuTrigger,
)
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem, use_sidebar

__js__ = {"lucide-react": ["ChevronsUpDownIcon", "PlusIcon"]}


def TeamSwitcher(teams=None, **_):
    is_mobile = use_sidebar().get("isMobile")
    active_team, set_active_team = use_state(teams[0])

    if not active_team:
        return None

    def render_team(team, index):
        return t"""
            <{DropdownMenuItem} key={team["name"]} onClick={(lambda: set_active_team(team))} class="gap-2 p-2">
                <div class="flex size-6 items-center justify-center rounded-md border">{team["logo"]}</div>
                {team["name"]}
                <{DropdownMenuShortcut}>⌘{index + 1}</{DropdownMenuShortcut}>
            </{DropdownMenuItem}>
        """

    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenu}>
                    <{DropdownMenuTrigger} asChild>
                        <{SidebarMenuButton}
                            size="lg"
                            class="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
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
                    </{DropdownMenuTrigger}>
                    <{DropdownMenuContent}
                        class="w-fit"
                        align="start"
                        side={"bottom" if is_mobile else "right"}
                        sideOffset={4}
                    >
                        <{DropdownMenuLabel} class="text-xs text-muted-foreground">Teams</{DropdownMenuLabel}>
                        {[render_team(team, index) for index, team in enumerate(teams)]}
                        <{DropdownMenuSeparator} />
                        <{DropdownMenuItem} class="gap-2 p-2">
                            <div class="flex size-6 items-center justify-center rounded-md border bg-transparent">
                                <{PlusIcon} class="size-4" />
                            </div>
                            <div class="font-medium text-muted-foreground">Add team</div>
                        </{DropdownMenuItem}>
                    </{DropdownMenuContent}>
                </{DropdownMenu}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
