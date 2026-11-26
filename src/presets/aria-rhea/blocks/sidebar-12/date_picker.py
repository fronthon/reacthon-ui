from javascript import Date
from reacthon import use_state
from calendar import Calendar
from sidebar import SidebarGroup, SidebarGroupContent

__js__ = {"@internationalized/date": ["CalendarDate"]}


def DatePicker():
    date, set_date = use_state(CalendarDate.new(Date.new().getFullYear(), Date.new().getMonth() + 1, 12))
    return t"""
        <{SidebarGroup} class="px-0">
            <{SidebarGroupContent}>
                <{Calendar}
                    value={date}
                    onChange={set_date}
                    captionLayout="dropdown"
                    class="bg-transparent [--cell-size:2.1rem]"
                />
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
