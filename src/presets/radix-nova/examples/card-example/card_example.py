from reacthon import use_state
from example import Example, ExampleWrapper
from avatar import Avatar, AvatarFallback, AvatarGroup, AvatarGroupCount, AvatarImage
from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldGroup, FieldLabel
from input import Input
from toggle_group import ToggleGroup, ToggleGroupItem

__js__ = {"lucide-react": ["CaptionsIcon", "PlusIcon"]}

spacing_options = [
    {"className": "[--card-spacing:--spacing(4)]", "label": "16px", "value": "4"},
    {"className": "[--card-spacing:--spacing(5)]", "label": "20px", "value": "5"},
    {"className": "[--card-spacing:--spacing(6)]", "label": "24px", "value": "6"},
    {"className": "[--card-spacing:--spacing(8)]", "label": "32px", "value": "8"},
]


def CardExample():
    return t"""
        <{ExampleWrapper}>
            <{CardDefault} />
            <{CardSmall} />
            <{CardContentEdgeToEdge} />
            <{CardCustomSpacing} />
            <{CardHeaderWithBorder} />
            <{CardFooterWithBorder} />
            <{CardHeaderWithBorderSmall} />
            <{CardFooterWithBorderSmall} />
            <{CardWithImage} />
            <{CardWithImageSmall} />
            <{CardLogin} />
            <{CardMeetingNotes} />
        </{ExampleWrapper}>
    """


