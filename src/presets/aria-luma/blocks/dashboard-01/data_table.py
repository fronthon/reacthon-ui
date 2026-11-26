from browser import window
from javascript import NULL
from reacthon import use_state
from badge import Badge
from button import Button
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from checkbox import Checkbox
from drawer import (
    Drawer, DrawerClose, DrawerContent, DrawerDescription, DrawerFooter, DrawerHeader, DrawerTitle, DrawerTrigger,
)
from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger
from input import Input
from label import Label
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from separator import Separator
from table import Table, TableBody, TableCell, TableHead, TableHeader, TableRow
from tabs import Tabs, TabsContent, TabsList, TabsTrigger

__js__ = {
    "@tanstack/react-table": [
        "columnFilteringFeature",
        "columnVisibilityFeature",
        "createColumnHelper",
        "createFilteredRowModel",
        "createPaginatedRowModel",
        "createSortedRowModel",
        "rowPaginationFeature",
        "rowSelectionFeature",
        "rowSortingFeature",
        "tableFeatures",
        "useTable",
    ],
    "react-aria-components": ["DropIndicator", "useDragAndDrop", "useListData"],
    "recharts": ["Area", "AreaChart", "CartesianGrid", "XAxis"],
    "sonner": ["toast"],
    "zod": ["z"],
    "@/hooks/use-mobile": ["useIsMobile"],
    "lucide-react": [
        "GripVerticalIcon",
        "CircleCheckIcon",
        "LoaderIcon",
        "EllipsisVerticalIcon",
        "PlusIcon",
        "ChevronsLeftIcon",
        "ChevronLeftIcon",
        "ChevronRightIcon",
        "ChevronsRightIcon",
        "TrendingUpIcon",
    ],
}

features = tableFeatures(
    {
        "columnFilteringFeature": columnFilteringFeature,
        "columnVisibilityFeature": columnVisibilityFeature,
        "rowPaginationFeature": rowPaginationFeature,
        "rowSelectionFeature": rowSelectionFeature,
        "rowSortingFeature": rowSortingFeature,
        "filteredRowModel": createFilteredRowModel(),
        "paginatedRowModel": createPaginatedRowModel(),
        "sortedRowModel": createSortedRowModel(),
    },
)

column_helper = createColumnHelper()

schema = z.object(
    {
        "id": z.number(),
        "header": z.string(),
        "type": z.string(),
        "status": z.string(),
        "target": z.string(),
        "limit": z.string(),
        "reviewer": z.string(),
    },
)


def DragHandle():
    return t"""
        <{Button} slot="drag" variant="ghost" size="icon" class="size-7 text-muted-foreground hover:bg-transparent">
            <{GripVerticalIcon} class="size-3 text-muted-foreground" />
        </{Button}>
    """


def drag_cell(props):
    row = props.row

    return t"<{DragHandle} />"


def header_cell(props):
    row = props.row

    return t"<{TableCellViewer} item={row.original} />"


def type_cell(props):
    row = props.row

    return t"""
        <div class="w-32">
            <{Badge} variant="outline" class="px-1.5 text-muted-foreground">{row.original["type"]}</{Badge}>
        </div>
    """


def status_cell(props):
    row = props.row

    return t"""
        <{Badge}
            variant="outline"
            class="px-1.5 text-muted-foreground"
        >
            {t'<{CircleCheckIcon} class="fill-green-500 dark:fill-green-400" />' if row.original["status"] == "Done" else t'<{LoaderIcon} />'}
            {row.original["status"]}
        </{Badge}>
    """


def target_cell(props):
    row = props.row

    def on_submit(e):
        e.preventDefault()
        toast.promise(
            window.Promise.new(lambda resolve: window.setTimeout(resolve, 1000)),
            {"loading": f"Saving {row.original["header"]}", "success": "Done", "error": "Error"},
        )

    return t"""
        <form onSubmit={on_submit}>
            <{Label} for={f"{row.original["id"]}-target"} class="sr-only">Target</{Label}>
            <{Input}
                class="h-8 w-16 border-transparent bg-transparent text-right shadow-none hover:bg-input/30 focus-visible:border focus-visible:bg-background dark:bg-transparent dark:hover:bg-input/30 dark:focus-visible:bg-input/30"
                defaultValue={row.original["target"]}
                id={f"{row.original["id"]}-target"}
            />
        </form>
    """


