from utils import cn
from button import button_variants

__js__ = {"@shadcn/react/questionnaire": ["Questionnaire as QuestionnairePrimitive"], "lucide-react": ["CheckIcon"]}


def Questionnaire(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Root}
            data-slot="questionnaire"
            class={cn("flex w-full min-w-0 flex-col gap-6", className)}
            ...{props}
        />
    """


def QuestionnaireProgress(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Progress}
            data-slot="questionnaire-progress"
            class={cn("min-h-[1lh] w-fit min-w-[14ch] text-xs font-medium text-muted-foreground tabular-nums", className)}
            ...{props}
        />
    """


def QuestionnaireItem(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Item}
            data-slot="questionnaire-item"
            class={cn("flex min-w-0 flex-col gap-5 border-0 p-0 outline-none", className)}
            ...{props}
        />
    """


def QuestionnaireTitle(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Title}
            data-slot="questionnaire-title"
            class={cn("font-heading text-base font-semibold text-pretty [&:not(:has(~[data-slot=questionnaire-description]))]:mb-5", className)}
            ...{props}
        />
    """


def QuestionnaireDescription(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Description}
            data-slot="questionnaire-description"
            class={cn("text-sm text-pretty text-muted-foreground", className)}
            ...{props}
        />
    """


def QuestionnaireChoices(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Choices}
            data-slot="questionnaire-choices"
            class={cn("group/questionnaire-choices grid min-w-0 gap-3", className)}
            ...{props}
        />
    """


