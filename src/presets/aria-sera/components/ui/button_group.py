from utils import cn, cva
from separator import Separator

button_group_variants = cva(
    "flex w-fit items-stretch *:focus-visible:relative *:focus-visible:z-10 has-[>[data-slot=button-group]]:gap-2 *:data-[slot=input]:px-4 has-[>[data-variant=outline]]:*:data-[slot=input-group]:border-border has-[>[data-variant=outline]]:*:data-[slot=input-group]:px-2.5 has-[>[data-variant=outline]]:*:data-[slot=select-trigger]:border-border has-[>[data-variant=outline]]:*:[[role=combobox]]:px-2.5 has-[>[data-variant=outline]]:[&>[data-slot=input-group]:has(:focus-visible)]:border-ring has-[>[data-variant=outline]]:[&>[data-slot=select-trigger]:focus-visible]:border-ring has-[select[aria-hidden=true]:last-child]:[&>[data-slot=select-trigger]:last-of-type]:rounded-none [&>[data-slot=select-trigger]:not([class*='w-'])]:w-fit [&>input]:flex-1 has-[>[data-variant=outline]]:[&>input]:border-border has-[>[data-variant=outline]]:[&>input:focus-visible]:border-ring",
    {
        "orientation": {
            "horizontal": "**:data-slot:rounded-r-none [&_[data-slot]~[data-slot]]:rounded-l-none [&_[data-slot]~[data-slot]]:border-l-0 [&>[data-slot]:not(:has(~[data-slot]))]:rounded-none!",
            "vertical": "flex-col **:data-slot:rounded-b-none [&_[data-slot]~[data-slot]]:rounded-t-none [&_[data-slot]~[data-slot]]:border-t-0 [&>[data-slot]:not(:has(~[data-slot]))]:rounded-none!",
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
    if render:
        render_props = {
            "data-slot": "button-group-text",
            "className": cn(
                "flex items-center gap-2 border border-transparent border-b-input bg-transparent px-2.5 text-xs font-semibold uppercase group-has-[>[data-variant=outline]]/button-group:border-border [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-3.5",
                className,
            ),
            **props,
        }

        return render(render_props)

    return t"""
        <div
            data-slot="button-group-text"
            class={cn("flex items-center gap-2 border border-transparent border-b-input bg-transparent px-2.5 text-xs font-semibold uppercase group-has-[>[data-variant=outline]]/button-group:border-border [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-3.5", className)}
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
