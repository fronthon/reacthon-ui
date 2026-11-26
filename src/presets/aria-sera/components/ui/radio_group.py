from utils import cn

__js__ = {
    "react-aria-components": ["composeRenderProps", "RadioGroup as RadioGroupPrimitive", "Radio as RadioPrimitive"],
}


def RadioGroup(className=None, **props):
    return t'<{RadioGroupPrimitive} data-slot="radio-group" class={cn("grid w-full gap-3", className)} ...{props} />'


def RadioGroupItem(className=None, children=None, **props):
    def callback(children, props_2):
        is_selected = props_2.get("isSelected")

        span = t"""
            <span class="absolute top-1/2 left-1/2 size-2 -translate-x-1/2 -translate-y-1/2 rounded-full bg-foreground" />
        """

        return t"""
            <span data-slot="radio-group-indicator" class="flex size-4.5 items-center justify-center">
                {is_selected and span}
            </span>
            {children}
        """

    return t"""
        <{RadioPrimitive}
            data-slot="radio-group-item"
            class={cn("group/radio-group-item peer relative flex aspect-square size-4.5 shrink-0 rounded-full border border-input bg-transparent outline-none group-has-[:focus-visible]/field-label:ring-0 group-has-[:focus-visible]/field-label:not-data-checked:border-input after:absolute after:-inset-x-3 after:-inset-y-2 focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring/30 aria-invalid:border-destructive aria-invalid:ring-2 aria-invalid:ring-destructive/20 aria-invalid:aria-checked:border-foreground data-focus-visible:border-ring data-focus-visible:ring-2 data-focus-visible:ring-ring/30 data-invalid:border-destructive data-invalid:ring-2 data-invalid:ring-destructive/20 data-[disabled]:cursor-not-allowed data-[disabled]:opacity-50 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 dark:data-invalid:border-destructive/50 dark:data-invalid:ring-destructive/40 data-checked:border-foreground group-has-[:focus-visible]/field-label:data-checked:border-foreground data-selected:border-foreground data-invalid:data-selected:border-foreground", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{RadioPrimitive}>
    """
