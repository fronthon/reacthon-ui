from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle

__js__ = {"lucide-react": ["PlusIcon"]}


def EmptyDistributeTrack():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Empty} class="p-4">
                    <{EmptyMedia} variant="icon">
                        <{PlusIcon} />
                    </{EmptyMedia}>
                    <{EmptyHeader}>
                        <{EmptyTitle}>Distribute Track</{EmptyTitle}>
                        <{EmptyDescription}>
                            Upload your first master to start reaching listeners on Spotify, Apple Music, and more.
                        </{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button}>Create Release</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
