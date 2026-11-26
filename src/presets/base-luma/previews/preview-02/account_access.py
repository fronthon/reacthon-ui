from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldGroup, FieldLabel
from input import Input
from item import Item, ItemContent, ItemDescription, ItemMedia, ItemTitle

__js__ = {"lucide-react": ["AlertCircleIcon", "ArrowRightIcon", "LockKeyholeIcon"]}


def AccountAccess():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Account Access</{CardTitle}>
                <{CardDescription}>Update your credentials or re-authenticate.</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="email-address">Email Address</{FieldLabel}>
                        <{Input} id="email-address" type="email" defaultValue="artist@studio.inc" />
                    </{Field}>
                    <{Field}>
                        <div class="flex items-center justify-between">
                            <{FieldLabel} for="current-password">Current Password</{FieldLabel}>
                            <a
                                href="#"
                                class="text-xs font-medium tracking-wider text-muted-foreground uppercase hover:text-foreground"
                            >
                                Forgot?
                            </a>
                        </div>
                        <{Input} id="current-password" type="password" defaultValue="password123" />
                    </{Field}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter} class="flex-col gap-4">
                <{Button} class="w-full">
                    <{LockKeyholeIcon} />
                    Update Security
                </{Button}>
                <{Item} variant="muted" render={t'<a href="#" />'}>
                    <{ItemMedia} variant="icon">
                        <{AlertCircleIcon} class="text-destructive" />
                    </{ItemMedia}>
                    <{ItemContent}>
                        <{ItemTitle}>Danger Zone</{ItemTitle}>
                        <{ItemDescription} class="line-clamp-1">Archive account and remove catalog</{ItemDescription}>
                    </{ItemContent}>
                    <{ArrowRightIcon} class="size-4" />
                </{Item}>
            </{CardFooter}>
        </{Card}>
    """
