from javascript import NULL
from reacthon import use_state
from example import Example, ExampleWrapper
from field import Field, FieldDescription, FieldLabel
from input import Input
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from toggle_group import ToggleGroup, ToggleGroupItem

__js__ = {
    "lucide-react": [
        "BoldIcon",
        "ItalicIcon",
        "UnderlineIcon",
        "StarIcon",
        "HeartIcon",
        "BookmarkIcon",
        "ArrowDownIcon",
        "ArrowUpIcon",
        "TrendingUpIcon",
    ],
}


def ToggleGroupExample():
    return t"""
        <{ExampleWrapper}>
            <{ToggleGroupBasic} />
            <{ToggleGroupOutline} />
            <{ToggleGroupOutlineWithIcons} />
            <{ToggleGroupSizes} />
            <{ToggleGroupSpacing} />
            <{ToggleGroupWithIcons} />
            <{ToggleGroupFilter} />
            <{ToggleGroupDateRange} />
            <{ToggleGroupSort} />
            <{ToggleGroupWithInputAndSelect} />
            <{ToggleGroupVertical} />
            <{ToggleGroupVerticalOutline} />
            <{ToggleGroupVerticalOutlineWithIcons} />
            <{ToggleGroupVerticalWithSpacing} />
            <{ToggleGroupFontWeightSelector} />
        </{ExampleWrapper}>
    """


def ToggleGroupBasic():
    return t"""
        <{Example} title="Basic">
            <{ToggleGroup} selectionMode="multiple" spacing={1}>
                <{ToggleGroupItem} id="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupOutline():
    return t"""
        <{Example} title="Outline">
            <{ToggleGroup} variant="outline" defaultSelectedKeys={["all"]}>
                <{ToggleGroupItem} id="all" aria-label="Toggle all">All</{ToggleGroupItem}>
                <{ToggleGroupItem} id="missed" aria-label="Toggle missed">Missed</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupOutlineWithIcons():
    return t"""
        <{Example} title="Outline With Icons">
            <{ToggleGroup} variant="outline" selectionMode="multiple" size="sm">
                <{ToggleGroupItem} id="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-4">
                <{ToggleGroup} size="sm" defaultSelectedKeys={["top"]} variant="outline">
                    <{ToggleGroupItem} id="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
                </{ToggleGroup}>
                <{ToggleGroup} defaultSelectedKeys={["top"]} variant="outline">
                    <{ToggleGroupItem} id="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
                </{ToggleGroup}>
            </div>
        </{Example}>
    """


def ToggleGroupSpacing():
    return t"""
        <{Example} title="With Spacing">
            <{ToggleGroup} size="sm" defaultSelectedKeys={["top"]} spacing={2}>
                <{ToggleGroupItem} id="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                <{ToggleGroupItem} id="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                <{ToggleGroupItem} id="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                <{ToggleGroupItem} id="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{ToggleGroup} selectionMode="multiple" variant="outline" spacing={2} size="sm">
                <{ToggleGroupItem}
                    id="star"
                    aria-label="Toggle star"
                    class="data-selected:bg-transparent data-selected:*:[svg]:fill-foreground data-selected:*:[svg]:stroke-foreground"
                >
                    <{StarIcon} />
                    Star
                </{ToggleGroupItem}>
                <{ToggleGroupItem}
                    id="heart"
                    aria-label="Toggle heart"
                    class="data-selected:bg-transparent data-selected:*:[svg]:fill-foreground data-selected:*:[svg]:stroke-foreground"
                >
                    <{HeartIcon} />
                    Heart
                </{ToggleGroupItem}>
                <{ToggleGroupItem}
                    id="bookmark"
                    aria-label="Toggle bookmark"
                    class="data-selected:bg-transparent data-selected:*:[svg]:fill-foreground data-selected:*:[svg]:stroke-foreground"
                >
                    <{BookmarkIcon} />
                    Bookmark
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupFilter():
    return t"""
        <{Example} title="Filter">
            <{ToggleGroup} defaultSelectedKeys={["all"]} variant="outline" size="sm">
                <{ToggleGroupItem} id="all" aria-label="All">All</{ToggleGroupItem}>
                <{ToggleGroupItem} id="active" aria-label="Active">Active</{ToggleGroupItem}>
                <{ToggleGroupItem} id="completed" aria-label="Completed">Completed</{ToggleGroupItem}>
                <{ToggleGroupItem} id="archived" aria-label="Archived">Archived</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupDateRange():
    return t"""
        <{Example} title="Date Range">
            <{ToggleGroup} defaultSelectedKeys={["today"]} variant="outline" size="sm" spacing={2}>
                <{ToggleGroupItem} id="today" aria-label="Today">Today</{ToggleGroupItem}>
                <{ToggleGroupItem} id="week" aria-label="This Week">This Week</{ToggleGroupItem}>
                <{ToggleGroupItem} id="month" aria-label="This Month">This Month</{ToggleGroupItem}>
                <{ToggleGroupItem} id="year" aria-label="This Year">This Year</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupSort():
    return t"""
        <{Example} title="Sort">
            <{ToggleGroup} defaultSelectedKeys={["newest"]} variant="outline" size="sm">
                <{ToggleGroupItem} id="newest" aria-label="Newest">
                    <{ArrowDownIcon} />
                    Newest
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="oldest" aria-label="Oldest">
                    <{ArrowUpIcon} />
                    Oldest
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="popular" aria-label="Popular">
                    <{TrendingUpIcon} />
                    Popular
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupWithInputAndSelect():
    items = [
        {"label": "All", "value": "all"},
        {"label": "Active", "value": "active"},
        {"label": "Archived", "value": "archived"},
    ]
    return t"""
        <{Example} title="With Input and Select">
            <div class="flex items-center gap-2">
                <{Input} type="search" placeholder="Search..." class="flex-1" />
                <{Select} defaultValue={items[0]["value"]}>
                    <{SelectTrigger} class="w-32">
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
                <{ToggleGroup} defaultSelectedKeys={["grid"]} variant="outline">
                    <{ToggleGroupItem} id="grid" aria-label="Grid view">Grid</{ToggleGroupItem}>
                    <{ToggleGroupItem} id="list" aria-label="List view">List</{ToggleGroupItem}>
                </{ToggleGroup}>
            </div>
        </{Example}>
    """


