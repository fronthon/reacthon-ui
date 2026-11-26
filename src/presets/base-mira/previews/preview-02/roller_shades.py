from reacthon import use_state
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from slider import Slider
from toggle_group import ToggleGroup, ToggleGroupItem


def RollerShades():
    position, set_position = use_state([50])

    preset = "open" if position[0] <= 10 else "closed" if position[0] >= 90 else "half"

    def on_value_change(value):
        v = value[0]
        if v == "open":
            set_position([0])
        if v == "half":
            set_position([50])
        if v == "closed":
            set_position([100])

    def on_value_change_2(value):
        return set_position(list(value) if isinstance(value, list) else [value])

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Living Room</{CardTitle}>
                <{CardDescription}>Roller Shades</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <div class="flex h-32 flex-col overflow-hidden rounded-lg border bg-muted">
                    <div
                        class="bg-muted-foreground transition-all duration-300"
                        style={ {
                            "height": f"{position[0]}%",
                        } }
                    />
                </div>
                <div class="flex items-center gap-3">
                    <span class="text-xs font-medium tracking-wider text-muted-foreground uppercase">Open</span>
                    <{Slider} value={position} onValueChange={on_value_change_2} max={100} class="flex-1" />
                    <span class="text-xs font-medium tracking-wider text-muted-foreground uppercase">Close</span>
                </div>
            </{CardContent}>
            <{CardFooter}>
                <{ToggleGroup}
                    value={[preset]}
                    onValueChange={on_value_change}
                    variant="outline"
                    spacing={1}
                    class="w-full"
                >
                    <{ToggleGroupItem} value="open" class="flex-1">Open</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="half" class="flex-1">Half</{ToggleGroupItem}>
                    <{ToggleGroupItem} value="closed" class="flex-1">Closed</{ToggleGroupItem}>
                </{ToggleGroup}>
            </{CardFooter}>
        </{Card}>
    """
