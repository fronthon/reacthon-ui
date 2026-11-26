__js__ = {"@base-ui/react/collapsible": ["Collapsible as CollapsiblePrimitive"]}


def Collapsible(**props):
    return t'<{CollapsiblePrimitive.Root} data-slot="collapsible" ...{props} />'


def CollapsibleTrigger(**props):
    return t'<{CollapsiblePrimitive.Trigger} data-slot="collapsible-trigger" ...{props} />'


def CollapsibleContent(**props):
    return t'<{CollapsiblePrimitive.Panel} data-slot="collapsible-content" ...{props} />'
