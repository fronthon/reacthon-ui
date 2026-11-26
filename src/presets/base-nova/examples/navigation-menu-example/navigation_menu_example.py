from example import Example, ExampleWrapper
from navigation_menu import (
    NavigationMenu,
    NavigationMenuContent,
    NavigationMenuItem,
    NavigationMenuLink,
    NavigationMenuList,
    NavigationMenuTrigger,
    navigation_menu_trigger_style,
)

__js__ = {"next/link": ["default as Link"], "lucide-react": ["CircleAlertIcon"]}

components = [
    {
        "title": "Alert Dialog",
        "href": "/docs/primitives/alert-dialog",
        "description": "A modal dialog that interrupts the user with important content and expects a response.",
    },
    {
        "title": "Hover Card",
        "href": "/docs/primitives/hover-card",
        "description": "For sighted users to preview content available behind a link.",
    },
    {
        "title": "Progress",
        "href": "/docs/primitives/progress",
        "description": "Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.",
    },
    {
        "title": "Scroll-area",
        "href": "/docs/primitives/scroll-area",
        "description": "Visually or semantically separates content.",
    },
    {
        "title": "Tabs",
        "href": "/docs/primitives/tabs",
        "description": "A set of layered sections of content—known as tab panels—that are displayed one at a time.",
    },
    {
        "title": "Tooltip",
        "href": "/docs/primitives/tooltip",
        "description": "A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.",
    },
]


def NavigationMenuExample():
    return t"""
        <{ExampleWrapper} class="lg:grid-cols-1">
            <{NavigationMenuBasic} />
        </{ExampleWrapper}>
    """


def NavigationMenuBasic():
    return t"""
        <{Example} title="Basic">
            <{NavigationMenu}>
                <{NavigationMenuList}>
                    <{NavigationMenuItem}>
                        <{NavigationMenuTrigger}>Getting started</{NavigationMenuTrigger}>
                        <{NavigationMenuContent}>
                            <ul class="w-96">
                                <{ListItem} href="/docs" title="Introduction">
                                    Re-usable components built with Tailwind CSS.
                                </{ListItem}>
                                <{ListItem} href="/docs/installation" title="Installation">
                                    How to install dependencies and structure your app.
                                </{ListItem}>
                                <{ListItem} href="/docs/primitives/typography" title="Typography">
                                    Styles for headings, paragraphs, lists...etc
                                </{ListItem}>
                            </ul>
                        </{NavigationMenuContent}>
                    </{NavigationMenuItem}>
                    <{NavigationMenuItem}>
                        <{NavigationMenuTrigger}>Components</{NavigationMenuTrigger}>
                        <{NavigationMenuContent}>
                            <ul class="grid w-[400px] gap-2 md:w-[500px] md:grid-cols-2 lg:w-[600px]">
                                {[t'''
                                    <{ListItem}
                                        key={component["title"]}
                                        title={component["title"]}
                                        href={component["href"]}
                                    >
                                        {component["description"]}
                                    </{ListItem}>
                                ''' for component in components]}
                            </ul>
                        </{NavigationMenuContent}>
                    </{NavigationMenuItem}>
                    <{NavigationMenuItem}>
                        <{NavigationMenuTrigger}>With Icon</{NavigationMenuTrigger}>
                        <{NavigationMenuContent}>
                            <ul class="grid w-[200px]">
                                <li>
                                    <{NavigationMenuLink} render={t'<{Link} href="#" class="flex-row items-center gap-2" />'}>
                                        <{CircleAlertIcon} />
                                        Backlog
                                    </{NavigationMenuLink}>
                                    <{NavigationMenuLink} render={t'<{Link} href="#" class="flex-row items-center gap-2" />'}>
                                        <{CircleAlertIcon} />
                                        To Do
                                    </{NavigationMenuLink}>
                                    <{NavigationMenuLink} render={t'<{Link} href="#" class="flex-row items-center gap-2" />'}>
                                        <{CircleAlertIcon} />
                                        Done
                                    </{NavigationMenuLink}>
                                </li>
                            </ul>
                        </{NavigationMenuContent}>
                    </{NavigationMenuItem}>
                    <{NavigationMenuItem}>
                        <{NavigationMenuLink} render={t'<{Link} href="/docs" />'} class={navigation_menu_trigger_style()}>
                            Documentation
                        </{NavigationMenuLink}>
                    </{NavigationMenuItem}>
                </{NavigationMenuList}>
            </{NavigationMenu}>
        </{Example}>
    """


def ListItem(title=None, children=None, href=None, **props):
    return t"""
        <li ...{props}>
            <{NavigationMenuLink} render={t'<{Link} href={href} />'}>
                <div class="flex flex-col gap-1 style-vega:text-sm style-nova:text-sm style-lyra:text-xs style-maia:text-sm style-mira:text-xs style-luma:text-sm">
                    <div class="leading-none font-medium">{title}</div>
                    <div class="line-clamp-2 text-muted-foreground">{children}</div>
                </div>
            </{NavigationMenuLink}>
        </li>
    """
