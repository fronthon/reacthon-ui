from utils import cn

__js__ = {"radix-ui": ["Accordion as AccordionPrimitive"], "lucide-react": ["ChevronDownIcon", "ChevronUpIcon"]}


def Accordion(className=None, **props):
    return t"""
        <{AccordionPrimitive.Root}
            data-slot="accordion"
            class={cn("flex w-full flex-col", className)}
            ...{props}
        />
    """


def AccordionItem(className=None, **props):
    return t"""
        <{AccordionPrimitive.Item}
            data-slot="accordion-item"
            class={cn("not-last:border-b", className)}
            ...{props}
        />
    """


def AccordionTrigger(className=None, children=None, **props):
    return t"""
        <{AccordionPrimitive.Header} class="flex">
            <{AccordionPrimitive.Trigger}
                data-slot="accordion-trigger"
                class={cn("group/accordion-trigger relative flex flex-1 items-start justify-between rounded-none border border-transparent py-2.5 text-left text-xs font-medium transition-all outline-none hover:underline focus-visible:border-ring focus-visible:ring-1 focus-visible:ring-ring/50 focus-visible:after:border-ring disabled:pointer-events-none disabled:opacity-50 **:data-[slot=accordion-trigger-icon]:ml-auto **:data-[slot=accordion-trigger-icon]:size-4 **:data-[slot=accordion-trigger-icon]:text-muted-foreground", className)}
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
        <{AccordionPrimitive.Content}
            data-slot="accordion-content"
            class="overflow-hidden text-xs data-open:animate-accordion-down data-closed:animate-accordion-up"
            ...{props}
        >
            <div class={cn("h-(--radix-accordion-content-height) pt-0 pb-2.5 [&_a]:underline [&_a]:underline-offset-3 [&_a]:hover:text-foreground [&_p:not(:last-child)]:mb-4", className)}>
                {children}
            </div>
        </{AccordionPrimitive.Content}>
    """
