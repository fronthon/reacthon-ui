from example import Example, ExampleWrapper
from button import Button
from dialog import Dialog, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from hover_card import HoverCard, HoverCardTrigger


def HoverCardExample():
    return t"""
        <{ExampleWrapper}>
            <{HoverCardSides} />
            <{HoverCardInDialog} />
        </{ExampleWrapper}>
    """


HOVER_CARD_PLACEMENTS = ["start", "left", "top", "bottom", "right", "end"]


def HoverCardSides():
    return t"""
        <{Example} title="Sides" containerClassName="col-span-2">
            <div class="flex flex-wrap items-center justify-center gap-2">
                {[t'''
                    <{HoverCardTrigger} key={placement} delay={100} closeDelay={100}>
                        <{Button} variant="outline" class="capitalize">{placement}</{Button}>
                        <{HoverCard} placement={placement}>
                            <div class="flex flex-col style-vega:gap-2 style-nova:gap-1.5 style-lyra:gap-1 style-maia:gap-2 style-mira:gap-1 style-luma:gap-2">
                                <h4 class="font-medium">Hover Card</h4>
                                <p>This hover card appears on the {placement} side of the trigger.</p>
                            </div>
                        </{HoverCard}>
                    </{HoverCardTrigger}>
                ''' for placement in HOVER_CARD_PLACEMENTS]}
            </div>
        </{Example}>
    """


def HoverCardInDialog():
    return t"""
        <{Example} title="In Dialog">
            <{DialogTrigger}>
                <{Button} variant="outline">Open Dialog</{Button}>
                <{Dialog}>
                    <{DialogHeader}>
                        <{DialogTitle}>Hover Card Example</{DialogTitle}>
                        <{DialogDescription}>Hover over the button below to see the hover card.</{DialogDescription}>
                    </{DialogHeader}>
                    <{HoverCardTrigger} delay={100} closeDelay={100}>
                        <{Button} variant="outline" class="w-fit">Hover me</{Button}>
                        <{HoverCard}>
                            <div class="flex flex-col style-vega:gap-2 style-nova:gap-1.5 style-lyra:gap-1 style-maia:gap-2 style-mira:gap-1 style-luma:gap-2">
                                <h4 class="font-medium">Hover Card</h4>
                                <p>This hover card appears inside a dialog. Hover over the button to see it.</p>
                            </div>
                        </{HoverCard}>
                    </{HoverCardTrigger}>
                </{Dialog}>
            </{DialogTrigger}>
        </{Example}>
    """
