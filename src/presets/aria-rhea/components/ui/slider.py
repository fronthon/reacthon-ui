from utils import cn

__js__ = {"react-aria-components": ["SliderFill", "Slider as SliderPrimitive", "SliderThumb", "SliderTrack"]}


def Slider(className=None, **props):
    def callback(props):
        state = props.get("state")

        return t"""
            <{SliderTrack}
                data-slot="slider-track"
                class="relative grow overflow-hidden rounded-2xl bg-input/90 select-none data-horizontal:h-1 data-horizontal:w-full data-vertical:h-full data-vertical:w-1"
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
                    class="block size-4 shrink-0 rounded-2xl bg-white shadow-md ring-1 ring-black/10 transition-[color,box-shadow] duration-200 select-none not-dark:bg-clip-padding group-data-horizontal:top-[50%] group-data-vertical:left-[50%] hover:ring-4 hover:ring-ring/30 focus-visible:ring-4 focus-visible:ring-ring/30 focus-visible:outline-hidden disabled:pointer-events-none disabled:opacity-50"
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
