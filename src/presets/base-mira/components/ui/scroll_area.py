from utils import cn

__js__ = {"@base-ui/react/scroll-area": ["ScrollArea as ScrollAreaPrimitive"]}


def ScrollArea(className=None, children=None, **props):
    return t"""
        <{ScrollAreaPrimitive.Root} data-slot="scroll-area" class={cn("relative", className)} ...{props}>
            <{ScrollAreaPrimitive.Viewport}
                data-slot="scroll-area-viewport"
                class="size-full rounded-[inherit] transition-[color,box-shadow] outline-none focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1"
            >
                {children}
            </{ScrollAreaPrimitive.Viewport}>
            <{ScrollBar} />
            <{ScrollAreaPrimitive.Corner} />
        </{ScrollAreaPrimitive.Root}>
    """


def ScrollBar(className=None, orientation="vertical", **props):
    return t"""
        <{ScrollAreaPrimitive.Scrollbar}
            data-slot="scroll-area-scrollbar"
            data-orientation={orientation}
            orientation={orientation}
            class={cn("flex touch-none p-px transition-colors select-none data-horizontal:h-2.5 data-horizontal:flex-col data-horizontal:border-t data-horizontal:border-t-transparent data-vertical:h-full data-vertical:w-2.5 data-vertical:border-l data-vertical:border-l-transparent", className)}
            ...{props}
        >
            <{ScrollAreaPrimitive.Thumb} data-slot="scroll-area-thumb" class="relative flex-1 rounded-full bg-border" />
        </{ScrollAreaPrimitive.Scrollbar}>
    """
