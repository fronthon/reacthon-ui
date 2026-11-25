from utils import cn

__js__ = {"radix-ui": ["Select as SelectPrimitive"], "lucide-react": ["ChevronDownIcon", "CheckIcon", "ChevronUpIcon"]}


def Select(**props):
    return t'<{SelectPrimitive.Root} data-slot="select" ...{props} />'


def SelectGroup(className=None, **props):
    return t'<{SelectPrimitive.Group} data-slot="select-group" class={cn("scroll-my-1 p-1", className)} ...{props} />'


def SelectValue(**props):
    return t'<{SelectPrimitive.Value} data-slot="select-value" ...{props} />'


def SelectTrigger(className=None, size="default", children=None, **props):
    return t"""
        <{SelectPrimitive.Trigger}
            data-slot="select-trigger"
            data-size={size}
            class={cn("flex w-fit items-center justify-between gap-1.5 rounded-lg border border-input bg-transparent py-2 pr-2 pl-2.5 text-sm whitespace-nowrap transition-colors outline-none select-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 data-placeholder:text-muted-foreground data-[size=default]:h-8 data-[size=sm]:h-7 data-[size=sm]:rounded-[min(var(--radius-md),10px)] *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-1.5 dark:bg-input/30 dark:hover:bg-input/50 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            {children}
            <{SelectPrimitive.Icon} asChild>
                <{ChevronDownIcon} class="pointer-events-none size-4 text-muted-foreground" />
            </{SelectPrimitive.Icon}>
        </{SelectPrimitive.Trigger}>
    """


def SelectContent(className=None, children=None, position="item-aligned", align="center", **props):
    return t"""
        <{SelectPrimitive.Portal}>
            <{SelectPrimitive.Content}
                data-slot="select-content"
                data-align-trigger={position == "item-aligned"}
                class={cn(
                    "relative z-50 max-h-(--radix-select-content-available-height) min-w-36 origin-(--radix-select-content-transform-origin) overflow-x-hidden overflow-y-auto rounded-lg bg-popover text-popover-foreground shadow-md ring-1 ring-foreground/10 duration-100 data-[align-trigger=true]:animate-none data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-open:animate-in data-open:fade-in-0 data-open:zoom-in-95 data-closed:animate-out data-closed:fade-out-0 data-closed:zoom-out-95",
                    position == "popper" and "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
                    className,
                )}
                position={position}
                align={align}
                ...{props}
            >
                <{SelectScrollUpButton} />
                <{SelectPrimitive.Viewport}
                    data-position={position}
                    class={cn("data-[position=popper]:h-(--radix-select-trigger-height) data-[position=popper]:w-full data-[position=popper]:min-w-(--radix-select-trigger-width)", position == "popper" and "")}
                >
                    {children}
                </{SelectPrimitive.Viewport}>
                <{SelectScrollDownButton} />
            </{SelectPrimitive.Content}>
        </{SelectPrimitive.Portal}>
    """


def SelectLabel(className=None, **props):
    return t"""
        <{SelectPrimitive.Label}
            data-slot="select-label"
            class={cn("px-1.5 py-1 text-xs text-muted-foreground", className)}
            ...{props}
        />
    """


def SelectItem(className=None, children=None, **props):
    return t"""
        <{SelectPrimitive.Item}
            data-slot="select-item"
            class={cn("relative flex w-full cursor-default items-center gap-1.5 rounded-md py-1 pr-8 pl-1.5 text-sm outline-hidden select-none focus:bg-accent focus:text-accent-foreground not-data-[variant=destructive]:focus:**:text-accent-foreground data-disabled:pointer-events-none data-disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 *:[span]:last:flex *:[span]:last:items-center *:[span]:last:gap-2", className)}
            ...{props}
        >
            <span class="pointer-events-none absolute right-2 flex size-4 items-center justify-center">
                <{SelectPrimitive.ItemIndicator}>
                    <{CheckIcon} class="pointer-events-none" />
                </{SelectPrimitive.ItemIndicator}>
            </span>
            <{SelectPrimitive.ItemText}>{children}</{SelectPrimitive.ItemText}>
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
        <{SelectPrimitive.ScrollUpButton}
            data-slot="select-scroll-up-button"
            class={cn("z-10 flex cursor-default items-center justify-center bg-popover py-1 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <{ChevronUpIcon} />
        </{SelectPrimitive.ScrollUpButton}>
    """


def SelectScrollDownButton(className=None, **props):
    return t"""
        <{SelectPrimitive.ScrollDownButton}
            data-slot="select-scroll-down-button"
            class={cn("z-10 flex cursor-default items-center justify-center bg-popover py-1 [&_svg:not([class*='size-'])]:size-4", className)}
            ...{props}
        >
            <{ChevronDownIcon} />
        </{SelectPrimitive.ScrollDownButton}>
    """
