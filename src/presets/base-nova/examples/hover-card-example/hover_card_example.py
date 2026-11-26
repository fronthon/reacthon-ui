from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from hover_card import HoverCard, HoverCardContent, HoverCardTrigger


def HoverCardExample():
    return t"""
        <{ExampleWrapper}>
            <{HoverCardSides} />
            <{HoverCardInDialog} />
        </{ExampleWrapper}>
    """


HOVER_CARD_SIDES = ["inline-start", "left", "top", "bottom", "right", "inline-end"]


def HoverCardSides():
    return t"""
        <{Example} title="Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap items-center justify-center gap-2">
                {[t'''
                    <{HoverCard} key={side}>
                        <{HoverCardTrigger}
                            delay={100}
                            closeDelay={100}
                            render={t"""<{Button} variant="outline" class="capitalize" />"""}
                        >
                            {side.replace("-", " ")}
                        </{HoverCardTrigger}>
                        <{HoverCardContent} side={side}>
                            <div class="flex flex-col style-vega:gap-2 style-nova:gap-1.5 style-lyra:gap-1 style-maia:gap-2 style-mira:gap-1 style-luma:gap-2">
                                <h4 class="font-medium">Hover Card</h4>
                                <p>This hover card appears on the {side.replace("-", " ")} side of the trigger.</p>
                            </div>
                        </{HoverCardContent}>
                    </{HoverCard}>
                ''' for side in HOVER_CARD_SIDES]}
            </div>
        </{Example}>
    """


def HoverCardInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open Dialog</{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Hover Card Example</{DialogTitle}>
                        <{DialogDescription}>Hover over the button below to see the hover card.</{DialogDescription}>
                    </{DialogHeader}>
                    <{HoverCard}>
                        <{HoverCardTrigger}
                            delay={100}
                            closeDelay={100}
                            render={t'<{Button} variant="outline" class="w-fit" />'}
                        >
                            Hover me
                        </{HoverCardTrigger}>
                        <{HoverCardContent}>
                            <div class="flex flex-col style-vega:gap-2 style-nova:gap-1.5 style-lyra:gap-1 style-maia:gap-2 style-mira:gap-1 style-luma:gap-2">
                                <h4 class="font-medium">Hover Card</h4>
                                <p>This hover card appears inside a dialog. Hover over the button to see it.</p>
                            </div>
                        </{HoverCardContent}>
                    </{HoverCard}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
