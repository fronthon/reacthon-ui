__js__ = {"radix-ui": ["Collapsible as CollapsiblePrimitive"]}


def Collapsible(**props):
    return t'<{CollapsiblePrimitive.Root} data-slot="collapsible" ...{props} />'


def CollapsibleTrigger(**props):
    return t'<{CollapsiblePrimitive.CollapsibleTrigger} data-slot="collapsible-trigger" ...{props} />'


def CollapsibleContent(**props):
    return t'<{CollapsiblePrimitive.CollapsibleContent} data-slot="collapsible-content" ...{props} />'
