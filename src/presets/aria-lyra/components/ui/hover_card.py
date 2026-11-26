from utils import cn

__js__ = {"react-aria-components": ["Popover as PopoverPrimitive", "PreviewTrigger as PreviewTriggerPrimitive"]}


def HoverCardTrigger(children=None, **props):
    return t"""
        <{PreviewTriggerPrimitive}
            data-slot="hover-card-trigger"
            ...{props}
        >
            {children}
        </{PreviewTriggerPrimitive}>
    """


def HoverCard(className=None, placement="bottom", offset=4, crossOffset=0, **props):
    return t"""
        <{PopoverPrimitive}
            data-slot="hover-card-content"
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            class={cn("z-50 w-64 origin-(--trigger-anchor-point) rounded-none bg-popover p-2.5 text-xs/relaxed text-popover-foreground shadow-md ring-1 ring-foreground/10 outline-hidden duration-100 data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2", className)}
            ...{props}
        />
    """
