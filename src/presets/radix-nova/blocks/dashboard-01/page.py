from app_sidebar import AppSidebar
from chart_area_interactive import ChartAreaInteractive
from data_table import DataTable
from section_cards import SectionCards
from site_header import SiteHeader
from sidebar import SidebarInset, SidebarProvider

__js__ = {"./data.json": ["default as data"]}


def Page():
    return t"""
        <{SidebarProvider}
            style={ {"--sidebar-width": "calc(var(--spacing) * 72)", "--header-height": "calc(var(--spacing) * 12)"} }
        >
            <{AppSidebar} variant="inset" />
            <{SidebarInset}>
                <{SiteHeader} />
                <div class="flex flex-1 flex-col">
                    <div class="@container/main flex flex-1 flex-col gap-2">
                        <div class="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
                            <{SectionCards} />
                            <div class="px-4 lg:px-6">
                                <{ChartAreaInteractive} />
                            </div>
                            <{DataTable} data={data} />
                        </div>
                    </div>
                </div>
            </{SidebarInset}>
        </{SidebarProvider}>
    """
