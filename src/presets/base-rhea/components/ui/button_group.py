from utils import cn, cva
from separator import Separator

__js__ = {"@base-ui/react/merge-props": ["mergeProps"], "@base-ui/react/use-render": ["useRender"]}

button_group_variants = cva(
    "flex w-fit items-stretch *:focus-visible:relative *:focus-visible:z-10 has-[>[data-slot=button-group]]:gap-2 has-[>[data-variant=outline]]:*:data-[slot=input-group]:border-border has-[>[data-variant=outline]]:*:data-[slot=select-trigger]:border-border has-[>[data-variant=outline]]:[&>[data-slot=input-group]:has(:focus-visible)]:border-ring has-[>[data-variant=outline]]:[&>[data-slot=select-trigger]:focus-visible]:border-ring has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-r-2xl [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[>[data-variant=outline]]:[&>input]:border-border has-[>[data-variant=outline]]:[&>input:focus-visible]:border-ring",
    {
        "orientation": {
            "horizontal": "*:data-slot:rounded-r-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-r-2xl! [&>[data-slot]~[data-slot]]:rounded-l-none [&>[data-slot]~[data-slot]]:border-l-0",
            "vertical": "flex-col *:data-slot:rounded-b-none [&>[data-slot]:not(:has(~[data-slot]))]:rounded-b-2xl! [&>[data-slot]~[data-slot]]:rounded-t-none [&>[data-slot]~[data-slot]]:border-t-0",
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
                        "flex items-center gap-2 rounded-2xl border bg-muted px-2.5 text-sm font-medium [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4",
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
