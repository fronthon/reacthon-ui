from javascript import Date
from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from calendar import Calendar, RangeCalendar
from card import Card, CardContent, CardFooter
from field import Field, FieldGroup, FieldLabel
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from popover import Popover, PopoverTrigger

__js__ = {
    "@internationalized/date": ["CalendarDate", "getLocalTimeZone", "isSameDay", "isWeekend", "today"],
    "react-aria-components": ["I18nProvider", "useLocale"],
    "lucide-react": ["CalendarIcon", "Clock2Icon", "ChevronDownIcon"],
}


def CalendarExample():
    return t"""
        <{ExampleWrapper}>
            <{CalendarSingle} />
            <{CalendarMultiple} />
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
                    <{Calendar} />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarInPopover():
    return t"""
        <{Example} title="In Popover">
            <{PopoverTrigger}>
                <{Button} variant="outline" class="px-2.5 font-normal">
                    <{CalendarIcon} data-icon="inline-start" />
                    Open Calendar
                </{Button}>
                <{Popover} class="w-auto p-0" placement="bottom start">
                    <{Calendar} />
                </{Popover}>
            </{PopoverTrigger}>
        </{Example}>
    """


def CalendarSingle():
    date, set_date = use_state(CalendarDate.new(Date.new().getFullYear(), Date.new().getMonth() + 1, 12))
    return t"""
        <{Example} title="Single">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar} value={date} onChange={set_date} captionLayout="dropdown" />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarMultiple():
    return t"""
        <{Example} title="Multiple">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar} selectionMode="multiple" />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarRange():
    date_range, set_date_range = use_state(
        {"start": CalendarDate.new(Date.new().getFullYear(), 1, 12), "end": CalendarDate.new(Date.new().getFullYear(), 1, 12).add({"days": 30})},
    )

    return t"""
        <{Example} title="Range" containerClassName="lg:col-span-full 2xl:col-span-full" class="p-12">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{RangeCalendar}
                        value={date_range}
                        onChange={set_date_range}
                        numberOfMonths={2}
                        maxValue={today(getLocalTimeZone())}
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarRangeMultipleMonths():
    range_, set_range = use_state(
        {"start": CalendarDate.new(Date.new().getFullYear(), 4, 12), "end": CalendarDate.new(Date.new().getFullYear(), 4, 12).add({"days": 60})},
    )

    return t"""
        <{Example} title="Range Multiple Months" containerClassName="lg:col-span-full 2xl:col-span-full" class="p-12">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{I18nProvider} locale="es">
                        <{RangeCalendar} value={range_} onChange={set_range} numberOfMonths={3} weeksInMonth={6} />
                    </{I18nProvider}>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarBookedDates():
    date, set_date = use_state(CalendarDate.new(Date.new().getFullYear(), 2, 3))
    booked_dates = [CalendarDate.new(Date.new().getFullYear(), 2, 12 + i) for i in range(15)]

    return t"""
        <{Example} title="Booked Dates">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{Calendar}
                        value={date}
                        onChange={set_date}
                        isDateUnavailable={(lambda date: any(isSameDay(date, d) for d in booked_dates))}
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarWithTime():
    date, set_date = use_state(CalendarDate.new(Date.new().getFullYear(), Date.new().getMonth() + 1, 12))

    return t"""
        <{Example} title="With Time">
            <{Card} size="sm" class="mx-auto w-fit">
                <{CardContent}>
                    <{Calendar} value={date} onChange={set_date} class="p-0" />
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
    locale = useLocale().get("locale")
    range_, set_range = use_state(
        {"start": CalendarDate.new(Date.new().getFullYear(), 12, 8), "end": CalendarDate.new(Date.new().getFullYear(), 12, 8).add({"days": 10})},
    )

    def render_cell(props):
        is_outside_month, date, default_children = props.get("isOutsideMonth"), props.get("date"), props.get("defaultChildren")

        return t"""
            {default_children}
            {not is_outside_month and t'<span>{"$120" if isWeekend(date, locale) else "$100"}</span>'}
        """

    return t"""
        <{Example} title="Custom Days">
            <{Card} class="mx-auto w-fit p-0">
                <{CardContent} class="p-0">
                    <{RangeCalendar}
                        value={range_}
                        onChange={set_range}
                        numberOfMonths={1}
                        captionLayout="dropdown"
                        class="[--cell-size:--spacing(10)] md:[--cell-size:--spacing(12)]"
                        headerFormat={ {"month": "long"} }
                        renderCell={render_cell}
                    />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CalendarWithPresets():
    date, set_date = use_state(CalendarDate.new(Date.new().getFullYear(), 2, 12))
    current_month, set_current_month = use_state(
        CalendarDate.new(Date.new().getFullYear(), Date.new().getMonth() + 1, 1),
    )

    def render_preset(preset):
        def on_press():
            new_date = today(getLocalTimeZone()).add({"days": preset["value"]})
            set_date(new_date)
            set_current_month(new_date)

        return t"""
            <{Button}
                key={preset["value"]}
                variant="outline"
                size="sm"
                class="flex-1"
                onPress={on_press}
            >
                {preset["label"]}
            </{Button}>
        """

    return t"""
        <{Example} title="With Presets">
            <{Card} class="mx-auto w-fit max-w-[300px]" size="sm">
                <{CardContent}>
                    <{Calendar}
                        value={date}
                        onChange={set_date}
                        focusedValue={current_month}
                        onFocusChange={set_current_month}
                        weeksInMonth={6}
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

    return t"""
        <{Example} title="Date Picker Simple">
            <{Field} class="mx-auto w-72">
                <{FieldLabel} for="date-picker-simple">Date</{FieldLabel}>
                <{PopoverTrigger}>
                    <{Button} variant="outline" id="date-picker-simple" class="justify-start px-2.5 font-normal">
                        <{CalendarIcon} data-icon="inline-start" />
                        {date.toDate(getLocalTimeZone()).toLocaleDateString(None, {"dateStyle": "long"}) if date else t'<span>Pick a date</span>'}
                    </{Button}>
                    <{Popover} class="w-auto p-0" placement="bottom start">
                        <{Calendar} value={date} onChange={set_date} />
                    </{Popover}>
                </{PopoverTrigger}>
            </{Field}>
        </{Example}>
    """


def DatePickerWithRange():
    date, set_date = use_state(
        {"start": CalendarDate.new(Date.new().getFullYear(), 1, 20), "end": CalendarDate.new(Date.new().getFullYear(), 1, 20).add({"days": 20})},
    )

    return t"""
        <{Example} title="Date Picker Range">
            <{Field} class="mx-auto w-72">
                <{FieldLabel} for="date-picker-range">Date Picker Range</{FieldLabel}>
                <{PopoverTrigger}>
                    <{Button} variant="outline" id="date-picker-range" class="justify-start px-2.5 font-normal">
                        <{CalendarIcon} data-icon="inline-start" />
                        {Intl.DateTimeFormat.new(None, {"dateStyle": "long"}).formatRange(date["start"].toDate(getLocalTimeZone()), date["end"].toDate(getLocalTimeZone())) if (date["start"] if date else None) and date["end"] else t'<span>Pick a date</span>'}
                    </{Button}>
                    <{Popover} class="w-auto p-0" placement="bottom start">
                        <{RangeCalendar} value={date} onChange={set_date} numberOfMonths={2} />
                    </{Popover}>
                </{PopoverTrigger}>
            </{Field}>
        </{Example}>
    """


def DataPickerWithDropdowns():
    date, set_date = use_state(None)
    open_, set_open = use_state(False)

    return t"""
        <{Example} title="Date Picker with Dropdowns">
            <{Field} class="mx-auto w-72">
                <{FieldLabel} for="date-picker-with-dropdowns-desktop">Date</{FieldLabel}>
                <{PopoverTrigger} isOpen={open_} onOpenChange={set_open}>
                    <{Button}
                        variant="outline"
                        id="date-picker-with-dropdowns-desktop"
                        class="justify-start px-2.5 font-normal"
                    >
                        {date.toDate(getLocalTimeZone()).toLocaleDateString(None, {"dateStyle": "long"}) if date else t'<span>Pick a date</span>'}
                        <{ChevronDownIcon} data-icon="inline-start" class="ml-auto" />
                    </{Button}>
                    <{Popover} class="w-auto p-0" placement="bottom start">
                        <{Calendar} value={date} onChange={set_date} captionLayout="dropdown" />
                        <div class="flex gap-2 border-t p-2">
                            <{Button} variant="outline" size="sm" class="w-full" onPress={(lambda: set_open(False))}>
                                Done
                            </{Button}>
                        </div>
                    </{Popover}>
                </{PopoverTrigger}>
            </{Field}>
        </{Example}>
    """
