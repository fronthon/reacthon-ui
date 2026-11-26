from utils import cn, cva

__js__ = {
    "react-aria-components": [
        "TabList as TabListPrimitive",
        "TabPanel as TabPanelPrimitive",
        "Tab as TabPrimitive",
        "Tabs as TabsPrimitive",
    ],
}


def Tabs(className=None, **props):
    return t"""
        <{TabsPrimitive}
            data-slot="tabs"
            class={cn("group/tabs flex gap-2 data-horizontal:flex-col", className)}
            ...{props}
        />
    """


tabs_list_variants = cva(
    "group/tabs-list inline-flex w-fit items-center justify-center p-1 text-muted-foreground group-data-horizontal/tabs:h-10 group-data-vertical/tabs:h-fit group-data-vertical/tabs:flex-col",
    {"variant": {"default": "bg-muted", "line": "gap-1 bg-transparent"}},
    {"variant": "default"},
)


def TabsList(className=None, variant="default", **props):
    return t"""
        <{TabListPrimitive}
            data-slot="tabs-list"
            data-variant={variant}
            class={cn(tabs_list_variants(variant=variant), className)}
            ...{props}
        />
    """


def TabsTrigger(className=None, **props):
    return t"""
        <{TabPrimitive}
            data-slot="tabs-trigger"
            class={cn(
                "relative inline-flex h-[calc(100%-1px)] flex-1 cursor-default items-center justify-center gap-2 border border-transparent px-4 py-1.5 text-xs font-semibold tracking-wider whitespace-nowrap text-foreground/60 uppercase transition-all group-data-vertical/tabs:w-full group-data-vertical/tabs:justify-start group-data-vertical/tabs:px-4 group-data-vertical/tabs:py-2 hover:text-foreground focus-visible:border-ring focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1 focus-visible:outline-ring disabled:pointer-events-none disabled:opacity-50 has-data-[icon=inline-end]:pr-2.5 has-data-[icon=inline-start]:pl-2.5 data-[disabled]:pointer-events-none data-[disabled]:opacity-50 dark:text-muted-foreground dark:hover:text-foreground [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-3.5",
                "group-data-[variant=line]/tabs-list:bg-transparent group-data-[variant=line]/tabs-list:data-selected:bg-transparent dark:group-data-[variant=line]/tabs-list:data-selected:border-transparent dark:group-data-[variant=line]/tabs-list:data-selected:bg-transparent",
                "data-selected:bg-background data-selected:text-foreground dark:data-selected:border-input dark:data-selected:bg-input/30 dark:data-selected:text-foreground",
                "after:absolute after:bg-foreground after:opacity-0 after:transition-opacity group-data-horizontal/tabs:after:inset-x-0 group-data-horizontal/tabs:after:bottom-[-5px] group-data-horizontal/tabs:after:h-0.5 group-data-vertical/tabs:after:inset-y-0 group-data-vertical/tabs:after:-right-1 group-data-vertical/tabs:after:w-0.5 group-data-[variant=line]/tabs-list:data-selected:after:opacity-100",
                className,
            )}
            ...{props}
        />
    """


def TabsContent(className=None, **props):
    return t"""
        <{TabPanelPrimitive}
            data-slot="tabs-content"
            class={cn("flex-1 text-sm outline-none", className)}
            ...{props}
        />
    """
