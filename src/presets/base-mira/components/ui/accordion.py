from utils import cn

__js__ = {
    "@base-ui/react/accordion": ["Accordion as AccordionPrimitive"],
    "lucide-react": ["ChevronDownIcon", "ChevronUpIcon"],
}


def Accordion(className=None, **props):
    return t"""
        <{AccordionPrimitive.Root}
            data-slot="accordion"
            class={cn("flex w-full flex-col overflow-hidden rounded-md border", className)}
            ...{props}
        />
    """


def AccordionItem(className=None, **props):
    return t"""
        <{AccordionPrimitive.Item}
            data-slot="accordion-item"
            class={cn("not-last:border-b data-open:bg-muted/50", className)}
            ...{props}
        />
    """


def AccordionTrigger(className=None, children=None, **props):
    return t"""
        <{AccordionPrimitive.Header} class="flex">
            <{AccordionPrimitive.Trigger}
                data-slot="accordion-trigger"
                class={cn("group/accordion-trigger relative flex flex-1 items-start justify-between gap-6 border border-transparent p-2 text-left text-xs/relaxed font-medium transition-all outline-none hover:underline aria-disabled:pointer-events-none aria-disabled:opacity-50 **:data-[slot=accordion-trigger-icon]:ml-auto **:data-[slot=accordion-trigger-icon]:size-4 **:data-[slot=accordion-trigger-icon]:text-muted-foreground", className)}
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
            </{AccordionPrimitive.Trigger}>
        </{AccordionPrimitive.Header}>
    """


def AccordionContent(className=None, children=None, **props):
    return t"""
        <{AccordionPrimitive.Panel}
            data-slot="accordion-content"
            class="overflow-hidden px-2 text-xs/relaxed data-open:animate-accordion-down data-closed:animate-accordion-up"
            ...{props}
        >
            <div class={cn("h-(--accordion-panel-height) pt-0 pb-4 data-ending-style:h-0 data-starting-style:h-0 [&_a]:underline [&_a]:underline-offset-3 [&_a]:hover:text-foreground [&_p:not(:last-child)]:mb-4", className)}>
                {children}
            </div>
        </{AccordionPrimitive.Panel}>
    """
