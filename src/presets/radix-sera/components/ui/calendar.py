from reacthon import use_effect, use_ref
from utils import cn
from button import Button, button_variants

__js__ = {
    "react-day-picker": ["DayPicker", "getDefaultClassNames"],
    "lucide-react": ["ChevronLeftIcon", "ChevronRightIcon", "ChevronDownIcon"],
}


def Calendar(className=None, classNames=None, showOutsideDays=True, captionLayout="label", buttonVariant="ghost", locale=None, formatters=None, components=None, **props):
    default_class_names = getDefaultClassNames()

    def Root(className=None, rootRef=None, **props):
        return t'<div data-slot="calendar" ref={rootRef} class={cn(className)} ...{props} />'

    def Chevron(className=None, orientation=None, **props):
        if orientation == "left":
            return t"<{ChevronLeftIcon} class={cn("size-4", className)} ...{props} />"

        if orientation == "right":
            return t"<{ChevronRightIcon} class={cn("size-4", className)} ...{props} />"

        return t"<{ChevronDownIcon} class={cn("size-4", className)} ...{props} />"

    def DayButton(**props):
        return t"<{CalendarDayButton} locale={locale} ...{props} />"

    def WeekNumber(children=None, **props):
        return t"""
            <td ...{props}>
                <div class="flex size-(--cell-size) items-center justify-center text-center">{children}</div>
            </td>
        """

    return t"""
        <{DayPicker}
            showOutsideDays={showOutsideDays}
            class={cn(
                "group/calendar bg-background p-3 [--cell-radius:0] [--cell-size:--spacing(8)] in-data-[slot=card-content]:bg-transparent in-data-[slot=popover-content]:bg-transparent",
                r"rtl:**:[.rdp-button\_next>svg]:rotate-180",
                r"rtl:**:[.rdp-button\_previous>svg]:rotate-180",
                className,
            )}
            captionLayout={captionLayout}
            locale={locale}
            formatters={ {
                "formatMonthDropdown": lambda date: date.toLocaleString(locale.get("code") if locale else None, {"month": "short"}),
                **(formatters or {}),
            } }
            classNames={ {
                "root": cn("w-fit", default_class_names["root"]),
                "months": cn("relative flex flex-col gap-4 md:flex-row", default_class_names["months"]),
                "month": cn("flex w-full flex-col gap-4", default_class_names["month"]),
                "nav": cn("absolute inset-x-0 top-0 flex w-full items-center justify-between gap-1", default_class_names["nav"]),
                "button_previous": cn(button_variants(variant=buttonVariant), "size-(--cell-size) p-0 select-none aria-disabled:opacity-50", default_class_names["button_previous"]),
                "button_next": cn(button_variants(variant=buttonVariant), "size-(--cell-size) p-0 select-none aria-disabled:opacity-50", default_class_names["button_next"]),
                "month_caption": cn("flex h-(--cell-size) w-full items-center justify-center px-(--cell-size)", default_class_names["month_caption"]),
                "dropdowns": cn("flex h-(--cell-size) w-full items-center justify-center gap-1.5 text-sm font-medium", default_class_names["dropdowns"]),
                "dropdown_root": cn("relative rounded-(--cell-radius)", default_class_names["dropdown_root"]),
                "dropdown": cn("absolute inset-0 bg-popover opacity-0", default_class_names["dropdown"]),
                "caption_label": cn("font-medium select-none", "text-sm" if captionLayout == "label" else "flex items-center gap-1 rounded-(--cell-radius) text-sm [&>svg]:size-3.5 [&>svg]:text-muted-foreground", default_class_names["caption_label"]),
                "month_grid": cn("w-full border-collapse", default_class_names["month_grid"]),
                "weekdays": cn("flex", default_class_names["weekdays"]),
                "weekday": cn("flex-1 rounded-(--cell-radius) text-[0.8rem] font-normal text-muted-foreground select-none", default_class_names["weekday"]),
                "week": cn("mt-2 flex w-full", default_class_names["week"]),
                "week_number_header": cn("w-(--cell-size) select-none", default_class_names["week_number_header"]),
                "week_number": cn("text-[0.8rem] text-muted-foreground select-none", default_class_names["week_number"]),
                "day": cn("group/day relative aspect-square h-full w-full rounded-(--cell-radius) p-0 text-center select-none [&:last-child[data-selected=true]_button]:rounded-r-(--cell-radius)", "[&:nth-child(2)[data-selected=true]_button]:rounded-l-(--cell-radius)" if props.get("showWeekNumber") else "[&:first-child[data-selected=true]_button]:rounded-l-(--cell-radius)", default_class_names["day"]),
                "range_start": cn("relative isolate z-0 rounded-l-(--cell-radius) bg-muted after:absolute after:inset-y-0 after:right-0 after:w-4 after:bg-muted", default_class_names["range_start"]),
                "range_middle": cn("rounded-none", default_class_names["range_middle"]),
                "range_end": cn("relative isolate z-0 rounded-r-(--cell-radius) bg-muted after:absolute after:inset-y-0 after:left-0 after:w-4 after:bg-muted", default_class_names["range_end"]),
                "today": cn("rounded-(--cell-radius) bg-muted text-foreground data-[selected=true]:rounded-none", default_class_names["today"]),
                "outside": cn("text-muted-foreground aria-selected:text-muted-foreground", default_class_names["outside"]),
                "disabled": cn("text-muted-foreground opacity-50", default_class_names["disabled"]),
                "hidden": cn("invisible", default_class_names["hidden"]),
                **(classNames or {}),
            } }
            components={ {
                "Root": Root,
                "Chevron": Chevron,
                "DayButton": DayButton,
                "WeekNumber": WeekNumber,
                **(components or {}),
            } }
            ...{props}
        />
    """


def CalendarDayButton(className=None, day=None, modifiers=None, locale=None, **props):
    default_class_names = getDefaultClassNames()

    ref = use_ref(None)

    def effect():
        if modifiers.get("focused"):
            if ref.current:
                ref.current.focus()

    use_effect(effect, [modifiers.get("focused")])

    return t"""
        <{Button}
            ref={ref}
            variant="ghost"
            size="icon"
            data-day={day.date.toLocaleDateString(locale.get("code") if locale else None)}
            data-selected-single={modifiers.get("selected") and not modifiers.get("range_start") and not modifiers.get("range_end") and not modifiers.get("range_middle")}
            data-range-start={modifiers.get("range_start")}
            data-range-end={modifiers.get("range_end")}
            data-range-middle={modifiers.get("range_middle")}
            class={cn("relative isolate z-10 flex aspect-square size-auto w-full min-w-(--cell-size) flex-col gap-1 border-0 leading-none font-normal group-data-[focused=true]/day:relative group-data-[focused=true]/day:z-10 group-data-[focused=true]/day:border-ring group-data-[focused=true]/day:ring-[3px] group-data-[focused=true]/day:ring-ring/50 data-[range-end=true]:rounded-(--cell-radius) data-[range-end=true]:rounded-r-(--cell-radius) data-[range-end=true]:bg-primary data-[range-end=true]:text-primary-foreground data-[range-middle=true]:rounded-none data-[range-middle=true]:bg-muted data-[range-middle=true]:text-foreground data-[range-start=true]:rounded-(--cell-radius) data-[range-start=true]:rounded-l-(--cell-radius) data-[range-start=true]:bg-primary data-[range-start=true]:text-primary-foreground data-[selected-single=true]:bg-primary data-[selected-single=true]:text-primary-foreground dark:hover:text-foreground [&>span]:text-xs [&>span]:opacity-70", default_class_names["day"], className)}
            ...{props}
        />
    """
