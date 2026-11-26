from utils import cn

__js__ = {"react-resizable-panels": ["* as ResizablePrimitive"]}


def ResizablePanelGroup(className=None, **props):
    return t"""
        <{ResizablePrimitive.Group}
            data-slot="resizable-panel-group"
            class={cn("flex h-full w-full aria-[orientation=vertical]:flex-col", className)}
            ...{props}
        />
    """


def ResizablePanel(**props):
    return t'<{ResizablePrimitive.Panel} data-slot="resizable-panel" ...{props} />'


def ResizableHandle(withHandle=None, className=None, **props):
    return t"""
        <{ResizablePrimitive.Separator}
            data-slot="resizable-handle"
            class={cn("relative flex w-px items-center justify-center bg-border ring-offset-background after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:ring-1 focus-visible:ring-ring focus-visible:outline-hidden aria-[orientation=horizontal]:h-px aria-[orientation=horizontal]:w-full aria-[orientation=horizontal]:after:left-0 aria-[orientation=horizontal]:after:h-1 aria-[orientation=horizontal]:after:w-full aria-[orientation=horizontal]:after:translate-x-0 aria-[orientation=horizontal]:after:-translate-y-1/2 [&[aria-orientation=horizontal]>div]:rotate-90", className)}
            ...{props}
        >
            {withHandle and t'<div class="z-10 flex h-6 w-1 shrink-0 rounded-lg bg-border" />'}
        </{ResizablePrimitive.Separator}>
    """
