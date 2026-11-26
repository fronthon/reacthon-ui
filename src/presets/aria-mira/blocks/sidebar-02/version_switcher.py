from reacthon import use_state
from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuTrigger
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem

__js__ = {"lucide-react": ["GalleryVerticalEndIcon", "ChevronsUpDownIcon", "CheckIcon"]}


def VersionSwitcher(versions=None, defaultVersion=None):
    selected_version, set_selected_version = use_state(defaultVersion)
    return t"""
        <{SidebarMenu}>
            <{SidebarMenuItem}>
                <{DropdownMenuTrigger}>
                    <{SidebarMenuButton}
                        size="lg"
                        class="aria-expanded:bg-sidebar-accent aria-expanded:text-sidebar-accent-foreground"
                    >
                        <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                            <{GalleryVerticalEndIcon} class="size-4" />
                        </div>
                        <div class="flex flex-col gap-0.5 leading-none">
                            <span class="font-medium">Documentation</span>
                            <span class="">v{selected_version}</span>
                        </div>
                        <{ChevronsUpDownIcon} class="ml-auto" />
                    </{SidebarMenuButton}>
                    <{DropdownMenu} placement="bottom start">
                        {[t'''
                            <{DropdownMenuItem}
                                key={version}
                                onAction={(lambda: set_selected_version(version))}
                            >
                                v{version}
                                {" "}
                                {version == selected_version and t"""<{CheckIcon} class="ml-auto" />"""}
                            </{DropdownMenuItem}>
                        ''' for version in versions]}
                    </{DropdownMenu}>
                </{DropdownMenuTrigger}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
