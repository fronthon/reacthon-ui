from utils import cn

__js__ = {
    "react-aria-components": [
        "Focusable",
        "OverlayArrow",
        "Tooltip as TooltipPrimitive",
        "TooltipTrigger as TooltipTriggerPrimitive",
    ],
    "react": ["Children"],
}


def TooltipTrigger(delay=0, children=None, **props):
    trigger, tooltip = Children.toArray(children)

    return t"""
        <{TooltipTriggerPrimitive} data-slot="tooltip-trigger" delay={delay} ...{props}>
            <{Focusable}>{trigger}</{Focusable}>
            {tooltip}
        </{TooltipTriggerPrimitive}>
    """


def Tooltip(className=None, placement="top", offset=4, crossOffset=0, children=None, **props):
    def style(props_2):
        placement, default_style = props_2.get("placement"), props_2.get("defaultStyle")

        return {
            **default_style,
            "rotate": "0deg",
            "translate": "0 0",
            "transform": "translate(-50%, calc(50% + 2px)) rotate(45deg)" if placement == "bottom" else "translate(-50%, calc(-50% - 2px)) rotate(45deg)" if placement == "top" else "translate(calc(-50% - 2px), -50%) rotate(45deg)" if placement == "left" else "translate(calc(50% + 2px), -50%) rotate(45deg)",
        }

    return t"""
        <{TooltipPrimitive}
            data-slot="tooltip-content"
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            class={cn("z-50 inline-flex w-fit max-w-xs origin-(--trigger-anchor-point) items-center gap-1.5 rounded-xl bg-foreground px-3 py-1.5 text-xs text-background has-data-[slot=kbd]:pr-1.5 data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2 **:data-[slot=kbd]:relative **:data-[slot=kbd]:isolate **:data-[slot=kbd]:z-50 **:data-[slot=kbd]:rounded-lg", className)}
            ...{props}
        >
            {children}
            <{OverlayArrow}
                class="z-50 size-2.5 translate-y-[calc(-50%-2px)] rotate-45 rounded-[2px] bg-foreground fill-foreground data-[side=left]:translate-x-[-1.5px] data-[side=right]:translate-x-[1.5px]"
                style={style}
            />
        </{TooltipPrimitive}>
    """
