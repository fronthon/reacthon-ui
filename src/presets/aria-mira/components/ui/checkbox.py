from utils import cn

__js__ = {
    "react-aria-components": ["Checkbox as CheckboxPrimitive", "composeRenderProps"],
    "lucide-react": ["CheckIcon"],
}


def Checkbox(className=None, children=None, **props):
    def callback(children, props):
        is_selected, is_indeterminate = props.get("isSelected"), props.get("isIndeterminate")

        return t"""
            <span
                data-slot="checkbox-indicator"
                class="grid place-content-center text-current transition-none [&>svg]:size-3.5"
            >
                {(is_selected or is_indeterminate) and t'<{CheckIcon} />'}
            </span>
            {children}
        """

    return t"""
        <{CheckboxPrimitive}
            data-slot="checkbox"
            class={cn("peer relative flex size-4 shrink-0 items-center justify-center rounded-[4px] border border-input transition-shadow outline-none group-has-disabled/field:opacity-50 group-has-[:focus-visible]/field-label:ring-0 group-has-[:focus-visible]/field-label:not-data-checked:border-input after:absolute after:-inset-x-3 after:-inset-y-2 focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring/30 aria-invalid:border-destructive aria-invalid:ring-2 aria-invalid:ring-destructive/20 aria-invalid:aria-checked:border-primary data-focus-visible:border-ring data-focus-visible:ring-2 data-focus-visible:ring-ring/30 data-invalid:border-destructive data-invalid:ring-2 data-invalid:ring-destructive/20 data-[disabled]:cursor-not-allowed data-[disabled]:opacity-50 dark:bg-input/30 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40 dark:data-invalid:border-destructive/50 dark:data-invalid:ring-destructive/40 data-checked:border-primary data-checked:bg-primary data-checked:text-primary-foreground group-has-[:focus-visible]/field-label:data-checked:border-primary dark:data-checked:bg-primary data-selected:border-primary data-selected:bg-primary data-selected:text-primary-foreground data-invalid:data-selected:border-primary dark:data-selected:bg-primary", className)}
            ...{props}
        >
            {composeRenderProps(children, callback)}
        </{CheckboxPrimitive}>
    """
