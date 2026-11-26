__js__ = {
    "react-aria-components": [
        "DisclosurePanel as CollapsibleContentPrimitive",
        "Disclosure as CollapsiblePrimitive",
        "Button as CollapsibleTriggerPrimitive",
    ],
}


def Collapsible(**props):
    return t'<{CollapsiblePrimitive} data-slot="collapsible" ...{props} />'


def CollapsibleTrigger(**props):
    return t'<{CollapsibleTriggerPrimitive} slot="trigger" data-slot="collapsible-trigger" ...{props} />'


def CollapsibleContent(**props):
    return t'<{CollapsibleContentPrimitive} data-slot="collapsible-content" ...{props} />'
