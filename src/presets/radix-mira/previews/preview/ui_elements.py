from reacthon import use_callback, use_state
from alert_dialog import (
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger,
)
from badge import Badge
from button import Button
from button_group import ButtonGroup
from card import Card, CardContent
from checkbox import Checkbox
from dropdown_menu import (
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuGroup,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
)
from field import Field, FieldGroup
from input_group import InputGroup, InputGroupAddon, InputGroupInput, InputGroupText
from item import Item, ItemActions, ItemContent, ItemDescription, ItemTitle
from radio_group import RadioGroup, RadioGroupItem
from slider import Slider
from switch import Switch
from textarea import Textarea

__js__ = {"lucide-react": ["ChevronUpIcon", "SearchIcon"]}


def UIElements():
    slider_value, set_slider_value = use_state([500])

    def handle_slider_value_change(value):
        if isinstance(value, (int, float)):
            set_slider_value([value])
        else:
            set_slider_value(list(value))

    handle_slider_value_change = use_callback(handle_slider_value_change, [])

    return t"""
        <{Card} class="w-full">
            <{CardContent} class="flex flex-col gap-6">
                <div class="flex flex-col gap-4">
                    <div class="flex flex-wrap gap-2">
                        <{Button}>Button</{Button}>
                        <{Button} variant="secondary">Secondary</{Button}>
                        <{Button} variant="outline">Outline</{Button}>
                        <{Button} variant="ghost">Ghost</{Button}>
                    </div>
                    <{Item} variant="outline">
                        <{ItemContent}>
                            <{ItemTitle}>Two-factor authentication</{ItemTitle}>
                            <{ItemDescription} class="text-pretty xl:hidden 2xl:block">
                                Verify via email or phone number.
                            </{ItemDescription}>
                        </{ItemContent}>
                        <{ItemActions} class="hidden md:flex">
                            <{Button} size="sm" variant="secondary">Enable</{Button}>
                        </{ItemActions}>
                    </{Item}>
                </div>
                <{Slider}
                    value={slider_value}
                    onValueChange={handle_slider_value_change}
                    max={1000}
                    min={0}
                    step={10}
                    class="flex-1"
                    aria-label="Slider"
                />
                <{FieldGroup}>
                    <{Field}>
                        <{InputGroup}>
                            <{InputGroupInput} placeholder="Name" />
                            <{InputGroupAddon} align="inline-end">
                                <{InputGroupText}>
                                    <{SearchIcon} />
                                </{InputGroupText}>
                            </{InputGroupAddon}>
                        </{InputGroup}>
                    </{Field}>
                    <{Field} class="flex-1">
                        <{Textarea} placeholder="Message" class="resize-none" />
                    </{Field}>
                </{FieldGroup}>
                <div class="flex items-center gap-2">
                    <div class="flex gap-2">
                        <{Badge}>Badge</{Badge}>
                        <{Badge} variant="secondary">Secondary</{Badge}>
                        <{Badge} variant="outline">Outline</{Badge}>
                    </div>
                    <{RadioGroup} defaultValue="apple" class="ml-auto flex w-fit gap-3">
                        <{RadioGroupItem} value="apple" />
                        <{RadioGroupItem} value="banana" />
                    </{RadioGroup}>
                    <div class="flex gap-3">
                        <{Checkbox} defaultChecked />
                        <{Checkbox} />
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <{AlertDialog}>
                        <{AlertDialogTrigger} asChild>
                            <{Button} variant="outline">
                                <span class="hidden md:flex style-sera:md:hidden">Alert Dialog</span>
                                <span class="flex md:hidden style-sera:md:flex">Dialog</span>
                            </{Button}>
                        </{AlertDialogTrigger}>
                        <{AlertDialogContent} size="sm">
                            <{AlertDialogHeader}>
                                <{AlertDialogTitle}>Allow accessory to connect?</{AlertDialogTitle}>
                                <{AlertDialogDescription}>
                                    Do you want to allow the USB accessory to connect to this device and your data?
                                </{AlertDialogDescription}>
                            </{AlertDialogHeader}>
                            <{AlertDialogFooter}>
                                <{AlertDialogCancel}>Don't allow</{AlertDialogCancel}>
                                <{AlertDialogAction}>Allow</{AlertDialogAction}>
                            </{AlertDialogFooter}>
                        </{AlertDialogContent}>
                    </{AlertDialog}>
                    <{ButtonGroup}>
                        <{Button} variant="outline">
                            <span class="style-sera:hidden">Button Group</span>
                            <span class="hidden style-sera:block">Group</span>
                        </{Button}>
                        <{DropdownMenu}>
                            <{DropdownMenuTrigger} asChild>
                                <{Button} variant="outline" size="icon">
                                    <{ChevronUpIcon} />
                                </{Button}>
                            </{DropdownMenuTrigger}>
                            <{DropdownMenuContent} align="end" side="top" class="w-fit">
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuLabel}>Quick Actions</{DropdownMenuLabel}>
                                    <{DropdownMenuItem}>Mute Conversation</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Mark as Read</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Block User</{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuLabel}>Conversation</{DropdownMenuLabel}>
                                    <{DropdownMenuItem}>Share Conversation</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Copy Conversation</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Report Conversation</{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                                <{DropdownMenuSeparator} />
                                <{DropdownMenuGroup}>
                                    <{DropdownMenuItem} variant="destructive">Delete Conversation</{DropdownMenuItem}>
                                </{DropdownMenuGroup}>
                            </{DropdownMenuContent}>
                        </{DropdownMenu}>
                    </{ButtonGroup}>
                    <{Switch} defaultChecked class="ml-auto" />
                </div>
            </{CardContent}>
        </{Card}>
    """
