from reacthon import use_state
from example import Example, ExampleWrapper
from button import Button
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
from collapsible import Collapsible, CollapsibleContent, CollapsibleTrigger
from field import Field, FieldGroup, FieldLabel
from input import Input
from tabs import Tabs, TabsList, TabsTrigger

__js__ = {"lucide-react": ["ChevronRightIcon", "FolderIcon", "FileIcon", "MinimizeIcon", "MaximizeIcon"]}


def CollapsibleExample():
    return t"""
        <{ExampleWrapper}>
            <{CollapsibleFileTree} />
            <{CollapsibleSettings} />
        </{ExampleWrapper}>
    """


def CollapsibleFileTree():
    file_tree = [
        {
            "name": "components",
            "items": [
                {
                    "name": "ui",
                    "items": [
                        {"name": "button.tsx"},
                        {"name": "card.tsx"},
                        {"name": "dialog.tsx"},
                        {"name": "input.tsx"},
                        {"name": "select.tsx"},
                        {"name": "table.tsx"},
                    ],
                },
                {"name": "login-form.tsx"},
                {"name": "register-form.tsx"},
            ],
        },
        {"name": "lib", "items": [{"name": "utils.ts"}, {"name": "cn.ts"}, {"name": "api.ts"}]},
        {
            "name": "hooks",
            "items": [{"name": "use-media-query.ts"}, {"name": "use-debounce.ts"}, {"name": "use-local-storage.ts"}],
        },
        {"name": "types", "items": [{"name": "index.d.ts"}, {"name": "api.d.ts"}]},
        {"name": "public", "items": [{"name": "favicon.ico"}, {"name": "logo.svg"}, {"name": "images"}]},
        {"name": "app.tsx"},
        {"name": "layout.tsx"},
        {"name": "globals.css"},
        {"name": "package.json"},
        {"name": "tsconfig.json"},
        {"name": "README.md"},
        {"name": ".gitignore"},
    ]

    def render_item(file_item):
        if "items" in file_item:
        button = t"""
            <{Button}
                variant="ghost"
                size="sm"
                class="group w-full justify-start transition-none hover:bg-accent hover:text-accent-foreground"
            />
        """

            return t"""
                <{Collapsible} key={file_item["name"]}>
                    <{CollapsibleTrigger} render={button}>
                        <{ChevronRightIcon} class="transition-transform group-data-[state=open]:rotate-90" />
                        <{FolderIcon} />
                        {file_item["name"]}
                    </{CollapsibleTrigger}>
                    <{CollapsibleContent} class="mt-1 ml-5 style-lyra:ml-4">
                        <div class="flex flex-col gap-1">{[render_item(child) for child in file_item["items"]]}</div>
                    </{CollapsibleContent}>
                </{Collapsible}>
            """
        return t"""
            <{Button} key={file_item["name"]} variant="link" size="sm" class="w-full justify-start gap-2 text-foreground">
                <{FileIcon} />
                <span>{file_item["name"]}</span>
            </{Button}>
        """

    return t"""
        <{Example} title="File Tree" class="items-center">
            <{Card} class="mx-auto w-full max-w-[16rem] gap-2" size="sm">
                <{CardHeader}>
                    <{Tabs} defaultValue="explorer">
                        <{TabsList} class="w-full">
                            <{TabsTrigger} value="explorer">Explorer</{TabsTrigger}>
                            <{TabsTrigger} value="settings">Outline</{TabsTrigger}>
                        </{TabsList}>
                    </{Tabs}>
                </{CardHeader}>
                <{CardContent}>
                    <div class="flex flex-col gap-1">{[render_item(item) for item in file_tree]}</div>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CollapsibleSettings():
    is_open, set_is_open = use_state(False)

    return t"""
        <{Example} title="Settings" class="items-center">
            <{Card} class="mx-auto w-full max-w-xs" size="sm">
                <{CardHeader}>
                    <{CardTitle}>Radius</{CardTitle}>
                    <{CardDescription}>Set the corner radius of the element.</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <{Collapsible} open={is_open} onOpenChange={set_is_open} class="flex items-start gap-2">
                        <{FieldGroup} class="grid w-full grid-cols-2 gap-2">
                            <{Field}>
                                <{FieldLabel} for="radius-x" class="sr-only">Radius X</{FieldLabel}>
                                <{Input} id="radius" placeholder="0" defaultValue={0} />
                            </{Field}>
                            <{Field}>
                                <{FieldLabel} for="radius-y" class="sr-only">Radius Y</{FieldLabel}>
                                <{Input} id="radius" placeholder="0" defaultValue={0} />
                            </{Field}>
                            <{CollapsibleContent} class="col-span-full grid grid-cols-subgrid gap-2">
                                <{Field}>
                                    <{FieldLabel} for="radius-x" class="sr-only">Radius X</{FieldLabel}>
                                    <{Input} id="radius" placeholder="0" defaultValue={0} />
                                </{Field}>
                                <{Field}>
                                    <{FieldLabel} for="radius-y" class="sr-only">Radius Y</{FieldLabel}>
                                    <{Input} id="radius" placeholder="0" defaultValue={0} />
                                </{Field}>
                            </{CollapsibleContent}>
                        </{FieldGroup}>
                        <{CollapsibleTrigger} render={t'<{Button} variant="outline" size="icon" />'}>
                            {t'<{MinimizeIcon} />' if is_open else t'<{MaximizeIcon} />'}
                        </{CollapsibleTrigger}>
                    </{Collapsible}>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """
