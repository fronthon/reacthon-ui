from app_sidebar import AppSidebar
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbList, BreadcrumbPage
from separator import Separator
from sidebar import SidebarInset, SidebarProvider, SidebarTrigger


def Page():
    return t"""
        <{SidebarProvider}>
            <{AppSidebar} />
            <{SidebarInset}>
                <header class="sticky top-0 flex h-16 shrink-0 items-center gap-2 border-b bg-background px-4">
                    <{SidebarTrigger} class="-ml-1" />
                    <{Separator} orientation="vertical" class="mr-2 data-vertical:h-4 data-vertical:self-auto" />
                    <{Breadcrumb}>
                        <{BreadcrumbList}>
                            <{BreadcrumbItem}>
                                <{BreadcrumbPage}>October 2024</{BreadcrumbPage}>
                            </{BreadcrumbItem}>
                        </{BreadcrumbList}>
                    </{Breadcrumb}>
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4">
                    <div class="grid auto-rows-min gap-4 md:grid-cols-5">
                        {[t'<div key={i} class="aspect-square rounded-xl bg-muted/50" />' for i in range(20)]}
                    </div>
                </div>
            </{SidebarInset}>
        </{SidebarProvider}>
    """
