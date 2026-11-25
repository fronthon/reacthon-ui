from utils import cn

__js__ = {"radix-ui": ["HoverCard as HoverCardPrimitive"]}


def HoverCard(**props):
    return t'<{HoverCardPrimitive.Root} data-slot="hover-card" ...{props} />'


def HoverCardTrigger(**props):
    return t'<{HoverCardPrimitive.Trigger} data-slot="hover-card-trigger" ...{props} />'


def HoverCardContent(className=None, align="center", sideOffset=4, **props):
    return t"""
        <{HoverCardPrimitive.Portal} data-slot="hover-card-portal">
            <{HoverCardPrimitive.Content}
                data-slot="hover-card-content"
                align={align}
                sideOffset={sideOffset}
                class={cn("z-50 w-64 origin-(--radix-hover-card-content-transform-origin) rounded-lg bg-popover p-2.5 text-sm text-popover-foreground shadow-md ring-1 ring-foreground/10 outline-hidden duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                ...{props}
            />
        </{HoverCardPrimitive.Portal}>
    """
