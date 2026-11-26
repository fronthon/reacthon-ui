from utils import cn

__js__ = {"react-aria-components": ["LabelContext", "Label as LabelPrimitive"]}


def Label(className=None, htmlFor=None, slot=None, **props):
    label = t"""
        <{LabelPrimitive}
            data-slot="label"
            class={cn("flex items-center gap-2 text-sm leading-none font-medium select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 peer-data-disabled:opacity-50", className)}
            ...{props}
            for={htmlFor}
            slot={slot}
        />
    """

    if htmlFor and slot is None:
        return t"<{LabelContext.Provider} value={None}>{label}</{LabelContext.Provider}>"

    return label
