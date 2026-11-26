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
            <{PopoverWithForm} />
            <{PopoverAlignments} />
            <{PopoverInDialog} />
        </{ExampleWrapper}>
    """


def PopoverBasic():
    return t"""
        <{Example} title="Basic">
            <{Popover}>
                <{PopoverTrigger} asChild>
                    <{Button} variant="outline">Open Popover</{Button}>
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


def PopoverWithForm():
    return t"""
        <{Example} title="With Form">
            <{Popover}>
                <{PopoverTrigger} asChild>
                    <{Button} variant="outline">Open Popover</{Button}>
                </{PopoverTrigger}>
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
                    <{PopoverTrigger} asChild>
                        <{Button} variant="outline" size="sm">Start</{Button}>
                    </{PopoverTrigger}>
                    <{PopoverContent} align="start" class="w-40">Aligned to start</{PopoverContent}>
                </{Popover}>
                <{Popover}>
                    <{PopoverTrigger} asChild>
                        <{Button} variant="outline" size="sm">Center</{Button}>
                    </{PopoverTrigger}>
                    <{PopoverContent} align="center" class="w-40">Aligned to center</{PopoverContent}>
                </{Popover}>
                <{Popover}>
                    <{PopoverTrigger} asChild>
                        <{Button} variant="outline" size="sm">End</{Button}>
                    </{PopoverTrigger}>
                    <{PopoverContent} align="end" class="w-40">Aligned to end</{PopoverContent}>
                </{Popover}>
            </div>
        </{Example}>
    """


def PopoverInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Open Dialog</{Button}>
                </{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Popover Example</{DialogTitle}>
                        <{DialogDescription}>Click the button below to see the popover.</{DialogDescription}>
                    </{DialogHeader}>
                    <{Popover}>
                        <{PopoverTrigger} asChild>
                            <{Button} variant="outline" class="w-fit">Open Popover</{Button}>
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
