from example import Example, ExampleWrapper
from button import Button

__js__ = {"lucide-react": ["ArrowRightIcon", "ArrowLeftCircleIcon"]}


def ButtonExample():
    return t"""
        <{ExampleWrapper} class="lg:grid-cols-1 2xl:grid-cols-1">
            <{ButtonVariantsAndSizes} />
            <{ButtonIconRight} />
            <{ButtonIconLeft} />
            <{ButtonIconOnly} />
            <{ButtonInvalidStates} />
            <{ButtonExamples} />
        </{ExampleWrapper}>
    """


def ButtonVariantsAndSizes():
    return t"""
        <{Example} title="Variants & Sizes">
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="xs">Default</{Button}>
                <{Button} size="xs" variant="secondary">Secondary</{Button}>
                <{Button} size="xs" variant="outline">Outline</{Button}>
                <{Button} size="xs" variant="ghost">Ghost</{Button}>
                <{Button} size="xs" variant="destructive">Destructive</{Button}>
                <{Button} size="xs" variant="link">Link</{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="sm">Default</{Button}>
                <{Button} size="sm" variant="secondary">Secondary</{Button}>
                <{Button} size="sm" variant="outline">Outline</{Button}>
                <{Button} size="sm" variant="ghost">Ghost</{Button}>
                <{Button} size="sm" variant="destructive">Destructive</{Button}>
                <{Button} size="sm" variant="link">Link</{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button}>Default</{Button}>
                <{Button} variant="secondary">Secondary</{Button}>
                <{Button} variant="outline">Outline</{Button}>
                <{Button} variant="ghost">Ghost</{Button}>
                <{Button} variant="destructive">Destructive</{Button}>
                <{Button} variant="link">Link</{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="lg">Default</{Button}>
                <{Button} size="lg" variant="secondary">Secondary</{Button}>
                <{Button} size="lg" variant="outline">Outline</{Button}>
                <{Button} size="lg" variant="ghost">Ghost</{Button}>
                <{Button} size="lg" variant="destructive">Destructive</{Button}>
                <{Button} size="lg" variant="link">Link</{Button}>
            </div>
        </{Example}>
    """


def ButtonIconRight():
    return t"""
        <{Example} title="Icon Right">
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="xs">
                    Default{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="xs" variant="secondary">
                    Secondary{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="xs" variant="outline">
                    Outline{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="xs" variant="ghost">
                    Ghost{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="xs" variant="destructive">
                    Destructive{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="xs" variant="link">
                    Link{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="sm">
                    Default
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="sm" variant="secondary">
                    Secondary{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="sm" variant="outline">
                    Outline{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="sm" variant="ghost">
                    Ghost{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="sm" variant="destructive">
                    Destructive{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="sm" variant="link">
                    Link{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button}>
                    Default{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} variant="secondary">
                    Secondary{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} variant="outline">
                    Outline{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} variant="ghost">
                    Ghost{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} variant="destructive">
                    Destructive{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} variant="link">
                    Link{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="lg">
                    Default{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="lg" variant="secondary">
                    Secondary{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="lg" variant="outline">
                    Outline{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="lg" variant="ghost">
                    Ghost{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="lg" variant="destructive">
                    Destructive{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
                <{Button} size="lg" variant="link">
                    Link{" "}
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
            </div>
        </{Example}>
    """


def ButtonIconLeft():
    return t"""
        <{Example} title="Icon Left">
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="xs">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Default
                </{Button}>
                <{Button} size="xs" variant="secondary">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Secondary
                </{Button}>
                <{Button} size="xs" variant="outline">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Outline
                </{Button}>
                <{Button} size="xs" variant="ghost">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Ghost
                </{Button}>
                <{Button} size="xs" variant="destructive">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Destructive
                </{Button}>
                <{Button} size="xs" variant="link">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Link
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="sm">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Default
                </{Button}>
                <{Button} size="sm" variant="secondary">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Secondary
                </{Button}>
                <{Button} size="sm" variant="outline">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Outline
                </{Button}>
                <{Button} size="sm" variant="ghost">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Ghost
                </{Button}>
                <{Button} size="sm" variant="destructive">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Destructive
                </{Button}>
                <{Button} size="sm" variant="link">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Link
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button}>
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Default
                </{Button}>
                <{Button} variant="secondary">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Secondary
                </{Button}>
                <{Button} variant="outline">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Outline
                </{Button}>
                <{Button} variant="ghost">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Ghost
                </{Button}>
                <{Button} variant="destructive">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Destructive
                </{Button}>
                <{Button} variant="link">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Link
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="lg">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Default
                </{Button}>
                <{Button} size="lg" variant="secondary">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Secondary
                </{Button}>
                <{Button} size="lg" variant="outline">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Outline
                </{Button}>
                <{Button} size="lg" variant="ghost">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Ghost
                </{Button}>
                <{Button} size="lg" variant="destructive">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Destructive
                </{Button}>
                <{Button} size="lg" variant="link">
                    <{ArrowLeftCircleIcon} data-icon="inline-start" />
                    {" "}
                    Link
                </{Button}>
            </div>
        </{Example}>
    """


