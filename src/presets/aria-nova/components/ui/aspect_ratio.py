from utils import cn


def AspectRatio(ratio=None, className=None, **props):
    return t"""
        <div
            data-slot="aspect-ratio"
            style={ {
                "--ratio": ratio,
            } }
            class={cn("relative aspect-(--ratio)", className)}
            ...{props}
        />
    """
