from utils import cn


def Table(className=None, **props):
    return t"""
        <div data-slot="table-container" class="relative w-full overflow-x-auto">
            <table data-slot="table" class={cn("w-full caption-bottom text-sm", className)} ...{props} />
        </div>
    """


def TableHeader(className=None, **props):
    return t'<thead data-slot="table-header" class={cn("[&_tr]:border-b", className)} ...{props} />'


def TableBody(className=None, **props):
    return t'<tbody data-slot="table-body" class={cn("[&_tr:last-child]:border-0", className)} ...{props} />'


def TableFooter(className=None, **props):
    return t"""
        <tfoot
            data-slot="table-footer"
            class={cn("border-t bg-muted/50 font-medium [&>tr]:last:border-b-0", className)}
            ...{props}
        />
    """


def TableRow(className=None, **props):
    return t"""
        <tr
            data-slot="table-row"
            class={cn("border-b transition-colors hover:bg-muted/50 has-aria-expanded:bg-muted/50 data-[state=selected]:bg-muted", className)}
            ...{props}
        />
    """


def TableHead(className=None, **props):
    return t"""
        <th
            data-slot="table-head"
            class={cn("h-12 px-3 text-left align-middle text-xs font-medium tracking-wider whitespace-nowrap text-muted-foreground uppercase [&:has([role=checkbox])]:pr-0", className)}
            ...{props}
        />
    """


def TableCell(className=None, **props):
    return t"""
        <td
            data-slot="table-cell"
            class={cn("p-3 align-middle whitespace-nowrap [&:has([role=checkbox])]:pr-0", className)}
            ...{props}
        />
    """


def TableCaption(className=None, **props):
    return t"""
        <caption
            data-slot="table-caption"
            class={cn("mt-4 text-sm text-muted-foreground", className)}
            ...{props}
        />
    """
