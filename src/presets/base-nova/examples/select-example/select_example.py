from javascript import NULL
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
            <{SelectSides} />
            <{SelectWithIcons} />
            <{SelectWithGroups} />
            <{SelectLargeList} />
            <{SelectMultiple} />
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
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Basic">
            <{Select} items={items}>
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in items]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectSides():
    items = [
        {"label": "Select", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    return t"""
        <{Example} title="Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap justify-center gap-2">
                {[t'''
                    <{Select} key={side} items={items}>
                        <{SelectTrigger} class="w-28 capitalize">
                            <{SelectValue} placeholder={side.replace("-", " ")} />
                        </{SelectTrigger}>
                        <{SelectContent} side={side} alignItemWithTrigger={False}>
                            <{SelectGroup}>
                                {[t"""
                                    <{SelectItem}
                                        key={item["value"]}
                                        value={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                """ for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                ''' for side in ["inline-start", "left", "top", "bottom", "right", "inline-end"]]}
            </div>
        </{Example}>
    """


def SelectWithIcons():
    items = [
        {
            "label": t"""
                <{ChartLineIcon} />
                Chart Type
            """,
            "value": NULL,
        },
        {
            "label": t"""
                <{ChartLineIcon} />
                Line
            """,
            "value": "line",
        },
        {
            "label": t"""
                <{ChartBarIcon} />
                Bar
            """,
            "value": "bar",
        },
        {
            "label": t"""
                <{ChartPieIcon} />
                Pie
            """,
            "value": "pie",
        },
    ]
    return t"""
        <{Example} title="With Icons">
            <div class="flex flex-col gap-4">
                <{Select} items={items}>
                    <{SelectTrigger} size="sm">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Select} items={items}>
                    <{SelectTrigger} size="default">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
            </div>
        </{Example}>
    """


def SelectWithGroups():
    fruits = [
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    vegetables = [
        {"label": "Carrot", "value": "carrot"},
        {"label": "Broccoli", "value": "broccoli"},
        {"label": "Spinach", "value": "spinach"},
    ]
    all_items = [{"label": "Select a fruit", "value": NULL}, *fruits, *vegetables]
    return t"""
        <{Example} title="With Groups & Labels">
            <{Select} items={all_items}>
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        <{SelectLabel}>Fruits</{SelectLabel}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in fruits]}
                    </{SelectGroup}>
                    <{SelectSeparator} />
                    <{SelectGroup}>
                        <{SelectLabel}>Vegetables</{SelectLabel}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in vegetables]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectLargeList():
    items = [
        {"label": "Select an item", "value": NULL},
        *[{"label": f"Item {i}", "value": f"item-{i}"} for i in range(100)],
    ]
    return t"""
        <{Example} title="Large List">
            <{Select} items={items}>
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in items]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectSizes():
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-4">
                <{Select} items={items}>
                    <{SelectTrigger} size="sm">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Select} items={items}>
                    <{SelectTrigger} size="default">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
            </div>
        </{Example}>
    """


def SelectWithButton():
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    return t"""
        <{Example} title="With Button">
            <div class="flex flex-col gap-4">
                <div class="flex items-center gap-2">
                    <{Select} items={items}>
                        <{SelectTrigger} size="sm">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        value={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{Button} variant="outline" size="sm">Submit</{Button}>
                </div>
                <div class="flex items-center gap-2">
                    <{Select} items={items}>
                        <{SelectTrigger}>
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        value={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{Button} variant="outline">Submit</{Button}>
                </div>
            </div>
        </{Example}>
    """


def SelectItemAligned():
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes", "disabled": True},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Item Aligned">
            <{Select} items={items}>
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent} alignItemWithTrigger={True}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                                disabled={item.get("disabled")}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in items]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectWithField():
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="With Field">
            <{Field}>
                <{FieldLabel} for="select-fruit">Favorite Fruit</{FieldLabel}>
                <{Select} items={items}>
                    <{SelectTrigger} id="select-fruit">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{FieldDescription}>Choose your favorite fruit from the list.</{FieldDescription}>
            </{Field}>
        </{Example}>
    """


def SelectInvalid():
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Invalid">
            <div class="flex flex-col gap-4">
                <{Select} items={items}>
                    <{SelectTrigger} aria-invalid="true">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Field} data-invalid>
                    <{FieldLabel} for="select-fruit-invalid">Favorite Fruit</{FieldLabel}>
                    <{Select} items={items}>
                        <{SelectTrigger} id="select-fruit-invalid" aria-invalid>
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        value={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{FieldError} errors={[{"message": "Please select a valid fruit."}]} />
                </{Field}>
            </div>
        </{Example}>
    """


def SelectInline():
    items = [
        {"label": "Filter", "value": NULL},
        {"label": "All", "value": "all"},
        {"label": "Active", "value": "active"},
        {"label": "Inactive", "value": "inactive"},
    ]
    return t"""
        <{Example} title="Inline with Input & NativeSelect">
            <div class="flex items-center gap-2">
                <{Input} placeholder="Search..." class="flex-1" />
                <{Select} items={items}>
                    <{SelectTrigger} class="w-[140px]">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    value={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
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
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes", "disabled": True},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Disabled">
            <{Select} items={items} disabled>
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                                disabled={item.get("disabled")}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in items]}
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
    return t"""
        <{Example} title="Subscription Plan">
            <{Select} defaultValue={plans[0]} itemToStringValue={(lambda plan: plan["name"])}>
                <{SelectTrigger} class="h-auto! w-72">
                    <{SelectValue}>{(lambda value: t'<{SelectPlanItem} plan={value} />')}</{SelectValue}>
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem} key={plan["name"]} value={plan}>
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


def SelectMultiple():
    items = [
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
        {"label": "Strawberry", "value": "strawberry"},
        {"label": "Watermelon", "value": "watermelon"},
    ]

    def callback(value):
        if len(value) == 0:
            return "Select fruits"
        if len(value) == 1:
            return next((item for item in items if item["value"] == value[0]), None)["label"] if next((item for item in items if item["value"] == value[0]), None) else None
        return f"{len(value)} fruits selected"

    return t"""
        <{Example} title="Multiple Selection">
            <{Select} items={items} multiple defaultValue={[]}>
                <{SelectTrigger} class="w-72">
                    <{SelectValue}>{callback}</{SelectValue}>
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                value={item["value"]}
                            >
                                {item["label"]}
                            </{SelectItem}>
                        ''' for item in items]}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectInDialog():
    items = [
        {"label": "Select a fruit", "value": NULL},
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open Dialog</{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Select Example</{DialogTitle}>
                        <{DialogDescription}>Use the select below to choose a fruit.</{DialogDescription}>
                    </{DialogHeader}>
                    <{Select} items={items}>
                        <{SelectTrigger}>
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        value={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
