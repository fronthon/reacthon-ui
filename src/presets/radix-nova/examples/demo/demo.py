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
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
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

__js__ = {
    "lucide-react": [
        "CopyIcon",
        "CircleAlertIcon",
        "TrashIcon",
        "ShareIcon",
        "ShoppingBagIcon",
        "MoreHorizontalIcon",
        "Loader2Icon",
        "PlusIcon",
        "MinusIcon",
        "ArrowLeftIcon",
        "ArrowRightIcon",
        "CheckIcon",
        "ChevronDownIcon",
        "ChevronRightIcon",
        "SearchIcon",
        "SettingsIcon",
        "ChevronUpIcon",
    ],
}


def Demo():
    slider_value, set_slider_value = use_state([500])

    def handle_slider_value_change(value):
        set_slider_value(value)

    handle_slider_value_change = use_callback(handle_slider_value_change, [])

    return t"""
        <div class="flex min-h-screen w-full flex-col items-center justify-center bg-muted p-4 sm:p-6 lg:p-12 dark:bg-background">
            <div class="grid max-w-3xl gap-4 sm:grid-cols-2">
                <div class="flex flex-col gap-4">
                    <{Card}>
                        <{CardHeader}>
                            <{CardTitle}>Style Overview</{CardTitle}>
                            <{CardDescription} class="line-clamp-2">
                                Designers love packing quirky glyphs into test phrases. This is a preview of the typography styles.
                            </{CardDescription}>
                        </{CardHeader}>
                        <{CardContent}>
                            <div class="grid grid-cols-6 gap-3">
                                {[t'''
                                    <div key={variant} class="flex flex-col flex-wrap items-center gap-2">
                                        <div
                                            class="relative aspect-square w-full rounded-lg bg-(--color) after:absolute after:inset-0 after:rounded-lg after:border after:border-border after:mix-blend-darken dark:after:mix-blend-lighten"
                                            style={ {
                                                "--color": f"var({variant})",
                                            } }
                                        />
                                        <div class="hidden max-w-14 truncate font-mono text-[0.60rem] md:block">
                                            {variant}
                                        </div>
                                    </div>
                                ''' for variant in ["--background", "--foreground", "--primary", "--secondary", "--muted", "--accent", "--border", "--chart-1", "--chart-2", "--chart-3", "--chart-4", "--chart-5"]]}
                            </div>
                        </{CardContent}>
                    </{Card}>
                    <{Card}>
                        <{CardContent}>
                            <div class="grid grid-cols-8 place-items-center gap-4">
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{CopyIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{CircleAlertIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{TrashIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{ShareIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{ShoppingBagIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{MoreHorizontalIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{Loader2Icon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{PlusIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{MinusIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{ArrowLeftIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{ArrowRightIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{CheckIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{ChevronDownIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{ChevronRightIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{SearchIcon} />
                                </{Card}>
                                <{Card} class="flex size-8 items-center justify-center p-0 shadow-none *:[svg]:size-4">
                                    <{SettingsIcon} />
                                </{Card}>
                            </div>
                        </{CardContent}>
                    </{Card}>
                </div>
                <div class="flex flex-col gap-4">
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
                                            <span class="hidden md:block">Alert Dialog</span>
                                            <span class="block md:hidden">Dialog</span>
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
                                    <{Button} variant="outline">Button Group</{Button}>
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
                                                <{DropdownMenuItem} variant="destructive">
                                                    Delete Conversation
                                                </{DropdownMenuItem}>
                                            </{DropdownMenuGroup}>
                                        </{DropdownMenuContent}>
                                    </{DropdownMenu}>
                                </{ButtonGroup}>
                                <{Switch} defaultChecked class="ml-auto" />
                            </div>
                        </{CardContent}>
                    </{Card}>
                </div>
            </div>
        </div>
    """
