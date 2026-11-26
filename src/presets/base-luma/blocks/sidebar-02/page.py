from app_sidebar import AppSidebar
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator
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
                            <{BreadcrumbItem} class="hidden md:block">
                                <{BreadcrumbLink} href="#">Build Your Application</{BreadcrumbLink}>
                            </{BreadcrumbItem}>
                            <{BreadcrumbSeparator} class="hidden md:block" />
                            <{BreadcrumbItem}>
                                <{BreadcrumbPage}>Data Fetching</{BreadcrumbPage}>
                            </{BreadcrumbItem}>
                        </{BreadcrumbList}>
                    </{Breadcrumb}>
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4">
                    {[t'<div key={index} class="aspect-video h-12 w-full rounded-lg bg-muted/50" />' for index in range(24)]}
                </div>
            </{SidebarInset}>
        </{SidebarProvider}>
    """
