from utils import cn


def Kbd(className=None, **props):
    return t"""
        <kbd
            data-slot="kbd"
            class={cn("pointer-events-none inline-flex h-5 w-fit min-w-5 items-center justify-center gap-1 rounded-none bg-muted px-1 font-sans text-xs font-medium text-muted-foreground select-none in-data-[slot=tooltip-content]:bg-background/20 in-data-[slot=tooltip-content]:text-background dark:in-data-[slot=tooltip-content]:bg-background/10 [&_svg:not([class*='size-'])]:size-3", className)}
            ...{props}
        />
    """


def KbdGroup(className=None, **props):
    return t'<kbd data-slot="kbd-group" class={cn("inline-flex items-center gap-1", className)} ...{props} />'
