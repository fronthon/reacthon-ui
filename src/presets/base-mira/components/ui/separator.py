from utils import cn

__js__ = {"@base-ui/react/separator": ["Separator as SeparatorPrimitive"]}


def Separator(className=None, orientation="horizontal", **props):
    return t"""
        <{SeparatorPrimitive}
            data-slot="separator"
            orientation={orientation}
            class={cn("shrink-0 bg-border data-horizontal:h-px data-horizontal:w-full data-vertical:w-px data-vertical:self-stretch", className)}
            ...{props}
        />
    """
