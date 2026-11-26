from utils import cn

__js__ = {"react-aria-components": ["DialogTrigger", "Heading", "Popover as PopoverPrimitive"]}


def PopoverTrigger(children=None, **props):
    return t'<{DialogTrigger} data-slot="popover-trigger" ...{props}>{children}</{DialogTrigger}>'


def Popover(className=None, placement="bottom", offset=4, crossOffset=0, **props):
    return t"""
        <{PopoverPrimitive}
            data-slot="popover-content"
            placement={placement}
            offset={offset}
            crossOffset={crossOffset}
            class={cn("z-50 flex w-72 origin-(--trigger-anchor-point) flex-col gap-4 rounded-md bg-popover p-4 text-sm text-popover-foreground shadow-md ring-1 ring-foreground/10 outline-hidden duration-100 data-entering:animate-in data-entering:fade-in-0 data-entering:zoom-in-95 data-exiting:animate-out data-exiting:fade-out-0 data-exiting:zoom-out-95 data-[placement=bottom]:slide-in-from-top-2 data-[placement=left]:slide-in-from-right-2 data-[placement=right]:slide-in-from-left-2 data-[placement=top]:slide-in-from-bottom-2", className)}
            ...{props}
        />
    """


def PopoverHeader(className=None, **props):
    return t'<div data-slot="popover-header" class={cn("flex flex-col gap-1 text-sm", className)} ...{props} />'


def PopoverTitle(className=None, **props):
    return t'<{Heading} data-slot="popover-title" class={cn("font-medium", className)} ...{props} />'


def PopoverDescription(className=None, **props):
    return t'<div data-slot="popover-description" class={cn("text-muted-foreground", className)} ...{props} />'
