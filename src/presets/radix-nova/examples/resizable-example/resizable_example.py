from javascript import Math, NULL
from reacthon import use_state
from example import Example, ExampleWrapper
from resizable import ResizableHandle, ResizablePanel, ResizablePanelGroup


def ResizableExample():
    return t"""
        <{ExampleWrapper}>
            <{ResizableHorizontal} />
            <{ResizableVertical} />
            <{ResizableWithHandle} />
            <{ResizableNested} />
            <{ResizableControlled} />
        </{ExampleWrapper}>
    """


def ResizableHorizontal():
    return t"""
        <{Example} title="Horizontal">
            <{ResizablePanelGroup}
                orientation="horizontal"
                class="min-h-[200px] rounded-lg border style-lyra:rounded-none style-sera:rounded-none"
            >
                <{ResizablePanel} defaultSize="25%">
                    <div class="flex h-full items-center justify-center p-6">
                        <span class="font-semibold">Sidebar</span>
                    </div>
                </{ResizablePanel}>
                <{ResizableHandle} />
                <{ResizablePanel} defaultSize="75%">
                    <div class="flex h-full items-center justify-center p-6">
                        <span class="font-semibold">Content</span>
                    </div>
                </{ResizablePanel}>
            </{ResizablePanelGroup}>
        </{Example}>
    """


def ResizableVertical():
    return t"""
        <{Example} title="Vertical">
            <{ResizablePanelGroup}
                orientation="vertical"
                class="min-h-[200px] rounded-lg border style-lyra:rounded-none style-sera:rounded-none"
            >
                <{ResizablePanel} defaultSize="25%">
                    <div class="flex h-full items-center justify-center p-6">
                        <span class="font-semibold">Header</span>
                    </div>
                </{ResizablePanel}>
                <{ResizableHandle} />
                <{ResizablePanel} defaultSize="75%">
                    <div class="flex h-full items-center justify-center p-6">
                        <span class="font-semibold">Content</span>
                    </div>
                </{ResizablePanel}>
            </{ResizablePanelGroup}>
        </{Example}>
    """


def ResizableWithHandle():
    return t"""
        <{Example} title="With Handle">
            <{ResizablePanelGroup}
                orientation="horizontal"
                class="min-h-[200px] rounded-lg border style-lyra:rounded-none style-sera:rounded-none"
            >
                <{ResizablePanel} defaultSize="25%">
                    <div class="flex h-full items-center justify-center p-6">
                        <span class="font-semibold">Sidebar</span>
                    </div>
                </{ResizablePanel}>
                <{ResizableHandle} withHandle />
                <{ResizablePanel} defaultSize="75%">
                    <div class="flex h-full items-center justify-center p-6">
                        <span class="font-semibold">Content</span>
                    </div>
                </{ResizablePanel}>
            </{ResizablePanelGroup}>
        </{Example}>
    """


def ResizableNested():
    return t"""
        <{Example} title="Nested">
            <{ResizablePanelGroup}
                orientation="horizontal"
                class="rounded-lg border style-lyra:rounded-none style-sera:rounded-none"
            >
                <{ResizablePanel} defaultSize="50%">
                    <div class="flex h-[200px] items-center justify-center p-6">
                        <span class="font-semibold">One</span>
                    </div>
                </{ResizablePanel}>
                <{ResizableHandle} />
                <{ResizablePanel} defaultSize="50%">
                    <{ResizablePanelGroup} orientation="vertical">
                        <{ResizablePanel} defaultSize="25%">
                            <div class="flex h-full items-center justify-center p-6">
                                <span class="font-semibold">Two</span>
                            </div>
                        </{ResizablePanel}>
                        <{ResizableHandle} />
                        <{ResizablePanel} defaultSize="75%">
                            <div class="flex h-full items-center justify-center p-6">
                                <span class="font-semibold">Three</span>
                            </div>
                        </{ResizablePanel}>
                    </{ResizablePanelGroup}>
                </{ResizablePanel}>
            </{ResizablePanelGroup}>
        </{Example}>
    """


def ResizableControlled():
    layout, set_layout = use_state({})

    return t"""
        <{Example} title="Controlled">
            <{ResizablePanelGroup}
                orientation="horizontal"
                class="min-h-[200px] rounded-lg border style-lyra:rounded-none style-sera:rounded-none"
                onLayoutChange={set_layout}
            >
                <{ResizablePanel} defaultSize="30%" id="left" minSize="20%">
                    <div class="flex h-full flex-col items-center justify-center gap-2 p-6">
                        <span class="font-semibold">
                            {Math.round(layout.get("left") if layout.get("left") not in (None, NULL) else 30)}%
                        </span>
                    </div>
                </{ResizablePanel}>
                <{ResizableHandle} />
                <{ResizablePanel} defaultSize="70%" id="right" minSize="30%">
                    <div class="flex h-full flex-col items-center justify-center gap-2 p-6">
                        <span class="font-semibold">
                            {Math.round(layout.get("right") if layout.get("right") not in (None, NULL) else 70)}%
                        </span>
                    </div>
                </{ResizablePanel}>
            </{ResizablePanelGroup}>
        </{Example}>
    """
