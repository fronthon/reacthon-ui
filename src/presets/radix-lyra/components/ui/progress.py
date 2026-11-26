from utils import cn

__js__ = {"radix-ui": ["Progress as ProgressPrimitive"]}


def Progress(className=None, value=None, **props):
    return t"""
        <{ProgressPrimitive.Root}
            data-slot="progress"
            class={cn("relative flex h-1 w-full items-center overflow-x-hidden rounded-none bg-muted", className)}
            ...{props}
        >
            <{ProgressPrimitive.Indicator}
                data-slot="progress-indicator"
                class="size-full flex-1 bg-primary transition-all"
                style={ {
                    "transform": f"translateX(-{100 - (value or 0)}%)",
                } }
            />
        </{ProgressPrimitive.Root}>
    """
