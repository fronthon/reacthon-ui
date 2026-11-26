from javascript import NULL
from reacthon import use_state
from card import Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle
from item import Item, ItemActions, ItemContent, ItemGroup, ItemMedia, ItemTitle
from slider import Slider
from switch import Switch
from toggle_group import ToggleGroup, ToggleGroupItem

__js__ = {"lucide-react": ["SunIcon", "ThermometerIcon", "TimerIcon", "Volume2Icon"]}

SCENES = {
    "cooking": {"brightness": [90], "colorTemp": [70], "volume": [30], "fade": [0]},
    "dining": {"brightness": [50], "colorTemp": [40], "volume": [20], "fade": [60]},
    "nightlight": {"brightness": [15], "colorTemp": [20], "volume": [0], "fade": [80]},
    "focus": {"brightness": [100], "colorTemp": [85], "volume": [0], "fade": [0]},
}


def KitchenIsland():
    enabled, set_enabled = use_state(True)
    scene, set_scene = use_state("cooking")
    brightness, set_brightness = use_state([90])
    color_temp, set_color_temp = use_state([70])
    volume, set_volume = use_state([30])
    fade, set_fade = use_state([0])

    def handle_scene_change(value):
        if not value:
            return
        set_scene(value)
        preset = SCENES.get(value)
        set_brightness(list(preset["brightness"]))
        set_color_temp(list(preset["colorTemp"]))
        set_volume(list(preset["volume"]))
        set_fade(list(preset["fade"]))

    def on_selection_change(value):
        first = list(value)[0]
        return handle_scene_change(first if first not in (None, NULL) else "cooking")

    def on_change(value):
        return set_brightness(list(value) if isinstance(value, list) else [value])

    def on_change_2(value):
        return set_color_temp(list(value) if isinstance(value, list) else [value])

    def on_change_3(value):
        return set_volume(list(value) if isinstance(value, list) else [value])

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Kitchen Island</{CardTitle}>
                <{CardDescription}>Hue Color Ambient</{CardDescription}>
                <{CardAction}>
                    <{Switch} isSelected={enabled} onChange={set_enabled} />
                </{CardAction}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <div class="flex flex-col gap-2">
                    <span class="sr-only">Scenes</span>
                    <{ToggleGroup}
                        selectedKeys={[scene]}
                        onSelectionChange={on_selection_change}
                        variant="outline"
                        spacing={1}
                        class="flex-wrap"
                    >
                        <{ToggleGroupItem} id="cooking" isDisabled={not enabled}>Cooking</{ToggleGroupItem}>
                        <{ToggleGroupItem} id="dining" isDisabled={not enabled}>Dining</{ToggleGroupItem}>
                        <{ToggleGroupItem} id="nightlight" isDisabled={not enabled}>Nightlight</{ToggleGroupItem}>
                        <{ToggleGroupItem} id="focus" isDisabled={not enabled}>Focus</{ToggleGroupItem}>
                    </{ToggleGroup}>
                </div>
                <{ItemGroup}>
                    <{Item} size="sm" variant="outline">
                        <{ItemMedia} variant="icon">
                            <{SunIcon} />
                        </{ItemMedia}>
                        <{ItemContent} class="flex-row items-center gap-3">
                            <{ItemTitle} class="shrink-0">Brightness</{ItemTitle}>
                        </{ItemContent}>
                        <{ItemActions} class="flex-1">
                            <{Slider}
                                value={brightness}
                                onChange={on_change}
                                maxValue={100}
                                isDisabled={not enabled}
                                class="w-full"
                            />
                        </{ItemActions}>
                    </{Item}>
                    <{Item} size="sm" variant="outline">
                        <{ItemMedia} variant="icon">
                            <{ThermometerIcon} />
                        </{ItemMedia}>
                        <{ItemContent} class="flex-row items-center gap-3">
                            <{ItemTitle} class="shrink-0">Color Temp</{ItemTitle}>
                        </{ItemContent}>
                        <{ItemActions} class="flex-1">
                            <{Slider} value={color_temp} onChange={on_change_2} maxValue={100} isDisabled={not enabled} />
                        </{ItemActions}>
                    </{Item}>
                    <{Item} size="sm" variant="outline">
                        <{ItemMedia} variant="icon">
                            <{Volume2Icon} />
                        </{ItemMedia}>
                        <{ItemContent} class="flex-row items-center gap-3">
                            <{ItemTitle} class="shrink-0">Volume</{ItemTitle}>
                        </{ItemContent}>
                        <{ItemActions} class="flex-1">
                            <{Slider} value={volume} onChange={on_change_3} maxValue={100} isDisabled={not enabled} />
                        </{ItemActions}>
                    </{Item}>
                    <{Item} size="sm" variant="outline">
                        <{ItemMedia} variant="icon">
                            <{TimerIcon} />
                        </{ItemMedia}>
                        <{ItemContent} class="flex-row items-center gap-3">
                            <{ItemTitle} class="shrink-0">Fade</{ItemTitle}>
                        </{ItemContent}>
                        <{ItemActions} class="flex-1">
                            <{Slider}
                                value={fade}
                                onChange={(lambda value: set_fade(list(value) if isinstance(value, list) else [value]))}
                                maxValue={100}
                                isDisabled={not enabled}
                            />
                        </{ItemActions}>
                    </{Item}>
                </{ItemGroup}>
            </{CardContent}>
        </{Card}>
    """
