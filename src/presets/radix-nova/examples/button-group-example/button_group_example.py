from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from button_group import ButtonGroup, ButtonGroupText
from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from field import Field, FieldGroup
from input import Input
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from label import Label
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from tooltip import Tooltip, TooltipContent, TooltipTrigger

__js__ = {
    "lucide-react": [
        "ChevronDownIcon",
        "VolumeOffIcon",
        "CheckIcon",
        "AlertTriangleIcon",
        "UserRoundXIcon",
        "ShareIcon",
        "CopyIcon",
        "TrashIcon",
        "ArrowRightIcon",
        "FlipHorizontalIcon",
        "FlipVerticalIcon",
        "RotateCwIcon",
        "SearchIcon",
        "MinusIcon",
        "PlusIcon",
        "HeartIcon",
        "AudioLinesIcon",
        "ArrowLeftIcon",
    ],
}


def ButtonGroupExample():
    return t"""
        <{ExampleWrapper}>
            <{ButtonGroupBasic} />
            <{ButtonGroupWithInput} />
            <{ButtonGroupWithText} />
            <{ButtonGroupWithDropdown} />
            <{ButtonGroupWithSelect} />
            <{ButtonGroupWithIcons} />
            <{ButtonGroupWithInputGroup} />
            <{ButtonGroupWithFields} />
            <{ButtonGroupWithLike} />
            <{ButtonGroupWithSelectAndInput} />
            <{ButtonGroupNested} />
            <{ButtonGroupPagination} />
            <{ButtonGroupPaginationSplit} />
            <{ButtonGroupNavigation} />
            <{ButtonGroupTextAlignment} />
            <{ButtonGroupVertical} />
            <{ButtonGroupVerticalNested} />
        </{ExampleWrapper}>
    """


