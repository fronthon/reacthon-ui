from utils import cn

__js__ = {"lucide-react": ["Loader2Icon"]}


def Spinner(className=None, **props):
    return t"""
        <{Loader2Icon}
            data-slot="spinner"
            role="status"
            aria-label="Loading"
            class={cn("size-4 animate-spin", className)}
            ...{props}
        />
    """
