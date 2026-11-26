from example import Example, ExampleWrapper
from card import Card, CardContent, CardHeader
from skeleton import Skeleton


def SkeletonExample():
    return t"""
        <{ExampleWrapper}>
            <{SkeletonAvatar} />
            <{SkeletonCard} />
            <{SkeletonText} />
            <{SkeletonForm} />
            <{SkeletonTable} />
        </{ExampleWrapper}>
    """


def SkeletonAvatar():
    return t"""
        <{Example} title="Avatar">
            <div class="flex w-full items-center gap-4">
                <{Skeleton} class="size-10 shrink-0 rounded-full" />
                <div class="grid gap-2">
                    <{Skeleton} class="h-4 w-[150px]" />
                    <{Skeleton} class="h-4 w-[100px]" />
                </div>
            </div>
        </{Example}>
    """


def SkeletonCard():
    return t"""
        <{Example} title="Card">
            <{Card} class="w-full">
                <{CardHeader}>
                    <{Skeleton} class="h-4 w-2/3" />
                    <{Skeleton} class="h-4 w-1/2" />
                </{CardHeader}>
                <{CardContent}>
                    <{Skeleton} class="aspect-square w-full" />
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def SkeletonText():
    return t"""
        <{Example} title="Text">
            <div class="flex w-full flex-col gap-2">
                <{Skeleton} class="h-4 w-full" />
                <{Skeleton} class="h-4 w-full" />
                <{Skeleton} class="h-4 w-3/4" />
            </div>
        </{Example}>
    """


def SkeletonForm():
    return t"""
        <{Example} title="Form">
            <div class="flex w-full flex-col gap-7">
                <div class="flex flex-col gap-3">
                    <{Skeleton} class="h-4 w-20" />
                    <{Skeleton} class="h-10 w-full" />
                </div>
                <div class="flex flex-col gap-3">
                    <{Skeleton} class="h-4 w-24" />
                    <{Skeleton} class="h-10 w-full" />
                </div>
                <{Skeleton} class="h-9 w-24" />
            </div>
        </{Example}>
    """


def SkeletonTable():
    return t"""
        <{Example} title="Table">
            <div class="flex w-full flex-col gap-2">
                <div class="flex gap-4">
                    <{Skeleton} class="h-4 flex-1" />
                    <{Skeleton} class="h-4 w-24" />
                    <{Skeleton} class="h-4 w-20" />
                </div>
                <div class="flex gap-4">
                    <{Skeleton} class="h-4 flex-1" />
                    <{Skeleton} class="h-4 w-24" />
                    <{Skeleton} class="h-4 w-20" />
                </div>
                <div class="flex gap-4">
                    <{Skeleton} class="h-4 flex-1" />
                    <{Skeleton} class="h-4 w-24" />
                    <{Skeleton} class="h-4 w-20" />
                </div>
            </div>
        </{Example}>
    """
