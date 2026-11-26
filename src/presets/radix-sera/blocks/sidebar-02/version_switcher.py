from reacthon import use_state
from dropdown_menu import DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger
from sidebar import SidebarMenu, SidebarMenuButton, SidebarMenuItem

__js__ = {"lucide-react": ["GalleryVerticalEndIcon", "ChevronsUpDownIcon", "CheckIcon"]}


def VersionSwitcher(versions=None, defaultVersion=None, **_):
    selected_version, set_selected_version = use_state(defaultVersion)

    def render_version(version):
        return t"""
            <{DropdownMenuItem}
                key={version}
                onSelect={(lambda: set_selected_version(version))}
            >
                v{version}
                {" "}
                {version == selected_version and t'<{CheckIcon} class="ml-auto" />'}
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
                                <{GalleryVerticalEndIcon} class="size-4" />
                            </div>
                            <div class="flex flex-col gap-0.5 leading-none">
                                <span class="font-medium">Documentation</span>
                                <span class="">v{selected_version}</span>
                            </div>
                            <{ChevronsUpDownIcon} class="ml-auto" />
                        </{SidebarMenuButton}>
                    </{DropdownMenuTrigger}>
                    <{DropdownMenuContent} class="w-(--radix-dropdown-menu-trigger-width)" align="start">
                        {[render_version(version) for version in versions]}
                    </{DropdownMenuContent}>
                </{DropdownMenu}>
            </{SidebarMenuItem}>
        </{SidebarMenu}>
    """
