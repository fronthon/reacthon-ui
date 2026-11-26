from browser import window
from javascript import NULL
from reacthon import use_id, use_memo, use_state
from badge import Badge
from button import Button
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from checkbox import Checkbox
from drawer import (
    Drawer, DrawerClose, DrawerContent, DrawerDescription, DrawerFooter, DrawerHeader, DrawerTitle, DrawerTrigger,
)
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuCheckboxItem,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
)
from input import Input
from label import Label
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from separator import Separator
from table import Table, TableBody, TableCell, TableHead, TableHeader, TableRow
from tabs import Tabs, TabsContent, TabsList, TabsTrigger

__js__ = {
    "@dnd-kit/core": [
        "closestCenter",
        "DndContext",
        "KeyboardSensor",
        "MouseSensor",
        "TouchSensor",
        "useSensor",
        "useSensors",
    ],
    "@dnd-kit/modifiers": ["restrictToVerticalAxis"],
    "@dnd-kit/sortable": ["arrayMove", "SortableContext", "useSortable", "verticalListSortingStrategy"],
    "@dnd-kit/utilities": ["CSS"],
    "@tanstack/react-table": [
        "columnFilteringFeature",
        "columnVisibilityFeature",
        "createColumnHelper",
        "createFilteredRowModel",
        "createPaginatedRowModel",
        "createSortedRowModel",
        "FlexRender",
        "rowPaginationFeature",
        "rowSelectionFeature",
        "rowSortingFeature",
        "tableFeatures",
        "useTable",
    ],
    "recharts": ["Area", "AreaChart", "CartesianGrid", "XAxis"],
    "sonner": ["toast"],
    "zod": ["z"],
    "@/hooks/use-mobile": ["useIsMobile"],
    "lucide-react": [
        "GripVerticalIcon",
        "CircleCheckIcon",
        "LoaderIcon",
        "EllipsisVerticalIcon",
        "Columns3Icon",
        "ChevronDownIcon",
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


def DragHandle(id=None):
    sortable = useSortable({"id": id})
    attributes, listeners = sortable.attributes, sortable.listeners
    return t"""
        <{Button}
            ...{attributes}
            ...{listeners}
            variant="ghost"
            size="icon"
            class="size-7 text-muted-foreground hover:bg-transparent"
        >
            <{GripVerticalIcon} class="size-3 text-muted-foreground" />
            <span class="sr-only">Drag to reorder</span>
        </{Button}>
    """


def drag_cell(props):
    row = props.row

    return t"<{DragHandle} id={row.original["id"]} />"


def select_header(props):
    table = props.get("table")

    return t"""
        <div class="flex items-center justify-center">
            <{Checkbox}
                checked={table.getIsAllPageRowsSelected()}
                indeterminate={table.getIsSomePageRowsSelected() and not table.getIsAllPageRowsSelected()}
                onCheckedChange={(lambda value: table.toggleAllPageRowsSelected(bool(value)))}
                aria-label="Select all"
            />
        </div>
    """


def select_cell(props):
    row = props.row

    return t"""
        <div class="flex items-center justify-center">
            <{Checkbox}
                checked={row.getIsSelected()}
                onCheckedChange={(lambda value: row.toggleSelected(bool(value)))}
                aria-label="Select row"
            />
        </div>
    """


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
        <{Select} items={[{"label": "Eddie Lake", "value": "Eddie Lake"}, {"label": "Jamik Tashpulatov", "value": "Jamik Tashpulatov"}]}>
            <{SelectTrigger}
                class="w-38 **:data-[slot=select-value]:block **:data-[slot=select-value]:truncate"
                size="sm"
                id={f"{row.original["id"]}-reviewer"}
            >
                <{SelectValue} placeholder="Assign reviewer" />
            </{SelectTrigger}>
            <{SelectContent} align="end">
                <{SelectGroup}>
                    <{SelectItem} value="Eddie Lake">Eddie Lake</{SelectItem}>
                    <{SelectItem} value="Jamik Tashpulatov">Jamik Tashpulatov</{SelectItem}>
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
                "header": select_header,
                "cell": select_cell,
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
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} render={t'''
                            <{Button}
                                variant="ghost"
                                class="flex size-8 text-muted-foreground data-open:bg-muted"
                                size="icon"
                            />
                        '''}>
                            <{EllipsisVerticalIcon} />
                            <span class="sr-only">Open menu</span>
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent} align="end" class="w-32">
                            <{DropdownMenuItem}>Edit</{DropdownMenuItem}>
                            <{DropdownMenuItem}>Make a copy</{DropdownMenuItem}>
                            <{DropdownMenuItem}>Favorite</{DropdownMenuItem}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuItem} variant="destructive">Delete</{DropdownMenuItem}>
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                """,
            },
        ),
    ],
)


def DraggableRow(row=None):
    sortable = useSortable({"id": row["original"]["id"]})
    transform, transition, set_node_ref, is_dragging = sortable.transform, sortable.transition, sortable.setNodeRef, sortable.isDragging
    return t"""
        <{TableRow}
            data-state={row["getIsSelected"]() and "selected"}
            data-dragging={is_dragging}
            ref={set_node_ref}
            class="relative z-0 data-[dragging=true]:z-10 data-[dragging=true]:opacity-80"
            style={ {
                "transform": CSS.Transform.toString(transform),
                "transition": transition,
            } }
        >
            {[t'''
                <{TableCell} key={cell.id}>
                    <{FlexRender} cell={cell} />
                </{TableCell}>
            ''' for cell in row["getVisibleCells"]()]}
        </{TableRow}>
    """


def DataTable(data=None):
    initial_data = data

    data, set_data = use_state(lambda: initial_data)
    row_selection, set_row_selection = use_state({})
    column_visibility, set_column_visibility = use_state({})
    column_filters, set_column_filters = use_state([])
    sorting, set_sorting = use_state([])
    pagination, set_pagination = use_state({"pageIndex": 0, "pageSize": 10})
    sortable_id = use_id()
    sensors = useSensors(useSensor(MouseSensor, {}), useSensor(TouchSensor, {}), useSensor(KeyboardSensor, {}))
    data_ids = use_memo(lambda: [item["id"] for item in data] or [], [data])
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

    def handle_drag_end(event):
        active, over = event.get("active"), event.get("over")
        if active and over and active["id"] != over["id"]:
            def callback(data):
                old_index = data_ids.index(active["id"])
                new_index = data_ids.index(over["id"])
                return arrayMove(data, old_index, new_index)

            set_data(callback)

    def render_column(column):
        return t"""
            <{DropdownMenuCheckboxItem}
                key={column.id}
                class="capitalize"
                checked={column.getIsVisible()}
                onCheckedChange={(lambda value: column.toggleVisibility(bool(value)))}
            >
                {column.id}
            </{DropdownMenuCheckboxItem}>
        """

    def on_value_change(value):
        table.setPageSize(float(value))

    return t"""
        <{Tabs} defaultValue="outline" class="w-full flex-col justify-start gap-6">
            <div class="flex items-center justify-between px-4 lg:px-6">
                <{Label} for="view-selector" class="sr-only">View</{Label}>
                <{Select}
                    defaultValue="outline"
                    items={[{"label": "Outline", "value": "outline"}, {"label": "Past Performance", "value": "past-performance"}, {"label": "Key Personnel", "value": "key-personnel"}, {"label": "Focus Documents", "value": "focus-documents"}]}
                >
                    <{SelectTrigger} class="flex w-fit @4xl/main:hidden" size="sm" id="view-selector">
                        <{SelectValue} placeholder="Select a view" />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="outline">Outline</{SelectItem}>
                            <{SelectItem} value="past-performance">Past Performance</{SelectItem}>
                            <{SelectItem} value="key-personnel">Key Personnel</{SelectItem}>
                            <{SelectItem} value="focus-documents">Focus Documents</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{TabsList} class="hidden **:data-[slot=badge]:size-5 **:data-[slot=badge]:rounded-full **:data-[slot=badge]:bg-muted-foreground/30 **:data-[slot=badge]:px-1 @4xl/main:flex">
                    <{TabsTrigger} value="outline">Outline</{TabsTrigger}>
                    <{TabsTrigger} value="past-performance">
                        Past Performance <{Badge} variant="secondary">3</{Badge}>
                    </{TabsTrigger}>
                    <{TabsTrigger} value="key-personnel">
                        Key Personnel <{Badge} variant="secondary">2</{Badge}>
                    </{TabsTrigger}>
                    <{TabsTrigger} value="focus-documents">Focus Documents</{TabsTrigger}>
                </{TabsList}>
                <div class="flex items-center gap-2">
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} render={t'<{Button} variant="outline" size="sm" />'}>
                            <{Columns3Icon} data-icon="inline-start" />
                            Columns
                            <{ChevronDownIcon} data-icon="inline-end" />
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent} align="end" class="w-32">
                            {[render_column(column) for column in table.getAllColumns() if getattr(column, "accessorFn", None) is not None and column.getCanHide()]}
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                    <{Button} variant="outline" size="sm">
                        <{PlusIcon} />
                        <span class="hidden lg:inline">Add Section</span>
                    </{Button}>
                </div>
            </div>
            <{TabsContent} value="outline" class="relative flex flex-col gap-4 overflow-auto px-4 lg:px-6">
                <div class="overflow-hidden rounded-lg border">
                    <{DndContext}
                        collisionDetection={closestCenter}
                        modifiers={[restrictToVerticalAxis]}
                        onDragEnd={handle_drag_end}
                        sensors={sensors}
                        id={sortable_id}
                    >
                        <{Table}>
                            <{TableHeader} class="sticky top-0 z-10 bg-muted">
                                {[t'''
                                    <{TableRow} key={header_group["id"]}>
                                        {[t"""
                                            <{TableHead}
                                                key={header.id}
                                                colSpan={header.colSpan}
                                            >
                                                {None if header.isPlaceholder else t'<{FlexRender} header={header} />'}
                                            </{TableHead}>
                                        """ for header in header_group["headers"]]}
                                    </{TableRow}>
                                ''' for header_group in table.getHeaderGroups()]}
                            </{TableHeader}>
                            <{TableBody} class="**:data-[slot=table-cell]:first:w-8">
                                {t'''
                                    <{SortableContext}
                                        items={data_ids}
                                        strategy={verticalListSortingStrategy}
                                    >
                                        {[t"<{DraggableRow} key={row.id} row={row} />" for row in table.getRowModel()["rows"]]}
                                    </{SortableContext}>
                                ''' if len(table.getRowModel()["rows"]) else t'''
                                    <{TableRow}>
                                        <{TableCell} colSpan={columns.length} class="h-24 text-center">
                                            No results.
                                        </{TableCell}>
                                    </{TableRow}>
                                '''}
                            </{TableBody}>
                        </{Table}>
                    </{DndContext}>
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
                                value={f"{table.state["pagination"]["pageSize"]}"}
                                onValueChange={on_value_change}
                                items={[{
                                    "label": f"{page_size}",
                                    "value": f"{page_size}",
                                } for page_size in [10, 20, 30, 40, 50]]}
                            >
                                <{SelectTrigger} size="sm" class="w-20" id="rows-per-page">
                                    <{SelectValue} placeholder={table.state["pagination"]["pageSize"]} />
                                </{SelectTrigger}>
                                <{SelectContent} side="top">
                                    <{SelectGroup}>
                                        {[t'''
                                            <{SelectItem}
                                                key={page_size}
                                                value={f"{page_size}"}
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
                                onClick={(lambda: table.setPageIndex(0))}
                                disabled={not table.getCanPreviousPage()}
                            >
                                <span class="sr-only">Go to first page</span>
                                <{ChevronsLeftIcon} />
                            </{Button}>
                            <{Button}
                                variant="outline"
                                class="size-8"
                                size="icon"
                                onClick={(lambda: table.previousPage())}
                                disabled={not table.getCanPreviousPage()}
                            >
                                <span class="sr-only">Go to previous page</span>
                                <{ChevronLeftIcon} />
                            </{Button}>
                            <{Button}
                                variant="outline"
                                class="size-8"
                                size="icon"
                                onClick={(lambda: table.nextPage())}
                                disabled={not table.getCanNextPage()}
                            >
                                <span class="sr-only">Go to next page</span>
                                <{ChevronRightIcon} />
                            </{Button}>
                            <{Button}
                                variant="outline"
                                class="hidden size-8 lg:flex"
                                size="icon"
                                onClick={(lambda: table.setPageIndex(table.getPageCount() - 1))}
                                disabled={not table.getCanNextPage()}
                            >
                                <span class="sr-only">Go to last page</span>
                                <{ChevronsRightIcon} />
                            </{Button}>
                        </div>
                    </div>
                </div>
            </{TabsContent}>
            <{TabsContent} value="past-performance" class="flex flex-col px-4 lg:px-6">
                <div class="aspect-video w-full flex-1 rounded-lg border border-dashed"></div>
            </{TabsContent}>
            <{TabsContent} value="key-personnel" class="flex flex-col px-4 lg:px-6">
                <div class="aspect-video w-full flex-1 rounded-lg border border-dashed"></div>
            </{TabsContent}>
            <{TabsContent} value="focus-documents" class="flex flex-col px-4 lg:px-6">
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
                                <{Select}
                                    defaultValue={item["type"]}
                                    items={[{"label": "Table of Contents", "value": "Table of Contents"}, {"label": "Executive Summary", "value": "Executive Summary"}, {"label": "Technical Approach", "value": "Technical Approach"}, {"label": "Design", "value": "Design"}, {"label": "Capabilities", "value": "Capabilities"}, {"label": "Focus Documents", "value": "Focus Documents"}, {"label": "Narrative", "value": "Narrative"}, {"label": "Cover Page", "value": "Cover Page"}]}
                                >
                                    <{SelectTrigger} id="type" class="w-full">
                                        <{SelectValue} placeholder="Select a type" />
                                    </{SelectTrigger}>
                                    <{SelectContent}>
                                        <{SelectGroup}>
                                            <{SelectItem} value="Table of Contents">Table of Contents</{SelectItem}>
                                            <{SelectItem} value="Executive Summary">Executive Summary</{SelectItem}>
                                            <{SelectItem} value="Technical Approach">Technical Approach</{SelectItem}>
                                            <{SelectItem} value="Design">Design</{SelectItem}>
                                            <{SelectItem} value="Capabilities">Capabilities</{SelectItem}>
                                            <{SelectItem} value="Focus Documents">Focus Documents</{SelectItem}>
                                            <{SelectItem} value="Narrative">Narrative</{SelectItem}>
                                            <{SelectItem} value="Cover Page">Cover Page</{SelectItem}>
                                        </{SelectGroup}>
                                    </{SelectContent}>
                                </{Select}>
                            </div>
                            <div class="flex flex-col gap-3">
                                <{Label} for="status">Status</{Label}>
                                <{Select}
                                    defaultValue={item["status"]}
                                    items={[{"label": "Done", "value": "Done"}, {"label": "In Progress", "value": "In Progress"}, {"label": "Not Started", "value": "Not Started"}]}
                                >
                                    <{SelectTrigger} id="status" class="w-full">
                                        <{SelectValue} placeholder="Select a status" />
                                    </{SelectTrigger}>
                                    <{SelectContent}>
                                        <{SelectGroup}>
                                            <{SelectItem} value="Done">Done</{SelectItem}>
                                            <{SelectItem} value="In Progress">In Progress</{SelectItem}>
                                            <{SelectItem} value="Not Started">Not Started</{SelectItem}>
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
                                defaultValue={item["reviewer"]}
                                items={[{"label": "Eddie Lake", "value": "Eddie Lake"}, {"label": "Jamik Tashpulatov", "value": "Jamik Tashpulatov"}, {"label": "Emily Whalen", "value": "Emily Whalen"}]}
                            >
                                <{SelectTrigger} id="reviewer" class="w-full">
                                    <{SelectValue} placeholder="Select a reviewer" />
                                </{SelectTrigger}>
                                <{SelectContent}>
                                    <{SelectGroup}>
                                        <{SelectItem} value="Eddie Lake">Eddie Lake</{SelectItem}>
                                        <{SelectItem} value="Jamik Tashpulatov">Jamik Tashpulatov</{SelectItem}>
                                        <{SelectItem} value="Emily Whalen">Emily Whalen</{SelectItem}>
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
