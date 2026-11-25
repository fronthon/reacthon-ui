from utils import cn

__js__ = {"radix-ui": ["Separator as SeparatorPrimitive"]}


def Separator(className=None, orientation="horizontal", decorative=True, **props):
    return t"""
        <{SeparatorPrimitive.Root}
            data-slot="separator"
            decorative={decorative}
            orientation={orientation}
            class={cn("shrink-0 bg-border data-horizontal:h-px data-horizontal:w-full data-vertical:w-px data-vertical:self-stretch", className)}
            ...{props}
        />
    """
