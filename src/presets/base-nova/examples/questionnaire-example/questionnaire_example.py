from browser import window
from javascript import NULL
from reacthon import use_id
from example import Example, ExampleWrapper
from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from dialog import Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger
from questionnaire import (
    Questionnaire,
    QuestionnaireActions,
    QuestionnaireChoice,
    QuestionnaireChoiceDescription,
    QuestionnaireChoices,
    QuestionnaireDescription,
    QuestionnaireError,
    QuestionnaireInput,
    QuestionnaireItem,
    QuestionnaireNext,
    QuestionnairePrevious,
    QuestionnaireProgress,
    QuestionnaireSkip,
    QuestionnaireSubmit,
    QuestionnaireTitle,
)

__js__ = {"sonner": ["toast"]}

questionnaire_items = [
    {
        "choices": [{"value": "delegation"}, {"value": "questions"}, {"value": "both"}],
        "name": "direction",
        "required": True,
    },
    {"choices": [{"value": "progress"}, {"value": "decisions"}, {"value": "risks"}], "name": "signals"},
    {"choices": [{"value": "week"}, {"value": "cycle"}, {"value": "later"}], "name": "timing", "required": True},
]

task_items = [
    {
        "choices": [{"value": "inspect"}, {"value": "implement"}, {"value": "review"}],
        "name": "task",
        "required": True,
    },
]

plan_items = [
    {
        "choices": [{"value": "plus"}, {"value": "pro"}, {"value": "enterprise", "disabled": True}],
        "name": "plan",
        "required": True,
    },
]


def QuestionnaireExample():
    return t"""
        <{ExampleWrapper}>
            <{QuestionnaireStandalone} />
            <{QuestionnaireCard} />
            <{QuestionnaireDialog} />
            <{QuestionnaireNoDescription} />
            <{QuestionnaireDisabled} />
        </{ExampleWrapper}>
    """


def QuestionnaireDisabled():
    return t"""
        <{Example} title="Disabled" containerClassName="md:col-span-2">
            <{Questionnaire} class="mx-auto max-w-lg" defaultItem="plan" items={plan_items} onSubmit={handle_submit}>
                <{QuestionnaireItem} name="plan" required>
                    <{QuestionnaireTitle}>Choose a plan</{QuestionnaireTitle}>
                    <{QuestionnaireDescription}>
                        Enterprise is not available on your account.
                    </{QuestionnaireDescription}>
                    <{QuestionnaireChoices}>
                        <{QuestionnaireChoice} value="plus">
                            <span class="font-medium">Plus</span>
                            <{QuestionnaireChoiceDescription}>
                                For individuals and small teams
                            </{QuestionnaireChoiceDescription}>
                        </{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="pro">
                            <span class="font-medium">Pro</span>
                            <{QuestionnaireChoiceDescription}>For growing businesses</{QuestionnaireChoiceDescription}>
                        </{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="enterprise" disabled>
                            <span class="font-medium">Enterprise</span>
                            <{QuestionnaireChoiceDescription}>
                                For large teams and enterprises
                            </{QuestionnaireChoiceDescription}>
                        </{QuestionnaireChoice}>
                    </{QuestionnaireChoices}>
                    <{QuestionnaireError} />
                </{QuestionnaireItem}>
                <{QuestionnaireNavigation} />
            </{Questionnaire}>
        </{Example}>
    """


def QuestionnaireNoDescription():
    return t"""
        <{Example} title="No description" containerClassName="md:col-span-2">
            <{Questionnaire}
                class="mx-auto max-w-lg"
                defaultItem="task"
                items={task_items}
                shortcuts="letters"
                onSubmit={handle_submit}
            >
                <{QuestionnaireProgress} />
                <{QuestionnaireItem} name="task" required>
                    <{QuestionnaireTitle}>What should the agent do next?</{QuestionnaireTitle}>
                    <{QuestionnaireChoices}>
                        <{QuestionnaireChoice} value="inspect">Inspect the codebase</{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="implement">Implement the change</{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="review">Review the result</{QuestionnaireChoice}>
                    </{QuestionnaireChoices}>
                    <{QuestionnaireError} />
                </{QuestionnaireItem}>
                <{QuestionnaireNavigation} />
            </{Questionnaire}>
        </{Example}>
    """


def QuestionnaireStandalone():
    return t"""
        <{Example} title="Standalone" containerClassName="md:col-span-2">
            <{Questionnaire}
                class="mx-auto max-w-lg"
                defaultItem="direction"
                items={questionnaire_items}
                shortcuts="letters"
                onSubmit={handle_submit}
            >
                <{QuestionnaireProgress} />
                <{QuestionnaireQuestions} />
                <{QuestionnaireNavigation} />
            </{Questionnaire}>
        </{Example}>
    """