def CardContentEdgeToEdge():
    return t"""
        <{Example} title="Content Edge to Edge">
            <{Card} class="mx-auto w-full max-w-sm">
                <{CardHeader}>
                    <{CardTitle}>Terms of Service</{CardTitle}>
                    <{CardDescription}>Review the terms before accepting the agreement.</{CardDescription}>
                </{CardHeader}>
                <{CardContent} class="-mb-(--card-spacing) px-0">
                    <div class="max-h-48 space-y-4 overflow-y-scroll border-t bg-muted/50 px-(--card-spacing) py-4 text-sm leading-relaxed">
                        <p>
                            These terms govern your use of the workspace, including access to shared documents, project files, and collaboration tools.
                        </p>
                        <p>
                            You are responsible for the content you upload and for ensuring that your team has the appropriate permissions to view or edit it.
                        </p>
                        <p>
                            We may update features or limits as the service evolves. When those changes materially affect your workflow, we will notify your workspace administrators.
                        </p>
                        <p>
                            By continuing, you agree to keep your account credentials secure and to follow your organization's acceptable use policies.
                        </p>
                    </div>
                </{CardContent}>
                <{CardFooter} class="justify-end gap-2">
                    <{Button} variant="outline">Decline</{Button}>
                    <{Button}>Accept</{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardCustomSpacing():
    spacing, set_spacing = use_state("4")
    selected_spacing = next((option for option in spacing_options if option["value"] == spacing), None)

    def on_value_change(value):
        if value:
            set_spacing(value)

    return t"""
        <{Example} title="Custom Spacing">
            <div class="mx-auto grid w-full max-w-sm gap-4">
                <{ToggleGroup}
                    type="single"
                    value={spacing}
                    onValueChange={on_value_change}
                    variant="outline"
                    size="sm"
                    class="justify-center"
                >
                    {[t'''
                        <{ToggleGroupItem}
                            key={option["value"]}
                            value={option["value"]}
                        >
                            {option["label"]}
                        </{ToggleGroupItem}>
                    ''' for option in spacing_options]}
                </{ToggleGroup}>
                <{Card} class={selected_spacing["className"] if selected_spacing else None}>
                    <{CardHeader}>
                        <{CardTitle}>Release Health</{CardTitle}>
                        <{CardDescription}>Track readiness across launch signals.</{CardDescription}>
                    </{CardHeader}>
                    <{CardContent}>
                        <div class="grid gap-2 rounded-lg bg-muted/50 p-3 text-sm style-lyra:rounded-none style-sera:rounded-none">
                            <div class="flex items-center justify-between gap-2">
                                <span class="text-muted-foreground">Checks passed</span>
                                <span class="font-medium">24 / 26</span>
                            </div>
                            <div class="flex items-center justify-between gap-2">
                                <span class="text-muted-foreground">Open blockers</span>
                                <span class="font-medium">2</span>
                            </div>
                        </div>
                    </{CardContent}>
                </{Card}>
            </div>
        </{Example}>
    """


def CardLogin():
    return t"""
        <{Example} title="Login">
            <{Card} class="mx-auto w-full max-w-sm">
                <{CardHeader}>
                    <{CardTitle}>Login to your account</{CardTitle}>
                    <{CardDescription}>Enter your email below to login to your account</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <form>
                        <{FieldGroup}>
                            <{Field}>
                                <{FieldLabel} for="email">Email</{FieldLabel}>
                                <{Input} id="email" type="email" placeholder="m@example.com" required />
                            </{Field}>
                            <{Field}>
                                <div class="flex items-center">
                                    <{FieldLabel} for="password">Password</{FieldLabel}>
                                    <a href="#" class="ml-auto inline-block underline-offset-4 hover:underline">
                                        Forgot your password?
                                    </a>
                                </div>
                                <{Input} id="password" type="password" required />
                            </{Field}>
                        </{FieldGroup}>
                    </form>
                </{CardContent}>
                <{CardFooter} class="flex-col gap-2">
                    <{Button} type="submit" class="w-full">Login</{Button}>
                    <{Button} variant="outline" class="w-full">Login with Google</{Button}>
                    <div class="mt-4 text-center style-nova:mt-2">
                        Don't have an account?{" "}
                        <a href="#" class="underline underline-offset-4">Sign up</a>
                    </div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardMeetingNotes():
    return t"""
        <{Example} title="Meeting Notes">
            <{Card} class="mx-auto w-full max-w-sm">
                <{CardHeader}>
                    <{CardTitle}>Meeting Notes</{CardTitle}>
                    <{CardDescription}>Transcript from the meeting with the client.</{CardDescription}>
                    <{CardAction}>
                        <{Button} variant="outline" size="sm">
                            <{CaptionsIcon} data-icon="inline-start" />
                            Transcribe
                        </{Button}>
                    </{CardAction}>
                </{CardHeader}>
                <{CardContent}>
                    <p>Client requested dashboard redesign with focus on mobile responsiveness.</p>
                    <ol class="mt-4 flex list-decimal flex-col gap-2 pl-6">
                        <li>New analytics widgets for daily/weekly metrics</li>
                        <li>Simplified navigation menu</li>
                        <li>Dark mode support</li>
                        <li>Timeline: 6 weeks</li>
                        <li>Follow-up meeting scheduled for next Tuesday</li>
                    </ol>
                </{CardContent}>
                <{CardFooter}>
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
                        <{AvatarGroupCount}>+8</{AvatarGroupCount}>
                    </{AvatarGroup}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardWithImage():
    return t"""
        <{Example} title="With Image">
            <{Card} size="default" class="relative mx-auto w-full max-w-sm pt-0">
                <div class="absolute inset-0 z-30 aspect-video bg-primary opacity-50 mix-blend-color" />
                <img
                    src="https://images.unsplash.com/photo-1604076850742-4c7221f3101b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    alt="Photo by mymind on Unsplash"
                    title="Photo by mymind on Unsplash"
                    class="relative z-20 aspect-video w-full object-cover brightness-60 grayscale"
                />
                <{CardHeader}>
                    <{CardTitle}>Beautiful Landscape</{CardTitle}>
                    <{CardDescription}>A stunning view that captures the essence of natural beauty.</{CardDescription}>
                </{CardHeader}>
                <{CardFooter}>
                    <{Button} class="w-full">
                        <{PlusIcon} data-icon="inline-start" />
                        Button
                    </{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardWithImageSmall():
    return t"""
        <{Example} title="With Image (Small)">
            <{Card} size="sm" class="relative mx-auto w-full max-w-sm pt-0">
                <div class="absolute inset-0 z-30 aspect-video bg-primary opacity-50 mix-blend-color" />
                <img
                    src="https://images.unsplash.com/photo-1604076850742-4c7221f3101b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
                    alt="Photo by mymind on Unsplash"
                    title="Photo by mymind on Unsplash"
                    class="relative z-20 aspect-video w-full object-cover brightness-60 grayscale"
                />
                <{CardHeader}>
                    <{CardTitle}>Beautiful Landscape</{CardTitle}>
                    <{CardDescription}>A stunning view that captures the essence of natural beauty.</{CardDescription}>
                </{CardHeader}>
                <{CardFooter}>
                    <{Button} size="sm" class="w-full">
                        <{PlusIcon} data-icon="inline-start" />
                        Button
                    </{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardHeaderWithBorder():
    return t"""
        <{Example} title="Header with Border">
            <{Card} class="mx-auto w-full max-w-sm">
                <{CardHeader} class="border-b">
                    <{CardTitle}>Header with Border</{CardTitle}>
                    <{CardDescription}>This is a card with a header that has a bottom border.</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <p>
                        The header has a border-b class applied, creating a visual separation between the header and content sections.
                    </p>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CardFooterWithBorder():
    return t"""
        <{Example} title="Footer with Border">
            <{Card} class="mx-auto w-full max-w-sm">
                <{CardContent}>
                    <p>
                        The footer has a border-t class applied, creating a visual separation between the content and footer sections.
                    </p>
                </{CardContent}>
                <{CardFooter} class="border-t">
                    <{Button} variant="outline" class="w-full">Footer with Border</{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardDefault():
    return t"""
        <{Example} title="Default Size">
            <{Card} size="default" class="mx-auto w-full max-w-sm">
                <{CardHeader}>
                    <{CardTitle}>Default Card</{CardTitle}>
                    <{CardDescription}>This card uses the default size variant.</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <p>
                        The card component supports a size prop that defaults to "default" for standard spacing and sizing.
                    </p>
                </{CardContent}>
                <{CardFooter}>
                    <{Button} variant="outline" class="w-full">Action</{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardSmall():
    return t"""
        <{Example} title="Small Size">
            <{Card} size="sm" class="mx-auto w-full max-w-sm">
                <{CardHeader}>
                    <{CardTitle}>Small Card</{CardTitle}>
                    <{CardDescription}>This card uses the small size variant.</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <p>
                        The card component supports a size prop that can be set to "sm" for a more compact appearance.
                    </p>
                </{CardContent}>
                <{CardFooter}>
                    <{Button} variant="outline" size="sm" class="w-full">Action</{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


def CardHeaderWithBorderSmall():
    return t"""
        <{Example} title="Header with Border (Small)">
            <{Card} size="sm" class="mx-auto w-full max-w-sm">
                <{CardHeader} class="border-b">
                    <{CardTitle}>Header with Border</{CardTitle}>
                    <{CardDescription}>This is a small card with a header that has a bottom border.</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <p>
                        The header has a border-b class applied, creating a visual separation between the header and content sections.
                    </p>
                </{CardContent}>
            </{Card}>
        </{Example}>
    """


def CardFooterWithBorderSmall():
    return t"""
        <{Example} title="Footer with Border (Small)">
            <{Card} size="sm" class="mx-auto w-full max-w-sm">
                <{CardContent}>
                    <p>
                        The footer has a border-t class applied, creating a visual separation between the content and footer sections.
                    </p>
                </{CardContent}>
                <{CardFooter} class="border-t">
                    <{Button} variant="outline" size="sm" class="w-full">Footer with Border</{Button}>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """
