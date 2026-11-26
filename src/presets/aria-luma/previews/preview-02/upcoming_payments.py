from reacthon import use_state
from badge import Badge
from calendar import Calendar
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
from item import Item, ItemContent, ItemDescription, ItemGroup, ItemTitle

__js__ = {"@internationalized/date": ["getLocalTimeZone", "today"]}


def UpcomingPayments():
    date, set_date = use_state(today(getLocalTimeZone()))

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Upcoming Payments</{CardTitle}>
                <{CardDescription}>Select a date to view scheduled payments.</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <{Item} variant="outline" class="justify-center">
                    <{Calendar}
                        value={date}
                        onChange={set_date}
                        class="w-full [--cell-size:--spacing(8)] md:[--cell-size:--spacing(10)] style-sera:md:[--cell-size:--spacing(9)]"
                    />
                </{Item}>
                <{ItemGroup} class="w-full">
                    <{Item} variant="muted">
                        <{ItemContent}>
                            <{ItemTitle}>Netflix Subscription</{ItemTitle}>
                            <{ItemDescription}>Apr 15, 2024</{ItemDescription}>
                        </{ItemContent}>
                        <{Badge} variant="secondary">$19.99</{Badge}>
                    </{Item}>
                    <{Item} variant="muted">
                        <{ItemContent}>
                            <{ItemTitle}>Rent Payment</{ItemTitle}>
                            <{ItemDescription}>Apr 1, 2024</{ItemDescription}>
                        </{ItemContent}>
                        <{Badge} variant="secondary">$2,400.00</{Badge}>
                    </{Item}>
                    <{Item} variant="muted">
                        <{ItemContent}>
                            <{ItemTitle}>Auto Insurance</{ItemTitle}>
                            <{ItemDescription}>Apr 22, 2024</{ItemDescription}>
                        </{ItemContent}>
                        <{Badge} variant="secondary">$186.00</{Badge}>
                    </{Item}>
                </{ItemGroup}>
            </{CardContent}>
        </{Card}>
    """
