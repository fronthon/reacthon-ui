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


HOVER_CARD_SIDES = ["top", "right", "bottom", "left"]


def HoverCardSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-wrap items-center justify-center gap-4">
                {[t'''
                    <{HoverCard} key={side} openDelay={100} closeDelay={100}>
                        <{HoverCardTrigger} asChild>
                            <{Button} variant="outline" class="capitalize style-sera:uppercase">{side}</{Button}>
                        </{HoverCardTrigger}>
                        <{HoverCardContent} side={side} class="w-64">
                            <div class="flex flex-col style-vega:gap-2 style-nova:gap-1.5 style-lyra:gap-1 style-maia:gap-2 style-mira:gap-1 style-luma:gap-2 style-sera:gap-2">
                                <h4 class="font-medium style-sera:font-heading style-sera:font-semibold style-sera:tracking-wide">
                                    Hover Card
                                </h4>
                                <p class="style-sera:leading-relaxed">
                                    This hover card appears on the {side} side of the trigger.
                                </p>
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
                <{DialogTrigger} asChild>
                    <{Button} variant="outline">Open Dialog</{Button}>
                </{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Hover Card Example</{DialogTitle}>
                        <{DialogDescription}>Hover over the button below to see the hover card.</{DialogDescription}>
                    </{DialogHeader}>
                    <{HoverCard} openDelay={100} closeDelay={100}>
                        <{HoverCardTrigger} asChild>
                            <{Button} variant="outline" class="w-fit">Hover me</{Button}>
                        </{HoverCardTrigger}>
                        <{HoverCardContent} class="w-64">
                            <div class="flex flex-col style-vega:gap-2 style-nova:gap-1.5 style-lyra:gap-1 style-maia:gap-2 style-mira:gap-1 style-luma:gap-2 style-sera:gap-2">
                                <h4 class="font-medium style-sera:font-heading style-sera:font-semibold style-sera:tracking-wide">
                                    Hover Card
                                </h4>
                                <p class="style-sera:leading-relaxed">
                                    This hover card appears inside a dialog. Hover over the button to see it.
                                </p>
                            </div>
                        </{HoverCardContent}>
                    </{HoverCard}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
