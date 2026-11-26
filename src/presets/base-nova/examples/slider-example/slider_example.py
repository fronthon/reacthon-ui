from reacthon import use_state
from example import Example, ExampleWrapper
from label import Label
from slider import Slider


def SliderExample():
    return t"""
        <{ExampleWrapper}>
            <{SliderBasic} />
            <{SliderRange} />
            <{SliderMultiple} />
            <{SliderVertical} />
            <{SliderControlled} />
            <{SliderDisabled} />
        </{ExampleWrapper}>
    """


def SliderBasic():
    return t"""
        <{Example} title="Basic">
            <{Slider} defaultValue={50} max={100} step={1} />
        </{Example}>
    """


def SliderRange():
    return t"""
        <{Example} title="Range">
            <{Slider} defaultValue={[25, 50]} max={100} step={5} />
        </{Example}>
    """


def SliderMultiple():
    return t"""
        <{Example} title="Multiple Thumbs">
            <{Slider} defaultValue={[10, 20, 70]} max={100} step={10} />
        </{Example}>
    """


def SliderVertical():
    return t"""
        <{Example} title="Vertical">
            <div class="flex items-center gap-6">
                <{Slider} defaultValue={[50]} max={100} step={1} orientation="vertical" class="h-40" />
                <{Slider} defaultValue={[25]} max={100} step={1} orientation="vertical" class="h-40" />
            </div>
        </{Example}>
    """


def SliderControlled():
    value, set_value = use_state([0.3, 0.7])

    return t"""
        <{Example} title="Controlled">
            <div class="grid w-full gap-3">
                <div class="flex items-center justify-between gap-2">
                    <{Label} for="slider-demo-temperature">Temperature</{Label}>
                    <span class="text-sm text-muted-foreground">{", ".join(value)}</span>
                </div>
                <{Slider}
                    id="slider-demo-temperature"
                    value={value}
                    onValueChange={(lambda value: set_value(value))}
                    min={0}
                    max={1}
                    step={0.1}
                />
            </div>
        </{Example}>
    """


def SliderDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Slider} defaultValue={[50]} max={100} step={1} disabled />
        </{Example}>
    """
