from javascript import Date
from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from calendar import Calendar, CalendarDayButton
from card import Card, CardContent, CardFooter
from field import Field, FieldGroup, FieldLabel
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from popover import Popover, PopoverContent, PopoverTrigger

__js__ = {
    "date-fns": ["addDays", "format"],
    "react-day-picker/locale": ["es"],
    "lucide-react": ["CalendarIcon", "Clock2Icon", "ChevronDownIcon"],
}


def CalendarExample():
    return t"""
        <{ExampleWrapper}>
            <{CalendarSingle} />
            <{CalendarMultiple} />
            <{CalendarWeekNumbers} />
            <{CalendarBookedDates} />
            <{CalendarRange} />
            <{CalendarRangeMultipleMonths} />
            <{CalendarWithTime} />
            <{CalendarWithPresets} />
            <{CalendarCustomDays} />
            <{DatePickerSimple} />
            <{DataPickerWithDropdowns} />
            <{DatePickerWithRange} />
            <{CalendarInCard} />
            <{CalendarInPopover} />
        </{ExampleWrapper}>
    """


def CalendarInCard():
    return t"""
        <{Example} title="In Card">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar} mode="single" />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarInPopover():
    return t"""
        <{Example} title="In Popover">
            <{Popover}>
                <{PopoverTrigger} render={t'<{Button} variant="outline" class="px-2.5 font-normal" />'}>
                    <{CalendarIcon} data-icon="inline-start" />
                    Open Calendar
                </{PopoverTrigger}>
                <{PopoverContent} class="w-auto p-0" align="start">
                    <{Calendar} mode="single" />
                </{PopoverContent}>
            </{Popover}>
        </{Example}>
    """


def CalendarSingle():
    date, set_date = use_state(Date.new(Date.new().getFullYear(), Date.new().getMonth(), 12))
    return t"""
        <{Example} title="Single">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar} mode="single" selected={date} onSelect={set_date} captionLayout="dropdown" />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarMultiple():
    return t"""
        <{Example} title="Multiple">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar} mode="multiple" />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarRange():
    date_range, set_date_range = use_state(
        {"from": Date.new(Date.new().getFullYear(), 0, 12), "to": addDays(Date.new(Date.new().getFullYear(), 0, 12), 30)},
    )

    return t"""
        <{Example} title="Range" containerClassName="lg:col-span-full 2xl:col-span-full" class="p-12">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar}
                        mode="range"
                        defaultMonth={date_range["from"] if date_range else None}
                        selected={date_range}
                        onSelect={set_date_range}
                        numberOfMonths={2}
                        disabled={(lambda date: date > Date.new() or date < Date.new("1900-01-01"))}
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarRangeMultipleMonths():
    range_, set_range = use_state(
        {"from": Date.new(Date.new().getFullYear(), 3, 12), "to": addDays(Date.new(Date.new().getFullYear(), 3, 12), 60)},
    )

    return t"""
        <{Example} title="Range Multiple Months" containerClassName="lg:col-span-full 2xl:col-span-full" class="p-12">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar}
                        mode="range"
                        defaultMonth={range_["from"] if range_ else None}
                        selected={range_}
                        onSelect={set_range}
                        numberOfMonths={3}
                        locale={es}
                        fixedWeeks
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarBookedDates():
    date, set_date = use_state(Date.new(Date.new().getFullYear(), 1, 3))
    booked_dates = [Date.new(Date.new().getFullYear(), 1, 12 + i) for i in range(15)]

    return t"""
        <{Example} title="Booked Dates">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar}
                        mode="single"
                        defaultMonth={date}
                        selected={date}
                        onSelect={set_date}
                        disabled={booked_dates}
                        modifiers={ {
                            "booked": booked_dates,
                        } }
                        modifiersClassNames={ {"booked": "[&>button]:line-through opacity-100"} }
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarWithTime():
    date, set_date = use_state(Date.new(Date.new().getFullYear(), Date.new().getMonth(), 12))

    return t"""
        <{Example} title="With Time">
            <{Card} size="sm" class="mx-auto w-fit">
                <{CardContent}>
                    <{Calendar} mode="single" selected={date} onSelect={set_date} class="p-0" />
                </{CardContent}>
                <{CardFooter} class="border-t bg-card">
                    <{FieldGroup}>
                        <{Field}>
                            <{FieldLabel} for="time-from">Start Time</{FieldLabel}>
                            <{InputGroup}>
                                <{InputGroupInput}
                                    id="time-from"
                                    type="time"
                                    step="1"
                                    defaultValue="10:30:00"
                                    class="appearance-none [&::-webkit-calendar-picker-indicator]:hidden [&::-webkit-calendar-picker-indicator]:appearance-none"
                                />
                                <{InputGroupAddon}>
                                    <{Clock2Icon} class="text-muted-foreground" />
                                </{InputGroupAddon}>
                            </{InputGroup}>
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="time-to">End Time</{FieldLabel}>
                            <{InputGroup}>
                                <{InputGroupInput}
                                    id="time-to"
                                    type="time"
                                    step="1"
                                    defaultValue="12:30:00"
                                    class="appearance-none [&::-webkit-calendar-picker-indicator]:hidden [&::-webkit-calendar-picker-indicator]:appearance-none"
                                />
                                <{InputGroupAddon}>
                                    <{Clock2Icon} class="text-muted-foreground" />
                                </{InputGroupAddon}>
                            </{InputGroup}>
                        </{Field}>
                    </{FieldGroup}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CalendarCustomDays():
    range_, set_range = use_state(
        {"from": Date.new(Date.new().getFullYear(), 11, 8), "to": addDays(Date.new(Date.new().getFullYear(), 11, 8), 10)},
    )

    def DayButton(children=None, modifiers=None, day=None, **props):
        is_weekend = day.date.getDay() == 0 or day.date.getDay() == 6

        return t"""
            <{CalendarDayButton}
                day={day}
                modifiers={modifiers}
                ...{props}
            >
                {children}
                {not modifiers.get("outside") and t'<span>{"$120" if is_weekend else "$100"}</span>'}
            </{CalendarDayButton}>
        """

    return t"""
        <{Example} title="Custom Days">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar}
                        mode="range"
                        defaultMonth={range_["from"] if range_ else None}
                        selected={range_}
                        onSelect={set_range}
                        numberOfMonths={1}
                        captionLayout="dropdown"
                        class="[--cell-size:--spacing(10)] md:[--cell-size:--spacing(12)]"
                        formatters={ {
                            "formatMonthDropdown": lambda date: date.toLocaleString("default", {"month": "long"}),
                        } }
                        components={ {
                            "DayButton": DayButton,
                        } }
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarWithPresets():
    date, set_date = use_state(Date.new(Date.new().getFullYear(), 1, 12))
    current_month, set_current_month = use_state(Date.new(Date.new().getFullYear(), Date.new().getMonth(), 1))

    def render_preset(preset):
        def on_click():
            new_date = addDays(Date.new(), preset["value"])
            set_date(new_date)
            set_current_month(Date.new(new_date.getFullYear(), new_date.getMonth(), 1))

        return t"""
            <{Button}
                key={preset["value"]}
                variant="outline"
                size="sm"
                class="flex-1"
                onClick={on_click}
            >
                {preset["label"]}
            </{Button}>
        """

    return t"""
        <{Example} title="With Presets">
            <{Card} class="mx-auto w-fit max-w-[300px]" size="sm">
                <{CardContent}>
                    <{Calendar}
                        mode="single"
                        selected={date}
                        onSelect={set_date}
                        month={current_month}
                        onMonthChange={set_current_month}
                        fixedWeeks
                        class="p-0 [--cell-size:--spacing(9.5)]"
                    />
                </{CardContent}>
                <{CardFooter} class="flex flex-wrap gap-2 border-t">
                    {[render_preset(preset) for preset in [{"label": "Today", "value": 0}, {"label": "Tomorrow", "value": 1}, {"label": "In 3 days", "value": 3}, {"label": "In a week", "value": 7}, {"label": "In 2 weeks", "value": 14}]]}
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def DatePickerSimple():
    date, set_date = use_state(None)

    button = t'<{Button} variant="outline" id="date-picker-simple" class="justify-start px-2.5 font-normal" />'

    return t"""
        <{Example} title="Date Picker Simple">
            <{Field} class="mx-auto w-72">
                <{FieldLabel} for="date-picker-simple">Date</{FieldLabel}>
                <{Popover}>
                    <{PopoverTrigger} render={button}>
                        <{CalendarIcon} data-icon="inline-start" />
                        {format(date, "PPP") if date else t'<span>Pick a date</span>'}
                    </{PopoverTrigger}>
                    <{PopoverContent} class="w-auto p-0" align="start">
                        <{Calendar} mode="single" selected={date} onSelect={set_date} />
                    </{PopoverContent}>
                </{Popover}>
            </{Field}>
        </{Example}>
    """


def DatePickerWithRange():
    date, set_date = use_state(
        {"from": Date.new(Date.new().getFullYear(), 0, 20), "to": addDays(Date.new(Date.new().getFullYear(), 0, 20), 20)},
    )

    button = t'<{Button} variant="outline" id="date-picker-range" class="justify-start px-2.5 font-normal" />'

    return t"""
        <{Example} title="Date Picker Range">
            <{Field} class="mx-auto w-72">
                <{FieldLabel} for="date-picker-range">Date Picker Range</{FieldLabel}>
                <{Popover}>
                    <{PopoverTrigger} render={button}>
                        <{CalendarIcon} data-icon="inline-start" />
                        {(t'''
                            {format(date["from"], "LLL dd, y")} -{" "}
                            {format(date.get("to"), "LLL dd, y")}
                        ''' if date.get("to") else format(date["from"], "LLL dd, y")) if (date["from"] if date else None) else t'<span>Pick a date</span>'}
                    </{PopoverTrigger}>
                    <{PopoverContent} class="w-auto p-0" align="start">
                        <{Calendar}
                            mode="range"
                            defaultMonth={date["from"] if date else None}
                            selected={date}
                            onSelect={set_date}
                            numberOfMonths={2}
                        />
                    </{PopoverContent}>
                </{Popover}>
            </{Field}>
        </{Example}>
    """


def DataPickerWithDropdowns():
    date, set_date = use_state(None)
    open_, set_open = use_state(False)

    button = t"""
        <{Button}
            variant="outline"
            id="date-picker-with-dropdowns-desktop"
            class="justify-start px-2.5 font-normal"
        />
    """

    return t"""
        <{Example} title="Date Picker with Dropdowns">
            <{Field} class="mx-auto w-72">
                <{Popover} open={open_} onOpenChange={set_open}>
                    <{FieldLabel} for="date-picker-with-dropdowns-desktop">Date</{FieldLabel}>
                    <{PopoverTrigger} render={button}>
                        {format(date, "PPP") if date else t'<span>Pick a date</span>'}
                        <{ChevronDownIcon} data-icon="inline-start" class="ml-auto" />
                    </{PopoverTrigger}>
                    <{PopoverContent} class="w-auto p-0" align="start">
                        <{Calendar} mode="single" selected={date} onSelect={set_date} captionLayout="dropdown" />
                        <div class="flex gap-2 border-t p-2">
                            <{Button} variant="outline" size="sm" class="w-full" onClick={(lambda: set_open(False))}>
                                Done
                            </{Button}>
                        </div>
                    </{PopoverContent}>
                </{Popover}>
            </{Field}>
        </{Example}>
    """


def CalendarWeekNumbers():
    date, set_date = use_state(Date.new(Date.new().getFullYear(), 1, 3))

    return t"""
        <{Example} title="Week Numbers" class="justify-center">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar} mode="single" defaultMonth={date} selected={date} onSelect={set_date} showWeekNumber />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """
