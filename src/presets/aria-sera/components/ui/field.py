from javascript import NULL
from reacthon import use_memo
from utils import cn, cva
from label import Label
from separator import Separator


def FieldSet(className=None, **props):
    return t"""
        <fieldset
            data-slot="field-set"
            class={cn("flex flex-col gap-6 has-[>[data-slot=checkbox-group]]:gap-3 has-[>[data-slot=radio-group]]:gap-3", className)}
            ...{props}
        />
    """


def FieldLegend(className=None, variant="legend", **props):
    return t"""
        <legend
            data-slot="field-legend"
            data-variant={variant}
            class={cn("mb-3 font-semibold uppercase data-[variant=label]:text-xs data-[variant=legend]:text-xs", className)}
            ...{props}
        />
    """


def FieldGroup(className=None, **props):
    return t"""
        <div
            data-slot="field-group"
            class={cn("group/field-group @container/field-group flex w-full flex-col gap-10 data-[slot=checkbox-group]:gap-3 *:data-[slot=field-group]:gap-4", className)}
            ...{props}
        />
    """


field_variants = cva(
    "group/field flex w-full gap-3 data-[invalid=true]:text-destructive",
    {
        "orientation": {
            "vertical": "flex-col *:w-full [&>.sr-only]:w-auto",
            "horizontal": "flex-row items-center has-[>[data-slot=field-content]]:items-start *:data-[slot=field-label]:flex-auto has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
            "responsive": "flex-col *:w-full @md/field-group:flex-row @md/field-group:items-center @md/field-group:*:w-auto @md/field-group:has-[>[data-slot=field-content]]:items-start @md/field-group:*:data-[slot=field-label]:flex-auto [&>.sr-only]:w-auto @md/field-group:has-[>[data-slot=field-content]]:[&>[role=checkbox],[role=radio]]:mt-px",
        },
    },
    {"orientation": "vertical"},
)


def Field(className=None, orientation="vertical", **props):
    return t"""
        <div
            role="group"
            data-slot="field"
            data-orientation={orientation}
            class={cn(field_variants(orientation=orientation), className)}
            ...{props}
        />
    """


def FieldContent(className=None, **props):
    return t"""
        <div
            data-slot="field-content"
            class={cn("group/field-content flex flex-1 flex-col gap-1 leading-snug", className)}
            ...{props}
        />
    """


def FieldLabel(className=None, **props):
    return t"""
        <{Label}
            data-slot="field-label"
            class={cn(
                "group/field-label peer/field-label flex w-fit gap-2 leading-relaxed group-data-[disabled=true]/field:opacity-50 has-data-checked:border-primary/30 has-data-checked:bg-primary/5 has-data-selected:border-primary/30 has-data-selected:bg-primary/5 has-[>[data-slot=field]]:rounded-none has-[>[data-slot=field]]:border has-[>[data-slot=field]]:not-has-[:disabled,[data-disabled]]:hover:bg-muted/50 has-[>[data-slot=field]]:has-[:focus-visible]:ring-2 has-[>[data-slot=field]]:has-[:focus-visible]:ring-ring/30 *:data-[slot=field]:p-4 dark:has-data-checked:border-primary/20 dark:has-data-checked:bg-primary/10 dark:has-data-selected:border-primary/20 dark:has-data-selected:bg-primary/10",
                "has-[>[data-slot=field]]:w-full has-[>[data-slot=field]]:flex-col",
                className,
            )}
            ...{props}
        />
    """


def FieldTitle(className=None, **props):
    return t"""
        <div
            data-slot="field-label"
            class={cn("flex w-fit items-center gap-2 text-xs font-semibold uppercase group-data-[disabled=true]/field:opacity-50 in-data-[slot=field-label]:font-semibold", className)}
            ...{props}
        />
    """


def FieldDescription(className=None, **props):
    return t"""
        <p
            data-slot="field-description"
            class={cn(
                "text-left text-sm leading-normal font-normal tracking-normal text-muted-foreground normal-case group-has-data-horizontal/field:text-balance [[data-variant=legend]+&]:-mt-1.5",
                "last:mt-0 nth-last-2:-mt-1",
                "[&>a]:underline [&>a]:underline-offset-4 [&>a:hover]:text-primary",
                className,
            )}
            ...{props}
        />
    """


def FieldSeparator(children=None, className=None, **props):
    span = t"""
        <span
            class="relative mx-auto block w-fit bg-background px-2 text-muted-foreground"
            data-slot="field-separator-content"
        >
            {children}
        </span>
    """

    return t"""
        <div
            data-slot="field-separator"
            data-content={bool(children)}
            class={cn("relative -my-2 h-5 text-sm group-data-[variant=outline]/field-group:-mb-2", className)}
            ...{props}
        >
            <{Separator} class="absolute inset-0 top-1/2" />
            {children and span}
        </div>
    """


def FieldError(className=None, children=None, errors=None, **props):
    def content():
        if children:
            return children

        if not errors:
            return NULL

        unique_errors = list({error.get("message") if error else None: error for error in errors}.values())

        if len(unique_errors) == 1:
            return unique_errors[0].get("message") if unique_errors[0] else None

        return t"""
            <ul class="ml-4 flex list-disc flex-col gap-1">
                {[(error.get("message") if error else None) and t'<li key={index}>{error.get("message")}</li>' for index, error in enumerate(unique_errors)]}
            </ul>
        """

    content = use_memo(content, [children, errors])

    if not content:
        return None

    return t"""
        <div
            role="alert"
            data-slot="field-error"
            class={cn("text-sm font-normal text-destructive", className)}
            ...{props}
        >
            {content}
        </div>
    """
