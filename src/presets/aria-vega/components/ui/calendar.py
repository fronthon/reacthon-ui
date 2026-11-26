from utils import cn, cva
from button import Button, button_variants
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue

__js__ = {
    "react-aria-components": [
        "Calendar as AriaCalendar",
        "CalendarGridHeader as AriaCalendarGridHeader",
        "RangeCalendar as AriaRangeCalendar",
        "CalendarCell",
        "CalendarGrid",
        "CalendarGridBody",
        "CalendarHeaderCell",
        "CalendarHeading",
        "CalendarMonthPicker",
        "CalendarYearPicker",
    ],
    "lucide-react": ["ChevronLeftIcon", "ChevronRightIcon"],
}

cell_variants = cva(
    "group/day relative mt-2 aspect-square h-full w-full cursor-default rounded-(--cell-radius) p-0 text-center select-none [&:is(:last-child>[data-selected=true])>div]:rounded-r-(--cell-radius)",
    {
        "showWeekNumber": {
            "false": "[&:is(:first-child>[data-selected=true])>div]:rounded-l-(--cell-radius)",
            "true": "[&:is(:nth-child(2)>[data-selected=true])>div]:rounded-l-(--cell-radius)",
        },
        "isToday": {"true": "rounded-(--cell-radius) bg-muted text-foreground data-[selected=true]:rounded-none"},
        "isSelectionStart": {
            "true": "relative isolate z-0 rounded-l-(--cell-radius) bg-muted after:absolute after:inset-y-0 after:right-0 after:w-4 after:bg-muted",
        },
        "isSelectionEnd": {
            "true": "relative isolate z-0 rounded-r-(--cell-radius) bg-muted after:absolute after:inset-y-0 after:left-0 after:w-4 after:bg-muted",
        },
        "isUnavailable": {"true": "text-muted-foreground opacity-50 [&>div]:line-through"},
        "isDisabled": {"true": "text-muted-foreground opacity-50"},
        "isOutsideMonth": {"true": "text-muted-foreground aria-selected:text-muted-foreground"},
    },
)


def Calendar(**props):
    return t"""
        <{AriaCalendar}
            ...{props}
            data-slot="calendar"
            visibleDuration={ {
                "months": props.get("numberOfMonths") or 1,
            } }
            class={cn("group/calendar w-fit bg-background p-3 [--cell-radius:var(--radius-md)] [--cell-size:--spacing(8)] in-data-[slot=card-content]:bg-transparent in-data-[slot=popover-content]:bg-transparent", props.get("className"))}
        >
            <{CalendarInner} ...{props} />
        </{AriaCalendar}>
    """


def RangeCalendar(**props):
    return t"""
        <{AriaRangeCalendar}
            ...{props}
            data-slot="calendar"
            visibleDuration={ {
                "months": props.get("numberOfMonths") or 1,
            } }
            class={cn("group/calendar w-fit bg-background p-3 [--cell-radius:var(--radius-md)] [--cell-size:--spacing(8)] in-data-[slot=card-content]:bg-transparent in-data-[slot=popover-content]:bg-transparent", props.get("className"))}
        >
            <{CalendarInner} ...{props} isRange />
        </{AriaRangeCalendar}>
    """


