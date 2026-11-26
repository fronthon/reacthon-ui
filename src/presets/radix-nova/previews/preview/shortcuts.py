from card import Card, CardContent
from item import Item, ItemActions, ItemGroup, ItemHeader, ItemSeparator, ItemTitle
from kbd import Kbd

__js__ = {"react": ["Fragment"]}

shortcuts = [
    {"label": "Search", "keys": ["⌘", "K"]},
    {"label": "Quick Actions", "keys": ["⌘", "J"]},
    {"label": "New File", "keys": ["⌘", "N"]},
    {"label": "Save", "keys": ["⌘", "S"]},
    {"label": "Toggle Sidebar", "keys": ["⌘", "B"]},
]


def Shortcuts():
    return t"""
        <{Card}>
            <{CardContent}>
                <div class="flex flex-col gap-3">
                    <div class="text-sm font-medium">Shortcuts</div>
                    <{ItemGroup} class="gap-2 text-muted-foreground" data-size="xs">
                        {[t'''
                            <{Fragment} key={item["label"]}>
                                {i > 0 and t"<{ItemSeparator} />"}
                                <{Item} variant="default" size="xs" class="border-0 px-0 py-0">
                                    <{ItemHeader}>
                                        <{ItemTitle} class="font-normal">{item["label"]}</{ItemTitle}>
                                        <{ItemActions}>
                                            <div class="flex gap-1">
                                                {[t"<{Kbd} key={key}>{key}</{Kbd}>" for key in item["keys"]]}
                                            </div>
                                        </{ItemActions}>
                                    </{ItemHeader}>
                                </{Item}>
                            </{Fragment}>
                        ''' for i, item in enumerate(shortcuts)]}
                    </{ItemGroup}>
                </div>
            </{CardContent}>
        </{Card}>
    """
