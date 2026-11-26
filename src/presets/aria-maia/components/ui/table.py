from utils import cn

__js__ = {
    "react-aria-components": [
        "Cell as CellPrimitive",
        "Column as ColumnPrimitive",
        "Row as RowPrimitive",
        "TableBody as TableBodyPrimitive",
        "TableFooter as TableFooterPrimitive",
        "TableHeader as TableHeaderPrimitive",
        "Table as TablePrimitive",
    ],
}


def Table(className=None, **props):
    return t"""
        <div data-slot="table-container" class="relative w-full overflow-x-auto">
            <{TablePrimitive} data-slot="table" class={cn("w-full caption-bottom text-sm", className)} ...{props} />
        </div>
    """


def TableHeader(className=None, **props):
    return t'<{TableHeaderPrimitive} data-slot="table-header" class={cn("[&_tr]:border-b", className)} ...{props} />'


def TableBody(className=None, **props):
    return t"""
        <{TableBodyPrimitive}
            data-slot="table-body"
            class={cn("data-empty:h-24 data-empty:text-center [&_tr:last-child]:border-0", className)}
            ...{props}
        />
    """


def TableFooter(className=None, **props):
    return t"""
        <{TableFooterPrimitive}
            data-slot="table-footer"
            class={cn("border-t bg-muted/50 font-medium [&>tr]:last:border-b-0", className)}
            ...{props}
        />
    """


def TableRow(className=None, **props):
    return t"""
        <{RowPrimitive}
            data-slot="table-row"
            class={cn("border-b transition-colors hover:bg-muted/50 has-aria-expanded:bg-muted/50 data-[state=selected]:bg-muted data-selected:bg-muted", className)}
            ...{props}
        />
    """


def TableHead(className=None, **props):
    return t"""
        <{ColumnPrimitive}
            data-slot="table-head"
            class={cn("h-12 px-3 text-left align-middle font-medium whitespace-nowrap text-foreground [&:has([data-slot=checkbox])]:pr-0 [&:has([role=checkbox])]:pr-0", className)}
            ...{props}
        />
    """


def TableCell(className=None, **props):
    return t"""
        <{CellPrimitive}
            data-slot="table-cell"
            class={cn("p-3 align-middle whitespace-nowrap [&:has([data-slot=checkbox])]:pr-0 [&:has([role=checkbox])]:pr-0", className)}
            ...{props}
        />
    """


def TableCaption(className=None, **props):
    return t"""
        <figcaption
            data-slot="table-caption"
            class={cn("mt-4 text-center text-sm text-muted-foreground", className)}
            ...{props}
        />
    """
