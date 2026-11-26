from utils import cn
from collapsible import Collapsible, CollapsibleContent

__js__ = {"react-aria-components": ["Button as ButtonPrimitive"], "lucide-react": ["ChevronRightIcon"]}


def Trace(className=None, **props):
    return t"""
        <div
            data-slot="trace"
            class={cn("flex w-full min-w-0 flex-col gap-2 *:has-[>[data-slot=trace-line]]:flex *:has-[>[data-slot=trace-line]]:w-fit *:has-[>[data-slot=trace-line]]:max-w-full *:has-[>[data-slot=trace-line]]:min-w-0 *:has-[>[data-slot=trace-line]]:rounded-lg *:has-[>[data-slot=trace-line]]:text-left *:has-[>[data-slot=trace-line]]:outline-none *:has-[>[data-slot=trace-line]]:focus-visible:ring-3 *:has-[>[data-slot=trace-line]]:focus-visible:ring-ring/30", className)}
            ...{props}
        />
    """


def TraceLine(className=None, status=None, **props):
    return t"""
        <span
            data-slot="trace-line"
            data-status={status}
            class={cn("flex w-fit max-w-full min-w-0 items-center gap-2 text-sm text-muted-foreground transition-colors in-[a,button]:cursor-pointer in-[a:hover,button:hover]:text-foreground data-[status=error]:text-destructive data-[status=error]:in-[a:hover,button:hover]:text-destructive data-[status=pending]:opacity-60 data-[status=running]:*:data-[slot=trace-title]:shimmer", className)}
            ...{props}
        />
    """


def TraceIcon(className=None, **props):
    return t"""
        <span
            data-slot="trace-icon"
            aria-hidden="true"
            class={cn("flex size-4 shrink-0 items-center justify-center [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [[data-slot=trace-title]~&]:-ml-1", className)}
            ...{props}
        />
    """


def TraceTitle(className=None, **props):
    return t"""
        <span
            data-slot="trace-title"
            class={cn("min-w-0 truncate motion-reduce:shimmer-none", className)}
            ...{props}
        />
    """


def TraceDescription(className=None, **props):
    return t"""
        <span
            data-slot="trace-description"
            class={cn("shrink-0 text-muted-foreground/70 tabular-nums", className)}
            ...{props}
        />
    """


def TraceCollapsible(className=None, **props):
    return t"""
        <{Collapsible}
            data-slot="trace-collapsible"
            class={cn("flex w-full min-w-0 flex-col", className)}
            ...{props}
        />
    """


def TraceCollapsibleTrigger(className=None, children=None, **props):
    return t"""
        <{ButtonPrimitive}
            slot="trigger"
            ...{props}
            data-slot="trace-collapsible-trigger"
            class={cn("group/trace-collapsible-trigger flex w-fit max-w-full min-w-0 cursor-pointer items-center gap-1 rounded-lg text-left text-muted-foreground transition-colors outline-none hover:text-foreground focus-visible:ring-3 focus-visible:ring-ring/30 has-[[data-status=error]]:text-destructive", className)}
        >
            {children}
            <{TraceIcon} class="transition-transform group-aria-expanded/trace-collapsible-trigger:rotate-90">
                <{ChevronRightIcon} />
            </{TraceIcon}>
        </{ButtonPrimitive}>
    """


def TraceCollapsibleContent(className=None, children=None, **props):
    return t"""
        <{CollapsibleContent}
            data-slot="trace-collapsible-content"
            class="h-(--disclosure-panel-height) min-w-0 overflow-clip transition-[height] duration-200"
            ...{props}
        >
            <div
                data-slot="trace-collapsible-content-inner"
                class={cn("mt-2 mb-1 ml-[calc(--spacing(2)-1px)] min-w-0 border-l pr-1 pl-4 leading-relaxed wrap-break-word text-muted-foreground", className)}
            >
                {children}
            </div>
        </{CollapsibleContent}>
    """
