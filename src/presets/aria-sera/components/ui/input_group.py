from utils import closest, cn, cva
from button import Button
from input import Input
from textarea import Textarea

__js__ = {"react-aria-components": ["Group"]}


def InputGroup(className=None, **props):
    return t"""
        <{Group}
            data-slot="input-group"
            class={cn("group/input-group relative flex h-10 w-full min-w-0 items-center rounded-none border border-transparent border-b-input bg-transparent transition-[color,border-color] outline-none in-data-[slot=combobox-content]:focus-within:border-inherit in-data-[slot=combobox-content]:focus-within:ring-0 has-data-[align=block-end]:rounded-none has-data-[align=block-start]:rounded-none has-[[data-slot=input-group-control]:focus-visible]:border-b-ring has-[[data-slot][aria-invalid=true]]:border-b-destructive has-[textarea]:rounded-none has-[>[data-align=block-end]]:h-auto has-[>[data-align=block-end]]:flex-col has-[>[data-align=block-start]]:h-auto has-[>[data-align=block-start]]:flex-col has-[>textarea]:h-auto dark:has-[[data-slot][aria-invalid=true]]:border-b-destructive/50 has-[>[data-align=block-end]]:[&>input]:pt-3 has-[>[data-align=block-start]]:[&>input]:pb-3", className)}
            ...{props}
        />
    """


input_group_addon_variants = cva(
    "flex h-auto cursor-text items-center justify-center gap-2 py-2 text-sm font-medium text-muted-foreground select-none group-data-[disabled=true]/input-group:opacity-50 **:data-[slot=kbd]:rounded-none **:data-[slot=kbd]:bg-muted-foreground/10 **:data-[slot=kbd]:px-1.5 [&>svg:not([class*='size-'])]:size-3.5",
    {
        "align": {
            "inline-start": "order-first",
            "inline-end": "order-last",
            "block-start": "order-first w-full justify-start pt-3 group-has-[>input]/input-group:pt-3.5 [.border-b]:pb-3.5",
            "block-end": "order-last w-full justify-start pb-3 group-has-[>input]/input-group:pb-3.5 [.border-t]:pt-3.5",
        },
    },
    {"align": "inline-start"},
)


def InputGroupAddon(className=None, align="inline-start", **props):
    def on_click(e):
        if closest(e.target, "button"):
            return
        if e.currentTarget.parentElement and e.currentTarget.parentElement.querySelector("input"):
            e.currentTarget.parentElement.querySelector("input").focus()

    return t"""
        <div
            role="group"
            data-slot="input-group-addon"
            data-align={align}
            class={cn(input_group_addon_variants(align=align), className)}
            onClick={on_click}
            ...{props}
        />
    """


input_group_button_variants = cva(
    "flex items-center gap-2 rounded-none text-sm shadow-none",
    {
        "size": {
            "xs": "h-6 gap-1 rounded-none px-1.5 text-xs [&>svg:not([class*='size-'])]:size-3.5",
            "sm": "",
            "icon-xs": "size-6 p-0 text-xs has-[>svg]:p-0",
            "icon-sm": "size-8 p-0 has-[>svg]:p-0",
        },
    },
    {"size": "xs"},
)


def InputGroupButton(className=None, type="button", variant="ghost", size="xs", **props):
    return t"""
        <{Button}
            type={type}
            data-size={size}
            variant={variant}
            class={cn(input_group_button_variants(size=size), className)}
            ...{props}
        />
    """


def InputGroupText(className=None, **props):
    return t"""
        <span
            class={cn("flex items-center gap-2 text-sm text-muted-foreground [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-3.5", className)}
            ...{props}
        />
    """


def InputGroupInput(className=None, **props):
    return t"""
        <{Input}
            data-slot="input-group-control"
            class={cn("flex-1 border-0 bg-transparent ring-0 group-has-[>[data-align=inline-end]]/input-group:pr-2 group-has-[>[data-align=inline-start]]/input-group:pl-2 focus-visible:ring-0 aria-invalid:ring-0 dark:bg-transparent", className)}
            ...{props}
        />
    """


def InputGroupTextarea(className=None, **props):
    return t"""
        <{Textarea}
            data-slot="input-group-control"
            class={cn("flex-1 resize-none border-0 bg-transparent py-2.5 ring-0 focus-visible:ring-0 aria-invalid:ring-0 dark:bg-transparent", className)}
            ...{props}
        />
    """