def CalendarInner(captionLayout="label", buttonVariant="ghost", numberOfMonths=1, showWeekNumber=False, headerFormat=None, renderCell=None, isRange=None, **_):
    def class_name(render_props):
        return cell_variants(**dict(render_props), showWeekNumber=showWeekNumber)

    return t"""
        <div class="relative flex flex-col gap-4 md:flex-row">
            <header class="absolute inset-x-0 top-0 flex w-full items-center justify-between gap-1">
                <{Button}
                    variant={buttonVariant}
                    slot="previous"
                    class="size-(--cell-size) p-0 select-none aria-disabled:opacity-50"
                >
                    <{ChevronLeftIcon} class="size-4" />
                </{Button}>
                <{Button}
                    variant={buttonVariant}
                    slot="next"
                    class="size-(--cell-size) p-0 select-none aria-disabled:opacity-50"
                >
                    <{ChevronRightIcon} class="size-4" />
                </{Button}>
            </header>
            {[t'''
                <div key={i} class="flex w-full flex-col gap-4">
                    <div class="flex h-(--cell-size) w-full items-center justify-center gap-1 px-(--cell-size)">
                        {t"""
                            <{MonthDropdown} format={headerFormat} />
                            <{YearDropdown} format={headerFormat} />
                        """ if captionLayout == "dropdown" else t"""
                            <{CalendarHeading}
                                offset={ {
                                    "months": i,
                                } }
                                format={headerFormat}
                                class="text-sm font-medium select-none"
                            />
                        """}
                    </div>
                    <{CalendarGrid}
                        class="w-full border-collapse"
                        offset={ {
                            "months": i,
                        } }
                    >
                        <{AriaCalendarGridHeader}>
                            {(lambda day: t"""
                                <{CalendarHeaderCell} class="rounded-(--cell-radius) text-[0.8rem] font-normal text-muted-foreground select-none">
                                    {day}
                                </{CalendarHeaderCell}>
                            """)}
                        </{AriaCalendarGridHeader}>
                        <{CalendarGridBody}>
                            {(lambda date: t"""
                                <{CalendarCell}
                                    date={date}
                                    class={class_name}
                                >
                                    {(lambda render_props: t'''
                                        <div
                                            data-selected-single={render_props["isSelected"] and not isRange}
                                            data-range-start={render_props["isSelectionStart"] and isRange}
                                            data-range-end={render_props["isSelectionEnd"] and isRange}
                                            data-range-middle={render_props["isSelected"] and not render_props["isSelectionStart"] and not render_props["isSelectionEnd"] and isRange}
                                            class={cn(
                                                button_variants(variant="ghost", size="icon"),
                                                "relative isolate z-10 flex aspect-square h-full w-full min-w-(--cell-size) flex-col gap-1 border-0 leading-none font-normal group-data-[focused=true]/day:relative group-data-[focused=true]/day:z-10 group-data-[focused=true]/day:border-ring group-data-[focused=true]/day:ring-[3px] group-data-[focused=true]/day:ring-ring/50 data-[range-end=true]:rounded-(--cell-radius) data-[range-end=true]:rounded-r-(--cell-radius) data-[range-end=true]:bg-primary data-[range-end=true]:text-primary-foreground data-[range-middle=true]:rounded-none data-[range-middle=true]:bg-muted data-[range-middle=true]:text-foreground data-[range-start=true]:rounded-(--cell-radius) data-[range-start=true]:rounded-l-(--cell-radius) data-[range-start=true]:bg-primary data-[range-start=true]:text-primary-foreground data-[selected-single=true]:bg-primary data-[selected-single=true]:text-primary-foreground dark:hover:text-foreground [&>span]:text-xs [&>span]:opacity-70",
                                            )}
                                        >
                                            {renderCell(render_props) if renderCell else render_props["defaultChildren"]}
                                        </div>
                                    ''')}
                                </{CalendarCell}>
                            """)}
                        </{CalendarGridBody}>
                    </{CalendarGrid}>
                </div>
            ''' for i in range(numberOfMonths)]}
        </div>
    """


def MonthDropdown(format=None, **_):
    return t"""
        <{CalendarMonthPicker} format={format.month if format else None}>
            {(lambda props: t'''
                <{Select} ...{props} class="relative">
                    <{SelectTrigger}>
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent} class="min-w-0">
                        <{SelectGroup}>
                            {[t"""
                                <{SelectItem}
                                    key={item["id"]}
                                    id={item["id"]}
                                >
                                    {item["formatted"]}
                                </{SelectItem}>
                            """ for item in props.items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
            ''')}
        </{CalendarMonthPicker}>
    """


def YearDropdown(format=None, **_):
    return t"""
        <{CalendarYearPicker} format={format}>
            {(lambda props: t'''
                <{Select} ...{props} class="relative">
                    <{SelectTrigger}>
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent} class="min-w-0">
                        {[t"""
                            <{SelectItem}
                                key={item["id"]}
                                id={item["id"]}
                            >
                                {item["formatted"]}
                            </{SelectItem}>
                        """ for item in props.items]}
                    </{SelectContent}>
                </{Select}>
            ''')}
        </{CalendarYearPicker}>
    """
