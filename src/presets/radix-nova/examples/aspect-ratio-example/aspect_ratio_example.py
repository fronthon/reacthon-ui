from example import Example, ExampleWrapper
from aspect_ratio import AspectRatio

__js__ = {"next/image": ["default as Image"]}


def AspectRatioExample():
    return t"""
        <{ExampleWrapper} class="max-w-4xl 2xl:max-w-4xl">
            <{AspectRatio16x9} />
            <{AspectRatio21x9} />
            <{AspectRatio1x1} />
            <{AspectRatio9x16} />
        </{ExampleWrapper}>
    """


def AspectRatio16x9():
    return t"""
        <{Example} title="16:9" class="items-center justify-center">
            <{AspectRatio}
                ratio={16 / 9}
                class="rounded-lg bg-muted style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
            >
                <{Image}
                    src="https://avatar.vercel.sh/shadcn1"
                    alt="Photo"
                    fill
                    class="h-full w-full rounded-lg object-cover grayscale dark:brightness-20 style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
                />
            </{AspectRatio}>
        </{Example}>
    """


def AspectRatio1x1():
    return t"""
        <{Example} title="1:1" class="items-start">
            <{AspectRatio}
                ratio={1 / 1}
                class="rounded-lg bg-muted style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
            >
                <{Image}
                    src="https://avatar.vercel.sh/shadcn1"
                    alt="Photo"
                    fill
                    class="h-full w-full rounded-lg object-cover grayscale dark:brightness-20 style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
                />
            </{AspectRatio}>
        </{Example}>
    """


def AspectRatio9x16():
    return t"""
        <{Example} title="9:16" class="items-center justify-center">
            <{AspectRatio}
                ratio={9 / 16}
                class="rounded-lg bg-muted style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
            >
                <{Image}
                    src="https://avatar.vercel.sh/shadcn1"
                    alt="Photo"
                    fill
                    class="h-full w-full rounded-lg object-cover grayscale dark:brightness-20 style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
                />
            </{AspectRatio}>
        </{Example}>
    """


def AspectRatio21x9():
    return t"""
        <{Example} title="21:9" class="items-center justify-center">
            <{AspectRatio}
                ratio={21 / 9}
                class="rounded-lg bg-muted style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
            >
                <{Image}
                    src="https://avatar.vercel.sh/shadcn1"
                    alt="Photo"
                    fill
                    class="h-full w-full rounded-lg object-cover grayscale dark:brightness-20 style-lyra:rounded-none style-luma:rounded-3xl style-sera:rounded-none"
                />
            </{AspectRatio}>
        </{Example}>
    """
