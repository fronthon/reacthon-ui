from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyTitle
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from kbd import Kbd

__js__ = {"lucide-react": ["SearchIcon"]}


def NotFound():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Empty} class="h-72">
                    <{EmptyHeader}>
                        <{EmptyTitle}>404 - Not Found</{EmptyTitle}>
                        <{EmptyDescription}>
                            The page you're looking for doesn't exist. Try searching for what you need below.
                        </{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{InputGroup} class="w-3/4">
                            <{InputGroupInput} placeholder="Try searching for pages..." />
                            <{InputGroupAddon}>
                                <{SearchIcon} />
                            </{InputGroupAddon}>
                            <{InputGroupAddon} align="inline-end">
                                <{Kbd}>/</{Kbd}>
                            </{InputGroupAddon}>
                        </{InputGroup}>
                        <{Button} variant="link">Go to homepage</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
