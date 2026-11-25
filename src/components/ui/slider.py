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
                class="relative grow overflow-hidden rounded-full bg-muted data-horizontal:h-1 data-horizontal:w-full data-vertical:h-full data-vertical:w-1"
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
                    class="relative block size-3 shrink-0 rounded-full border border-ring bg-white ring-ring/50 transition-[color,box-shadow] select-none after:absolute after:-inset-2 hover:ring-3 focus-visible:ring-3 focus-visible:outline-hidden active:ring-3 disabled:pointer-events-none disabled:opacity-50"
                />
            ''' for index in range(len(_values))]}
        </{SliderPrimitive.Root}>
    """
