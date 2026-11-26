from example import Example, ExampleWrapper
from avatar import Avatar, AvatarBadge, AvatarFallback, AvatarGroup, AvatarGroupCount, AvatarImage
from button import Button
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle

__js__ = {"lucide-react": ["PlusIcon", "CheckIcon"]}


def AvatarExample():
    return t"""
        <{ExampleWrapper}>
            <{AvatarSizes} />
            <{AvatarWithBadge} />
            <{AvatarWithBadgeIcon} />
            <{AvatarGroupExample} />
            <{AvatarGroupWithCount} />
            <{AvatarGroupWithIconCount} />
            <{AvatarInEmpty} />
        </{ExampleWrapper}>
    """


def AvatarSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-wrap items-center gap-2">
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Avatar} size="sm">
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
            </div>
        </{Example}>
    """


def AvatarWithBadge():
    return t"""
        <{Example} title="Badge">
            <div class="flex flex-wrap items-center gap-2">
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/jorgezreik.png" alt="@jorgezreik" />
                    <{AvatarFallback}>JZ</{AvatarFallback}>
                    <{AvatarBadge} />
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/jorgezreik.png" alt="@jorgezreik" />
                    <{AvatarFallback}>JZ</{AvatarFallback}>
                    <{AvatarBadge} />
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/jorgezreik.png" alt="@jorgezreik" />
                    <{AvatarFallback}>JZ</{AvatarFallback}>
                    <{AvatarBadge} />
                </{Avatar}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Avatar} size="sm">
                    <{AvatarFallback}>JZ</{AvatarFallback}>
                    <{AvatarBadge} />
                </{Avatar}>
                <{Avatar}>
                    <{AvatarFallback}>JZ</{AvatarFallback}>
                    <{AvatarBadge} />
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarFallback}>JZ</{AvatarFallback}>
                    <{AvatarBadge} />
                </{Avatar}>
            </div>
        </{Example}>
    """


def AvatarWithBadgeIcon():
    return t"""
        <{Example} title="Badge with Icon">
            <div class="flex flex-wrap items-center gap-2">
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/pranathip.png" alt="@pranathip" />
                    <{AvatarFallback}>PP</{AvatarFallback}>
                    <{AvatarBadge}>
                        <{PlusIcon} />
                    </{AvatarBadge}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/pranathip.png" alt="@pranathip" />
                    <{AvatarFallback}>PP</{AvatarFallback}>
                    <{AvatarBadge}>
                        <{PlusIcon} />
                    </{AvatarBadge}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/pranathip.png" alt="@pranathip" />
                    <{AvatarFallback}>PP</{AvatarFallback}>
                    <{AvatarBadge}>
                        <{PlusIcon} />
                    </{AvatarBadge}>
                </{Avatar}>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <{Avatar} size="sm">
                    <{AvatarFallback}>PP</{AvatarFallback}>
                    <{AvatarBadge}>
                        <{CheckIcon} />
                    </{AvatarBadge}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarFallback}>PP</{AvatarFallback}>
                    <{AvatarBadge}>
                        <{CheckIcon} />
                    </{AvatarBadge}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarFallback}>PP</{AvatarFallback}>
                    <{AvatarBadge}>
                        <{CheckIcon} />
                    </{AvatarBadge}>
                </{Avatar}>
            </div>
        </{Example}>
    """


def AvatarGroupExample():
    return t"""
        <{Example} title="Group">
            <{AvatarGroup}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
            </{AvatarGroup}>
            <{AvatarGroup}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
            </{AvatarGroup}>
            <{AvatarGroup}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
            </{AvatarGroup}>
        </{Example}>
    """


def AvatarGroupWithCount():
    return t"""
        <{Example} title="Group with Count">
            <{AvatarGroup}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
                <{AvatarGroupCount}>+3</{AvatarGroupCount}>
            </{AvatarGroup}>
            <{AvatarGroup}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
                <{AvatarGroupCount}>+3</{AvatarGroupCount}>
            </{AvatarGroup}>
            <{AvatarGroup}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
                <{AvatarGroupCount}>+3</{AvatarGroupCount}>
            </{AvatarGroup}>
        </{Example}>
    """


def AvatarGroupWithIconCount():
    return t"""
        <{Example} title="Group with Icon Count">
            <{AvatarGroup}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="sm">
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
                <{AvatarGroupCount}>
                    <{PlusIcon} />
                </{AvatarGroupCount}>
            </{AvatarGroup}>
            <{AvatarGroup}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar}>
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
                <{AvatarGroupCount}>
                    <{PlusIcon} />
                </{AvatarGroupCount}>
            </{AvatarGroup}>
            <{AvatarGroup}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" class="grayscale" />
                    <{AvatarFallback}>CN</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" class="grayscale" />
                    <{AvatarFallback}>LR</{AvatarFallback}>
                </{Avatar}>
                <{Avatar} size="lg">
                    <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" class="grayscale" />
                    <{AvatarFallback}>ER</{AvatarFallback}>
                </{Avatar}>
                <{AvatarGroupCount}>
                    <{PlusIcon} />
                </{AvatarGroupCount}>
            </{AvatarGroup}>
        </{Example}>
    """


def AvatarInEmpty():
    return t"""
        <{Example} title="In Empty">
            <{Empty} class="w-full flex-none border">
                <{EmptyHeader}>
                    <{EmptyMedia}>
                        <{AvatarGroup}>
                            <{Avatar} size="lg">
                                <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" class="grayscale" />
                                <{AvatarFallback}>CN</{AvatarFallback}>
                            </{Avatar}>
                            <{Avatar} size="lg">
                                <{AvatarImage} src="https://github.com/maxleiter.png" alt="@maxleiter" class="grayscale" />
                                <{AvatarFallback}>LR</{AvatarFallback}>
                            </{Avatar}>
                            <{Avatar} size="lg">
                                <{AvatarImage}
                                    src="https://github.com/evilrabbit.png"
                                    alt="@evilrabbit"
                                    class="grayscale"
                                />
                                <{AvatarFallback}>ER</{AvatarFallback}>
                            </{Avatar}>
                            <{AvatarGroupCount}>
                                <{PlusIcon} />
                            </{AvatarGroupCount}>
                        </{AvatarGroup}>
                    </{EmptyMedia}>
                    <{EmptyTitle}>No Team Members</{EmptyTitle}>
                    <{EmptyDescription}>Invite your team to collaborate on this project.</{EmptyDescription}>
                </{EmptyHeader}>
                <{EmptyContent}>
                    <{Button}>
                        <{PlusIcon} />
                        Invite Members
                    </{Button}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """
