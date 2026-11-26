from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from field import Field, FieldGroup, FieldLabel
from input import Input
from popover import Popover, PopoverDescription, PopoverHeader, PopoverTitle, PopoverTrigger


def PopoverExample():
    return t"""
        <{ExampleWrapper}>
            <{PopoverBasic} />
            <{PopoverSides} />
            <{PopoverWithForm} />
            <{PopoverAlignments} />
            <{PopoverInDialog} />
        </{ExampleWrapper}>
    """


def PopoverBasic():
    return t"""
        <{Example} title="Basic">
            <{PopoverTrigger}>
                <{Button} variant="outline" class="w-fit">Open Popover</{Button}>
                <{Popover} placement="bottom start">
                    <{PopoverHeader}>
                        <{PopoverTitle}>Dimensions</{PopoverTitle}>
                        <{PopoverDescription}>Set the dimensions for the layer.</{PopoverDescription}>
                    </{PopoverHeader}>
                </{Popover}>
            </{PopoverTrigger}>
        </{Example}>
    """


def PopoverSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-col gap-2">
                <div class="flex flex-wrap gap-2">
                    {[t'''
                        <{PopoverTrigger} key={placement}>
                            <{Button} variant="outline" class="w-fit capitalize">{placement}</{Button}>
                            <{Popover} placement={placement} class="w-40">
                                <p>Popover on {placement}</p>
                            </{Popover}>
                        </{PopoverTrigger}>
                    ''' for placement in ["start", "left", "top"]]}
                </div>
                <div class="flex flex-wrap gap-2">
                    {[t'''
                        <{PopoverTrigger} key={placement}>
                            <{Button} variant="outline" class="w-fit capitalize">{placement}</{Button}>
                            <{Popover} placement={placement} class="w-40">
                                <p>Popover on {placement}</p>
                            </{Popover}>
                        </{PopoverTrigger}>
                    ''' for placement in ["bottom", "right", "end"]]}
                </div>
            </div>
        </{Example}>
    """


def PopoverWithForm():
    return t"""
        <{Example} title="With Form">
            <{PopoverTrigger}>
                <{Button} variant="outline">Open Popover</{Button}>
                <{Popover} class="w-64" placement="bottom start">
                    <{PopoverHeader}>
                        <{PopoverTitle}>Dimensions</{PopoverTitle}>
                        <{PopoverDescription}>Set the dimensions for the layer.</{PopoverDescription}>
                    </{PopoverHeader}>
                    <{FieldGroup} class="gap-4">
                        <{Field} orientation="horizontal">
                            <{FieldLabel} for="width" class="w-1/2">Width</{FieldLabel}>
                            <{Input} id="width" defaultValue="100%" />
                        </{Field}>
                        <{Field} orientation="horizontal">
                            <{FieldLabel} for="height" class="w-1/2">Height</{FieldLabel}>
                            <{Input} id="height" defaultValue="25px" />
                        </{Field}>
                    </{FieldGroup}>
                </{Popover}>
            </{PopoverTrigger}>
        </{Example}>
    """


def PopoverAlignments():
    return t"""
        <{Example} title="Alignments">
            <div class="flex gap-6">
                <{PopoverTrigger}>
                    <{Button} variant="outline" size="sm">Start</{Button}>
                    <{Popover} placement="bottom start" class="w-40">Aligned to start</{Popover}>
                </{PopoverTrigger}>
                <{PopoverTrigger}>
                    <{Button} variant="outline" size="sm">Center</{Button}>
                    <{Popover} placement="bottom" class="w-40">Aligned to center</{Popover}>
                </{PopoverTrigger}>
                <{PopoverTrigger}>
                    <{Button} variant="outline" size="sm">End</{Button}>
                    <{Popover} placement="bottom end" class="w-40">Aligned to end</{Popover}>
                </{PopoverTrigger}>
            </div>
        </{Example}>
    """


def PopoverInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{DialogTrigger}>
                <{Button} variant="outline">Open Dialog</{Button}>
                <{Dialog}>
                    <{DialogHeader}>
                        <{DialogTitle}>Popover Example</{DialogTitle}>
                        <{DialogDescription}>Click the button below to see the popover.</{DialogDescription}>
                    </{DialogHeader}>
                    <{PopoverTrigger}>
                        <{Button} variant="outline" class="w-fit">Open Popover</{Button}>
                        <{Popover} placement="bottom start">
                            <{PopoverHeader}>
                                <{PopoverTitle}>Popover in Dialog</{PopoverTitle}>
                                <{PopoverDescription}>
                                    This popover appears inside a dialog. Click the button to open it.
                                </{PopoverDescription}>
                            </{PopoverHeader}>
                        </{Popover}>
                    </{PopoverTrigger}>
                </{Dialog}>
            </{DialogTrigger}>
        </{Example}>
    """
