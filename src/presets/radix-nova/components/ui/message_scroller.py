from javascript import NULL
from utils import cn
from button import Button

__js__ = {
    "@shadcn/react/message-scroller": ["MessageScroller as MessageScrollerPrimitive"],
    "lucide-react": ["ArrowDownIcon"],
}


def MessageScrollerProvider(**props):
    return t"<{MessageScrollerPrimitive.Provider} ...{props} />"


def MessageScroller(className=None, **props):
    return t"""
        <{MessageScrollerPrimitive.Root}
            data-slot="message-scroller"
            class={cn("group/message-scroller relative flex size-full min-h-0 flex-col overflow-hidden", className)}
            ...{props}
        />
    """


def MessageScrollerViewport(className=None, **props):
    return t"""
        <{MessageScrollerPrimitive.Viewport}
            data-slot="message-scroller-viewport"
            class={cn("size-full min-h-0 min-w-0 scroll-fade-b scrollbar-thin scrollbar-gutter-stable overflow-y-auto overscroll-contain contain-content data-autoscrolling:scrollbar-thumb-transparent data-autoscrolling:scrollbar-track-transparent data-pending-scroll:invisible", className)}
            ...{props}
        />
    """


def MessageScrollerContent(className=None, **props):
    return t"""
        <{MessageScrollerPrimitive.Content}
            data-slot="message-scroller-content"
            class={cn("flex h-max min-h-full flex-col gap-6", className)}
            ...{props}
        />
    """


def MessageScrollerItem(className=None, scrollAnchor=False, **props):
    return t"""
        <{MessageScrollerPrimitive.Item}
            data-slot="message-scroller-item"
            scrollAnchor={scrollAnchor}
            class={cn("min-w-0 shrink-0 [contain-intrinsic-size:auto_10rem] [content-visibility:auto]", className)}
            ...{props}
        />
    """


def MessageScrollerButton(direction="end", className=None, children=None, render=None, variant="secondary", size="icon-sm", **props):
    return t"""
        <{MessageScrollerPrimitive.Button}
            data-slot="message-scroller-button"
            data-direction={direction}
            data-variant={variant}
            data-size={size}
            direction={direction}
            class={cn("absolute inset-s-1/2 -translate-x-1/2 border-border bg-background text-foreground transition-[translate,scale,opacity] duration-200 hover:bg-muted hover:text-foreground data-[active=false]:pointer-events-none data-[active=false]:scale-95 data-[active=false]:opacity-0 data-[active=false]:duration-400 data-[active=false]:ease-[cubic-bezier(0.7,0,0.84,0)] data-[active=true]:translate-y-0 data-[active=true]:scale-100 data-[active=true]:opacity-100 data-[active=true]:ease-[cubic-bezier(0.23,1,0.32,1)] data-[direction=end]:bottom-4 data-[direction=end]:data-[active=false]:translate-y-full data-[direction=start]:top-4 data-[direction=start]:data-[active=false]:-translate-y-full rtl:translate-x-1/2 data-[direction=start]:[&_svg]:rotate-180", className)}
            render={render if render not in (None, NULL) else t'<{Button} variant={variant} size={size} />'}
            ...{props}
        >
            {children if children not in (None, NULL) else t'''
                <{ArrowDownIcon} />
                <span class="sr-only">{"Scroll to end" if direction == "end" else "Scroll to start"}</span>
            '''}
        </{MessageScrollerPrimitive.Button}>
    """
