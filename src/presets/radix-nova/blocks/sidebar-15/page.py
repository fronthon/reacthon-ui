from sidebar_left import SidebarLeft
from sidebar_right import SidebarRight
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbList, BreadcrumbPage
from separator import Separator
from sidebar import SidebarInset, SidebarProvider, SidebarTrigger


def Page():
    return t"""
        <{SidebarProvider}>
            <{SidebarLeft} />
            <{SidebarInset}>
                <header class="sticky top-0 flex h-14 shrink-0 items-center gap-2 bg-background">
                    <div class="flex flex-1 items-center gap-2 px-3">
                        <{SidebarTrigger} />
                        <{Separator} orientation="vertical" class="mr-2 data-vertical:h-4 data-vertical:self-auto" />
                        <{Breadcrumb}>
                            <{BreadcrumbList}>
                                <{BreadcrumbItem}>
                                    <{BreadcrumbPage} class="line-clamp-1">
                                        Project Management & Task Tracking
                                    </{BreadcrumbPage}>
                                </{BreadcrumbItem}>
                            </{BreadcrumbList}>
                        </{Breadcrumb}>
                    </div>
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4">
                    <div class="mx-auto h-24 w-full max-w-3xl rounded-xl bg-muted/50" />
                    <div class="mx-auto h-screen w-full max-w-3xl rounded-xl bg-muted/50" />
                </div>
            </{SidebarInset}>
            <{SidebarRight} />
        </{SidebarProvider}>
    """
