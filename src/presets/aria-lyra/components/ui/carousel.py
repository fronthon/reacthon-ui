from javascript import NULL
from reacthon import create_context, use_callback, use_context, use_effect, use_state
from utils import cn
from button import Button

__js__ = {
    "embla-carousel-react": ["default as useEmblaCarousel"],
    "lucide-react": ["ChevronLeftIcon", "ChevronRightIcon"],
}

CarouselContext = create_context(NULL)


def use_carousel():
    context = use_context(CarouselContext)

    if not context:
        raise RuntimeError("useCarousel must be used within a <Carousel />")

    return context


def Carousel(orientation="horizontal", opts=None, setApi=None, plugins=None, className=None, children=None, **props):
    carousel_ref, api = useEmblaCarousel(
        {**(opts or {}), "axis": "x" if orientation == "horizontal" else "y"},
        plugins,
    )
    can_scroll_prev, set_can_scroll_prev = use_state(False)
    can_scroll_next, set_can_scroll_next = use_state(False)

    def on_select(api):
        if not api:
            return
        set_can_scroll_prev(api.canScrollPrev())
        set_can_scroll_next(api.canScrollNext())

    on_select = use_callback(on_select, [])

    def scroll_prev():
        if api:
            api.scrollPrev()

    scroll_prev = use_callback(scroll_prev, [api])

    def scroll_next():
        if api:
            api.scrollNext()

    scroll_next = use_callback(scroll_next, [api])

    def handle_key_down(event):
        if event.key == "ArrowLeft":
            event.preventDefault()
            scroll_prev()
        elif event.key == "ArrowRight":
            event.preventDefault()
            scroll_next()

    handle_key_down = use_callback(handle_key_down, [scroll_prev, scroll_next])

    def effect():
        if not api or not setApi:
            return
        setApi(api)

    use_effect(effect, [api, setApi])

    def effect_2():
        if not api:
            return
        on_select(api)
        api.on("reInit", on_select)
        api.on("select", on_select)

        def cleanup():
            api.off("select", on_select)

        return cleanup

    use_effect(effect_2, [api, on_select])

    return t"""
        <{CarouselContext.Provider} value={ {
            "carouselRef": carousel_ref,
            "api": api,
            "opts": opts,
            "orientation": orientation or ("vertical" if (opts.get("axis") if opts else None) == "y" else "horizontal"),
            "scrollPrev": scroll_prev,
            "scrollNext": scroll_next,
            "canScrollPrev": can_scroll_prev,
            "canScrollNext": can_scroll_next,
        } }>
            <div
                onKeyDownCapture={handle_key_down}
                class={cn("relative", className)}
                role="region"
                aria-roledescription="carousel"
                data-slot="carousel"
                ...{props}
            >
                {children}
            </div>
        </{CarouselContext.Provider}>
    """


def CarouselContent(className=None, **props):
    carousel = use_carousel()
    carousel_ref, orientation = carousel.get("carouselRef"), carousel.get("orientation")

    return t"""
        <div ref={carousel_ref} class="overflow-hidden" data-slot="carousel-content">
            <div class={cn("flex", "-ml-4" if orientation == "horizontal" else "-mt-4 flex-col", className)} ...{props} />
        </div>
    """


def CarouselItem(className=None, **props):
    orientation = use_carousel().get("orientation")

    return t"""
        <div
            role="group"
            aria-roledescription="slide"
            data-slot="carousel-item"
            class={cn("min-w-0 shrink-0 grow-0 basis-full", "pl-4" if orientation == "horizontal" else "pt-4", className)}
            ...{props}
        />
    """


def CarouselPrevious(className=None, variant="outline", size="icon-sm", **props):
    carousel = use_carousel()
    orientation, scroll_prev, can_scroll_prev = carousel.get("orientation"), carousel.get("scrollPrev"), carousel.get("canScrollPrev")

    return t"""
        <{Button}
            data-slot="carousel-previous"
            variant={variant}
            size={size}
            class={cn("absolute touch-manipulation", "inset-y-0 -left-12 my-auto" if orientation == "horizontal" else "-top-12 left-1/2 -translate-x-1/2 rotate-90", className)}
            isDisabled={not can_scroll_prev}
            onPress={scroll_prev}
            ...{props}
        >
            <{ChevronLeftIcon} />
            <span class="sr-only">Previous slide</span>
        </{Button}>
    """


def CarouselNext(className=None, variant="outline", size="icon-sm", **props):
    carousel = use_carousel()
    orientation, scroll_next, can_scroll_next = carousel.get("orientation"), carousel.get("scrollNext"), carousel.get("canScrollNext")

    return t"""
        <{Button}
            data-slot="carousel-next"
            variant={variant}
            size={size}
            class={cn("absolute touch-manipulation", "inset-y-0 -right-12 my-auto" if orientation == "horizontal" else "-bottom-12 left-1/2 -translate-x-1/2 rotate-90", className)}
            isDisabled={not can_scroll_next}
            onPress={scroll_next}
            ...{props}
        >
            <{ChevronRightIcon} />
            <span class="sr-only">Next slide</span>
        </{Button}>
    """
