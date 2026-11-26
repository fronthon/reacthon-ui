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
            <{ToggleGroup} multiple spacing={1}>
                <{ToggleGroupItem} value="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupOutline():
    return t"""
        <{Example} title="Outline">
            <{ToggleGroup} variant="outline" defaultValue={["all"]}>
                <{ToggleGroupItem} value="all" aria-label="Toggle all">All</{ToggleGroupItem}>
                <{ToggleGroupItem} value="missed" aria-label="Toggle missed">Missed</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupOutlineWithIcons():
    return t"""
        <{Example} title="Outline With Icons">
            <{ToggleGroup} variant="outline" multiple size="sm">
                <{ToggleGroupItem} value="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-4">
                <{ToggleGroup} size="sm" defaultValue={["top"]} variant="outline">
                    <{ToggleGroupItem} value="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
                </{ToggleGroup}>
                <{ToggleGroup} defaultValue={["top"]} variant="outline">
                    <{ToggleGroupItem} value="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
                </{ToggleGroup}>
            </div>
        </{Example}>
    """


def ToggleGroupSpacing():
    return t"""
        <{Example} title="With Spacing">
            <{ToggleGroup} size="sm" defaultValue={["top"]} spacing={2}>
                <{ToggleGroupItem} value="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                <{ToggleGroupItem} value="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                <{ToggleGroupItem} value="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                <{ToggleGroupItem} value="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{ToggleGroup} multiple variant="outline" spacing={2} size="sm">
                <{ToggleGroupItem}
                    value="star"
                    aria-label="Toggle star"
                    class="aria-pressed:bg-transparent aria-pressed:*:[svg]:fill-foreground aria-pressed:*:[svg]:stroke-foreground"
                >
                    <{StarIcon} />
                    Star
                </{ToggleGroupItem}>
                <{ToggleGroupItem}
                    value="heart"
                    aria-label="Toggle heart"
                    class="aria-pressed:bg-transparent aria-pressed:*:[svg]:fill-foreground aria-pressed:*:[svg]:stroke-foreground"
                >
                    <{HeartIcon} />
                    Heart
                </{ToggleGroupItem}>
                <{ToggleGroupItem}
                    value="bookmark"
                    aria-label="Toggle bookmark"
                    class="aria-pressed:bg-transparent aria-pressed:*:[svg]:fill-foreground aria-pressed:*:[svg]:stroke-foreground"
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
            <{ToggleGroup} defaultValue={["all"]} variant="outline" size="sm">
                <{ToggleGroupItem} value="all" aria-label="All">All</{ToggleGroupItem}>
                <{ToggleGroupItem} value="active" aria-label="Active">Active</{ToggleGroupItem}>
                <{ToggleGroupItem} value="completed" aria-label="Completed">Completed</{ToggleGroupItem}>
                <{ToggleGroupItem} value="archived" aria-label="Archived">Archived</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupDateRange():
    return t"""
        <{Example} title="Date Range">
            <{ToggleGroup} defaultValue={["today"]} variant="outline" size="sm" spacing={2}>
                <{ToggleGroupItem} value="today" aria-label="Today">Today</{ToggleGroupItem}>
                <{ToggleGroupItem} value="week" aria-label="This Week">This Week</{ToggleGroupItem}>
                <{ToggleGroupItem} value="month" aria-label="This Month">This Month</{ToggleGroupItem}>
                <{ToggleGroupItem} value="year" aria-label="This Year">This Year</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupSort():
    return t"""
        <{Example} title="Sort">
            <{ToggleGroup} defaultValue={["newest"]} variant="outline" size="sm">
                <{ToggleGroupItem} value="newest" aria-label="Newest">
                    <{ArrowDownIcon} />
                    Newest
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="oldest" aria-label="Oldest">
                    <{ArrowUpIcon} />
                    Oldest
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="popular" aria-label="Popular">
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
                <{Select} items={items} defaultValue={items[0]}>
                    <{SelectTrigger} class="w-32">
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
                <{ToggleGroup} defaultValue={["grid"]} variant="outline">
                    <{ToggleGroupItem} value="grid" aria-label="Grid view">Grid</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="list" aria-label="List view">List</{ToggleGroupItem}>
                </{ToggleGroup}>
            </div>
        </{Example}>
    """


def ToggleGroupVertical():
    return t"""
        <{Example} title="Vertical">
            <{ToggleGroup} multiple orientation="vertical" spacing={1}>
                <{ToggleGroupItem} value="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupVerticalOutline():
    return t"""
        <{Example} title="Vertical Outline">
            <{ToggleGroup} variant="outline" defaultValue={["all"]} orientation="vertical" size="sm">
                <{ToggleGroupItem} value="all" aria-label="Toggle all">All</{ToggleGroupItem}>
                <{ToggleGroupItem} value="active" aria-label="Toggle active">Active</{ToggleGroupItem}>
                <{ToggleGroupItem} value="completed" aria-label="Toggle completed">Completed</{ToggleGroupItem}>
                <{ToggleGroupItem} value="archived" aria-label="Toggle archived">Archived</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupVerticalOutlineWithIcons():
    return t"""
        <{Example} title="Vertical Outline With Icons">
            <{ToggleGroup} variant="outline" multiple orientation="vertical" size="sm">
                <{ToggleGroupItem} value="bold" aria-label="Toggle bold">
                    <{BoldIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="italic" aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{ToggleGroupItem}>
                <{ToggleGroupItem} value="underline" aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """


def ToggleGroupFontWeightSelector():
    font_weight, set_font_weight = use_state("normal")
    return t"""
        <{Example} title="Font Weight Selector">
            <{Field}>
                <{FieldLabel}>Font Weight</{FieldLabel}>
                <{ToggleGroup}
                    value={[font_weight]}
                    onValueChange={(lambda value: set_font_weight(value[0]))}
                    variant="outline"
                    spacing={2}
                    size="lg"
                >
                    <{ToggleGroupItem}
                        value="light"
                        aria-label="Light"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-light">Aa</span>
                        <span class="text-xs text-muted-foreground">Light</span>
                    </{ToggleGroupItem}>
                    <{ToggleGroupItem}
                        value="normal"
                        aria-label="Normal"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-normal">Aa</span>
                        <span class="text-xs text-muted-foreground">Normal</span>
                    </{ToggleGroupItem}>
                    <{ToggleGroupItem}
                        value="medium"
                        aria-label="Medium"
                        class="flex size-16 flex-col items-center justify-center rounded-xl"
                    >
                        <span class="text-2xl leading-none font-medium">Aa</span>
                        <span class="text-xs text-muted-foreground">Medium</span>
                    </{ToggleGroupItem}>
                    <{ToggleGroupItem}
                        value="bold"
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
            <{ToggleGroup} size="sm" defaultValue={["top"]} orientation="vertical" spacing={1}>
                <{ToggleGroupItem} value="top" aria-label="Toggle top">Top</{ToggleGroupItem}>
                <{ToggleGroupItem} value="bottom" aria-label="Toggle bottom">Bottom</{ToggleGroupItem}>
                <{ToggleGroupItem} value="left" aria-label="Toggle left">Left</{ToggleGroupItem}>
                <{ToggleGroupItem} value="right" aria-label="Toggle right">Right</{ToggleGroupItem}>
            </{ToggleGroup}>
        </{Example}>
    """
