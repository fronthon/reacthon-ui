from utils import cn, cva
from separator import Separator

__js__ = {"@base-ui/react/merge-props": ["mergeProps"], "@base-ui/react/use-render": ["useRender"]}

button_group_variants = cva(
    "flex w-fit items-stretch *:focus-visible:relative *:focus-visible:z-10 has-[>[data-slot=button-group]]:gap-2 has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-md [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1",
    {
        "orientation": {
            "horizontal": "*:data-slot:rounded-r-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-r-md! [&>[data-slot]~[data-slot]]:rounded-l-none [&>[data-slot]~[data-slot]]:border-l-0",
            "vertical": "flex-col *:data-slot:rounded-b-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-b-md! [&>[data-slot]~[data-slot]]:rounded-t-none [&>[data-slot]~[data-slot]]:border-t-0",
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


def ButtonGroupText(className=None, render=None, **props):
    return useRender(
        {
            "defaultTagName": "div",
            "props": mergeProps(
                {
                    "className": cn(
                        "flex items-center gap-2 rounded-md border bg-muted px-2.5 text-xs/relaxed font-medium [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4",
                        className,
                    ),
                },
                props,
            ),
            "render": render,
            "state": {"slot": "button-group-text"},
        },
    )


def ButtonGroupSeparator(className=None, orientation="vertical", **props):
    return t"""
        <{Separator}
            data-slot="button-group-separator"
            orientation={orientation}
            class={cn("relative self-stretch bg-input data-horizontal:mx-px data-horizontal:w-auto data-vertical:my-px data-vertical:h-auto", className)}
            ...{props}
        />
    """
