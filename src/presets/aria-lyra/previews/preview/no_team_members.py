from avatar import Avatar, AvatarFallback, AvatarGroup, AvatarImage
from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle


def NoTeamMembers():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Empty} class="h-56 border">
                    <{EmptyHeader}>
                        <{EmptyMedia}>
                            <{AvatarGroup} class="grayscale">
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
                        </{EmptyMedia}>
                        <{EmptyTitle}>No Team Members</{EmptyTitle}>
                        <{EmptyDescription}>Invite your team to collaborate on this project.</{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button} size="sm">Invite Members</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
