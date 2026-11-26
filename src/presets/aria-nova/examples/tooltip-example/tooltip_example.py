from example import Example, ExampleWrapper
from button import Button
from kbd import Kbd
from tooltip import Tooltip, TooltipTrigger

__js__ = {"react-aria-components": ["Link"], "lucide-react": ["InfoIcon", "SaveIcon"]}


def TooltipExample():
    return t"""
        <{ExampleWrapper}>
            <{TooltipBasic} />
            <{TooltipSides} />
            <{TooltipWithIcon} />
            <{TooltipLongContent} />
            <{TooltipDisabled} />
            <{TooltipWithKeyboard} />
            <{TooltipOnLink} />
            <{TooltipFormatted} />
        </{ExampleWrapper}>
    """


def TooltipBasic():
    return t"""
        <{Example} title="Basic">
            <{TooltipTrigger}>
                <{Button} variant="outline" class="w-fit">Show Tooltip</{Button}>
                <{Tooltip}>
                    <p>Add to library</p>
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """


def TooltipSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-wrap gap-2">
                {[t'''
                    <{TooltipTrigger} key={placement}>
                        <{Button} variant="outline" class="w-fit capitalize">{placement}</{Button}>
                        <{Tooltip} placement={placement}>
                            <p>Add to library</p>
                        </{Tooltip}>
                    </{TooltipTrigger}>
                ''' for placement in ["start", "left", "top", "bottom", "right", "end"]]}
            </div>
        </{Example}>
    """


def TooltipWithIcon():
    return t"""
        <{Example} title="With Icon">
            <{TooltipTrigger}>
                <{Button} variant="ghost" size="icon">
                    <{InfoIcon} />
                    <span class="sr-only">Info</span>
                </{Button}>
                <{Tooltip}>
                    <p>Additional information</p>
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """


def TooltipLongContent():
    return t"""
        <{Example} title="Long Content">
            <{TooltipTrigger}>
                <{Button} variant="outline" class="w-fit">Show Tooltip</{Button}>
                <{Tooltip}>
                    To learn more about how this works, check out the docs. If you have any questions, please reach out to us.
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """


def TooltipDisabled():
    return t"""
        <{Example} title="Disabled">
            <{TooltipTrigger}>
                <span class="inline-block w-fit">
                    <{Button} variant="outline" isDisabled>Disabled</{Button}>
                </span>
                <{Tooltip}>
                    <p>This feature is currently unavailable</p>
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """


def TooltipWithKeyboard():
    return t"""
        <{Example} title="With Keyboard Shortcut">
            <{TooltipTrigger}>
                <{Button} variant="outline" size="icon-sm">
                    <{SaveIcon} />
                </{Button}>
                <{Tooltip}>
                    Save Changes <{Kbd}>S</{Kbd}>
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """


def TooltipOnLink():
    return t"""
        <{Example} title="On Link">
            <{TooltipTrigger}>
                <{Link}
                    href="#"
                    class="w-fit text-sm text-primary underline-offset-4 hover:underline"
                    onClick={(lambda e: e.preventDefault())}
                >
                    Learn more
                </{Link}>
                <{Tooltip}>
                    <p>Click to read the documentation</p>
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """


def TooltipFormatted():
    return t"""
        <{Example} title="Formatted Content">
            <{TooltipTrigger}>
                <{Button} variant="outline" class="w-fit">Status</{Button}>
                <{Tooltip}>
                    <div class="flex flex-col gap-1">
                        <p class="font-semibold">Active</p>
                        <p class="text-xs opacity-80">Last updated 2 hours ago</p>
                    </div>
                </{Tooltip}>
            </{TooltipTrigger}>
        </{Example}>
    """
