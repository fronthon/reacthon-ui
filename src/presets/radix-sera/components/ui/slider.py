from reacthon import use_memo
from utils import cn

__js__ = {"radix-ui": ["Slider as SliderPrimitive"]}


def Slider(className=None, defaultValue=None, value=None, min=0, max=100, **props):
    _values = use_memo(
        lambda: value if isinstance(value, list) else defaultValue if isinstance(defaultValue, list) else [min, max],
        [value, defaultValue, min, max],
    )

    return t"""
        <{SliderPrimitive.Root}
            data-slot="slider"
            defaultValue={defaultValue}
            value={value}
            min={min}
            max={max}
            class={cn("relative flex w-full touch-none items-center select-none data-disabled:opacity-50 data-vertical:h-full data-vertical:min-h-40 data-vertical:w-auto data-vertical:flex-col", className)}
            ...{props}
        >
            <{SliderPrimitive.Track}
                data-slot="slider-track"
                class="relative grow overflow-hidden bg-input/50 data-horizontal:h-0.5 data-horizontal:w-full data-vertical:h-full data-vertical:w-0.5"
            >
                <{SliderPrimitive.Range}
                    data-slot="slider-range"
                    class="absolute bg-primary select-none data-horizontal:h-full data-vertical:w-full"
                />
            </{SliderPrimitive.Track}>
            {[t'''
                <{SliderPrimitive.Thumb}
                    data-slot="slider-thumb"
                    key={index}
                    class="block size-3 shrink-0 border-none bg-primary transition-colors select-none hover:ring-2 hover:ring-ring/30 focus-visible:ring-2 focus-visible:ring-ring/30 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50"
                />
            ''' for index in range(len(_values))]}
        </{SliderPrimitive.Root}>
    """
