from example import Example, ExampleWrapper
from button import Button
from toggle import Toggle

__js__ = {"lucide-react": ["BoldIcon", "ItalicIcon", "UnderlineIcon", "BookmarkIcon"]}


def ToggleExample():
    return t"""
        <{ExampleWrapper}>
            <{ToggleBasic} />
            <{ToggleOutline} />
            <{ToggleSizes} />
            <{ToggleWithButtonText} />
            <{ToggleWithButtonIcon} />
            <{ToggleWithButtonIconText} />
            <{ToggleDisabled} />
            <{ToggleWithIcon} />
        </{ExampleWrapper}>
    """


def ToggleBasic():
    return t"""
        <{Example} title="Basic">
            <div class="flex flex-wrap items-center gap-2">
                <{Toggle} aria-label="Toggle bold" defaultPressed>
                    <{BoldIcon} />
                </{Toggle}>
                <{Toggle} aria-label="Toggle italic">
                    <{ItalicIcon} />
                </{Toggle}>
                <{Toggle} aria-label="Toggle underline">
                    <{UnderlineIcon} />
                </{Toggle}>
            </div>
        </{Example}>
    """


def ToggleOutline():
    return t"""
        <{Example} title="Outline">
            <div class="flex flex-wrap items-center gap-2">
                <{Toggle} variant="outline" aria-label="Toggle italic">
                    <{ItalicIcon} />
                    Italic
                </{Toggle}>
                <{Toggle} variant="outline" aria-label="Toggle bold">
                    <{BoldIcon} />
                    Bold
                </{Toggle}>
            </div>
        </{Example}>
    """


def ToggleSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-wrap items-center gap-2">
                <{Toggle} variant="outline" aria-label="Toggle small" size="sm">Small</{Toggle}>
                <{Toggle} variant="outline" aria-label="Toggle default" size="default">Default</{Toggle}>
                <{Toggle} variant="outline" aria-label="Toggle large" size="lg">Large</{Toggle}>
            </div>
        </{Example}>
    """


def ToggleWithButtonText():
    return t"""
        <{Example} title="With Button Text">
            <div class="flex flex-col gap-4">
                <div class="flex items-center gap-2">
                    <{Button} size="sm" variant="outline">Button</{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle sm" size="sm">Toggle</{Toggle}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} size="default" variant="outline">Button</{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle default" size="default">Toggle</{Toggle}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} size="lg" variant="outline">Button</{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle lg" size="lg">Toggle</{Toggle}>
                </div>
            </div>
        </{Example}>
    """


def ToggleWithButtonIcon():
    return t"""
        <{Example} title="With Button Icon">
            <div class="flex flex-col gap-4">
                <div class="flex items-center gap-2">
                    <{Button} variant="outline" size="icon-sm">
                        <{BoldIcon} />
                    </{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle sm icon" size="sm">
                        <{BoldIcon} />
                    </{Toggle}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} variant="outline" size="icon">
                        <{ItalicIcon} />
                    </{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle default icon" size="default">
                        <{ItalicIcon} />
                    </{Toggle}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} variant="outline" size="icon-lg">
                        <{UnderlineIcon} />
                    </{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle lg icon" size="lg">
                        <{UnderlineIcon} />
                    </{Toggle}>
                </div>
            </div>
        </{Example}>
    """


def ToggleWithButtonIconText():
    return t"""
        <{Example} title="With Button Icon + Text">
            <div class="flex flex-col gap-4">
                <div class="flex items-center gap-2">
                    <{Button} size="sm" variant="outline">
                        <{BoldIcon} data-icon="inline-start" />
                        Button
                    </{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle sm icon text" size="sm">
                        <{BoldIcon} />
                        Toggle
                    </{Toggle}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} size="default" variant="outline">
                        <{ItalicIcon} data-icon="inline-start" />
                        Button
                    </{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle default icon text" size="default">
                        <{ItalicIcon} />
                        Toggle
                    </{Toggle}>
                </div>
                <div class="flex items-center gap-2">
                    <{Button} size="lg" variant="outline">
                        <{UnderlineIcon} data-icon="inline-start" />
                        Button
                    </{Button}>
                    <{Toggle} variant="outline" aria-label="Toggle lg icon text" size="lg">
                        <{UnderlineIcon} />
                        Toggle
                    </{Toggle}>
                </div>
            </div>
        </{Example}>
    """


def ToggleDisabled():
    return t"""
        <{Example} title="Disabled">
            <div class="flex flex-wrap items-center gap-2">
                <{Toggle} aria-label="Toggle disabled" disabled>Disabled</{Toggle}>
                <{Toggle} variant="outline" aria-label="Toggle disabled outline" disabled>Disabled</{Toggle}>
            </div>
        </{Example}>
    """


def ToggleWithIcon():
    return t"""
        <{Example} title="With Icon">
            <div class="flex flex-wrap items-center gap-2">
                <{Toggle} aria-label="Toggle bookmark" defaultPressed>
                    <{BookmarkIcon} class="group-data-[state=on]/toggle:fill-accent-foreground" />
                </{Toggle}>
                <{Toggle} variant="outline" aria-label="Toggle bookmark outline">
                    <{BookmarkIcon} class="group-data-[state=on]/toggle:fill-accent-foreground" />
                    Bookmark
                </{Toggle}>
            </div>
        </{Example}>
    """
