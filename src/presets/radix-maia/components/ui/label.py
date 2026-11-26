from utils import cn

__js__ = {"radix-ui": ["Label as LabelPrimitive"]}


def Label(className=None, **props):
    return t"""
        <{LabelPrimitive.Root}
            data-slot="label"
            class={cn("flex items-center gap-2 text-sm leading-none font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50", className)}
            ...{props}
        />
    """
