from example import Example, ExampleWrapper
from badge import Badge
from button import Button
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle
from field import Field, FieldLabel
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from spinner import Spinner

__js__ = {"lucide-react": ["ArrowRightIcon"]}


def SpinnerExample():
    return t"""
        <{ExampleWrapper}>
            <{SpinnerBasic} />
            <{SpinnerInButtons} />
            <{SpinnerInBadges} />
            <{SpinnerInInputGroup} />
            <{SpinnerInEmpty} />
        </{ExampleWrapper}>
    """


def SpinnerBasic():
    return t"""
        <{Example} title="Basic">
            <div class="flex items-center gap-6">
                <{Spinner} />
                <{Spinner} class="size-6" />
            </div>
        </{Example}>
    """


def SpinnerInButtons():
    return t"""
        <{Example} title="In Buttons">
            <div class="flex flex-wrap items-center gap-4">
                <{Button}>
                    <{Spinner} data-icon="inline-start" /> Submit
                </{Button}>
                <{Button} disabled>
                    <{Spinner} data-icon="inline-start" /> Disabled
                </{Button}>
                <{Button} variant="outline" disabled>
                    <{Spinner} data-icon="inline-start" /> Outline
                </{Button}>
                <{Button} variant="outline" size="icon" disabled>
                    <{Spinner} data-icon="inline-start" />
                    <span class="sr-only">Loading...</span>
                </{Button}>
            </div>
        </{Example}>
    """


def SpinnerInBadges():
    return t"""
        <{Example} title="In Badges" class="items-center justify-center">
            <div class="flex flex-wrap items-center justify-center gap-4">
                <{Badge}>
                    <{Spinner} data-icon="inline-start" />
                    Badge
                </{Badge}>
                <{Badge} variant="secondary">
                    <{Spinner} data-icon="inline-start" />
                    Badge
                </{Badge}>
                <{Badge} variant="destructive">
                    <{Spinner} data-icon="inline-start" />
                    Badge
                </{Badge}>
                <{Badge} variant="outline">
                    <{Spinner} data-icon="inline-start" />
                    Badge
                </{Badge}>
            </div>
        </{Example}>
    """


def SpinnerInInputGroup():
    return t"""
        <{Example} title="In Input Group">
            <{Field}>
                <{FieldLabel} for="input-group-spinner">Input Group</{FieldLabel}>
                <{InputGroup}>
                    <{InputGroupInput} id="input-group-spinner" />
                    <{InputGroupAddon}>
                        <{Spinner} />
                    </{InputGroupAddon}>
                </{InputGroup}>
            </{Field}>
        </{Example}>
    """


def SpinnerInEmpty():
    return t"""
        <{Example} title="In Empty State" containerClassName="lg:col-span-full">
            <{Empty} class="min-h-[300px]">
                <{EmptyHeader}>
                    <{EmptyMedia} variant="icon">
                        <{Spinner} />
                    </{EmptyMedia}>
                    <{EmptyTitle}>No projects yet</{EmptyTitle}>
                    <{EmptyDescription}>
                        You haven't created any projects yet. Get started by creating your first project.
                    </{EmptyDescription}>
                </{EmptyHeader}>
                <{EmptyContent}>
                    <div class="flex gap-2">
                        <{Button} render={t'<a href="#" />'} nativeButton={False}>Create project</{Button}>
                        <{Button} variant="outline">Import project</{Button}>
                    </div>
                    <{Button}
                        variant="link"
                        render={t'<a href="#" />'}
                        nativeButton={False}
                        class="text-muted-foreground"
                    >
                        Learn more{" "}
                        <{ArrowRightIcon} />
                    </{Button}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """
