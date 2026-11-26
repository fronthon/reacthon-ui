from app_sidebar import AppSidebar
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator
from sidebar import SidebarInset, SidebarProvider, SidebarTrigger


def Page():
    return t"""
        <{SidebarProvider}>
            <{SidebarInset}>
                <header class="flex h-16 shrink-0 items-center gap-2 border-b px-4">
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
                    <{SidebarTrigger} class="-mr-1 ml-auto rotate-180" />
                </header>
                <div class="flex flex-1 flex-col gap-4 p-4">
                    <div class="grid auto-rows-min gap-4 md:grid-cols-3">
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                        <div class="aspect-video rounded-xl bg-muted/50" />
                    </div>
                    <div class="min-h-[100vh] flex-1 rounded-xl bg-muted/50 md:min-h-min" />
                </div>
            </{SidebarInset}>
            <{AppSidebar} side="right" />
        </{SidebarProvider}>
    """
