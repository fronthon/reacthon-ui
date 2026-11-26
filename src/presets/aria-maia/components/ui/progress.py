from javascript import NULL
from reacthon import create_context, use_context, use_memo
from utils import cn

__js__ = {"react-aria-components": ["Label as LabelPrimitive", "ProgressBar as ProgressPrimitive"]}

ProgressContext = create_context(NULL)


def use_progress():
    context = use_context(ProgressContext)
    if not context:
        raise RuntimeError("useProgress must be used within a Progress.")

    return context


def ProgressContent(children=None, percentage=None, isIndeterminate=None, valueText=None, **_):
    context = use_memo(
        lambda: {"percentage": percentage, "isIndeterminate": isIndeterminate, "valueText": valueText},
        [percentage, isIndeterminate, valueText],
    )

    return t"""
        <{ProgressContext} value={context}>
            {children}
            <{ProgressTrack}>
                <{ProgressIndicator} />
            </{ProgressTrack}>
        </{ProgressContext}>
    """


def Progress(className=None, children=None, **props):
    def callback(props):
        percentage, value_text, is_indeterminate = props.get("percentage"), props.get("valueText"), props.get("isIndeterminate")

        return t"""
            <{ProgressContent}
                percentage={percentage}
                valueText={value_text}
                isIndeterminate={is_indeterminate}
            >
                {children}
            </{ProgressContent}>
        """

    return t"""
        <{ProgressPrimitive}
            data-slot="progress"
            class={cn("flex flex-wrap gap-3", className)}
            ...{props}
        >
            {callback}
        </{ProgressPrimitive}>
    """


def ProgressTrack(className=None, **props):
    return t"""
        <span
            class={cn("relative flex h-3 w-full items-center overflow-x-hidden rounded-4xl bg-muted", className)}
            data-slot="progress-track"
            ...{props}
        />
    """


def ProgressIndicator(className=None, style=None, **props):
    progress = use_progress()
    percentage, is_indeterminate = progress.get("percentage"), progress.get("isIndeterminate")

    return t"""
        <span
            data-slot="progress-indicator"
            class={cn("h-full bg-primary transition-all", className)}
            style={ {
                **(style or {}),
                "width": f"{100 if is_indeterminate else percentage if percentage not in (None, NULL) else 0}%",
            } }
            ...{props}
        />
    """


def ProgressLabel(className=None, **props):
    return t'<{LabelPrimitive} class={cn("text-sm font-medium", className)} data-slot="progress-label" ...{props} />'


def ProgressValue(className=None, children=None, **props):
    value_text = use_progress().get("valueText")
    return t"""
        <span
            class={cn("ml-auto text-sm text-muted-foreground tabular-nums", className)}
            data-slot="progress-value"
            ...{props}
        >
            {children(value_text) if children and value_text not in (None, NULL) else value_text}
        </span>
    """
