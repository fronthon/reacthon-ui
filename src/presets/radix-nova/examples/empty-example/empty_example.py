from example import Example, ExampleWrapper
from button import Button
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle
from input_group import InputGroup, InputGroupAddon, InputGroupInput
from kbd import Kbd

__js__ = {"lucide-react": ["ArrowUpRightIcon", "CircleDashedIcon", "FolderIcon", "PlusIcon"]}


def EmptyExample():
    return t"""
        <{ExampleWrapper} class="grid-cols-1!">
            <{EmptyBasic} />
            <{EmptyWithMutedBackground} />
            <{EmptyWithBorder} />
            <{EmptyWithIcon} />
            <{EmptyWithMutedBackgroundAlt} />
            <{EmptyInCard} />
        </{ExampleWrapper}>
    """


def EmptyBasic():
    return t"""
        <{Example} title="Basic">
            <{Empty}>
                <{EmptyHeader}>
                    <{EmptyTitle}>No projects yet</{EmptyTitle}>
                    <{EmptyDescription}>
                        You haven't created any projects yet. Get started by creating your first project.
                    </{EmptyDescription}>
                </{EmptyHeader}>
                <{EmptyContent}>
                    <div class="flex gap-2">
                        <{Button} asChild>
                            <a href="#">Create project</a>
                        </{Button}>
                        <{Button} variant="outline">Import project</{Button}>
                    </div>
                    <{Button} variant="link" asChild class="text-muted-foreground">
                        <a href="#">
                            Learn more{" "}
                            <{ArrowUpRightIcon} />
                        </a>
                    </{Button}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """


def EmptyWithMutedBackground():
    return t"""
        <{Example} title="With Muted Background">
            <{Empty} class="bg-muted">
                <{EmptyHeader}>
                    <{EmptyTitle}>No results found</{EmptyTitle}>
                    <{EmptyDescription}>
                        No results found for your search. Try adjusting your search terms.
                    </{EmptyDescription}>
                </{EmptyHeader}>
                <{EmptyContent}>
                    <{Button}>Try again</{Button}>
                    <{Button} variant="link" asChild class="text-muted-foreground">
                        <a href="#">
                            Learn more{" "}
                            <{ArrowUpRightIcon} />
                        </a>
                    </{Button}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """


def EmptyWithBorder():
    return t"""
        <{Example} title="With Border">
            <{Empty} class="border">
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
                            <{CircleDashedIcon} />
                        </{InputGroupAddon}>
                        <{InputGroupAddon} align="inline-end">
                            <{Kbd}>/</{Kbd}>
                        </{InputGroupAddon}>
                    </{InputGroup}>
                    <{EmptyDescription}>
                        Need help? <a href="#">Contact support</a>
                    </{EmptyDescription}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """


def EmptyWithIcon():
    return t"""
        <{Example} title="With Icon">
            <{Empty} class="border">
                <{EmptyHeader}>
                    <{EmptyMedia} variant="icon">
                        <{FolderIcon} />
                    </{EmptyMedia}>
                    <{EmptyTitle}>Nothing to see here</{EmptyTitle}>
                    <{EmptyDescription}>
                        No posts have been created yet. Get started by{" "}
                        <a href="#">creating your first post</a>.
                    </{EmptyDescription}>
                </{EmptyHeader}>
                <{EmptyContent}>
                    <{Button} variant="outline">
                        <{PlusIcon} data-icon="inline-start" />
                        New Post
                    </{Button}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """


def EmptyWithMutedBackgroundAlt():
    return t"""
        <{Example} title="With Muted Background Alt">
            <{Empty} class="bg-muted/50">
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
                            <{CircleDashedIcon} />
                        </{InputGroupAddon}>
                        <{InputGroupAddon} align="inline-end">
                            <{Kbd}>/</{Kbd}>
                        </{InputGroupAddon}>
                    </{InputGroup}>
                    <{EmptyDescription}>
                        Need help? <a href="#">Contact support</a>
                    </{EmptyDescription}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """


def EmptyInCard():
    return t"""
        <{Example} title="In Card">
            <{Empty}>
                <{EmptyHeader}>
                    <{EmptyMedia} variant="icon">
                        <{FolderIcon} />
                    </{EmptyMedia}>
                    <{EmptyTitle}>No projects yet</{EmptyTitle}>
                    <{EmptyDescription}>
                        You haven't created any projects yet. Get started by creating your first project.
                    </{EmptyDescription}>
                </{EmptyHeader}>
                <{EmptyContent}>
                    <div class="flex gap-2">
                        <{Button} asChild>
                            <a href="#">Create project</a>
                        </{Button}>
                        <{Button} variant="outline">Import project</{Button}>
                    </div>
                    <{Button} variant="link" asChild class="text-muted-foreground">
                        <a href="#">
                            Learn more{" "}
                            <{ArrowUpRightIcon} />
                        </a>
                    </{Button}>
                </{EmptyContent}>
            </{Empty}>
        </{Example}>
    """
