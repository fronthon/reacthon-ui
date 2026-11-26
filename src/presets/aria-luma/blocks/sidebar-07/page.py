from app_sidebar import AppSidebar
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage
from separator import Separator
from sidebar import SidebarInset, SidebarProvider, SidebarTrigger


def Page():
    return t"""
        <{SidebarProvider}>
            <{AppSidebar} />
            <{SidebarInset}>
                <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
                    <div class="flex items-center gap-2 px-4">
                        <{SidebarTrigger} class="-ml-1" />
                        <{Separator} orientation="vertical" class="mr-2 data-vertical:h-4 data-vertical:self-auto" />
                        <{Breadcrumb}>
                            <{BreadcrumbList}>
                                <{BreadcrumbItem} class="hidden md:inline-flex">
                                    <{BreadcrumbLink} href="#">Build Your Application</{BreadcrumbLink}>
                                </{BreadcrumbItem}>
                                <{BreadcrumbItem}>
                                    <{BreadcrumbPage}>Data Fetching</{BreadcrumbPage}>
                                </{BreadcrumbItem}>
                            </{BreadcrumbList}>
                        </{Breadcrumb}>
                    </div>
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
                    <div class="grid auto-rows-min gap-4 md:grid-cols-3">
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                    </div>
                    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
                </div>
            </{SidebarInset}>
        </{SidebarProvider}>
    """
