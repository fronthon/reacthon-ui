from utils import cn

__js__ = {"react-aria-components": ["composeRenderProps", "Switch as SwitchPrimitive"]}


def Switch(className=None, size="default", children=None, **props):
    def callback(children, props):
        is_selected = props.get("isSelected")

        return t"""
            <span
                data-slot="switch-thumb"
                data-selected={is_selected or None}
                class="pointer-events-none block bg-background ring-0 transition-transform not-data-selected:translate-x-0.25 group-data-[size=default]/switch:size-3.5 group-data-[size=sm]/switch:size-2.5 dark:not-data-selected:bg-foreground data-checked:translate-x-[calc(100%+2px)] dark:data-checked:bg-primary-foreground data-unchecked:translate-x-0.25 dark:data-unchecked:bg-foreground data-selected:translate-x-[calc(100%+2px)] dark:data-selected:bg-primary-foreground"
            />
            {children}
        """

    return t"""
        <{SwitchPrimitive}
            data-slot="switch"
            data-size={size}
            class={cn("peer group/switch relative inline-flex shrink-0 items-center rounded-none border transition-all outline-none not-data-selected:border-input/50 not-data-selected:bg-input group-has-[:focus-visible]/field-label:ring-0 after:absolute after:-inset-x-3 after:-inset-y-2 focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring/30 aria-invalid:border-destructive aria-invalid:ring-2 aria-invalid:ring-destructive/20 data-focus-visible:border-ring data-focus-visible:ring-2 data-focus-visible:ring-ring/30 data-invalid:border-destructive data-invalid:ring-2 data-invalid:ring-destructive/20 data-[size=default]:h-4.5 data-[size=default]:w-8.25 data-[size=sm]:h-3.5 data-[size=sm]:w-6.25 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 dark:data-invalid:border-destructive/50 dark:data-invalid:ring-destructive/40 data-checked:border-primary data-checked:bg-primary group-has-[:focus-visible]/field-label:data-checked:border-primary data-unchecked:border-input/50 data-unchecked:bg-input group-has-[:focus-visible]/field-label:data-unchecked:border-input/50 data-selected:border-primary data-selected:bg-primary data-disabled:cursor-not-allowed data-disabled:opacity-50", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{SwitchPrimitive}>
    """
