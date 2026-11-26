from javascript import NULL
from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from field import Field, FieldDescription, FieldError, FieldLabel
from input import Input
from item import Item, ItemContent, ItemDescription, ItemTitle
from native_select import NativeSelect, NativeSelectOption
from select import (
    Select,
    SelectContent,
    SelectEmpty,
    SelectGroup,
    SelectInput,
    SelectItem,
    SelectLabel,
    SelectList,
    SelectPopover,
    SelectSeparator,
    SelectTrigger,
    SelectValue,
)

__js__ = {
    "react-aria-components": ["Autocomplete", "useFilter"],
    "lucide-react": ["ChartLineIcon", "ChartBarIcon", "ChartPieIcon"],
}


def SelectExample():
    return t"""
        <{ExampleWrapper}>
            <{SelectBasic} />
            <{SelectAutocomplete} />
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Basic">
            <{Select} aria-label="Fruits" placeholder="Select a fruit">
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                id={item["value"]}
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    return t"""
        <{Example} title="Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap justify-center gap-2">
                {[t'''
                    <{Select} key={placement} aria-label="Fruits" placeholder="Select">
                        <{SelectTrigger} class="w-28 capitalize">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent} placement={placement}>
                            <{SelectGroup}>
                                {[t"""
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                """ for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                ''' for placement in ["start", "left", "top", "bottom", "right", "end"]]}
            </div>
        </{Example}>
    """


def SelectWithIcons():
    items = [
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

    def callback(props):
        is_placeholder, default_children = props.get("isPlaceholder"), props.get("defaultChildren")

        return t"""
            <{ChartLineIcon} />
            Chart Type
        """ if is_placeholder else default_children

    def callback_2(props):
        is_placeholder, default_children = props.get("isPlaceholder"), props.get("defaultChildren")

        return t"""
            <{ChartLineIcon} />
            Chart Type
        """ if is_placeholder else default_children

    return t"""
        <{Example} title="With Icons">
            <div class="flex flex-col gap-4">
                <{Select} aria-label="Chart Type">
                    <{SelectTrigger} size="sm">
                        <{SelectValue}>{callback}</{SelectValue}>
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Select} aria-label="Chart Type">
                    <{SelectTrigger} size="default">
                        <{SelectValue}>{callback_2}</{SelectValue}>
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
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
    return t"""
        <{Example} title="With Groups & Labels">
            <{Select} aria-label="Fruits and Vegetables">
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        <{SelectLabel}>Fruits</{SelectLabel}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                id={item["value"]}
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
                                id={item["value"]}
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
    items = [{"label": f"Item {i}", "value": f"item-{i}"} for i in range(100)]
    return t"""
        <{Example} title="Large List">
            <{Select} aria-label="Items">
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                id={item["value"]}
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-4">
                <{Select} aria-label="Fruits" placeholder="Select a fruit">
                    <{SelectTrigger} size="sm">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Select} aria-label="Fruits">
                    <{SelectTrigger} size="default">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
    ]
    return t"""
        <{Example} title="With Button">
            <div class="flex flex-col gap-4">
                <div class="flex items-center gap-2">
                    <{Select} aria-label="Fruits" placeholder="Select a fruit">
                        <{SelectTrigger} size="sm">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
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
                    <{Select} aria-label="Fruits">
                        <{SelectTrigger}>
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes", "disabled": True},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Item Aligned">
            <{Select} aria-label="Fruits" placeholder="Select a fruit">
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                id={item["value"]}
                                isDisabled={item.get("disabled")}
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
                <{Select} aria-label="Fruits" placeholder="Select a fruit">
                    <{SelectTrigger} id="select-fruit">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Invalid">
            <div class="flex flex-col gap-4">
                <{Select} aria-label="Fruits" placeholder="Select a fruit" isInvalid>
                    <{SelectTrigger}>
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
                                >
                                    {item["label"]}
                                </{SelectItem}>
                            ''' for item in items]}
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Field} data-invalid>
                    <{FieldLabel} for="select-fruit-invalid">Favorite Fruit</{FieldLabel}>
                    <{Select} aria-label="Fruits" isInvalid>
                        <{SelectTrigger} id="select-fruit-invalid">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
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
        {"label": "All", "value": "all"},
        {"label": "Active", "value": "active"},
        {"label": "Inactive", "value": "inactive"},
    ]
    return t"""
        <{Example} title="Inline with Input & NativeSelect">
            <div class="flex items-center gap-2">
                <{Input} placeholder="Search..." class="flex-1" />
                <{Select} aria-label="Filter" placeholder="Filter">
                    <{SelectTrigger} class="w-[140px]">
                        <{SelectValue} />
                    </{SelectTrigger}>
                    <{SelectContent}>
                        <{SelectGroup}>
                            {[t'''
                                <{SelectItem}
                                    key={item["value"]}
                                    id={item["value"]}
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
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes", "disabled": True},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="Disabled">
            <{Select} aria-label="Fruits" placeholder="Select a fruit" isDisabled>
                <{SelectTrigger}>
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem}
                                key={item["value"]}
                                id={item["value"]}
                                isDisabled={item.get("disabled")}
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
            <{Select} aria-label="Subscription Plan" defaultValue={plans[0]["name"]}>
                <{SelectTrigger} class="h-auto! w-72">
                    <{SelectValue} />
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup}>
                        {[t'''
                            <{SelectItem} key={plan["name"]} id={plan["name"]} textValue={plan["name"]}>
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

    def callback(props):
        selected_items = props.get("selectedItems")

        return "Select fruits" if len(selected_items) == 0 else ((selected_items[0]["label"] if selected_items[0] else None) if (selected_items[0]["label"] if selected_items[0] else None) not in (None, NULL) else "") if len(selected_items) == 1 else f"{len(selected_items)} fruits selected"

    return t"""
        <{Example} title="Multiple Selection">
            <{Select} selectionMode="multiple" aria-label="Fruits">
                <{SelectTrigger} class="w-72">
                    <{SelectValue}>{callback}</{SelectValue}>
                </{SelectTrigger}>
                <{SelectContent}>
                    <{SelectGroup} items={items}>
                        {(lambda item: t'<{SelectItem} id={item["value"]}>{item["label"]}</{SelectItem}>')}
                    </{SelectGroup}>
                </{SelectContent}>
            </{Select}>
        </{Example}>
    """


def SelectInDialog():
    items = [
        {"label": "Apple", "value": "apple"},
        {"label": "Banana", "value": "banana"},
        {"label": "Blueberry", "value": "blueberry"},
        {"label": "Grapes", "value": "grapes"},
        {"label": "Pineapple", "value": "pineapple"},
    ]
    return t"""
        <{Example} title="In Dialog">
            <{DialogTrigger}>
                <{Button} variant="outline">Open Dialog</{Button}>
                <{Dialog}>
                    <{DialogHeader}>
                        <{DialogTitle}>Select Example</{DialogTitle}>
                        <{DialogDescription}>Use the select below to choose a fruit.</{DialogDescription}>
                    </{DialogHeader}>
                    <{Select} aria-label="Fruits" placeholder="Select a fruit">
                        <{SelectTrigger}>
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectGroup}>
                                {[t'''
                                    <{SelectItem}
                                        key={item["value"]}
                                        id={item["value"]}
                                    >
                                        {item["label"]}
                                    </{SelectItem}>
                                ''' for item in items]}
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{Dialog}>
            </{DialogTrigger}>
        </{Example}>
    """


countries = [
    {"code": "ar", "value": "argentina", "label": "Argentina", "continent": "South America"},
    {"code": "au", "value": "australia", "label": "Australia", "continent": "Oceania"},
    {"code": "br", "value": "brazil", "label": "Brazil", "continent": "South America"},
    {"code": "ca", "value": "canada", "label": "Canada", "continent": "North America"},
    {"code": "cn", "value": "china", "label": "China", "continent": "Asia"},
    {"code": "co", "value": "colombia", "label": "Colombia", "continent": "South America"},
    {"code": "eg", "value": "egypt", "label": "Egypt", "continent": "Africa"},
    {"code": "fr", "value": "france", "label": "France", "continent": "Europe"},
    {"code": "de", "value": "germany", "label": "Germany", "continent": "Europe"},
    {"code": "it", "value": "italy", "label": "Italy", "continent": "Europe"},
    {"code": "jp", "value": "japan", "label": "Japan", "continent": "Asia"},
    {"code": "ke", "value": "kenya", "label": "Kenya", "continent": "Africa"},
    {"code": "mx", "value": "mexico", "label": "Mexico", "continent": "North America"},
    {"code": "nz", "value": "new-zealand", "label": "New Zealand", "continent": "Oceania"},
    {"code": "ng", "value": "nigeria", "label": "Nigeria", "continent": "Africa"},
    {"code": "za", "value": "south-africa", "label": "South Africa", "continent": "Africa"},
    {"code": "kr", "value": "south-korea", "label": "South Korea", "continent": "Asia"},
    {"code": "gb", "value": "united-kingdom", "label": "United Kingdom", "continent": "Europe"},
    {"code": "us", "value": "united-states", "label": "United States", "continent": "North America"},
]


def SelectAutocomplete():
    contains = useFilter({"sensitivity": "base"}).contains

    return t"""
        <{Example} title="With Autocomplete">
            <{Select} placeholder="Select country">
                <{SelectTrigger} class="w-full max-w-48">
                    <{SelectValue} />
                </{SelectTrigger}>
                <{Autocomplete} filter={contains}>
                    <{SelectPopover}>
                        <{SelectInput} />
                        <{SelectList} renderEmptyState={(lambda: t'<{SelectEmpty}>No items found.</{SelectEmpty}>')}>
                            <{SelectGroup} items={countries}>
                                {(lambda item: t'<{SelectItem} id={item["value"]}>{item["label"]}</{SelectItem}>')}
                            </{SelectGroup}>
                        </{SelectList}>
                    </{SelectPopover}>
                </{Autocomplete}>
            </{Select}>
        </{Example}>
    """
