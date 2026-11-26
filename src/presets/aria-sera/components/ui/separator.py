from utils import cn

__js__ = {"react-aria-components": ["Separator as SeparatorPrimitive"]}


def Separator(className=None, orientation="horizontal", **props):
    return t"""
        <{SeparatorPrimitive}
            data-slot="separator"
            orientation={orientation}
            class={cn("block shrink-0 border-0 bg-border aria-[orientation=horizontal]:h-px aria-[orientation=horizontal]:w-full aria-[orientation=vertical]:w-px aria-[orientation=vertical]:self-stretch [:is(hr)]:h-px [:is(hr)]:w-full", className)}
            ...{props}
        />
    """