def ToggleGroupVertical():
    return t"""
        <{Example} title="Vertical">
            <{ToggleGroup} selectionMode="multiple" orientation="vertical" spacing={1}>
                <{ToggleGroupItem} id="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupVerticalOutline():
    return t"""
        <{Example} title="Vertical Outline">
            <{ToggleGroup} variant="outline" defaultSelectedKeys={["all"]} orientation="vertical" size="sm">
                <{ToggleGroupItem} id="all" aria-label="Toggle all">All</{ToggleGroupItem}>
                <{ToggleGroupItem} id="active" aria-label="Toggle active">Active</{ToggleGroupItem}>
                <{ToggleGroupItem} id="completed" aria-label="Toggle completed">Completed</{ToggleGroupItem}>
                <{ToggleGroupItem} id="archived" aria-label="Toggle archived">Archived</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupVerticalOutlineWithIcons():
    return t"""
        <{Example} title="Vertical Outline With Icons">
            <{ToggleGroup} variant="outline" selectionMode="multiple" orientation="vertical" size="sm">
                <{ToggleGroupItem} id="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} id="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupFontWeightSelector():
    font_weight, set_font_weight = use_state("normal")

    def on_selection_change(value):
        first = list(value)[0]
        set_font_weight(first if first not in (None, NULL) else "normal")

    return t"""
        <{Example} title="Font Weight Selector">
            <{Field}>
                <{FieldLabel}>Font Weight</{FieldLabel}>
                <{ToggleGroup}
                    selectedKeys={[font_weight]}
                    onSelectionChange={on_selection_change}
                    variant="outline"
                    spacing={2}
                    size="lg"
                >
                    <{ToggleGroupItem}
                        id="light"
                        aria-label="Light"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-light">Aa</span>
                        <span class="text-xs text-muted-foreground">Light</span>
                    </{ToggleGroupItem}>
                    <{ToggleGroupItem}
                        id="normal"
                        aria-label="Normal"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-normal">Aa</span>
                        <span class="text-xs text-muted-foreground">Normal</span>
                    </{ToggleGroupItem}>
                    <{ToggleGroupItem}
                        id="medium"
                        aria-label="Medium"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-medium">Aa</span>
                        <span class="text-xs text-muted-foreground">Medium</span>
                    </{ToggleGroupItem}>
                    <{ToggleGroupItem}
                        id="bold"
                        aria-label="Bold"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-bold">Aa</span>
                        <span class="text-xs text-muted-foreground">Bold</span>
                    </{ToggleGroupItem}>
                </{ToggleGroup}>
                <{FieldDescription}>
                    Use{" "}
                    <code class="rounded-md bg-muted px-1 py-0.5 font-mono">font-{font_weight}</code>
                    {" "}
                    to set the font weight.
                </{FieldDescription}>
            </{Field}>
        </{Example}>
    """


def ToggleGroupVerticalWithSpacing():
    return t"""
        <{Example} title="Vertical With Spacing">
            <{ToggleGroup} size="sm" defaultSelectedKeys={["top"]} orientation="vertical" spacing={1}>
                <{ToggleGroupItem} id="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                <{ToggleGroupItem} id="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                <{ToggleGroupItem} id="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                <{ToggleGroupItem} id="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """
