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
            <span class="absolute top-1/2 left-1/2 size-2 -translate-x-1/2 -translate-y-1/2 rounded-full bg-primary-foreground dark:size-2.5" />
        """

        return t"""
            <span data-slot="radio-group-indicator" class="flex size-4 items-center justify-center">
                {is_selected and span}
            </span>
            {children}
        """

    return t"""
        <{RadioPrimitive}
            data-slot="radio-group-item"
            class={cn("group/radio-group-item peer relative flex aspect-square size-4 shrink-0 rounded-full border border-transparent bg-input/90 outline-none group-has-[:focus-visible]/field-label:border-transparent group-has-[:focus-visible]/field-label:ring-0 after:absolute after:-inset-x-3 after:-inset-y-2 focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/30 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 data-focus-visible:border-ring data-focus-visible:ring-3 data-focus-visible:ring-ring/30 data-invalid:border-destructive data-invalid:ring-3 data-invalid:ring-destructive/20 data-[disabled]:cursor-not-allowed data-[disabled]:opacity-50 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 dark:data-invalid:border-destructive/50 dark:data-invalid:ring-destructive/40 data-checked:bg-primary data-checked:text-primary-foreground dark:data-checked:bg-primary data-selected:bg-primary data-selected:text-primary-foreground dark:data-selected:bg-primary", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{RadioPrimitive}>
    """