def QuestionnaireCard():
    return t"""
        <{Example} title="Card" containerClassName="md:col-span-2">
            <{Questionnaire}
                defaultItem="direction"
                items={questionnaire_items}
                shortcuts="numbers"
                onSubmit={handle_submit}
            >
                <{QuestionnaireCardQuestions} />
            </{Questionnaire}>
        </{Example}>
    """


def QuestionnaireDialog():
    return t"""
        <{Example} title="Dialog" class="items-center justify-center" containerClassName="md:col-span-2">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open questionnaire</{DialogTrigger}>
                <{DialogContent}>
                    <{Questionnaire} defaultItem="direction" items={questionnaire_items} onSubmit={handle_submit}>
                        <{DialogHeader}>
                            <{DialogTitle} class="sr-only">Plan an agent interface</{DialogTitle}>
                            <{DialogDescription} class="sr-only">
                                Answer three questions to shape the next prototype.
                            </{DialogDescription}>
                            <{QuestionnaireProgress}
                                class="font-semibold tracking-widest text-foreground uppercase"
                                render={(lambda props, state: t'''
                                    <span ...{props}>Question {state["current"]} of {state["total"]}</span>
                                ''')}
                            />
                        </{DialogHeader}>
                        <{QuestionnaireQuestions} />
                        <{DialogFooter}>
                            <{QuestionnaireNavigation} />
                        </{DialogFooter}>
                    </{Questionnaire}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


def QuestionnaireCardQuestions():
    direction_title_id = use_id()
    signals_title_id = use_id()
    timing_title_id = use_id()

    return t"""
        <{QuestionnaireItem} aria-labelledby={direction_title_id} name="direction" required>
            <{Card} class="mx-auto w-full max-w-lg">
                <{CardHeader}>
                    <{QuestionnaireTitle} id={direction_title_id} render={t'<{CardTitle} />'}>
                        What should we prototype next?
                    </{QuestionnaireTitle}>
                    <{QuestionnaireDescription} render={t'<{CardDescription} />'}>
                        Choose one direction or write another answer.
                    </{QuestionnaireDescription}>
                    <{CardAction}>
                        <{QuestionnaireProgress} />
                    </{CardAction}>
                </{CardHeader}>
                <{CardContent}>
                    <{QuestionnaireChoices}>
                        <{QuestionnaireChoice} value="delegation">
                            <span class="font-medium">Sub-agent delegation</span>
                            <{QuestionnaireChoiceDescription}>
                                Show when work is delegated and what comes back.
                            </{QuestionnaireChoiceDescription}>
                        </{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="questions">
                            <span class="font-medium">Question prompts</span>
                            <{QuestionnaireChoiceDescription}>
                                Show choices while the agent waits for input.
                            </{QuestionnaireChoiceDescription}>
                        </{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="both">
                            <span class="font-medium">Both together</span>
                            <{QuestionnaireChoiceDescription}>
                                Explore one unified interaction pattern.
                            </{QuestionnaireChoiceDescription}>
                        </{QuestionnaireChoice}>
                        <{QuestionnaireInput} aria-label="Another direction" placeholder="Type another direction…" />
                    </{QuestionnaireChoices}>
                    <{QuestionnaireError} />
                </{CardContent}>
                <{CardFooter}>
                    <{QuestionnaireNavigation} />
                </{CardFooter}>
            </{Card}>
        </{QuestionnaireItem}>
        <{QuestionnaireItem} aria-labelledby={signals_title_id} name="signals" multiple>
            <{Card} class="mx-auto w-full max-w-lg">
                <{CardHeader}>
                    <{QuestionnaireTitle} id={signals_title_id} render={t'<{CardTitle} />'}>
                        What should every progress update include?
                    </{QuestionnaireTitle}>
                    <{QuestionnaireDescription} render={t'<{CardDescription} />'}>
                        Select all that apply, or skip this question.
                    </{QuestionnaireDescription}>
                    <{CardAction}>
                        <{QuestionnaireProgress} />
                    </{CardAction}>
                </{CardHeader}>
                <{CardContent}>
                    <{QuestionnaireChoices}>
                        <{QuestionnaireChoice} value="progress">Progress</{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="decisions">Decisions</{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="risks">Risks</{QuestionnaireChoice}>
                    </{QuestionnaireChoices}>
                    <{QuestionnaireError} />
                </{CardContent}>
                <{CardFooter}>
                    <{QuestionnaireNavigation} />
                </{CardFooter}>
            </{Card}>
        </{QuestionnaireItem}>
        <{QuestionnaireItem} aria-labelledby={timing_title_id} name="timing" required>
            <{Card} class="mx-auto w-full max-w-lg">
                <{CardHeader}>
                    <{QuestionnaireTitle} id={timing_title_id} render={t'<{CardTitle} />'}>
                        When should this be revisited?
                    </{QuestionnaireTitle}>
                    <{QuestionnaireDescription} render={t'<{CardDescription} />'}>
                        Choose when this should be revisited.
                    </{QuestionnaireDescription}>
                    <{CardAction}>
                        <{QuestionnaireProgress} />
                    </{CardAction}>
                </{CardHeader}>
                <{CardContent}>
                    <{QuestionnaireChoices}>
                        <{QuestionnaireChoice} value="week">This week</{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="cycle">Next cycle</{QuestionnaireChoice}>
                        <{QuestionnaireChoice} value="later">Revisit later</{QuestionnaireChoice}>
                    </{QuestionnaireChoices}>
                    <{QuestionnaireError} />
                </{CardContent}>
                <{CardFooter}>
                    <{QuestionnaireNavigation} />
                </{CardFooter}>
            </{Card}>
        </{QuestionnaireItem}>
    """


def QuestionnaireQuestions():
    return t"""
        <{QuestionnaireItem} name="direction" required>
            <{QuestionnaireTitle}>What should we prototype next?</{QuestionnaireTitle}>
            <{QuestionnaireDescription}>Choose one direction or write another answer.</{QuestionnaireDescription}>
            <{QuestionnaireChoices}>
                <{QuestionnaireChoice} value="delegation">
                    <span class="font-medium">Sub-agent delegation</span>
                    <{QuestionnaireChoiceDescription}>
                        Show when work is delegated and what comes back.
                    </{QuestionnaireChoiceDescription}>
                </{QuestionnaireChoice}>
                <{QuestionnaireChoice} value="questions">
                    <span class="font-medium">Question prompts</span>
                    <{QuestionnaireChoiceDescription}>
                        Show choices while the agent waits for input.
                    </{QuestionnaireChoiceDescription}>
                </{QuestionnaireChoice}>
                <{QuestionnaireChoice} value="both">
                    <span class="font-medium">Both together</span>
                    <{QuestionnaireChoiceDescription}>
                        Explore one unified interaction pattern.
                    </{QuestionnaireChoiceDescription}>
                </{QuestionnaireChoice}>
                <{QuestionnaireInput} aria-label="Another direction" placeholder="Type another direction…" />
            </{QuestionnaireChoices}>
            <{QuestionnaireError} />
        </{QuestionnaireItem}>
        <{QuestionnaireItem} name="signals" multiple>
            <{QuestionnaireTitle}>What should every progress update include?</{QuestionnaireTitle}>
            <{QuestionnaireDescription}>Select all that apply, or skip this question.</{QuestionnaireDescription}>
            <{QuestionnaireChoices}>
                <{QuestionnaireChoice} value="progress">Progress</{QuestionnaireChoice}>
                <{QuestionnaireChoice} value="decisions">Decisions</{QuestionnaireChoice}>
                <{QuestionnaireChoice} value="risks">Risks</{QuestionnaireChoice}>
            </{QuestionnaireChoices}>
            <{QuestionnaireError} />
        </{QuestionnaireItem}>
        <{QuestionnaireItem} name="timing" required>
            <{QuestionnaireTitle}>When should this be revisited?</{QuestionnaireTitle}>
            <{QuestionnaireDescription}>Choose when this should be revisited.</{QuestionnaireDescription}>
            <{QuestionnaireChoices}>
                <{QuestionnaireChoice} value="week">This week</{QuestionnaireChoice}>
                <{QuestionnaireChoice} value="cycle">Next cycle</{QuestionnaireChoice}>
                <{QuestionnaireChoice} value="later">Revisit later</{QuestionnaireChoice}>
            </{QuestionnaireChoices}>
            <{QuestionnaireError} />
        </{QuestionnaireItem}>
    """


def QuestionnaireNavigation():
    return t"""
        <{QuestionnaireActions} class="w-full">
            <{QuestionnairePrevious} />
            <{QuestionnaireSkip} />
            <{QuestionnaireNext}>Next</{QuestionnaireNext}>
            <{QuestionnaireSubmit}>Save answers</{QuestionnaireSubmit}>
        </{QuestionnaireActions}>
    """


def handle_submit(event):
    event.preventDefault()

    form_data = window.FormData.new(event.currentTarget)
    values = {
        "direction": form_data.get("direction"),
        "signals": form_data.getAll("signals"),
        "timing": form_data.get("timing"),
    }

    toast(
        "Questionnaire submitted",
        {
            "description": f"Direction: {values["direction"] if values["direction"] not in (None, NULL) else "None"} · Progress signals: {", ".join(values["signals"]) or "None"} · Timing: {values["timing"] if values["timing"] not in (None, NULL) else "None"}",
        },
    )
