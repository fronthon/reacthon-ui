from utils import cn

__js__ = {"react-aria-components": ["LabelContext", "Label as LabelPrimitive"]}


def Label(className=None, htmlFor=None, slot=None, **props):
    label = t"""
        <{LabelPrimitive}
            data-slot="label"
            class={cn("flex items-center gap-2 text-xs font-semibold tracking-wide uppercase select-none group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 peer-data-[slot=checkbox]:text-sm peer-data-[slot=checkbox]:font-normal peer-data-[slot=checkbox]:tracking-normal peer-data-[slot=checkbox]:normal-case peer-data-[slot=radio-group-item]:text-sm peer-data-[slot=radio-group-item]:font-normal peer-data-[slot=radio-group-item]:tracking-normal peer-data-[slot=radio-group-item]:normal-case peer-data-[slot=switch]:text-sm peer-data-[slot=switch]:font-normal peer-data-[slot=switch]:tracking-normal peer-data-[slot=switch]:normal-case peer-data-disabled:opacity-50", className)}
            ...{props}
            for={htmlFor}
            slot={slot}
        />
    """

    if htmlFor and slot is None:
        return t"<{LabelContext.Provider} value={None}>{label}</{LabelContext.Provider}>"

    return label
