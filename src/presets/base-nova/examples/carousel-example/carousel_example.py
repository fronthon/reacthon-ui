from example import Example, ExampleWrapper
from card import Card, CardContent
from carousel import Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious


def CarouselExample():
    return t"""
        <{ExampleWrapper} class="lg:grid-cols-1">
            <{CarouselBasic} />
            <{CarouselMultiple} />
            <{CarouselWithGap} />
        </{ExampleWrapper}>
    """


def CarouselBasic():
    return t"""
        <{Example} title="Basic">
            <{Carousel} class="mx-auto max-w-xs sm:max-w-sm">
                <{CarouselContent}>
                    {[t'''
                        <{CarouselItem} key={index}>
                            <div class="p-1 style-luma:p-2.5">
                                <{Card}>
                                    <{CardContent} class="flex aspect-square items-center justify-center p-6">
                                        <span class="text-4xl font-semibold">{index + 1}</span>
                                    </{CardContent}>
                                </{Card}>
                            </div>
                        </{CarouselItem}>
                    ''' for index in range(5)]}
                </{CarouselContent}>
                <{CarouselPrevious} class="hidden sm:inline-flex" />
                <{CarouselNext} class="hidden sm:inline-flex" />
            </{Carousel}>
        </{Example}>
    """


def CarouselMultiple():
    return t"""
        <{Example} title="Multiple">
            <{Carousel} class="mx-auto max-w-xs sm:max-w-sm" opts={ {"align": "start"} }>
                <{CarouselContent}>
                    {[t'''
                        <{CarouselItem} key={index} class="sm:basis-1/2 lg:basis-1/3">
                            <div class="p-1 style-luma:p-2.5">
                                <{Card}>
                                    <{CardContent} class="flex aspect-square items-center justify-center p-6">
                                        <span class="text-3xl font-semibold">{index + 1}</span>
                                    </{CardContent}>
                                </{Card}>
                            </div>
                        </{CarouselItem}>
                    ''' for index in range(5)]}
                </{CarouselContent}>
                <{CarouselPrevious} class="hidden sm:inline-flex" />
                <{CarouselNext} class="hidden sm:inline-flex" />
            </{Carousel}>
        </{Example}>
    """


def CarouselWithGap():
    return t"""
        <{Example} title="With Gap">
            <{Carousel} class="mx-auto max-w-xs sm:max-w-sm">
                <{CarouselContent} class="-ml-1">
                    {[t'''
                        <{CarouselItem} key={index} class="pl-1 md:basis-1/2">
                            <div class="p-1 style-luma:p-2.5">
                                <{Card}>
                                    <{CardContent} class="flex aspect-square items-center justify-center p-6">
                                        <span class="text-2xl font-semibold">{index + 1}</span>
                                    </{CardContent}>
                                </{Card}>
                            </div>
                        </{CarouselItem}>
                    ''' for index in range(5)]}
                </{CarouselContent}>
                <{CarouselPrevious} class="hidden sm:inline-flex" />
                <{CarouselNext} class="hidden sm:inline-flex" />
            </{Carousel}>
        </{Example}>
    """
