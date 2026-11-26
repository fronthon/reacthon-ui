from example import Example, ExampleWrapper
from badge import Badge
from spinner import Spinner

__js__ = {"lucide-react": ["BadgeCheck", "ArrowRightIcon", "ArrowUpRightIcon"]}


def BadgeExample():
    return t"""
        <{ExampleWrapper} class="lg:grid-cols-1">
            <{BadgeVariants} />
            <{BadgeWithIconLeft} />
            <{BadgeWithIconRight} />
            <{BadgeWithSpinner} />
            <{BadgeAsLink} />
            <{BadgeLongText} />
            <{BadgeCustomColors} />
        </{ExampleWrapper}>
    """


def BadgeVariants():
    return t"""
        <{Example} title="Variants">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge}>Default</{Badge}>
                <{Badge} variant="secondary">Secondary</{Badge}>
                <{Badge} variant="destructive">Destructive</{Badge}>
                <{Badge} variant="outline">Outline</{Badge}>
                <{Badge} variant="ghost">Ghost</{Badge}>
                <{Badge} variant="link">Link</{Badge}>
            </div>
        </{Example}>
    """


def BadgeWithIconLeft():
    return t"""
        <{Example} title="Icon Left" class="max-w-fit">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge}>
                    <{BadgeCheck} data-icon="inline-start" />
                    Default
                </{Badge}>
                <{Badge} variant="secondary">
                    <{BadgeCheck} data-icon="inline-start" />
                    Secondary
                </{Badge}>
                <{Badge} variant="destructive">
                    <{BadgeCheck} data-icon="inline-start" />
                    Destructive
                </{Badge}>
                <{Badge} variant="outline">
                    <{BadgeCheck} data-icon="inline-start" />
                    Outline
                </{Badge}>
                <{Badge} variant="ghost">
                    <{BadgeCheck} data-icon="inline-start" />
                    Ghost
                </{Badge}>
                <{Badge} variant="link">
                    <{BadgeCheck} data-icon="inline-start" />
                    Link
                </{Badge}>
            </div>
        </{Example}>
    """


def BadgeWithIconRight():
    return t"""
        <{Example} title="Icon Right" class="max-w-fit">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge}>
                    Default
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Badge}>
                <{Badge} variant="secondary">
                    Secondary
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Badge}>
                <{Badge} variant="destructive">
                    Destructive
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Badge}>
                <{Badge} variant="outline">
                    Outline
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Badge}>
                <{Badge} variant="ghost">
                    Ghost
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Badge}>
                <{Badge} variant="link">
                    Link
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Badge}>
            </div>
        </{Example}>
    """


def BadgeWithSpinner():
    return t"""
        <{Example} title="With Spinner" class="max-w-fit">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge}>
                    <{Spinner} data-icon="inline-start" />
                    Default
                </{Badge}>
                <{Badge} variant="secondary">
                    <{Spinner} data-icon="inline-start" />
                    Secondary
                </{Badge}>
                <{Badge} variant="destructive">
                    <{Spinner} data-icon="inline-start" />
                    Destructive
                </{Badge}>
                <{Badge} variant="outline">
                    <{Spinner} data-icon="inline-start" />
                    Outline
                </{Badge}>
                <{Badge} variant="ghost">
                    <{Spinner} data-icon="inline-start" />
                    Ghost
                </{Badge}>
                <{Badge} variant="link">
                    <{Spinner} data-icon="inline-start" />
                    Link
                </{Badge}>
            </div>
        </{Example}>
    """


def BadgeAsLink():
    a = t"""
        <a href="#">
            Link{" "}
            <{ArrowUpRightIcon} data-icon="inline-end" />
        </a>
    """

    a_2 = t"""
        <a href="#">
            Link{" "}
            <{ArrowUpRightIcon} data-icon="inline-end" />
        </a>
    """

    a_3 = t"""
        <a href="#">
            Link{" "}
            <{ArrowUpRightIcon} data-icon="inline-end" />
        </a>
    """

    a_4 = t"""
        <a href="#">
            Link{" "}
            <{ArrowUpRightIcon} data-icon="inline-end" />
        </a>
    """

    return t"""
        <{Example} title="asChild">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge} render={a} />
                <{Badge} variant="secondary" render={a_2} />
                <{Badge} variant="destructive" render={a_3} />
                <{Badge} variant="ghost" render={a_4} />
            </div>
        </{Example}>
    """


def BadgeLongText():
    return t"""
        <{Example} title="Long Text">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge} variant="secondary">A badge with a lot of text to see how it wraps</{Badge}>
            </div>
        </{Example}>
    """


def BadgeCustomColors():
    return t"""
        <{Example} title="Custom Colors" class="max-w-fit">
            <div class="flex flex-wrap gap-2 style-sera:gap-6">
                <{Badge} class="bg-blue-600 text-blue-50 dark:bg-blue-600 dark:text-blue-50">Blue</{Badge}>
                <{Badge} class="bg-green-600 text-green-50 dark:bg-green-600 dark:text-green-50">Green</{Badge}>
                <{Badge} class="bg-sky-600 text-sky-50 dark:bg-sky-600 dark:text-sky-50">Sky</{Badge}>
                <{Badge} class="bg-purple-600 text-purple-50 dark:bg-purple-600 dark:text-purple-50">Purple</{Badge}>
                <{Badge} class="bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300">Blue</{Badge}>
                <{Badge} class="bg-green-50 text-green-700 dark:bg-green-950 dark:text-green-300">Green</{Badge}>
                <{Badge} class="bg-sky-50 text-sky-700 dark:bg-sky-950 dark:text-sky-300">Sky</{Badge}>
                <{Badge} class="bg-purple-50 text-purple-700 dark:bg-purple-950 dark:text-purple-300">Purple</{Badge}>
                <{Badge} class="bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300">Red</{Badge}>
            </div>
        </{Example}>
    """
