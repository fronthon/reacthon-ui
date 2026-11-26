from reacthon import use_memo, use_state
from example import Example, ExampleWrapper
from item import Item, ItemActions, ItemContent, ItemGroup, ItemMedia, ItemTitle
from progress import Progress, ProgressLabel, ProgressValue
from slider import Slider

__js__ = {"lucide-react": ["FileIcon"]}


def ProgressExample():
    return t"""
        <{ExampleWrapper}>
            <{ProgressValues} />
            <{ProgressWithLabel} />
            <{ProgressControlled} />
            <{FileUploadList} />
        </{ExampleWrapper}>
    """


def ProgressValues():
    return t"""
        <{Example} title="Progress Bar">
            <div class="flex w-full flex-col gap-4">
                <{Progress} value={0} />
                <{Progress} value={25} class="w-full" />
                <{Progress} value={50} />
                <{Progress} value={75} />
                <{Progress} value={100} />
            </div>
        </{Example}>
    """


def ProgressWithLabel():
    return t"""
        <{Example} title="With Label">
            <{Progress} value={56}>
                <{ProgressLabel}>Upload progress</{ProgressLabel}>
                <{ProgressValue} />
            </{Progress}>
        </{Example}>
    """


def ProgressControlled():
    value, set_value = use_state(50)

    return t"""
        <{Example} title="Controlled">
            <div class="flex w-full flex-col gap-4">
                <{Progress} value={value} class="w-full" />
                <{Slider} value={value} onChange={set_value} minValue={0} maxValue={100} step={1} />
            </div>
        </{Example}>
    """


def FileUploadList():
    files = use_memo(
        lambda: [
            {"id": "1", "name": "document.pdf", "progress": 45, "timeRemaining": "2m 30s"},
            {"id": "2", "name": "presentation.pptx", "progress": 78, "timeRemaining": "45s"},
            {"id": "3", "name": "spreadsheet.xlsx", "progress": 12, "timeRemaining": "5m 12s"},
            {"id": "4", "name": "image.jpg", "progress": 100, "timeRemaining": "Complete"},
        ],
        [],
    )

    return t"""
        <{Example} title="File Upload List">
            <{ItemGroup}>
                {[t'''
                    <{Item} key={file["id"]} size="xs" class="px-0">
                        <{ItemMedia} variant="icon">
                            <{FileIcon} class="size-5" />
                        </{ItemMedia}>
                        <{ItemContent} class="inline-block truncate">
                            <{ItemTitle} class="inline">{file["name"]}</{ItemTitle}>
                        </{ItemContent}>
                        <{ItemContent}>
                            <{Progress} value={file["progress"]} class="w-32" />
                        </{ItemContent}>
                        <{ItemActions} class="w-16 justify-end">
                            <span class="text-sm text-muted-foreground">{file["timeRemaining"]}</span>
                        </{ItemActions}>
                    </{Item}>
                ''' for file in files]}
            </{ItemGroup}>
        </{Example}>
    """
