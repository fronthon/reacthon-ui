from example import Example, ExampleWrapper
from button import Button
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from kbd import Kbd, KbdGroup
from tooltip import Tooltip, TooltipContent, TooltipTrigger

__js__ = {"lucide-react": ["CircleDashedIcon", "ArrowLeftIcon", "ArrowRightIcon", "SaveIcon"]}


def KbdExample():
    return t"""
        <{ExampleWrapper}>
            <{KbdBasic} />
            <{KbdModifierKeys} />
            <{KbdGroupExample} />
            <{KbdArrowKeys} />
            <{KbdWithIcons} />
            <{KbdWithIconsAndText} />
            <{KbdInInputGroup} />
            <{KbdInTooltip} />
            <{KbdWithSamp} />
        </{ExampleWrapper}>
    """


def KbdBasic():
    return t"""
        <{Example} title="Basic">
            <div class="flex items-center gap-2">
                <{Kbd}>Ctrl</{Kbd}>
                <{Kbd}>⌘K</{Kbd}>
                <{Kbd}>Ctrl + B</{Kbd}>
            </div>
        </{Example}>
    """


def KbdModifierKeys():
    return t"""
        <{Example} title="Modifier Keys">
            <div class="flex items-center gap-2">
                <{Kbd}>⌘</{Kbd}>
                <{Kbd}>C</{Kbd}>
            </div>
        </{Example}>
    """


def KbdGroupExample():
    return t"""
        <{Example} title="KbdGroup">
            <{KbdGroup}>
                <{Kbd}>Ctrl</{Kbd}>
                <{Kbd}>Shift</{Kbd}>
                <{Kbd}>P</{Kbd}>
            </{KbdGroup}>
        </{Example}>
    """


def KbdArrowKeys():
    return t"""
        <{Example} title="Arrow Keys">
            <div class="flex items-center gap-2">
                <{Kbd}>↑</{Kbd}>
                <{Kbd}>↓</{Kbd}>
                <{Kbd}>←</{Kbd}>
                <{Kbd}>→</{Kbd}>
            </div>
        </{Example}>
    """


def KbdWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{KbdGroup}>
                <{Kbd}>
                    <{CircleDashedIcon} />
                </{Kbd}>
                <{Kbd}>
                    <{ArrowLeftIcon} />
                </{Kbd}>
                <{Kbd}>
                    <{ArrowRightIcon} />
                </{Kbd}>
            </{KbdGroup}>
        </{Example}>
    """


def KbdWithIconsAndText():
    return t"""
        <{Example} title="With Icons and Text">
            <{KbdGroup}>
                <{Kbd}>
                    <{ArrowLeftIcon} />
                    Left
                </{Kbd}>
                <{Kbd}>
                    <{CircleDashedIcon} />
                    Voice Enabled
                </{Kbd}>
            </{KbdGroup}>
        </{Example}>
    """


def KbdInInputGroup():
    return t"""
        <{Example} title="InputGroup">
            <{InputGroup}>
                <{InputGroupInput} />
                <{InputGroupAddon}>
                    <{Kbd}>Space</{Kbd}>
                </{InputGroupAddon}>
            </{InputGroup}>
        </{Example}>
    """


def KbdInTooltip():
    return t"""
        <{Example} title="Tooltip">
            <{Tooltip}>
                <{TooltipTrigger} render={t'<{Button} size="icon-sm" variant="outline" />'}>
                    <{SaveIcon} />
                </{TooltipTrigger}>
                <{TooltipContent} class="pr-1.5">
                    <div class="flex items-center gap-2">
                        Save Changes <{Kbd}>S</{Kbd}>
                    </div>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def KbdWithSamp():
    return t"""
        <{Example} title="With samp">
            <{Kbd}>
                <samp>File</samp>
            </{Kbd}>
        </{Example}>
    """
