from utils import cn, cva
from separator import Separator

__js__ = {"radix-ui": ["Slot"]}

button_group_variants = cva(
    "group/button-group flex w-fit items-stretch *:focus-visible:relative *:focus-visible:z-10 has-[>[data-slot=button-group]]:gap-2 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1",
    {
        "orientation": {
            "horizontal": "[&>*:not(:first-child)]:rounded-l-none [&>*:not(:first-child)]:border-l-0 [&>*:not(:last-child)]:rounded-r-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-r-md!",
            "vertical": "flex-col [&>*:not(:first-child)]:rounded-t-none [&>*:not(:first-child)]:border-t-0 [&>*:not(:last-child)]:rounded-b-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-b-md!",
        },
    },
    {"orientation": "horizontal"},
)


def ButtonGroup(className=None, orientation=None, **props):
    return t"""
        <div
            role="group"
            data-slot="button-group"
            data-orientation={orientation}
            class={cn(button_group_variants(orientation=orientation), className)}
            ...{props}
        />
    """


def ButtonGroupText(className=None, asChild=False, **props):
    Comp = Slot.Root if asChild else "div"

    return t"""
        <{Comp}
            class={cn("flex items-center gap-2 rounded-md border bg-muted px-2.5 text-sm font-medium shadow-xs [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        />
    """


def ButtonGroupSeparator(className=None, orientation="vertical", **props):
    return t"""
        <{Separator}
            data-slot="button-group-separator"
            orientation={orientation}
            class={cn("relative self-stretch bg-input data-horizontal:mx-px data-horizontal:w-auto data-vertical:my-px data-vertical:h-auto", className)}
            ...{props}
        />
    """
