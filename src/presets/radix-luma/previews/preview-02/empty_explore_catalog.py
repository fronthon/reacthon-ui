from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle

__js__ = {"lucide-react": ["AudioLinesIcon"]}


def EmptyExploreCatalog():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Empty} class="p-4">
                    <{EmptyMedia} variant="icon">
                        <{AudioLinesIcon} />
                    </{EmptyMedia}>
                    <{EmptyHeader}>
                        <{EmptyTitle}>Explore Catalog</{EmptyTitle}>
                        <{EmptyDescription}>
                            Check your ISRC codes, metadata, and visual assets before going live.
                        </{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button}>View Catalog</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
