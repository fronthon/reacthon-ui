from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from field import Field, FieldDescription, FieldError, FieldLabel
from input import Input
from item import Item, ItemContent, ItemDescription, ItemTitle
from native_select import NativeSelect, NativeSelectOption
from select import (
    Select, SelectContent, SelectGroup, SelectItem, SelectLabel, SelectSeparator, SelectTrigger, SelectValue,
)

__js__ = {"lucide-react": ["ChartLineIcon", "ChartBarIcon", "ChartPieIcon"]}


def SelectExample():
    return t"""
        <{ExampleWrapper}>
            <{SelectBasic} />
            <{SelectWithIcons} />
            <{SelectWithGroups} />
            <{SelectLargeList} />
            <{SelectSizes} />
            <{SelectPlan} />
            <{SelectWithButton} />
            <{SelectItemAligned} />
            <{SelectWithField} />
            <{SelectInvalid} />
            <{SelectInline} />
            <{SelectDisabled} />
            <{SelectInDialog} />
        </{ExampleWrapper}>
    """


def SelectBasic():
    return t"""
        <{Example} title="Basic">
            <{Select}>
                <{SelectTrigger}>
                    <{SelectValue} placeholder="Select a fruit" />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        <{SelectItem} value="apple">Apple</{SelectItem}>
                        <{SelectItem} value="banana">Banana</{SelectItem}>
                        <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                        <{SelectItem} value="grapes" disabled>Grapes</{SelectItem}>
                        <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectWithIcons():
    return t"""
        <{Example} title="With Icons">
            <div class="flex flex-col gap-4">
                <{Select}>
                    <{SelectTrigger} size="sm">
                        <{SelectValue} placeholder={t'''
                            <{ChartLineIcon} />
                            Chart Type
                        '''} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="line">
                                <{ChartLineIcon} />
                                Line
                            </{SelectItem}>
                            <{SelectItem} value="bar">
                                <{ChartBarIcon} />
                                Bar
                            </{SelectItem}>
                            <{SelectItem} value="pie">
                                <{ChartPieIcon} />
                                Pie
                            </{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Select}>
                    <{SelectTrigger} size="default">
                        <{SelectValue} placeholder={t'''
                            <{ChartLineIcon} />
                            Chart Type
                        '''} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="line">
                                <{ChartLineIcon} />
                                Line
                            </{SelectItem}>
                            <{SelectItem} value="bar">
                                <{ChartBarIcon} />
                                Bar
                            </{SelectItem}>
                            <{SelectItem} value="pie">
                                <{ChartPieIcon} />
                                Pie
                            </{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
            </div>
        </{Example}>
    """


def SelectWithGroups():
    return t"""
        <{Example} title="With Groups & Labels">
            <{Select}>
                <{SelectTrigger}>
                    <{SelectValue} placeholder="Select a fruit" />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        <{SelectLabel}>Fruits</{SelectLabel}>
                        <{SelectItem} value="apple">Apple</{SelectItem}>
                        <{SelectItem} value="banana">Banana</{SelectItem}>
                        <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                    </{SelectGroup}>
                    <{SelectSeparator} />
                    <{SelectGroup}>
                        <{SelectLabel}>Vegetables</{SelectLabel}>
                        <{SelectItem} value="carrot">Carrot</{SelectItem}>
                        <{SelectItem} value="broccoli">Broccoli</{SelectItem}>
                        <{SelectItem} value="spinach">Spinach</{SelectItem}>
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectLargeList():
    return t"""
        <{Example} title="Large List">
            <{Select}>
                <{SelectTrigger}>
                    <{SelectValue} placeholder="Select an item" />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'<{SelectItem} key={i} value={f"item-{i}"}>Item {i}</{SelectItem}>' for i in range(100)]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-4">
                <{Select}>
                    <{SelectTrigger} size="sm">
                        <{SelectValue} placeholder="Small size" />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="apple">Apple</{SelectItem}>
                            <{SelectItem} value="banana">Banana</{SelectItem}>
                            <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Select}>
                    <{SelectTrigger} size="default">
                        <{SelectValue} placeholder="Default size" />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="apple">Apple</{SelectItem}>
                            <{SelectItem} value="banana">Banana</{SelectItem}>
                            <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
            </div>
        </{Example}>
    """


def SelectWithButton():
    return t"""
        <{Example} title="With Button">
            <div class="flex flex-col gap-4">
                <div class="flex items-center gap-2">
                    <{Select}>
                        <{SelectTrigger} size="sm">
                            <{SelectValue} placeholder="Small" />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                <{SelectItem} value="apple">Apple</{SelectItem}>
                                <{SelectItem} value="banana">Banana</{SelectItem}>
                                <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{Button} variant="outline" size="sm">Submit</{Button}>
                </div>
                <div class="flex items-center gap-2">
                    <{Select}>
                        <{SelectTrigger}>
                            <{SelectValue} placeholder="Default" />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                <{SelectItem} value="apple">Apple</{SelectItem}>
                                <{SelectItem} value="banana">Banana</{SelectItem}>
                                <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{Button} variant="outline">Submit</{Button}>
                </div>
            </div>
        </{Example}>
    """


def SelectItemAligned():
    return t"""
        <{Example} title="Popper">
            <{Select}>
                <{SelectTrigger}>
                    <{SelectValue} placeholder="Select a fruit" />
                </{SelectTrigger}>
                <{SelectContent} position="popper">
                    <{SelectGroup}>
                        <{SelectItem} value="apple">Apple</{SelectItem}>
                        <{SelectItem} value="banana">Banana</{SelectItem}>
                        <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                        <{SelectItem} value="grapes" disabled>Grapes</{SelectItem}>
                        <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectWithField():
    return t"""
        <{Example} title="With Field">
            <{Field}>
                <{FieldLabel} for="select-fruit">Favorite Fruit</{FieldLabel}>
                <{Select}>
                    <{SelectTrigger} id="select-fruit">
                        <{SelectValue} placeholder="Select a fruit" />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="apple">Apple</{SelectItem}>
                            <{SelectItem} value="banana">Banana</{SelectItem}>
                            <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                            <{SelectItem} value="grapes">Grapes</{SelectItem}>
                            <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{FieldDescription}>Choose your favorite fruit from the list.</{FieldDescription}>
            </{Field}>
        </{Example}>
    """


def SelectInvalid():
    return t"""
        <{Example} title="Invalid">
            <div class="flex flex-col gap-4">
                <{Select}>
                    <{SelectTrigger} aria-invalid="true">
                        <{SelectValue} placeholder="Select a fruit" />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="apple">Apple</{SelectItem}>
                            <{SelectItem} value="banana">Banana</{SelectItem}>
                            <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                            <{SelectItem} value="grapes">Grapes</{SelectItem}>
                            <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Field} data-invalid>
                    <{FieldLabel} for="select-fruit-invalid">Favorite Fruit</{FieldLabel}>
                    <{Select}>
                        <{SelectTrigger} id="select-fruit-invalid" aria-invalid>
                            <{SelectValue} placeholder="Select a fruit" />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                <{SelectItem} value="apple">Apple</{SelectItem}>
                                <{SelectItem} value="banana">Banana</{SelectItem}>
                                <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                                <{SelectItem} value="grapes">Grapes</{SelectItem}>
                                <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{FieldError} errors={[{"message": "Please select a valid fruit."}]} />
                </{Field}>
            </div>
        </{Example}>
    """


def SelectInline():
    return t"""
        <{Example} title="Inline with Input & NativeSelect">
            <div class="flex items-center gap-2">
                <{Input} placeholder="Search..." class="flex-1" />
                <{Select}>
                    <{SelectTrigger} class="w-[140px]">
                        <{SelectValue} placeholder="Filter" />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            <{SelectItem} value="all">All</{SelectItem}>
                            <{SelectItem} value="active">Active</{SelectItem}>
                            <{SelectItem} value="inactive">Inactive</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{NativeSelect} class="w-[140px]">
                    <{NativeSelectOption} value="">Sort by</{NativeSelectOption}>
                    <{NativeSelectOption} value="name">Name</{NativeSelectOption}>
                    <{NativeSelectOption} value="date">Date</{NativeSelectOption}>
                    <{NativeSelectOption} value="status">Status</{NativeSelectOption}>
                </{NativeSelect}>
            </div>
        </{Example}>
    """


def SelectDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Select} disabled>
                <{SelectTrigger}>
                    <{SelectValue} placeholder="Disabled" />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        <{SelectItem} value="apple">Apple</{SelectItem}>
                        <{SelectItem} value="banana">Banana</{SelectItem}>
                        <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                        <{SelectItem} value="grapes" disabled>Grapes</{SelectItem}>
                        <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


plans = [
    {"name": "Starter", "description": "Perfect for individuals getting started."},
    {"name": "Professional", "description": "Ideal for growing teams and businesses."},
    {"name": "Enterprise", "description": "Advanced features for large organizations."},
]


def SelectPlan():
    plan, set_plan = use_state(plans[0]["name"])

    selected_plan = next((p for p in plans if p["name"] == plan), None)

    return t"""
        <{Example} title="Subscription Plan">
            <{Select} value={plan} onValueChange={set_plan}>
                <{SelectTrigger} class="h-auto! w-72">
                    <{SelectValue}>{selected_plan and t'<{SelectPlanItem} plan={selected_plan} />'}</{SelectValue}>
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem} key={plan["name"]} value={plan["name"]}>
                                <{SelectPlanItem} plan={plan} />
                            </{SelectItem}>
                        ''' for plan in plans]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectPlanItem(plan=None, **_):
    return t"""
        <{Item} size="xs" class="w-full p-0">
            <{ItemContent} class="gap-0 normal-case">
                <{ItemTitle} class="font-sans">{plan["name"]}</{ItemTitle}>
                <{ItemDescription} class="text-xs font-normal tracking-normal">{plan["description"]}</{ItemDescription}>
            </{ItemContent}>
        </{Item}>
    """


def SelectInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Open Dialog</{Button}>
                </{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Select Example</{DialogTitle}>
                        <{DialogDescription}>Use the select below to choose a fruit.</{DialogDescription}>
                    </{DialogHeader}>
                    <{Select}>
                        <{SelectTrigger}>
                            <{SelectValue} placeholder="Select a fruit" />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                <{SelectItem} value="apple">Apple</{SelectItem}>
                                <{SelectItem} value="banana">Banana</{SelectItem}>
                                <{SelectItem} value="blueberry">Blueberry</{SelectItem}>
                                <{SelectItem} value="grapes">Grapes</{SelectItem}>
                                <{SelectItem} value="pineapple">Pineapple</{SelectItem}>
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
