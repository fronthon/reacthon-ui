from utils import cn

__js__ = {"react-aria-components": ["SliderFill", "Slider as SliderPrimitive", "SliderThumb", "SliderTrack"]}


def Slider(className=None, **props):
    def callback(props):
        state = props.get("state")

        return t"""
            <{SliderTrack}
                data-slot="slider-track"
                class="relative grow overflow-hidden rounded-4xl bg-muted select-none data-horizontal:h-3 data-horizontal:w-full data-vertical:h-full data-vertical:w-3"
            >
                <{SliderFill}
                    data-slot="slider-range"
                    class="absolute bg-primary select-none data-horizontal:h-full data-vertical:w-full"
                />
            </{SliderTrack}>
            {[t'''
                <{SliderThumb}
                    data-slot="slider-thumb"
                    key={index}
                    index={index}
                    class="block size-4 shrink-0 rounded-4xl border border-primary bg-white shadow-sm ring-ring/50 transition-colors select-none group-data-horizontal:top-[50%] group-data-vertical:left-[50%] hover:ring-4 focus-visible:ring-4 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50"
                />
            ''' for index, _ in enumerate(state.values)]}
        """

    return t"""
        <{SliderPrimitive}
            class={cn("group relative flex w-full touch-none items-center select-none data-disabled:opacity-50 data-vertical:h-full data-vertical:min-h-40 data-vertical:w-auto data-vertical:flex-col", className)}
            data-slot="slider"
            ...{props}
        >
            {callback}
        </{SliderPrimitive}>
    """