def QuestionnaireChoice(children=None, className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Choice}
            data-slot="questionnaire-choice"
            class={cn(
                "group/questionnaire-choice relative flex min-h-11 cursor-pointer items-start gap-3 rounded-md border border-input bg-transparent px-4 py-3.5 text-start text-sm shadow-xs transition-colors outline-none select-none hover:bg-muted/50 has-[>input:focus-visible]:border-ring has-[>input:focus-visible]:ring-3 has-[>input:focus-visible]:ring-ring/50 data-invalid:border-destructive dark:bg-input/20 data-checked:border-primary/40 data-checked:bg-muted dark:data-checked:bg-muted",
                "data-disabled:pointer-events-none data-disabled:cursor-not-allowed data-disabled:opacity-50",
                className,
            )}
            ...{props}
        >
            <{QuestionnairePrimitive.ChoiceInput}
                data-slot="questionnaire-choice-input"
                class="absolute inset-0 z-10 size-full cursor-pointer opacity-0"
            />
            <span
                aria-hidden="true"
                data-slot="questionnaire-choice-indicator"
                class="pointer-events-none relative flex size-4 shrink-0 translate-y-[--spacing(0.45)] items-center justify-center rounded-[4px] border border-input group-has-data-[slot=questionnaire-choice-description]/questionnaire-choice:translate-y-0.5 group-data-[type=radio]/questionnaire-choice:rounded-full group-data-checked/questionnaire-choice:border-primary group-data-checked/questionnaire-choice:bg-primary group-data-checked/questionnaire-choice:text-primary-foreground dark:bg-input/30 dark:group-data-checked/questionnaire-choice:bg-primary"
            >
                <span
                    data-slot="questionnaire-choice-indicator-dot"
                    class="hidden size-2 rounded-full bg-primary-foreground group-data-[type=checkbox]/questionnaire-choice:hidden group-data-checked/questionnaire-choice:block"
                />
                <{CheckIcon}
                    data-slot="questionnaire-choice-indicator-check"
                    class="hidden size-3.5 group-data-[type=radio]/questionnaire-choice:hidden group-data-checked/questionnaire-choice:block"
                />
            </span>
            <{QuestionnairePrimitive.ChoiceLabel}
                data-slot="questionnaire-choice-label"
                class="flex min-w-0 flex-1 flex-col gap-1 leading-snug"
            >
                {children}
            </{QuestionnairePrimitive.ChoiceLabel}>
            <{QuestionnairePrimitive.ChoiceShortcut}
                data-slot="questionnaire-choice-shortcut"
                class="pointer-events-none ms-auto hidden size-5 shrink-0 translate-y-[--spacing(0.45)] items-center justify-center rounded-md border border-input bg-background font-mono text-[0.625rem] leading-none font-medium text-muted-foreground shadow-xs group-has-data-[slot=questionnaire-choice-description]/questionnaire-choice:translate-y-0.5 group-data-[shortcut]/questionnaire-choice:inline-flex"
            />
        </{QuestionnairePrimitive.Choice}>
    """


def QuestionnaireChoiceDescription(className=None, **props):
    return t"""
        <span
            data-slot="questionnaire-choice-description"
            class={cn("text-muted-foreground", className)}
            ...{props}
        />
    """


def QuestionnaireInput(className=None, **props):
    return t"""
        <div data-slot="questionnaire-input-wrapper" class="group/questionnaire-input relative w-full min-w-0">
            <{QuestionnairePrimitive.Input}
                data-slot="questionnaire-input"
                class={cn(
                    "h-9 min-h-11 w-full min-w-0 rounded-md border border-input bg-transparent px-2.5 py-1 text-base shadow-xs transition-[color,box-shadow,background-color] outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-3 aria-invalid:ring-destructive/20 sm:min-h-0 md:text-sm dark:bg-input/30 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40",
                    "selection:bg-primary selection:text-primary-foreground placeholder:text-muted-foreground",
                    className,
                )}
                ...{props}
            />
        </div>
    """


def QuestionnaireError(className=None, **props):
    return t"""
        <{QuestionnairePrimitive.Error}
            data-slot="questionnaire-error"
            class={cn("text-sm text-destructive", className)}
            ...{props}
        />
    """


def QuestionnaireActions(className=None, **props):
    return t"""
        <div
            data-slot="questionnaire-actions"
            class={cn("grid min-h-11 w-full grid-cols-[minmax(0,1fr)_auto_auto] items-center gap-2 sm:min-h-9", className)}
            ...{props}
        />
    """


def QuestionnairePrevious(children=None, className=None, size="default", variant="outline", **props):
    return t"""
        <{QuestionnairePrimitive.Previous}
            data-slot="questionnaire-previous"
            data-size={size}
            data-variant={variant}
            class={cn(
                button_variants(size=size, variant=variant),
                "col-start-1 row-start-1 min-h-11 justify-self-start sm:min-h-0",
                className,
            )}
            ...{props}
        >
            {children if children is not None else "Previous"}
        </{QuestionnairePrimitive.Previous}>
    """


def QuestionnaireSkip(children=None, className=None, size="default", variant="outline", **props):
    return t"""
        <{QuestionnairePrimitive.Skip}
            data-slot="questionnaire-skip"
            data-size={size}
            data-variant={variant}
            class={cn(
                button_variants(size=size, variant=variant),
                "col-start-2 row-start-1 min-h-11 justify-self-end sm:min-h-0",
                className,
            )}
            ...{props}
        >
            {children if children is not None else "Skip"}
        </{QuestionnairePrimitive.Skip}>
    """


def QuestionnaireNext(children=None, className=None, size="default", variant="default", **props):
    return t"""
        <{QuestionnairePrimitive.Next}
            data-slot="questionnaire-next"
            data-size={size}
            data-variant={variant}
            class={cn(
                button_variants(size=size, variant=variant),
                "col-start-3 row-start-1 min-h-11 justify-self-end sm:min-h-0",
                className,
            )}
            ...{props}
        >
            {children if children is not None else "Next"}
        </{QuestionnairePrimitive.Next}>
    """


def QuestionnaireSubmit(children=None, className=None, size="default", variant="default", **props):
    return t"""
        <{QuestionnairePrimitive.Submit}
            data-slot="questionnaire-submit"
            data-size={size}
            data-variant={variant}
            class={cn(
                button_variants(size=size, variant=variant),
                "col-start-3 row-start-1 min-h-11 justify-self-end sm:min-h-0",
                className,
            )}
            ...{props}
        >
            {children if children is not None else "Submit"}
        </{QuestionnairePrimitive.Submit}>
    """