def limit_cell(props):
    row = props.row

    def on_submit(e):
        e.preventDefault()
        toast.promise(
            window.Promise.new(lambda resolve: window.setTimeout(resolve, 1000)),
            {"loading": f"Saving {row.original["header"]}", "success": "Done", "error": "Error"},
        )

    return t"""
        <form onSubmit={on_submit}>
            <{Label} for={f"{row.original["id"]}-limit"} class="sr-only">Limit</{Label}>
            <{Input}
                class="h-8 w-16 border-transparent bg-transparent text-right shadow-none hover:bg-input/30 focus-visible:border focus-visible:bg-background dark:bg-transparent dark:hover:bg-input/30 dark:focus-visible:bg-input/30"
                defaultValue={row.original["limit"]}
                id={f"{row.original["id"]}-limit"}
            />
        </form>
    """


def reviewer_cell(props):
    row = props.row

    is_assigned = row.original["reviewer"] != "Assign reviewer"
    if is_assigned:
        return row.original["reviewer"]
    return t"""
        <{Label} for={f"{row.original["id"]}-reviewer"} class="sr-only">Reviewer</{Label}>
        <{Select} placeholder="Assign reviewer">
            <{SelectTrigger}
                class="w-38 **:data-[slot=select-value]:block **:data-[slot=select-value]:truncate"
                size="sm"
                id={f"{row.original["id"]}-reviewer"}
            >
                <{SelectValue} />
            </{SelectTrigger}>
            <{SelectContent} placement="bottom end">
                <{SelectGroup}>
                    <{SelectItem} id="Eddie Lake">Eddie Lake</{SelectItem}>
                    <{SelectItem} id="Jamik Tashpulatov">Jamik Tashpulatov</{SelectItem}>
                </{SelectGroup}>
            </{SelectContent}>
        </{Select}>
    """


columns = column_helper.columns(
    [
        column_helper.display({"id": "drag", "header": lambda: NULL, "cell": drag_cell}),
        column_helper.display(
            {
                "id": "select",
                "header": lambda: t"""
                    <div class="flex items-center justify-center">
                        <{Checkbox} slot="selection" />
                    </div>
                """,
                "cell": lambda: t"""
                    <div class="flex items-center justify-center">
                        <{Checkbox} slot="selection" />
                    </div>
                """,
                "enableSorting": False,
                "enableHiding": False,
            },
        ),
        column_helper.accessor("header", {"header": "Header", "cell": header_cell, "enableHiding": False}),
        column_helper.accessor("type", {"header": "Section Type", "cell": type_cell}),
        column_helper.accessor("status", {"header": "Status", "cell": status_cell}),
        column_helper.accessor(
            "target",
            {"header": lambda: t'<div class="w-full text-right">Target</div>', "cell": target_cell},
        ),
        column_helper.accessor(
            "limit",
            {"header": lambda: t'<div class="w-full text-right">Limit</div>', "cell": limit_cell},
        ),
        column_helper.accessor("reviewer", {"header": "Reviewer", "cell": reviewer_cell}),
        column_helper.display(
            {
                "id": "actions",
                "cell": lambda: t"""
                    <{DropdownMenuTrigger}>
                        <{Button}
                            variant="ghost"
                            class="flex size-8 text-muted-foreground aria-expanded:bg-muted"
                            size="icon"
                        >
                            <{EllipsisVerticalIcon} />
                            <span class="sr-only">Open menu</span>
                        </{Button}>
                        <{DropdownMenu} placement="bottom end" class="w-32">
                            <{DropdownMenuItem}>Edit</{DropdownMenuItem}>
                            <{DropdownMenuItem}>Make a copy</{DropdownMenuItem}>
                            <{DropdownMenuItem}>Favorite</{DropdownMenuItem}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuItem} variant="destructive">Delete</{DropdownMenuItem}>
                        </{DropdownMenu}>
                    </{DropdownMenuTrigger}>
                """,
            },
        ),
    ],
)


