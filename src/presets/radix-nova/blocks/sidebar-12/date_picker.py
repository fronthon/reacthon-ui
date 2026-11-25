from javascript import Date
from reacthon import use_state
from calendar import Calendar
from sidebar import SidebarGroup, SidebarGroupContent


def DatePicker():
    date, set_date = use_state(Date.new(Date.new().getFullYear(), Date.new().getMonth(), 12))
    return t"""
        <{SidebarGroup} class="px-0">
            <{SidebarGroupContent}>
                <{Calendar}
                    mode="single"
                    selected={date}
                    onSelect={set_date}
                    captionLayout="dropdown"
                    class="bg-transparent [--cell-size:2.1rem]"
                />
            </{SidebarGroupContent}>
        </{SidebarGroup}>
    """
