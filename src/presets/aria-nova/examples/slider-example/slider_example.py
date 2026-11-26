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
            <{Slider} aria-label="Basic slider" defaultValue={50} maxValue={100} step={1} />
        </{Example}>
    """


def SliderRange():
    return t"""
        <{Example} title="Range">
            <{Slider} aria-label="Range slider" defaultValue={[25, 50]} maxValue={100} step={5} />
        </{Example}>
    """


def SliderMultiple():
    return t"""
        <{Example} title="Multiple Thumbs">
            <{Slider} aria-label="Multiple thumbs slider" defaultValue={[10, 20, 70]} maxValue={100} step={10} />
        </{Example}>
    """


def SliderVertical():
    return t"""
        <{Example} title="Vertical">
            <div class="flex items-center gap-6">
                <{Slider}
                    aria-label="Vertical slider"
                    defaultValue={[50]}
                    maxValue={100}
                    step={1}
                    orientation="vertical"
                    class="h-40"
                />
                <{Slider}
                    aria-label="Vertical slider"
                    defaultValue={[25]}
                    maxValue={100}
                    step={1}
                    orientation="vertical"
                    class="h-40"
                />
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
                    <span class="text-sm text-muted-foreground">{", ".join(str(one) for one in value)}</span>
                </div>
                <{Slider}
                    aria-label="Controlled slider"
                    id="slider-demo-temperature"
                    value={value}
                    onChange={set_value}
                    minValue={0}
                    maxValue={1}
                    step={0.1}
                />
            </div>
        </{Example}>
    """


def SliderDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Slider} aria-label="Disabled slider" defaultValue={[50]} maxValue={100} step={1} isDisabled />
        </{Example}>
    """
