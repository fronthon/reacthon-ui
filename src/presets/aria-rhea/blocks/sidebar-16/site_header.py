from search_form import SearchForm
from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage
from button import Button
from separator import Separator
from sidebar import use_sidebar

__js__ = {"lucide-react": ["PanelLeftIcon"]}


def SiteHeader():
    toggle_sidebar = use_sidebar().get("toggleSidebar")

    return t"""
        <header class="sticky top-0 z-50 flex w-full items-center border-b bg-background">
            <div class="flex h-(--header-height) w-full items-center gap-2 px-4">
                <{Button} class="h-8 w-8" variant="ghost" size="icon" onPress={toggle_sidebar}>
                    <{PanelLeftIcon} />
                </{Button}>
                <{Separator} orientation="vertical" class="mr-2 data-vertical:h-4 data-vertical:self-auto" />
                <{Breadcrumb} class="hidden sm:block">
                    <{BreadcrumbList}>
                        <{BreadcrumbItem}>
                            <{BreadcrumbLink} href="#">Build Your Application</{BreadcrumbLink}>
                        </{BreadcrumbItem}>
                        <{BreadcrumbItem}>
                            <{BreadcrumbPage}>Data Fetching</{BreadcrumbPage}>
                        </{BreadcrumbItem}>
                    </{BreadcrumbList}>
                </{Breadcrumb}>
                <{SearchForm} class="w-full sm:ml-auto sm:w-auto" />
            </div>
        </header>
    """
