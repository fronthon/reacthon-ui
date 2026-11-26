from utils import cn

__js__ = {
    "react-aria-components": [
        "DisclosurePanel as AccordionContentPrimitive",
        "Heading as AccordionHeaderPrimitive",
        "Disclosure as AccordionItemPrimitive",
        "DisclosureGroup as AccordionPrimitive",
        "Button as AccordionTriggerPrimitive",
    ],
    "lucide-react": ["ChevronDownIcon", "ChevronUpIcon"],
}


def Accordion(className=None, **props):
    return t'<{AccordionPrimitive} data-slot="accordion" class={cn("flex w-full flex-col", className)} ...{props} />'


def AccordionItem(className=None, **props):
    return t"""
        <{AccordionItemPrimitive}
            data-slot="accordion-item"
            class={cn("not-last:border-b", className)}
            ...{props}
        />
    """


def AccordionTrigger(className=None, children=None, **props):
    return t"""
        <{AccordionHeaderPrimitive} class="flex">
            <{AccordionTriggerPrimitive}
                slot="trigger"
                data-slot="accordion-trigger"
                class={cn("group/accordion-trigger relative flex flex-1 items-start justify-between rounded-lg border border-transparent py-2.5 text-left text-sm font-medium transition-all outline-none hover:underline focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 focus-visible:after:border-ring disabled:pointer-events-none disabled:opacity-50 **:data-[slot=accordion-trigger-icon]:ml-auto **:data-[slot=accordion-trigger-icon]:size-4 **:data-[slot=accordion-trigger-icon]:text-muted-foreground", className)}
                ...{props}
            >
                {children}
                <{ChevronDownIcon}
                    data-slot="accordion-trigger-icon"
                    class="pointer-events-none shrink-0 group-aria-expanded/accordion-trigger:hidden"
                />
                <{ChevronUpIcon}
                    data-slot="accordion-trigger-icon"
                    class="pointer-events-none hidden shrink-0 group-aria-expanded/accordion-trigger:inline"
                />
            </{AccordionTriggerPrimitive}>
        </{AccordionHeaderPrimitive}>
    """


def AccordionContent(className=None, children=None, **props):
    return t"""
        <{AccordionContentPrimitive}
            data-slot="accordion-content"
            class="h-(--disclosure-panel-height) overflow-clip text-sm transition-[height] data-open:animate-accordion-down data-closed:animate-accordion-up"
            ...{props}
        >
            <div class={cn("pt-0 pb-2.5 [&_a]:underline [&_a]:underline-offset-3 [&_a]:hover:text-foreground [&_p:not(:last-child)]:mb-4", className)}>
                {children}
            </div>
        </{AccordionContentPrimitive}>
    """
