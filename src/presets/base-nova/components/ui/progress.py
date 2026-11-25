from utils import cn

__js__ = {"@base-ui/react/progress": ["Progress as ProgressPrimitive"]}


def Progress(className=None, children=None, value=None, **props):
    return t"""
        <{ProgressPrimitive.Root}
            value={value}
            data-slot="progress"
            class={cn("flex flex-wrap gap-3", className)}
            ...{props}
        >
            {children}
            <{ProgressTrack}>
                <{ProgressIndicator} />
            </{ProgressTrack}>
        </{ProgressPrimitive.Root}>
    """


def ProgressTrack(className=None, **props):
    return t"""
        <{ProgressPrimitive.Track}
            class={cn("relative flex h-1 w-full items-center overflow-x-hidden rounded-full bg-muted", className)}
            data-slot="progress-track"
            ...{props}
        />
    """


def ProgressIndicator(className=None, **props):
    return t"""
        <{ProgressPrimitive.Indicator}
            data-slot="progress-indicator"
            class={cn("h-full bg-primary transition-all", className)}
            ...{props}
        />
    """


def ProgressLabel(className=None, **props):
    return t"""
        <{ProgressPrimitive.Label}
            class={cn("text-sm font-medium", className)}
            data-slot="progress-label"
            ...{props}
        />
    """


def ProgressValue(className=None, **props):
    return t"""
        <{ProgressPrimitive.Value}
            class={cn("ml-auto text-sm text-muted-foreground tabular-nums", className)}
            data-slot="progress-value"
            ...{props}
        />
    """
