from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle
from spinner import Spinner


def SyncingState():
    return t"""
        <{Card}>
            <{CardContent} class="p-0">
                <{Empty} class="p-4">
                    <{EmptyHeader}>
                        <{EmptyMedia} variant="icon">
                            <{Spinner} />
                        </{EmptyMedia}>
                        <{EmptyTitle}>Syncing your accounts</{EmptyTitle}>
                        <{EmptyDescription}>
                            We're pulling in your latest transactions. This usually takes a few seconds.
                        </{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button} variant="outline">Cancel</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
