from utils import cn

__js__ = {"@base-ui/react/popover": ["Popover as PopoverPrimitive"]}


def Popover(**props):
    return t'<{PopoverPrimitive.Root} data-slot="popover" ...{props} />'


def PopoverTrigger(**props):
    return t'<{PopoverPrimitive.Trigger} data-slot="popover-trigger" ...{props} />'


def PopoverContent(className=None, align="center", alignOffset=0, side="bottom", sideOffset=4, **props):
    return t"""
        <{PopoverPrimitive.Portal}>
            <{PopoverPrimitive.Positioner}
                align={align}
                alignOffset={alignOffset}
                side={side}
                sideOffset={sideOffset}
                class="isolate z-50"
            >
                <{PopoverPrimitive.Popup}
                    data-slot="popover-content"
                    class={cn("z-50 flex w-72 origin-(--transform-origin) flex-col gap-4 rounded-md bg-popover p-4 text-sm text-popover-foreground shadow-md ring-1 ring-foreground/10 outline-hidden duration-100 data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                    ...{props}
                />
            </{PopoverPrimitive.Positioner}>
        </{PopoverPrimitive.Portal}>
    """


def PopoverHeader(className=None, **props):
    return t'<div data-slot="popover-header" class={cn("flex flex-col gap-1 text-sm", className)} ...{props} />'


def PopoverTitle(className=None, **props):
    return t'<{PopoverPrimitive.Title} data-slot="popover-title" class={cn("font-medium", className)} ...{props} />'


def PopoverDescription(className=None, **props):
    return t"""
        <{PopoverPrimitive.Description}
            data-slot="popover-description"
            class={cn("text-muted-foreground", className)}
            ...{props}
        />
    """
