from example import Example, ExampleWrapper
from button import Button
from kbd import Kbd
from tooltip import Tooltip, TooltipContent, TooltipTrigger

__js__ = {"lucide-react": ["InfoIcon", "SaveIcon"]}


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
            <{Tooltip}>
                <{TooltipTrigger} render={t'<{Button} variant="outline" class="w-fit" />'}>
                    Show Tooltip
                </{TooltipTrigger}>
                <{TooltipContent}>
                    <p>Add to library</p>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def TooltipSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-wrap gap-2">
                {[t'''
                    <{Tooltip} key={side}>
                        <{TooltipTrigger} render={t"""<{Button} variant="outline" class="w-fit capitalize" />"""}>
                            {side.replace("-", " ")}
                        </{TooltipTrigger}>
                        <{TooltipContent} side={side}>
                            <p>Add to library</p>
                        </{TooltipContent}>
                    </{Tooltip}>
                ''' for side in ["inline-start", "left", "top", "bottom", "right", "inline-end"]]}
            </div>
        </{Example}>
    """


def TooltipWithIcon():
    return t"""
        <{Example} title="With Icon">
            <{Tooltip}>
                <{TooltipTrigger} render={t'<{Button} variant="ghost" size="icon" />'}>
                    <{InfoIcon} />
                    <span class="sr-only">Info</span>
                </{TooltipTrigger}>
                <{TooltipContent}>
                    <p>Additional information</p>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def TooltipLongContent():
    return t"""
        <{Example} title="Long Content">
            <{Tooltip}>
                <{TooltipTrigger} render={t'<{Button} variant="outline" class="w-fit" />'}>
                    Show Tooltip
                </{TooltipTrigger}>
                <{TooltipContent}>
                    To learn more about how this works, check out the docs. If you have any questions, please reach out to us.
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def TooltipDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Tooltip}>
                <{TooltipTrigger} render={t'<span class="inline-block w-fit" />'}>
                    <{Button} variant="outline" disabled>Disabled</{Button}>
                </{TooltipTrigger}>
                <{TooltipContent}>
                    <p>This feature is currently unavailable</p>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def TooltipWithKeyboard():
    return t"""
        <{Example} title="With Keyboard Shortcut">
            <{Tooltip}>
                <{TooltipTrigger} render={t'<{Button} variant="outline" size="icon-sm" />'}>
                    <{SaveIcon} />
                </{TooltipTrigger}>
                <{TooltipContent}>
                    Save Changes <{Kbd}>S</{Kbd}>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def TooltipOnLink():
    return t"""
        <{Example} title="On Link">
            <{Tooltip}>
                <{TooltipTrigger} render={t'''
                    <a
                        href="#"
                        class="w-fit text-sm text-primary underline-offset-4 hover:underline"
                        onClick={(lambda e: e.preventDefault())}
                    />
                '''}>
                    Learn more
                </{TooltipTrigger}>
                <{TooltipContent}>
                    <p>Click to read the documentation</p>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """


def TooltipFormatted():
    return t"""
        <{Example} title="Formatted Content">
            <{Tooltip}>
                <{TooltipTrigger} render={t'<{Button} variant="outline" class="w-fit" />'}>Status</{TooltipTrigger}>
                <{TooltipContent}>
                    <div class="flex flex-col gap-1">
                        <p class="font-semibold">Active</p>
                        <p class="text-xs opacity-80">Last updated 2 hours ago</p>
                    </div>
                </{TooltipContent}>
            </{Tooltip}>
        </{Example}>
    """
