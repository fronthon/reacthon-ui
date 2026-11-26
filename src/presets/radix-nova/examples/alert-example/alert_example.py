from example import Example, ExampleWrapper
from alert import Alert, AlertAction, AlertDescription, AlertTitle
from badge import Badge
from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldGroup, FieldLabel
from input import Input
from item import Item, ItemContent, ItemDescription, ItemMedia, ItemTitle
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue

__js__ = {"lucide-react": ["CircleAlertIcon", "FolderIcon"]}


def AlertExample():
    return t"""
        <{ExampleWrapper} class="lg:grid-cols-1">
            <{AlertExample1} />
            <{AlertExample2} />
            <{AlertExample3} />
            <{AlertExample4} />
            <{AlertExample5} />
        </{ExampleWrapper}>
    """


def AlertExample1():
    return t"""
        <{Example} title="Basic" class="style-sera:bg-transparent">
            <div class="mx-auto flex w-full max-w-lg flex-col gap-4">
                <{Alert}>
                    <{AlertTitle}>Success! Your changes have been saved.</{AlertTitle}>
                </{Alert}>
                <{Alert}>
                    <{AlertTitle}>Success! Your changes have been saved.</{AlertTitle}>
                    <{AlertDescription}>This is an alert with title and description.</{AlertDescription}>
                </{Alert}>
                <{Alert}>
                    <{AlertDescription}>This one has a description only. No title. No icon.</{AlertDescription}>
                </{Alert}>
            </div>
        </{Example}>
    """


def AlertExample2():
    return t"""
        <{Example} title="With Icons" class="style-sera:bg-transparent">
            <div class="mx-auto flex w-full max-w-lg flex-col gap-4">
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertTitle}>
                        Let's try one with icon, title and a <a href="#">link</a>.
                    </{AlertTitle}>
                </{Alert}>
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertDescription}>
                        This one has an icon and a description only. No title.{" "}
                        <a href="#">But it has a link</a> and a <a href="#">second link</a>.
                    </{AlertDescription}>
                </{Alert}>
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertTitle}>Success! Your changes have been saved</{AlertTitle}>
                    <{AlertDescription}>This is an alert with icon, title and description.</{AlertDescription}>
                </{Alert}>
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertTitle}>
                        This is a very long alert title that demonstrates how the component handles extended text content and potentially wraps across multiple lines
                    </{AlertTitle}>
                </{Alert}>
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertDescription}>
                        This is a very long alert description that demonstrates how the component handles extended text content and potentially wraps across multiple lines
                    </{AlertDescription}>
                </{Alert}>
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertTitle}>
                        This is an extremely long alert title that spans multiple lines to demonstrate how the component handles very lengthy headings while maintaining readability and proper text wrapping behavior
                    </{AlertTitle}>
                    <{AlertDescription}>
                        This is an equally long description that contains detailed information about the alert. It shows how the component can accommodate extensive content while preserving proper spacing, alignment, and readability across different screen sizes and viewport widths. This helps ensure the user experience remains consistent regardless of the content length.
                    </{AlertDescription}>
                </{Alert}>
            </div>
        </{Example}>
    """


def AlertExample3():
    return t"""
        <{Example} title="Destructive" class="style-sera:bg-transparent">
            <div class="mx-auto flex w-full max-w-lg flex-col gap-4">
                <{Alert} variant="destructive">
                    <{CircleAlertIcon} />
                    <{AlertTitle}>Something went wrong!</{AlertTitle}>
                    <{AlertDescription}>Your session has expired. Please log in again.</{AlertDescription}>
                </{Alert}>
                <{Alert} variant="destructive">
                    <{CircleAlertIcon} />
                    <{AlertTitle}>Unable to process your payment.</{AlertTitle}>
                    <{AlertDescription}>
                        <p>
                            Please verify your <a href="#">billing information</a> and try again.
                        </p>
                        <ul class="list-inside list-disc">
                            <li>Check your card details</li>
                            <li>Ensure sufficient funds</li>
                            <li>Verify billing address</li>
                        </ul>
                    </{AlertDescription}>
                </{Alert}>
            </div>
        </{Example}>
    """


def AlertExample4():
    return t"""
        <{Example} title="With Actions" class="style-sera:bg-transparent">
            <div class="mx-auto flex w-full max-w-lg flex-col gap-4">
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertTitle}>The selected emails have been marked as spam.</{AlertTitle}>
                    <{AlertAction}>
                        <{Button} size="xs">Undo</{Button}>
                    </{AlertAction}>
                </{Alert}>
                <{Alert}>
                    <{CircleAlertIcon} />
                    <{AlertTitle}>The selected emails have been marked as spam.</{AlertTitle}>
                    <{AlertDescription}>
                        This is a very long alert title that demonstrates how the component handles extended text content.
                    </{AlertDescription}>
                    <{AlertAction}>
                        <{Badge} variant="secondary">Badge</{Badge}>
                    </{AlertAction}>
                </{Alert}>
            </div>
        </{Example}>
    """


def AlertExample5():
    return t"""
        <{Example} title="Inside Card" class="style-sera:bg-transparent">
            <{Card} class="mx-auto w-full max-w-lg">
                <{CardHeader}>
                    <{CardTitle}>Create project</{CardTitle}>
                    <{CardDescription}>Fill in the form below to create a new project.</{CardDescription}>
                </{CardHeader}>
                <{CardContent} class="flex flex-col gap-4 style-sera:gap-8">
                    <{Alert}>
                        <{CircleAlertIcon} />
                        <{AlertTitle}>You have reached the limit of 3 free projects.</{AlertTitle}>
                        <{AlertDescription}>Upgrade to Pro to create unlimited projects.</{AlertDescription}>
                    </{Alert}>
                    <{FieldGroup}>
                        <{Field}>
                            <{FieldLabel} for="project-name">Name</{FieldLabel}>
                            <{Input} id="project-name" placeholder="My project" />
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="project-framework">Framework</{FieldLabel}>
                            <{Select}>
                                <{SelectTrigger} id="project-framework">
                                    <{SelectValue} placeholder="Select a framework" />
                                </{SelectTrigger}>
                                <{SelectContent}>
                                    <{SelectGroup}>
                                        <{SelectItem} value="next">Next.js</{SelectItem}>
                                        <{SelectItem} value="remix">Remix</{SelectItem}>
                                        <{SelectItem} value="astro">Astro</{SelectItem}>
                                        <{SelectItem} value="nuxt">Nuxt</{SelectItem}>
                                    </{SelectGroup}>
                                </{SelectContent}>
                            </{Select}>
                        </{Field}>
                    </{FieldGroup}>
                    <{Item} variant="outline">
                        <{ItemMedia} variant="image" class="border">
                            <{FolderIcon} />
                        </{ItemMedia}>
                        <{ItemContent}>
                            <{ItemTitle}>Project Alpha</{ItemTitle}>
                            <{ItemDescription}>Created 2 days ago</{ItemDescription}>
                        </{ItemContent}>
                    </{Item}>
                </{CardContent}>
                <{CardFooter}>
                    <{Button} class="w-full">Create project</{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """
