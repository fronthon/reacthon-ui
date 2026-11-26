from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from checkbox import Checkbox
from dialog import (
    Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger,
)
from field import Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldSeparator, FieldSet, FieldTitle
from input import Input
from input_group import InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput
from kbd import Kbd
from native_select import NativeSelect, NativeSelectOption
from select import Select, SelectContent, SelectGroup, SelectItem, SelectSeparator, SelectTrigger, SelectValue
from switch import Switch
from tabs import Tabs, TabsContent, TabsList, TabsTrigger
from textarea import Textarea
from tooltip import Tooltip, TooltipContent, TooltipTrigger

__js__ = {"lucide-react": ["InfoIcon"]}


def DialogExample():
    return t"""
        <{ExampleWrapper}>
            <{DialogWithForm} />
            <{DialogScrollableContent} />
            <{DialogWithStickyFooter} />
            <{DialogNoCloseButton} />
            <{DialogChatSettings} />
        </{ExampleWrapper}>
    """


def DialogWithForm():
    return t"""
        <{Example} title="With Form" class="items-center justify-center">
            <{Dialog}>
                <form>
                    <{DialogTrigger} asChild>
                        <{Button} variant="outline">Edit Profile</{Button}>
                    </{DialogTrigger}>
                    <{DialogContent}>
                        <{DialogHeader}>
                            <{DialogTitle}>Edit profile</{DialogTitle}>
                            <{DialogDescription}>
                                Make changes to your profile here. Click save when you're done. Your profile will be updated immediately.
                            </{DialogDescription}>
                        </{DialogHeader}>
                        <{FieldGroup}>
                            <{Field}>
                                <{FieldLabel} for="name-1">Name</{FieldLabel}>
                                <{Input} id="name-1" name="name" defaultValue="Pedro Duarte" />
                            </{Field}>
                            <{Field}>
                                <{FieldLabel} for="username-1">Username</{FieldLabel}>
                                <{Input} id="username-1" name="username" defaultValue="@peduarte" />
                            </{Field}>
                        </{FieldGroup}>
                        <{DialogFooter}>
                            <{DialogClose} asChild>
                                <{Button} variant="outline">Cancel</{Button}>
                            </{DialogClose}>
                            <{Button} type="submit">Save changes</{Button}>
                        </{DialogFooter}>
                    </{DialogContent}>
                </form>
            </{Dialog}>
        </{Example}>
    """


def DialogScrollableContent():
    return t"""
        <{Example} title="Scrollable Content" class="items-center justify-center">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Scrollable Content</{Button}>
                </{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Scrollable Content</{DialogTitle}>
                        <{DialogDescription}>This is a dialog with scrollable content.</{DialogDescription}>
                    </{DialogHeader}>
                    <div class="no-scrollbar max-h-[70vh] overflow-y-auto style-vega:-mx-6 style-vega:px-6 style-nova:-mx-4 style-nova:px-4 style-lyra:-mx-4 style-lyra:px-4 style-maia:-mx-6 style-maia:px-6 style-mira:-mx-4 style-mira:px-4 style-luma:-mx-6 style-luma:px-6 style-rhea:-mx-6 style-rhea:px-6">
                        {[t'''
                            <p
                                key={index}
                                class="mb-4 leading-normal style-lyra:mb-2 style-lyra:leading-relaxed"
                            >
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                            </p>
                        ''' for index in range(10)]}
                    </div>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


def DialogWithStickyFooter():
    return t"""
        <{Example} title="With Sticky Footer" class="items-center justify-center">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Sticky Footer</{Button}>
                </{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Scrollable Content</{DialogTitle}>
                        <{DialogDescription}>This is a dialog with scrollable content.</{DialogDescription}>
                    </{DialogHeader}>
                    <div class="no-scrollbar max-h-[70vh] overflow-y-auto style-vega:-mx-6 style-vega:px-6 style-nova:-mx-4 style-nova:px-4 style-lyra:-mx-4 style-lyra:px-4 style-maia:-mx-6 style-maia:px-6 style-mira:-mx-4 style-mira:px-4 style-luma:-mx-6 style-luma:px-6 style-rhea:-mx-6 style-rhea:px-6">
                        {[t'''
                            <p
                                key={index}
                                class="mb-4 leading-normal style-lyra:mb-2 style-lyra:leading-relaxed"
                            >
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                            </p>
                        ''' for index in range(10)]}
                    </div>
                    <{DialogFooter}>
                        <{DialogClose} asChild>
                            <{Button} variant="outline">Close</{Button}>
                        </{DialogClose}>
                    </{DialogFooter}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


def DialogNoCloseButton():
    return t"""
        <{Example} title="No Close Button" class="items-center justify-center">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">No Close Button</{Button}>
                </{DialogTrigger}>
                <{DialogContent} showCloseButton={False}>
                    <{DialogHeader}>
                        <{DialogTitle}>No Close Button</{DialogTitle}>
                        <{DialogDescription}>
                            This dialog doesn't have a close button in the top-right corner.
                        </{DialogDescription}>
                    </{DialogHeader}>
                    <{DialogFooter}>
                        <{DialogClose} asChild>
                            <{Button} variant="outline">Close</{Button}>
                        </{DialogClose}>
                    </{DialogFooter}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """


spoken_languages = [
    {"label": "English", "value": "en"},
    {"label": "Spanish", "value": "es"},
    {"label": "French", "value": "fr"},
    {"label": "German", "value": "de"},
    {"label": "Italian", "value": "it"},
    {"label": "Portuguese", "value": "pt"},
    {"label": "Russian", "value": "ru"},
    {"label": "Chinese", "value": "zh"},
    {"label": "Japanese", "value": "ja"},
    {"label": "Korean", "value": "ko"},
    {"label": "Arabic", "value": "ar"},
    {"label": "Hindi", "value": "hi"},
    {"label": "Bengali", "value": "bn"},
    {"label": "Telugu", "value": "te"},
    {"label": "Marathi", "value": "mr"},
    {"label": "Kannada", "value": "kn"},
    {"label": "Malayalam", "value": "ml"},
]

voices = [
    {"label": "Samantha", "value": "samantha"},
    {"label": "Alex", "value": "alex"},
    {"label": "Fred", "value": "fred"},
    {"label": "Victoria", "value": "victoria"},
    {"label": "Tom", "value": "tom"},
    {"label": "Karen", "value": "karen"},
    {"label": "Sam", "value": "sam"},
    {"label": "Daniel", "value": "daniel"},
]


def DialogChatSettings():
    tab, set_tab = use_state("general")
    theme, set_theme = use_state("system")
    accent_color, set_accent_color = use_state("default")
    spoken_language, set_spoken_language = use_state("en")
    voice, set_voice = use_state("samantha")

    return t"""
        <{Example} title="Chat Settings" class="items-center justify-center">
            <{Dialog}>
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Chat Settings</{Button}>
                </{DialogTrigger}>
                <{DialogContent} class="min-w-md">
                    <{DialogHeader}>
                        <{DialogTitle}>Chat Settings</{DialogTitle}>
                        <{DialogDescription}>
                            Customize your chat settings: theme, accent color, spoken language, voice, personality, and custom instructions.
                        </{DialogDescription}>
                    </{DialogHeader}>
                    <div class="flex flex-col gap-4">
                        <{NativeSelect}
                            value={tab}
                            onChange={(lambda e: set_tab(e.target.value))}
                            class="w-full md:hidden"
                        >
                            <{NativeSelectOption} value="general">General</{NativeSelectOption}>
                            <{NativeSelectOption} value="notifications">Notifications</{NativeSelectOption}>
                            <{NativeSelectOption} value="personalization">Personalization</{NativeSelectOption}>
                            <{NativeSelectOption} value="security">Security</{NativeSelectOption}>
                        </{NativeSelect}>
                        <{Tabs} value={tab} onValueChange={set_tab}>
                            <{TabsList} class="hidden w-full md:flex">
                                <{TabsTrigger} value="general">General</{TabsTrigger}>
                                <{TabsTrigger} value="notifications">Notifications</{TabsTrigger}>
                                <{TabsTrigger} value="personalization">Personalization</{TabsTrigger}>
                                <{TabsTrigger} value="security">Security</{TabsTrigger}>
                            </{TabsList}>
                            <div class="border **:data-[slot=select-trigger]:min-w-[125px] style-vega:min-h-[550px] style-vega:rounded-lg style-vega:p-6 style-nova:min-h-[460px] style-nova:rounded-lg style-nova:p-4 style-lyra:min-h-[450px] style-lyra:rounded-none style-lyra:p-4 style-maia:min-h-[550px] style-maia:rounded-xl style-maia:p-6 style-mira:min-h-[450px] style-mira:rounded-md style-mira:p-4 style-luma:min-h-[550px] style-luma:rounded-xl style-luma:p-6 style-rhea:min-h-[480px] style-rhea:rounded-2xl style-rhea:p-6">
                                <{TabsContent} value="general">
                                    <{FieldSet}>
                                        <{FieldGroup}>
                                            <{Field} orientation="horizontal">
                                                <{FieldLabel} for="theme">Theme</{FieldLabel}>
                                                <{Select} value={theme} onValueChange={set_theme}>
                                                    <{SelectTrigger} id="theme">
                                                        <{SelectValue} placeholder="Select" />
                                                    </{SelectTrigger}>
                                                    <{SelectContent} align="end">
                                                        <{SelectGroup}>
                                                            <{SelectItem} value="light">Light</{SelectItem}>
                                                            <{SelectItem} value="dark">Dark</{SelectItem}>
                                                            <{SelectItem} value="system">System</{SelectItem}>
                                                        </{SelectGroup}>
                                                    </{SelectContent}>
                                                </{Select}>
                                            </{Field}>
                                            <{FieldSeparator} />
                                            <{Field} orientation="horizontal">
                                                <{FieldLabel} for="accent-color">Accent Color</{FieldLabel}>
                                                <{Select} value={accent_color} onValueChange={set_accent_color}>
                                                    <{SelectTrigger} id="accent-color">
                                                        <{SelectValue} placeholder="Select" />
                                                    </{SelectTrigger}>
                                                    <{SelectContent} align="end">
                                                        <{SelectGroup}>
                                                            <{SelectItem} value="default">
                                                                <div class="size-3 rounded-full bg-neutral-500 dark:bg-neutral-400" />
                                                                Default
                                                            </{SelectItem}>
                                                            <{SelectItem} value="red">
                                                                <div class="size-3 rounded-full bg-red-500 dark:bg-red-400" />
                                                                Red
                                                            </{SelectItem}>
                                                            <{SelectItem} value="blue">
                                                                <div class="size-3 rounded-full bg-blue-500 dark:bg-blue-400" />
                                                                Blue
                                                            </{SelectItem}>
                                                            <{SelectItem} value="green">
                                                                <div class="size-3 rounded-full bg-green-500 dark:bg-green-400" />
                                                                Green
                                                            </{SelectItem}>
                                                            <{SelectItem} value="purple">
                                                                <div class="size-3 rounded-full bg-purple-500 dark:bg-purple-400" />
                                                                Purple
                                                            </{SelectItem}>
                                                            <{SelectItem} value="pink">
                                                                <div class="size-3 rounded-full bg-pink-500 dark:bg-pink-400" />
                                                                Pink
                                                            </{SelectItem}>
                                                        </{SelectGroup}>
                                                    </{SelectContent}>
                                                </{Select}>
                                            </{Field}>
                                            <{FieldSeparator} />
                                            <{Field} orientation="responsive">
                                                <{FieldContent}>
                                                    <{FieldLabel} for="spoken-language">Spoken Language</{FieldLabel}>
                                                    <{FieldDescription}>
                                                        For best results, select the language you mainly speak. If it's not listed, it may still be supported via auto-detection.
                                                    </{FieldDescription}>
                                                </{FieldContent}>
                                                <{Select} value={spoken_language} onValueChange={set_spoken_language}>
                                                    <{SelectTrigger} id="spoken-language">
                                                        <{SelectValue} placeholder="Select" />
                                                    </{SelectTrigger}>
                                                    <{SelectContent} align="end" position="item-aligned">
                                                        <{SelectGroup}>
                                                            <{SelectItem} value="auto">Auto</{SelectItem}>
                                                        </{SelectGroup}>
                                                        <{SelectSeparator} />
                                                        <{SelectGroup}>
                                                            {[t'''
                                                                <{SelectItem}
                                                                    key={language["value"]}
                                                                    value={language["value"]}
                                                                >
                                                                    {language["label"]}
                                                                </{SelectItem}>
                                                            ''' for language in spoken_languages]}
                                                        </{SelectGroup}>
                                                    </{SelectContent}>
                                                </{Select}>
                                            </{Field}>
                                            <{FieldSeparator} />
                                            <{Field} orientation="horizontal">
                                                <{FieldLabel} for="voice">Voice</{FieldLabel}>
                                                <{Select} value={voice} onValueChange={set_voice}>
                                                    <{SelectTrigger} id="voice">
                                                        <{SelectValue} placeholder="Select" />
                                                    </{SelectTrigger}>
                                                    <{SelectContent} align="end" position="item-aligned">
                                                        <{SelectGroup}>
                                                            {[t'''
                                                                <{SelectItem}
                                                                    key={voice["value"]}
                                                                    value={voice["value"]}
                                                                >
                                                                    {voice["label"]}
                                                                </{SelectItem}>
                                                            ''' for voice in voices]}
                                                        </{SelectGroup}>
                                                    </{SelectContent}>
                                                </{Select}>
                                            </{Field}>
                                        </{FieldGroup}>
                                    </{FieldSet}>
                                </{TabsContent}>
                                <{TabsContent} value="notifications">
                                    <{FieldGroup}>
                                        <{FieldSet}>
                                            <{FieldLabel}>Responses</{FieldLabel}>
                                            <{FieldDescription}>
                                                Get notified when ChatGPT responds to requests that take time, like research or image generation.
                                            </{FieldDescription}>
                                            <{FieldGroup} data-slot="checkbox-group">
                                                <{Field} orientation="horizontal">
                                                    <{Checkbox} id="push" defaultChecked disabled />
                                                    <{FieldLabel} for="push" class="font-normal">
                                                        Push notifications
                                                    </{FieldLabel}>
                                                </{Field}>
                                            </{FieldGroup}>
                                        </{FieldSet}>
                                        <{FieldSeparator} />
                                        <{FieldSet}>
                                            <{FieldLabel}>Tasks</{FieldLabel}>
                                            <{FieldDescription}>
                                                Get notified when tasks you've created have updates. <a href="#">Manage tasks</a>
                                            </{FieldDescription}>
                                            <{FieldGroup} data-slot="checkbox-group">
                                                <{Field} orientation="horizontal">
                                                    <{Checkbox} id="push-tasks" />
                                                    <{FieldLabel} for="push-tasks" class="font-normal">
                                                        Push notifications
                                                    </{FieldLabel}>
                                                </{Field}>
                                                <{Field} orientation="horizontal">
                                                    <{Checkbox} id="email-tasks" />
                                                    <{FieldLabel} for="email-tasks" class="font-normal">
                                                        Email notifications
                                                    </{FieldLabel}>
                                                </{Field}>
                                            </{FieldGroup}>
                                        </{FieldSet}>
                                    </{FieldGroup}>
                                </{TabsContent}>
                                <{TabsContent} value="personalization">
                                    <{FieldGroup}>
                                        <{Field} orientation="responsive">
                                            <{FieldLabel} for="nickname">Nickname</{FieldLabel}>
                                            <{InputGroup}>
                                                <{InputGroupInput}
                                                    id="nickname"
                                                    placeholder="Broski"
                                                    class="@md/field-group:max-w-[200px]"
                                                />
                                                <{InputGroupAddon} align="inline-end">
                                                    <{Tooltip}>
                                                        <{TooltipTrigger} asChild>
                                                            <{InputGroupButton} size="icon-xs">
                                                                <{InfoIcon} />
                                                            </{InputGroupButton}>
                                                        </{TooltipTrigger}>
                                                        <{TooltipContent} class="flex items-center gap-2">
                                                            Used to identify you in the chat. <{Kbd}>N</{Kbd}>
                                                        </{TooltipContent}>
                                                    </{Tooltip}>
                                                </{InputGroupAddon}>
                                            </{InputGroup}>
                                        </{Field}>
                                        <{FieldSeparator} />
                                        <{Field}
                                            orientation="responsive"
                                            class="@md/field-group:flex-col @2xl/field-group:flex-row"
                                        >
                                            <{FieldContent}>
                                                <{FieldLabel} for="about">More about you</{FieldLabel}>
                                                <{FieldDescription}>
                                                    Tell us more about yourself. This will be used to help us personalize your experience.
                                                </{FieldDescription}>
                                            </{FieldContent}>
                                            <{Textarea}
                                                id="about"
                                                placeholder="I'm a software engineer..."
                                                class="min-h-[120px] @md/field-group:min-w-full @2xl/field-group:min-w-[300px]"
                                            />
                                        </{Field}>
                                        <{FieldSeparator} />
                                        <{FieldLabel}>
                                            <{Field} orientation="horizontal">
                                                <{FieldContent}>
                                                    <{FieldLabel} for="customization">
                                                        Enable customizations
                                                    </{FieldLabel}>
                                                    <{FieldDescription}>
                                                        Enable customizations to make ChatGPT more personalized.
                                                    </{FieldDescription}>
                                                </{FieldContent}>
                                                <{Switch} id="customization" defaultChecked />
                                            </{Field}>
                                        </{FieldLabel}>
                                    </{FieldGroup}>
                                </{TabsContent}>
                                <{TabsContent} value="security">
                                    <{FieldGroup}>
                                        <{Field} orientation="horizontal">
                                            <{FieldContent}>
                                                <{FieldLabel} for="2fa">Multi-factor authentication</{FieldLabel}>
                                                <{FieldDescription}>
                                                    Enable multi-factor authentication to secure your account. If you do not have a two-factor authentication device, you can use a one-time code sent to your email.
                                                </{FieldDescription}>
                                            </{FieldContent}>
                                            <{Switch} id="2fa" />
                                        </{Field}>
                                        <{FieldSeparator} />
                                        <{Field} orientation="horizontal">
                                            <{FieldContent}>
                                                <{FieldTitle}>Log out</{FieldTitle}>
                                                <{FieldDescription}>
                                                    Log out of your account on this device.
                                                </{FieldDescription}>
                                            </{FieldContent}>
                                            <{Button} variant="outline" size="sm">Log Out</{Button}>
                                        </{Field}>
                                        <{FieldSeparator} />
                                        <{Field} orientation="horizontal">
                                            <{FieldContent}>
                                                <{FieldTitle}>Log out of all devices</{FieldTitle}>
                                                <{FieldDescription}>
                                                    This will log you out of all devices, including the current session. It may take up to 30 minutes for the changes to take effect.
                                                </{FieldDescription}>
                                            </{FieldContent}>
                                            <{Button} variant="outline" size="sm">Log Out All</{Button}>
                                        </{Field}>
                                    </{FieldGroup}>
                                </{TabsContent}>
                            </div>
                        </{Tabs}>
                    </div>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
