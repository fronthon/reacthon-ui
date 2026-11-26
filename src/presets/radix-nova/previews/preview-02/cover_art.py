from button import Button
from card import Card, CardContent, CardDescription, CardFooter
from item import Item
from label import Label

__js__ = {"lucide-react": ["ImageIcon"]}


def CoverArt():
    return t"""
        <{Card}>
            <{CardContent} class="flex flex-col gap-3">
                <{Label}
                    for="cover-art"
                    class="text-center text-xs font-normal tracking-wider text-muted-foreground uppercase"
                >
                    Cover Art
                </{Label}>
                <{Item} class="aspect-square" variant="outline">
                    <label for="cover-art" class="flex size-full cursor-pointer items-center justify-center">
                        <{ImageIcon} class="size-10 text-muted-foreground/50" />
                    </label>
                </{Item}>
                <input id="cover-art" type="file" accept="image/jpeg,image/png" class="sr-only" />
            </{CardContent}>
            <{CardFooter} class="flex-col gap-2">
                <{Button} variant="secondary" class="w-full" asChild>
                    <label for="cover-art" class="cursor-pointer">Upload Artwork</label>
                </{Button}>
                <{CardDescription} class="text-center text-xs">
                    Minimum 3000 × 3000px
                    <br />
                    JPEG or PNG only
                </{CardDescription}>
            </{CardFooter}>
        </{Card}>
    """
