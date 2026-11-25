from app_sidebar import AppSidebar
from site_header import SiteHeader
from sidebar import SidebarInset, SidebarProvider

iframe_height = "800px"

description = "A sidebar with a header and a search form."


def Page():
    return t"""
        <div class="[--header-height:calc(--spacing(14))]">
            <{SidebarProvider} class="flex flex-col">
                <{SiteHeader} />
                <div class="flex flex-1">
                    <{AppSidebar} />
                    <{SidebarInset}>
                        <div class="flex flex-1 flex-col gap-4 p-4">
                            <div class="grid auto-rows-min gap-4 md:grid-cols-3">
                                <div class="aspect-video rounded-xl bg-muted/50" />
                                <div class="aspect-video rounded-xl bg-muted/50" />
                                <div class="aspect-video rounded-xl bg-muted/50" />
                            </div>
                            <div class="min-h-screen flex-1 rounded-xl bg-muted/50 md:min-h-min" />
                        </div>
                    </{SidebarInset}>
                </div>
            </{SidebarProvider}>
        </div>
    """
