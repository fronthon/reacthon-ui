from utils import cn

__js__ = {"@base-ui/react/slider": ["Slider as SliderPrimitive"]}


def Slider(className=None, defaultValue=None, value=None, min=0, max=100, **props):
    _values = value if isinstance(value, list) else defaultValue if isinstance(defaultValue, list) else [min, max]

    return t"""
        <{SliderPrimitive.Root}
            class={cn("data-horizontal:w-full data-vertical:h-full", className)}
            data-slot="slider"
            defaultValue={defaultValue}
            value={value}
            min={min}
            max={max}
            thumbAlignment="edge"
            ...{props}
        >
            <{SliderPrimitive.Control} class="relative flex w-full touch-none items-center select-none data-disabled:opacity-50 data-vertical:h-full data-vertical:min-h-40 data-vertical:w-auto data-vertical:flex-col">
                <{SliderPrimitive.Track}
                    data-slot="slider-track"
                    class="relative grow overflow-hidden rounded-full bg-muted select-none data-horizontal:h-1.5 data-horizontal:w-full data-vertical:h-full data-vertical:w-1.5"
                >
                    <{SliderPrimitive.Indicator}
                        data-slot="slider-range"
                        class="bg-primary select-none data-horizontal:h-full data-vertical:w-full"
                    />
                </{SliderPrimitive.Track}>
                {[t'''
                    <{SliderPrimitive.Thumb}
                        data-slot="slider-thumb"
                        key={index}
                        class="block size-4 shrink-0 rounded-full border border-primary bg-white shadow-sm ring-ring/50 transition-[color,box-shadow] select-none hover:ring-4 focus-visible:ring-4 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50"
                    />
                ''' for index in range(len(_values))]}
            </{SliderPrimitive.Control}>
        </{SliderPrimitive.Root}>
    """