def ButtonIconOnly():
    return t"""
        <{Example} title="Icon Only">
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="icon-xs">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-xs" variant="secondary">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-xs" variant="outline">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-xs" variant="ghost">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-xs" variant="destructive">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-xs" variant="link">
                    <{ArrowRightIcon} />
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="icon-sm">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-sm" variant="secondary">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-sm" variant="outline">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-sm" variant="ghost">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-sm" variant="destructive">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-sm" variant="link">
                    <{ArrowRightIcon} />
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="icon">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon" variant="secondary">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon" variant="outline">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon" variant="ghost">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon" variant="destructive">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon" variant="link">
                    <{ArrowRightIcon} />
                </{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="icon-lg">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-lg" variant="secondary">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-lg" variant="outline">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-lg" variant="ghost">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-lg" variant="destructive">
                    <{ArrowRightIcon} />
                </{Button}>
                <{Button} size="icon-lg" variant="link">
                    <{ArrowRightIcon} />
                </{Button}>
            </div>
        </{Example}>
    """


def ButtonExamples():
    return t"""
        <{Example} title="Examples">
            <div class="flex flex-wrap items-center gap-4">
                <div class="flex items-center gap-2">
                    <{Button} variant="outline">Cancel</{Button}>
                    <{Button}>
                        Submit{" "}
                        <{ArrowRightIcon} data-icon="inline-end" />
                    </{Button}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} variant="destructive">Delete</{Button}>
                    <{Button} size="icon">
                        <{ArrowRightIcon} data-icon="inline-end" />
                    </{Button}>
                </div>
            </div>
        </{Example}>
    """


def ButtonInvalidStates():
    return t"""
        <{Example} title="Invalid States">
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="xs" aria-invalid="true">Default</{Button}>
                <{Button} size="xs" variant="secondary" aria-invalid="true">Secondary</{Button}>
                <{Button} size="xs" variant="outline" aria-invalid="true">Outline</{Button}>
                <{Button} size="xs" variant="ghost" aria-invalid="true">Ghost</{Button}>
                <{Button} size="xs" variant="destructive" aria-invalid="true">Destructive</{Button}>
                <{Button} size="xs" variant="link" aria-invalid="true">Link</{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="sm" aria-invalid="true">Default</{Button}>
                <{Button} size="sm" variant="secondary" aria-invalid="true">Secondary</{Button}>
                <{Button} size="sm" variant="outline" aria-invalid="true">Outline</{Button}>
                <{Button} size="sm" variant="ghost" aria-invalid="true">Ghost</{Button}>
                <{Button} size="sm" variant="destructive" aria-invalid="true">Destructive</{Button}>
                <{Button} size="sm" variant="link" aria-invalid="true">Link</{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} aria-invalid="true">Default</{Button}>
                <{Button} variant="secondary" aria-invalid="true">Secondary</{Button}>
                <{Button} variant="outline" aria-invalid="true">Outline</{Button}>
                <{Button} variant="ghost" aria-invalid="true">Ghost</{Button}>
                <{Button} variant="destructive" aria-invalid="true">Destructive</{Button}>
                <{Button} variant="link" aria-invalid="true">Link</{Button}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Button} size="lg" aria-invalid="true">Default</{Button}>
                <{Button} size="lg" variant="secondary" aria-invalid="true">Secondary</{Button}>
                <{Button} size="lg" variant="outline" aria-invalid="true">Outline</{Button}>
                <{Button} size="lg" variant="ghost" aria-invalid="true">Ghost</{Button}>
                <{Button} size="lg" variant="destructive" aria-invalid="true">Destructive</{Button}>
                <{Button} size="lg" variant="link" aria-invalid="true">Link</{Button}>
            </div>
        </{Example}>
    """
