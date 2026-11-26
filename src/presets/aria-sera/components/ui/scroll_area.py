from utils import cn


def ScrollArea(className=None, children=None, **props):
    # Use native scrollbar-width and scrollbar-color to customize the scrollbar.
    return t"""
        <div
            data-slot="scroll-area"
            class={cn("relative [scrollbar-width:thin] [scrollbar-color:var(--color-border)_transparent] overflow-auto outline-none focus-visible:ring-[3px] focus-visible:ring-ring/50 focus-visible:outline-1", className)}
            ...{props}
        >
            {children}
        </div>
    """
