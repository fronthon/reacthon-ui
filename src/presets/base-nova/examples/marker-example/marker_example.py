from example import Example, ExampleWrapper
from accordion import Accordion, AccordionContent, AccordionItem, AccordionTrigger
from button import Button
from drawer import (
    Drawer, DrawerClose, DrawerContent, DrawerDescription, DrawerFooter, DrawerHeader, DrawerTitle, DrawerTrigger,
)
from marker import Marker, MarkerContent, MarkerIcon
from spinner import Spinner

__js__ = {
    "sonner": ["toast"],
    "lucide-react": [
        "FileTextIcon",
        "GitBranchIcon",
        "ClockIcon",
        "ChevronRightIcon",
        "CircleUserIcon",
        "SearchIcon",
        "CheckIcon",
    ],
}


def MarkerExamples():
    return t"""
        <{ExampleWrapper}>
            <{MarkerExample} />
            <{MarkerBorder} />
            <{MarkerSeparator} />
            <{MarkerAccordion} />
            <{MarkerDrawer} />
        </{ExampleWrapper}>
    """


def MarkerExample():
    return t"""
        <{Example} title="Markers" class="gap-8">
            <{Marker}>
                <{MarkerContent}>A default marker</{MarkerContent}>
            </{Marker}>
            <{Marker}>
                <{MarkerIcon}>
                    <{FileTextIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Marker with icon</{MarkerContent}>
            </{Marker}>
            <{Marker} role="status">
                <{MarkerIcon}>
                    <{Spinner} />
                </{MarkerIcon}>
                <{MarkerContent}>Marker with a spinner</{MarkerContent}>
            </{Marker}>
            <{Marker} role="status">
                <{MarkerIcon}>
                    <{Spinner} />
                </{MarkerIcon}>
                <{MarkerContent} class="shimmer">Marker with shimmer effect</{MarkerContent}>
            </{Marker}>
            <{Marker} role="status">
                <{MarkerContent} class="shimmer">Thinking...</{MarkerContent}>
            </{Marker}>
            <{Marker} render={t'<a href="#" />'}>
                <{MarkerIcon}>
                    <{GitBranchIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Marker as a link</{MarkerContent}>
            </{Marker}>
            <{Marker} render={t'''
                <button
                    onClick={(lambda: toast("You clicked the button"))}
                    class="transition-colors hover:text-foreground"
                />
            '''}>
                <{MarkerIcon}>
                    <{ClockIcon} />
                </{MarkerIcon}>
                <{MarkerContent} class="flex-1">
                    <div>Marker as a button</div>
                </{MarkerContent}>
                <{MarkerIcon}>
                    <{ChevronRightIcon} />
                </{MarkerIcon}>
            </{Marker}>
            <{Marker}>
                <{MarkerIcon}>
                    <{CircleUserIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Rhea joined the chat</{MarkerContent}>
            </{Marker}>
            <{Marker} class="justify-center">
                <{MarkerContent}>
                    <strong class="font-medium">Olivia Rose</strong> left the chat
                </{MarkerContent}>
            </{Marker}>
            <{Marker} class="flex-col">
                <{MarkerIcon}>
                    <{FileTextIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Marker with icon at the top</{MarkerContent}>
            </{Marker}>
        </{Example}>
    """


def MarkerBorder():
    return t"""
        <{Example} title="Border" class="gap-3">
            <{Marker} variant="border">
                <{MarkerIcon}>
                    <{GitBranchIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Switched to release-candidate</{MarkerContent}>
            </{Marker}>
            <{Marker} variant="border">
                <{MarkerIcon}>
                    <{SearchIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Reviewed 8 related files</{MarkerContent}>
            </{Marker}>
            <{Marker} variant="border">
                <{MarkerIcon}>
                    <{FileTextIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Opened implementation notes</{MarkerContent}>
            </{Marker}>
        </{Example}>
    """


def MarkerSeparator():
    return t"""
        <{Example} title="Separator" class="gap-8">
            <{Marker} variant="separator">
                <{MarkerContent}>Worked for 42s</{MarkerContent}>
            </{Marker}>
            <{Marker} variant="separator" role="status">
                <{MarkerIcon}>
                    <{Spinner} />
                </{MarkerIcon}>
                <{MarkerContent}>Compacting conversation</{MarkerContent}>
            </{Marker}>
            <{Marker} variant="separator" role="status">
                <{MarkerContent} class="shimmer">Reading 4 files</{MarkerContent}>
            </{Marker}>
            <{Marker} variant="separator">
                <{MarkerIcon}>
                    <{CheckIcon} />
                </{MarkerIcon}>
                <{MarkerContent}>Conversation compacted</{MarkerContent}>
            </{Marker}>
            <{Marker} variant="separator">
                <{MarkerContent}>
                    With a <a href="#">link to learn more</a>
                </{MarkerContent}>
            </{Marker}>
            <{Marker} variant="separator">
                <{MarkerContent}>
                    <{Button} variant="outline">
                        <{GitBranchIcon} />
                        Button
                    </{Button}>
                </{MarkerContent}>
            </{Marker}>
        </{Example}>
    """


def MarkerAccordion():
    return t"""
        <{Example} title="Accordion" containerClassName="min-h-72">
            <{Accordion}>
                <{AccordionItem} value="1">
                    <{AccordionTrigger}>
                        <{Marker}>
                            <{MarkerIcon}>
                                <{ClockIcon} />
                            </{MarkerIcon}>
                            <{MarkerContent}>Worked for 42s</{MarkerContent}>
                        </{Marker}>
                    </{AccordionTrigger}>
                    <{AccordionContent}>
                        <p class="text-sm text-muted-foreground">
                            The user asked for a list of all the files in the current directory. The assistant responded with a list of all the files in the current directory.
                        </p>
                    </{AccordionContent}>
                </{AccordionItem}>
            </{Accordion}>
        </{Example}>
    """


def MarkerDrawer():
    return t"""
        <{Example} title="Drawer">
            <{Drawer} swipeDirection="right">
                <{Marker} variant="separator">
                    <{DrawerTrigger} render={t'<{Button} variant="outline" />'}>
                        <{SearchIcon} data-icon="inline-start" />
                        Explored 4 files
                    </{DrawerTrigger}>
                </{Marker}>
                <{DrawerContent}>
                    <{DrawerHeader}>
                        <{DrawerTitle}>File Activity</{DrawerTitle}>
                        <{DrawerDescription}>Files read while preparing the response.</{DrawerDescription}>
                    </{DrawerHeader}>
                    <div class="grid gap-3 px-4 text-sm">
                        <div class="flex items-center justify-between gap-4 rounded-md border px-3 py-2">
                            <span class="truncate">app/chat/page.tsx</span>
                            <span class="text-muted-foreground">read</span>
                        </div>
                        <div class="flex items-center justify-between gap-4 rounded-md border px-3 py-2">
                            <span class="truncate">components/message.tsx</span>
                            <span class="text-muted-foreground">read</span>
                        </div>
                        <div class="flex items-center justify-between gap-4 rounded-md border px-3 py-2">
                            <span class="truncate">lib/ai.ts</span>
                            <span class="text-muted-foreground">read</span>
                        </div>
                    </div>
                    <{DrawerFooter}>
                        <{DrawerClose} render={t'<{Button} variant="outline" />'}>Close</{DrawerClose}>
                    </{DrawerFooter}>
                </{DrawerContent}>
            </{Drawer}>
        </{Example}>
    """