def DataTable(data=None):
    initial_data = data

    list_ = useListData({"initialItems": initial_data, "getKey": lambda item: str(item["id"])})
    data = list_.items
    row_selection, set_row_selection = use_state({})
    column_visibility, set_column_visibility = use_state({})
    column_filters, set_column_filters = use_state([])
    sorting, set_sorting = use_state([])
    pagination, set_pagination = use_state({"pageIndex": 0, "pageSize": 10})
    table = useTable(
        {
            "features": features,
            "data": data,
            "columns": columns,
            "state": {
                "sorting": sorting,
                "columnVisibility": column_visibility,
                "rowSelection": row_selection,
                "columnFilters": column_filters,
                "pagination": pagination,
            },
            "getRowId": lambda row: str(row["id"]),
            "enableRowSelection": True,
            "onRowSelectionChange": set_row_selection,
            "onSortingChange": set_sorting,
            "onColumnFiltersChange": set_column_filters,
            "onColumnVisibilityChange": set_column_visibility,
            "onPaginationChange": set_pagination,
        },
    )

    def on_reorder(e):
        if e["target"]["dropPosition"] == "before":
            list_.moveBefore(e["target"]["key"], e["keys"])
        elif e["target"]["dropPosition"] == "after":
            list_.moveAfter(e["target"]["key"], e["keys"])

    def render_drop_indicator(target):
        return t'<{DropIndicator} target={target} class="outline-blue-400 data-drop-target:outline-1" />'

    drag_and_drop_hooks = useDragAndDrop({"getItems": lambda keys, items: [{"text/plain": item["header"]} for item in items], "onReorder": on_reorder, "renderDropIndicator": render_drop_indicator}).get("dragAndDropHooks")

    def on_selection_change(selection):
        if selection == "all":
            table.toggleAllRowsSelected()
        else:
            table.setRowSelection(dict([[key, True] for key in list(selection)]))

    def on_sort_change(sort_descriptor):
        table.setSorting(
            [{"id": "" + sort_descriptor["column"], "desc": sort_descriptor["direction"] == "descending"}],
        )

    def on_change(value):
        table.setPageSize(float(value))

    return t"""
        <{Tabs} defaultSelectedKey="outline" class="w-full flex-col justify-start gap-6">
            <div class="flex items-center justify-between px-4 lg:px-6">
                <{Label} for="view-selector" class="sr-only">View</{Label}>
                <{TabsList} class="hidden **:data-[slot=badge]:size-5 **:data-[slot=badge]:rounded-full **:data-[slot=badge]:bg-muted-foreground/30 **:data-[slot=badge]:px-1 @4xl/main:flex">
                    <{TabsTrigger} id="outline">Outline</{TabsTrigger}>
                    <{TabsTrigger} id="past-performance">
                        Past Performance <{Badge} variant="secondary">3</{Badge}>
                    </{TabsTrigger}>
                    <{TabsTrigger} id="key-personnel">
                        Key Personnel <{Badge} variant="secondary">2</{Badge}>
                    </{TabsTrigger}>
                    <{TabsTrigger} id="focus-documents">Focus Documents</{TabsTrigger}>
                </{TabsList}>
                <div class="flex items-center gap-2">
                    <{Button} variant="outline" size="sm">
                        <{PlusIcon} />
                        <span class="hidden lg:inline">Add Section</span>
                    </{Button}>
                </div>
            </div>
            <{TabsContent} id="outline" class="relative flex flex-col gap-4 overflow-auto px-4 lg:px-6">
                <div class="overflow-hidden rounded-lg border">
                    <{Table}
                        aria-label="Tasks"
                        dragAndDropHooks={drag_and_drop_hooks}
                        selectionMode="multiple"
                        onSelectionChange={on_selection_change}
                        sortDescriptor={ {
                            "column": sorting[0]["id"],
                            "direction": "descending" if sorting[0]["desc"] else "ascending",
                        } if len(sorting) else None }
                        onSortChange={on_sort_change}
                    >
                        <{TableHeader} class="sticky top-0 z-10 bg-muted">
                            {[t'''
                                <{TableHead}
                                    key={header.id}
                                    id={header.id}
                                    isRowHeader={header.index == 1}
                                    allowsSorting={header.column.getCanSort()}
                                >
                                    {None if header.isPlaceholder else t"<{table.FlexRender} header={header} />"}
                                </{TableHead}>
                            ''' for header in table.getFlatHeaders()]}
                        </{TableHeader}>
                        <{TableBody}
                            class="data-empty:h-24 data-empty:text-center **:data-[slot=table-cell]:first:w-8"
                            renderEmptyState={(lambda: "No results.")}
                        >
                            {[t'''
                                <{TableRow}
                                    key={row.id}
                                    id={row.id}
                                    value={row.original}
                                    class="relative z-0 data-[dragging=true]:z-10 data-[dragging=true]:opacity-80"
                                >
                                    {[t"""
                                        <{TableCell} key={cell.id}>
                                            <{table.FlexRender} cell={cell} />
                                        </{TableCell}>
                                    """ for cell in row.getVisibleCells()]}
                                </{TableRow}>
                            ''' for row in table.getRowModel()["rows"]]}
                        </{TableBody}>
                    </{Table}>
                </div>
                <div class="flex items-center justify-between px-4">
                    <div class="hidden flex-1 text-sm text-muted-foreground lg:flex">
                        {len(table.getFilteredSelectedRowModel()["rows"])} of{" "}
                        {len(table.getFilteredRowModel()["rows"])} row(s) selected.
                    </div>
                    <div class="flex w-full items-center gap-8 lg:w-fit">
                        <div class="hidden items-center gap-2 lg:flex">
                            <{Label} for="rows-per-page" class="text-sm font-medium">Rows per page</{Label}>
                            <{Select}
                                aria-label="Rows per page"
                                placeholder={f"{table.state["pagination"]["pageSize"]}"}
                                value={f"{table.state["pagination"]["pageSize"]}"}
                                onChange={on_change}
                            >
                                <{SelectTrigger} size="sm" class="w-20" id="rows-per-page">
                                    <{SelectValue} />
                                </{SelectTrigger}>
                                <{SelectContent} placement="top">
                                    <{SelectGroup}>
                                        {[t'''
                                            <{SelectItem}
                                                key={page_size}
                                                id={f"{page_size}"}
                                            >
                                                {page_size}
                                            </{SelectItem}>
                                        ''' for page_size in [10, 20, 30, 40, 50]]}
                                    </{SelectGroup}>
                                </{SelectContent}>
                            </{Select}>
                        </div>
                        <div class="flex w-fit items-center justify-center text-sm font-medium">
                            Page {table.state["pagination"]["pageIndex"] + 1} of{" "}
                            {table.getPageCount()}
                        </div>
                        <div class="ml-auto flex items-center gap-2 lg:ml-0">
                            <{Button}
                                variant="outline"
                                class="hidden h-8 w-8 p-0 lg:flex"
                                onPress={(lambda: table.setPageIndex(0))}
                                isDisabled={not table.getCanPreviousPage()}
                            >
                                <span class="sr-only">Go to first page</span>
                                <{ChevronsLeftIcon} />
                            </{Button}>
                            <{Button}
                                variant="outline"
                                class="size-8"
                                size="icon"
                                onPress={(lambda: table.previousPage())}
                                isDisabled={not table.getCanPreviousPage()}
                            >
                                <span class="sr-only">Go to previous page</span>
                                <{ChevronLeftIcon} />
                            </{Button}>
                            <{Button}
                                variant="outline"
                                class="size-8"
                                size="icon"
                                onPress={(lambda: table.nextPage())}
                                isDisabled={not table.getCanNextPage()}
                            >
                                <span class="sr-only">Go to next page</span>
                                <{ChevronRightIcon} />
                            </{Button}>
                            <{Button}
                                variant="outline"
                                class="hidden size-8 lg:flex"
                                size="icon"
                                onPress={(lambda: table.setPageIndex(table.getPageCount() - 1))}
                                isDisabled={not table.getCanNextPage()}
                            >
                                <span class="sr-only">Go to last page</span>
                                <{ChevronsRightIcon} />
                            </{Button}>
                        </div>
                    </div>
                </div>
            </{TabsContent}>
            <{TabsContent} id="past-performance" class="flex flex-col px-4 lg:px-6">
                <div class="aspect-video w-full flex-1 rounded-lg border border-dashed"></div>
            </{TabsContent}>
            <{TabsContent} id="key-personnel" class="flex flex-col px-4 lg:px-6">
                <div class="aspect-video w-full flex-1 rounded-lg border border-dashed"></div>
            </{TabsContent}>
            <{TabsContent} id="focus-documents" class="flex flex-col px-4 lg:px-6">
                <div class="aspect-video w-full flex-1 rounded-lg border border-dashed"></div>
            </{TabsContent}>
        </{Tabs}>
    """


chart_data = [
    {"month": "January", "desktop": 186, "mobile": 80},
    {"month": "February", "desktop": 305, "mobile": 200},
    {"month": "March", "desktop": 237, "mobile": 120},
    {"month": "April", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "June", "desktop": 214, "mobile": 140},
]

chart_config = {
    "desktop": {"label": "Desktop", "color": "var(--primary)"},
    "mobile": {"label": "Mobile", "color": "var(--primary)"},
}


def TableCellViewer(item=None):
    is_mobile = useIsMobile()
    return t"""
        <{Drawer} swipeDirection={"down" if is_mobile else "right"}>
            <{DrawerTrigger} render={t'<{Button} variant="link" class="w-fit px-0 text-left text-foreground" />'}>
                {item["header"]}
            </{DrawerTrigger}>
            <{DrawerContent}>
                <{DrawerHeader} class="gap-1">
                    <{DrawerTitle}>{item["header"]}</{DrawerTitle}>
                    <{DrawerDescription}>Showing total visitors for the last 6 months</{DrawerDescription}>
                </{DrawerHeader}>
                <div class="flex flex-col gap-4 overflow-y-auto px-4 text-sm">
                    {not is_mobile and t'''
                        <{ChartContainer} config={chart_config}>
                            <{AreaChart} accessibilityLayer data={chart_data} margin={ {"left": 0, "right": 10} }>
                                <{CartesianGrid} vertical={False} />
                                <{XAxis}
                                    dataKey="month"
                                    tickLine={False}
                                    axisLine={False}
                                    tickMargin={8}
                                    tickFormatter={(lambda value: value.slice(0, 3))}
                                    hide
                                />
                                <{ChartTooltip} cursor={False} content={t"""<{ChartTooltipContent} indicator="dot" />"""} />
                                <{Area}
                                    dataKey="mobile"
                                    type="natural"
                                    fill="var(--color-mobile)"
                                    fillOpacity={0.6}
                                    stroke="var(--color-mobile)"
                                    stackId="a"
                                />
                                <{Area}
                                    dataKey="desktop"
                                    type="natural"
                                    fill="var(--color-desktop)"
                                    fillOpacity={0.4}
                                    stroke="var(--color-desktop)"
                                    stackId="a"
                                />
                            </{AreaChart}>
                        </{ChartContainer}>
                        <{Separator} />
                        <div class="grid gap-2">
                            <div class="flex gap-2 leading-none font-medium">
                                Trending up by 5.2% this month{" "}
                                <{TrendingUpIcon} class="size-4" />
                            </div>
                            <div class="text-muted-foreground">
                                Showing total visitors for the last 6 months. This is just some random text to test the layout. It spans multiple lines and should wrap around.
                            </div>
                        </div>
                        <{Separator} />
                    '''}
                    <form class="flex flex-col gap-4">
                        <div class="flex flex-col gap-3">
                            <{Label} for="header">Header</{Label}>
                            <{Input} id="header" defaultValue={item["header"]} />
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="flex flex-col gap-3">
                                <{Label} for="type">Type</{Label}>
                                <{Select} placeholder="Select a type" aria-label="Type" defaultValue={item["type"]}>
                                    <{SelectTrigger} id="type" class="w-full">
                                        <{SelectValue} />
                                    </{SelectTrigger}>
                                    <{SelectContent}>
                                        <{SelectGroup}>
                                            <{SelectItem} id="Table of Contents">Table of Contents</{SelectItem}>
                                            <{SelectItem} id="Executive Summary">Executive Summary</{SelectItem}>
                                            <{SelectItem} id="Technical Approach">Technical Approach</{SelectItem}>
                                            <{SelectItem} id="Design">Design</{SelectItem}>
                                            <{SelectItem} id="Capabilities">Capabilities</{SelectItem}>
                                            <{SelectItem} id="Focus Documents">Focus Documents</{SelectItem}>
                                            <{SelectItem} id="Narrative">Narrative</{SelectItem}>
                                            <{SelectItem} id="Cover Page">Cover Page</{SelectItem}>
                                        </{SelectGroup}>
                                    </{SelectContent}>
                                </{Select}>
                            </div>
                            <div class="flex flex-col gap-3">
                                <{Label} for="status">Status</{Label}>
                                <{Select} aria-label="Status" placeholder="Select a status" defaultValue={item["status"]}>
                                    <{SelectTrigger} id="status" class="w-full">
                                        <{SelectValue} />
                                    </{SelectTrigger}>
                                    <{SelectContent}>
                                        <{SelectGroup}>
                                            <{SelectItem} id="Done">Done</{SelectItem}>
                                            <{SelectItem} id="In Progress">In Progress</{SelectItem}>
                                            <{SelectItem} id="Not Started">Not Started</{SelectItem}>
                                        </{SelectGroup}>
                                    </{SelectContent}>
                                </{Select}>
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="flex flex-col gap-3">
                                <{Label} for="target">Target</{Label}>
                                <{Input} id="target" defaultValue={item["target"]} />
                            </div>
                            <div class="flex flex-col gap-3">
                                <{Label} for="limit">Limit</{Label}>
                                <{Input} id="limit" defaultValue={item["limit"]} />
                            </div>
                        </div>
                        <div class="flex flex-col gap-3">
                            <{Label} for="reviewer">Reviewer</{Label}>
                            <{Select}
                                aria-label="Reviewer"
                                placeholder="Select a reviewer"
                                defaultValue={item["reviewer"]}
                            >
                                <{SelectTrigger} id="reviewer" class="w-full">
                                    <{SelectValue} />
                                </{SelectTrigger}>
                                <{SelectContent}>
                                    <{SelectGroup}>
                                        <{SelectItem} id="Eddie Lake">Eddie Lake</{SelectItem}>
                                        <{SelectItem} id="Jamik Tashpulatov">Jamik Tashpulatov</{SelectItem}>
                                        <{SelectItem} id="Emily Whalen">Emily Whalen</{SelectItem}>
                                    </{SelectGroup}>
                                </{SelectContent}>
                            </{Select}>
                        </div>
                    </form>
                </div>
                <{DrawerFooter}>
                    <{Button}>Submit</{Button}>
                    <{DrawerClose} render={t'<{Button} variant="outline" />'}>Done</{DrawerClose}>
                </{DrawerFooter}>
            </{DrawerContent}>
        </{Drawer}>
    """
