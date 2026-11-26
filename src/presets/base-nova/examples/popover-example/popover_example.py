from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from field import Field, FieldGroup, FieldLabel
from input import Input
from popover import Popover, PopoverContent, PopoverDescription, PopoverHeader, PopoverTitle, PopoverTrigger


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
            <{Popover}>
                <{PopoverTrigger} render={t'<{Button} variant="outline" class="w-fit" />'}>
                    Open Popover
                </{PopoverTrigger}>
                <{PopoverContent} align="start">
                    <{PopoverHeader}>
                        <{PopoverTitle}>Dimensions</{PopoverTitle}>
                        <{PopoverDescription}>Set the dimensions for the layer.</{PopoverDescription}>
                    </{PopoverHeader}>
                </{PopoverContent}>
            </{Popover}>
        </{Example}>
    """


def PopoverSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-col gap-2">
                <div class="flex flex-wrap gap-2">
                    {[t'''
                        <{Popover} key={side}>
                            <{PopoverTrigger} render={t"""<{Button} variant="outline" class="w-fit capitalize" />"""}>
                                {side.replace("-", " ")}
                            </{PopoverTrigger}>
                            <{PopoverContent} side={side} class="w-40">
                                <p>Popover on {side.replace("-", " ")}</p>
                            </{PopoverContent}>
                        </{Popover}>
                    ''' for side in ["inline-start", "left", "top"]]}
                </div>
                <div class="flex flex-wrap gap-2">
                    {[t'''
                        <{Popover} key={side}>
                            <{PopoverTrigger} render={t"""<{Button} variant="outline" class="w-fit capitalize" />"""}>
                                {side.replace("-", " ")}
                            </{PopoverTrigger}>
                            <{PopoverContent} side={side} class="w-40">
                                <p>Popover on {side.replace("-", " ")}</p>
                            </{PopoverContent}>
                        </{Popover}>
                    ''' for side in ["bottom", "right", "inline-end"]]}
                </div>
            </div>
        </{Example}>
    """


def PopoverWithForm():
    return t"""
        <{Example} title="With Form">
            <{Popover}>
                <{PopoverTrigger} render={t'<{Button} variant="outline" />'}>Open Popover</{PopoverTrigger}>
                <{PopoverContent} class="w-64" align="start">
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
                </{PopoverContent}>
            </{Popover}>
        </{Example}>
    """


def PopoverAlignments():
    return t"""
        <{Example} title="Alignments">
            <div class="flex gap-6">
                <{Popover}>
                    <{PopoverTrigger} render={t'<{Button} variant="outline" size="sm" />'}>Start</{PopoverTrigger}>
                    <{PopoverContent} align="start" class="w-40">Aligned to start</{PopoverContent}>
                </{Popover}>
                <{Popover}>
                    <{PopoverTrigger} render={t'<{Button} variant="outline" size="sm" />'}>Center</{PopoverTrigger}>
                    <{PopoverContent} align="center" class="w-40">Aligned to center</{PopoverContent}>
                </{Popover}>
                <{Popover}>
                    <{PopoverTrigger} render={t'<{Button} variant="outline" size="sm" />'}>End</{PopoverTrigger}>
                    <{PopoverContent} align="end" class="w-40">Aligned to end</{PopoverContent}>
                </{Popover}>
            </div>
        </{Example}>
    """


def PopoverInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open Dialog</{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Popover Example</{DialogTitle}>
                        <{DialogDescription}>Click the button below to see the popover.</{DialogDescription}>
                    </{DialogHeader}>
                    <{Popover}>
                        <{PopoverTrigger} render={t'<{Button} variant="outline" class="w-fit" />'}>
                            Open Popover
                        </{PopoverTrigger}>
                        <{PopoverContent} align="start">
                            <{PopoverHeader}>
                                <{PopoverTitle}>Popover in Dialog</{PopoverTitle}>
                                <{PopoverDescription}>
                                    This popover appears inside a dialog. Click the button to open it.
                                </{PopoverDescription}>
                            </{PopoverHeader}>
                        </{PopoverContent}>
                    </{Popover}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