def ButtonGroupBasic():
    return t"""
        <{Example} title="Basic">
            <div class="flex flex-col gap-4">
                <{ButtonGroup}>
                    <{Button} variant="outline">Button</{Button}>
                    <{Button} variant="outline">Another Button</{Button}>
                </{ButtonGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupWithInput():
    return t"""
        <{Example} title="With Input">
            <div class="flex flex-col gap-4">
                <{ButtonGroup}>
                    <{Button} variant="outline">Button</{Button}>
                    <{Input} placeholder="Type something here..." />
                </{ButtonGroup}>
                <{ButtonGroup}>
                    <{Input} placeholder="Type something here..." />
                    <{Button} variant="outline">Button</{Button}>
                </{ButtonGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupWithText():
    return t"""
        <{Example} title="With Text">
            <div class="flex flex-col gap-4">
                <{ButtonGroup}>
                    <{ButtonGroupText}>Text</{ButtonGroupText}>
                    <{Button} variant="outline">Another Button</{Button}>
                </{ButtonGroup}>
                <{ButtonGroup}>
                    <{ButtonGroupText} asChild>
                        <{Label} for="input-text">GPU Size</{Label}>
                    </{ButtonGroupText}>
                    <{Input} id="input-text" placeholder="Type something here..." class="style-luma:border-border" />
                </{ButtonGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupWithDropdown():
    return t"""
        <{Example} title="With Dropdown">
            <div class="flex flex-col gap-4">
                <{ButtonGroup}>
                    <{Button} variant="outline">Update</{Button}>
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} asChild>
                            <{Button} variant="outline" size="icon">
                                <{ChevronDownIcon} />
                            </{Button}>
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent} align="end">
                            <{DropdownMenuItem}>Disable</{DropdownMenuItem}>
                            <{DropdownMenuItem} variant="destructive">Uninstall</{DropdownMenuItem}>
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                </{ButtonGroup}>
                <{ButtonGroup}>
                    <{Button} variant="outline">Follow</{Button}>
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} asChild>
                            <{Button} variant="outline" size="icon">
                                <{ChevronDownIcon} />
                            </{Button}>
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent} align="end" class="w-50">
                            <{DropdownMenuGroup}>
                                <{DropdownMenuItem}>
                                    <{VolumeOffIcon} />
                                    Mute Conversation
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{CheckIcon} />
                                    Mark as Read
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{AlertTriangleIcon} />
                                    Report Conversation
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{UserRoundXIcon} />
                                    Block User
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{ShareIcon} />
                                    Share Conversation
                                </{DropdownMenuItem}>
                                <{DropdownMenuItem}>
                                    <{CopyIcon} />
                                    Copy Conversation
                                </{DropdownMenuItem}>
                            </{DropdownMenuGroup}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuGroup}>
                                <{DropdownMenuItem} variant="destructive">
                                    <{TrashIcon} />
                                    Delete Conversation
                                </{DropdownMenuItem}>
                            </{DropdownMenuGroup}>
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                </{ButtonGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupWithSelect():
    currency, set_currency = use_state("$")

    return t"""
        <{Example} title="With Select">
            <{Field}>
                <{Label} for="amount">Amount</{Label}>
                <{ButtonGroup}>
                    <{Select} value={currency} onValueChange={set_currency}>
                        <{SelectTrigger}>
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent} align="start">
                            <{SelectGroup}>
                                <{SelectItem} value="$">$</{SelectItem}>
                                <{SelectItem} value="€">€</{SelectItem}>
                                <{SelectItem} value="£">£</{SelectItem}>
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                    <{Input} placeholder="Enter amount to send" />
                    <{Button} variant="outline">
                        <{ArrowRightIcon} />
                    </{Button}>
                </{ButtonGroup}>
            </{Field}>
        </{Example}>
    """


def ButtonGroupWithIcons():
    return t"""
        <{Example} title="With Icons">
            <div class="flex flex-col gap-4">
                <{ButtonGroup}>
                    <{Button} variant="outline">
                        <{FlipHorizontalIcon} />
                    </{Button}>
                    <{Button} variant="outline">
                        <{FlipVerticalIcon} />
                    </{Button}>
                    <{Button} variant="outline">
                        <{RotateCwIcon} />
                    </{Button}>
                </{ButtonGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupWithInputGroup():
    return t"""
        <{Example} title="With Input Group">
            <div class="flex flex-col gap-4">
                <{InputGroup}>
                    <{InputGroupInput} placeholder="Type to search..." />
                    <{InputGroupAddon} align="inline-start" class="text-muted-foreground">
                        <{SearchIcon} />
                    </{InputGroupAddon}>
                </{InputGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupWithFields():
    return t"""
        <{Example} title="With Fields">
            <{FieldGroup} class="grid grid-cols-3 gap-4">
                <{Field} class="col-span-2">
                    <{Label} for="width">Width</{Label}>
                    <{ButtonGroup}>
                        <{InputGroup}>
                            <{InputGroupInput} id="width" />
                            <{InputGroupAddon} class="text-muted-foreground">W</{InputGroupAddon}>
                            <{InputGroupAddon} align="inline-end" class="text-muted-foreground">px</{InputGroupAddon}>
                        </{InputGroup}>
                        <{Button} variant="outline" size="icon">
                            <{MinusIcon} />
                        </{Button}>
                        <{Button} variant="outline" size="icon">
                            <{PlusIcon} />
                        </{Button}>
                    </{ButtonGroup}>
                </{Field}>
            </{FieldGroup}>
        </{Example}>
    """


def ButtonGroupWithLike():
    return t"""
        <{Example} title="With Like">
            <{ButtonGroup}>
                <{Button} variant="outline">
                    <{HeartIcon} data-icon="inline-start" />
                    {" "}
                    Like
                </{Button}>
                <{Button} variant="outline" asChild size="icon" class="w-12">
                    <span>1.2K</span>
                </{Button}>
            </{ButtonGroup}>
        </{Example}>
    """


def ButtonGroupWithSelectAndInput():
    return t"""
        <{Example} title="With Select and Input">
            <{ButtonGroup}>
                <{Select} defaultValue="hours">
                    <{SelectTrigger} id="duration">
                        <{SelectValue} placeholder="Select duration" />
                    </{SelectTrigger}>
                    <{SelectContent} align="start">
                        <{SelectGroup}>
                            <{SelectItem} value="hours">Hours</{SelectItem}>
                            <{SelectItem} value="days">Days</{SelectItem}>
                            <{SelectItem} value="weeks">Weeks</{SelectItem}>
                        </{SelectGroup}>
                    </{SelectContent}>
                </{Select}>
                <{Input} />
            </{ButtonGroup}>
        </{Example}>
    """


def ButtonGroupNested():
    return t"""
        <{Example} title="Nested">
            <{ButtonGroup}>
                <{ButtonGroup}>
                    <{Button} variant="outline" size="icon">
                        <{PlusIcon} />
                    </{Button}>
                </{ButtonGroup}>
                <{ButtonGroup}>
                    <{InputGroup}>
                        <{InputGroupInput} placeholder="Send a message..." />
                        <{Tooltip}>
                            <{TooltipTrigger} asChild>
                                <{InputGroupAddon} align="inline-end">
                                    <{AudioLinesIcon} />
                                </{InputGroupAddon}>
                            </{TooltipTrigger}>
                            <{TooltipContent}>Voice Mode</{TooltipContent}>
                        </{Tooltip}>
                    </{InputGroup}>
                </{ButtonGroup}>
            </{ButtonGroup}>
        </{Example}>
    """


def ButtonGroupPagination():
    return t"""
        <{Example} title="Pagination">
            <{ButtonGroup}>
                <{Button} variant="outline" size="sm">
                    <{ArrowLeftIcon} data-icon="inline-start" />
                    Previous
                </{Button}>
                <{Button} variant="outline" size="sm">1</{Button}>
                <{Button} variant="outline" size="sm">2</{Button}>
                <{Button} variant="outline" size="sm">3</{Button}>
                <{Button} variant="outline" size="sm">4</{Button}>
                <{Button} variant="outline" size="sm">5</{Button}>
                <{Button} variant="outline" size="sm">
                    Next
                    <{ArrowRightIcon} data-icon="inline-end" />
                </{Button}>
            </{ButtonGroup}>
        </{Example}>
    """


def ButtonGroupPaginationSplit():
    return t"""
        <{Example} title="Pagination Split">
            <{ButtonGroup}>
                <{ButtonGroup}>
                    <{Button} variant="outline" size="sm">1</{Button}>
                    <{Button} variant="outline" size="sm">2</{Button}>
                    <{Button} variant="outline" size="sm">3</{Button}>
                    <{Button} variant="outline" size="sm">4</{Button}>
                    <{Button} variant="outline" size="sm">5</{Button}>
                </{ButtonGroup}>
                <{ButtonGroup}>
                    <{Button} variant="outline" size="icon-xs">
                        <{ArrowLeftIcon} />
                    </{Button}>
                    <{Button} variant="outline" size="icon-xs">
                        <{ArrowRightIcon} />
                    </{Button}>
                </{ButtonGroup}>
            </{ButtonGroup}>
        </{Example}>
    """


def ButtonGroupNavigation():
    return t"""
        <{Example} title="Navigation">
            <{ButtonGroup}>
                <{ButtonGroup}>
                    <{Button} variant="outline">
                        <{ArrowLeftIcon} />
                    </{Button}>
                    <{Button} variant="outline">
                        <{ArrowRightIcon} />
                    </{Button}>
                </{ButtonGroup}>
                <{ButtonGroup} aria-label="Single navigation button">
                    <{Button} variant="outline" size="icon">
                        <{ArrowLeftIcon} />
                    </{Button}>
                </{ButtonGroup}>
            </{ButtonGroup}>
        </{Example}>
    """


def ButtonGroupTextAlignment():
    return t"""
        <{Example} title="Text Alignment">
            <{Field}>
                <{Label} id="alignment-label">Text Alignment</{Label}>
                <{ButtonGroup} aria-labelledby="alignment-label">
                    <{Button} variant="outline" size="sm">Left</{Button}>
                    <{Button} variant="outline" size="sm">Center</{Button}>
                    <{Button} variant="outline" size="sm">Right</{Button}>
                    <{Button} variant="outline" size="sm">Justify</{Button}>
                </{ButtonGroup}>
            </{Field}>
        </{Example}>
    """


def ButtonGroupVertical():
    return t"""
        <{Example} title="Vertical">
            <div class="flex gap-6">
                <{ButtonGroup} orientation="vertical" aria-label="Media controls" class="h-fit">
                    <{Button} variant="outline" size="icon">
                        <{PlusIcon} />
                    </{Button}>
                    <{Button} variant="outline" size="icon">
                        <{MinusIcon} />
                    </{Button}>
                </{ButtonGroup}>
            </div>
        </{Example}>
    """


def ButtonGroupVerticalNested():
    return t"""
        <{Example} title="Vertical Nested">
            <{ButtonGroup} orientation="vertical" aria-label="Design tools palette">
                <{ButtonGroup} orientation="vertical">
                    <{Button} variant="outline" size="icon">
                        <{SearchIcon} />
                    </{Button}>
                    <{Button} variant="outline" size="icon">
                        <{CopyIcon} />
                    </{Button}>
                    <{Button} variant="outline" size="icon">
                        <{ShareIcon} />
                    </{Button}>
                </{ButtonGroup}>
                <{ButtonGroup} orientation="vertical">
                    <{Button} variant="outline" size="icon">
                        <{FlipHorizontalIcon} />
                    </{Button}>
                    <{Button} variant="outline" size="icon">
                        <{FlipVerticalIcon} />
                    </{Button}>
                    <{Button} variant="outline" size="icon">
                        <{RotateCwIcon} />
                    </{Button}>
                </{ButtonGroup}>
                <{ButtonGroup}>
                    <{Button} variant="outline" size="icon">
                        <{TrashIcon} />
                    </{Button}>
                </{ButtonGroup}>
            </{ButtonGroup}>
        </{Example}>
    """
