from utils import cn

__js__ = {
    "@base-ui/react/select": ["Select as SelectPrimitive"],
    "lucide-react": ["ChevronDownIcon", "CheckIcon", "ChevronUpIcon"],
}

Select = SelectPrimitive.Root


def SelectGroup(className=None, **props):
    return t'<{SelectPrimitive.Group} data-slot="select-group" class={cn("scroll-my-1 p-1", className)} ...{props} />'


def SelectValue(className=None, **props):
    return t"""
        <{SelectPrimitive.Value}
            data-slot="select-value"
            class={cn("flex flex-1 text-left", className)}
            ...{props}
        />
    """


def SelectTrigger(className=None, size="default", children=None, **props):
    return t"""
        <{SelectPrimitive.Trigger}
            data-slot="select-trigger"
            data-size={size}
            class={cn("flex w-fit items-center justify-between gap-1.5 rounded-md border border-input bg-transparent py-2 pr-2 pl-2.5 text-sm whitespace-nowrap shadow-xs transition-[color,box-shadow] outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 data-placeholder:text-muted-foreground data-[size=default]:h-9 data-[size=sm]:h-8 *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-1.5 dark:bg-input/30 dark:hover:bg-input/50 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{SelectPrimitive.Icon} render={t'<{ChevronDownIcon} class="pointer-events-none size-4 text-muted-foreground" />'} />
        </{SelectPrimitive.Trigger}>
    """


def SelectContent(className=None, children=None, side="bottom", sideOffset=4, align="center", alignOffset=0, alignItemWithTrigger=True, **props):
    return t"""
        <{SelectPrimitive.Portal}>
            <{SelectPrimitive.Positioner}
                side={side}
                sideOffset={sideOffset}
                align={align}
                alignOffset={alignOffset}
                alignItemWithTrigger={alignItemWithTrigger}
                class="isolate z-50"
            >
                <{SelectPrimitive.Popup}
                    data-slot="select-content"
                    data-align-trigger={alignItemWithTrigger}
                    class={cn("relative isolate z-50 max-h-(--available-height) w-(--anchor-width) min-w-36 origin-(--transform-origin) overflow-x-hidden overflow-y-auto rounded-md bg-popover text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[align-trigger=true]:animate-none data-[side=bottom]:slide-in-from-top-2 data-[side=inline-end]:slide-in-from-left-2 data-[side=inline-start]:slide-in-from-right-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95", className)}
                    ...{props}
                >
                    <{SelectScrollUpButton} />
                    <{SelectPrimitive.List}>{children}</{SelectPrimitive.List}>
                    <{SelectScrollDownButton} />
                </{SelectPrimitive.Popup}>
            </{SelectPrimitive.Positioner}>
        </{SelectPrimitive.Portal}>
    """


def SelectLabel(className=None, **props):
    return t"""
        <{SelectPrimitive.GroupLabel}
            data-slot="select-label"
            class={cn("px-2 py-1.5 text-xs text-muted-foreground", className)}
            ...{props}
        />
    """


def SelectItem(className=None, children=None, **props):
    span = t'<span class="pointer-events-none absolute right-2 flex size-4 items-center justify-center" />'

    return t"""
        <{SelectPrimitive.Item}
            data-slot="select-item"
            class={cn("relative flex w-full cursor-default items-center gap-2 rounded-sm py-1.5 pr-8 pl-2 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2", className)}
            ...{props}
        >
            <{SelectPrimitive.ItemText} class="flex flex-1 shrink-0 gap-2 whitespace-nowrap">
                {children}
            </{SelectPrimitive.ItemText}>
            <{SelectPrimitive.ItemIndicator} render={span}>
                <{CheckIcon} class="pointer-events-none" />
            </{SelectPrimitive.ItemIndicator}>
        </{SelectPrimitive.Item}>
    """


def SelectSeparator(className=None, **props):
    return t"""
        <{SelectPrimitive.Separator}
            data-slot="select-separator"
            class={cn("pointer-events-none -mx-1 my-1 h-px bg-border", className)}
            ...{props}
        />
    """


def SelectScrollUpButton(className=None, **props):
    return t"""
        <{SelectPrimitive.ScrollUpArrow}
            data-slot="select-scroll-up-button"
            class={cn("top-0 z-10 flex w-full cursor-default items-center justify-center bg-popover py-1 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <{ChevronUpIcon} />
        </{SelectPrimitive.ScrollUpArrow}>
    """


def SelectScrollDownButton(className=None, **props):
    return t"""
        <{SelectPrimitive.ScrollDownArrow}
            data-slot="select-scroll-down-button"
            class={cn("bottom-0 z-10 flex w-full cursor-default items-center justify-center bg-popover py-1 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <{ChevronDownIcon} />
        </{SelectPrimitive.ScrollDownArrow}>
    """
