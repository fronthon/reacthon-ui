from example import Example, ExampleWrapper
from button import Button
from drawer import (
    Drawer, DrawerClose, DrawerContent, DrawerDescription, DrawerFooter, DrawerHeader, DrawerTitle, DrawerTrigger,
)


def DrawerExample():
    return t"""
        <{ExampleWrapper}>
            <{DrawerScrollableContent} />
            <{DrawerWithSides} />
        </{ExampleWrapper}>
    """


DRAWER_SIDES = ["top", "right", "bottom", "left"]


def DrawerWithSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-wrap gap-2">
                {[t'''
                    <{Drawer} key={side} direction={None if side == "bottom" else side}>
                        <{DrawerTrigger} asChild>
                            <{Button} variant="outline" class="capitalize style-sera:uppercase">{side}</{Button}>
                        </{DrawerTrigger}>
                        <{DrawerContent} class="data-[vaul-drawer-direction=bottom]:max-h-[50vh] data-[vaul-drawer-direction=top]:max-h-[50vh]">
                            <{DrawerHeader}>
                                <{DrawerTitle}>Move Goal</{DrawerTitle}>
                                <{DrawerDescription}>Set your daily activity goal.</{DrawerDescription}>
                            </{DrawerHeader}>
                            <div class="no-scrollbar overflow-y-auto px-4">
                                {[t"""
                                    <p
                                        key={index}
                                        class="mb-4 leading-normal style-lyra:mb-2 style-lyra:leading-relaxed style-sera:leading-relaxed"
                                    >
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                                    </p>
                                """ for index in range(10)]}
                            </div>
                            <{DrawerFooter}>
                                <{Button}>Submit</{Button}>
                                <{DrawerClose} asChild>
                                    <{Button} variant="outline">Cancel</{Button}>
                                </{DrawerClose}>
                            </{DrawerFooter}>
                        </{DrawerContent}>
                    </{Drawer}>
                ''' for side in DRAWER_SIDES]}
            </div>
        </{Example}>
    """


def DrawerScrollableContent():
    return t"""
        <{Example} title="Scrollable Content">
            <{Drawer} direction="right">
                <{DrawerTrigger} asChild>
                    <{Button} variant="outline">Scrollable Content</{Button}>
                </{DrawerTrigger}>
                <{DrawerContent}>
                    <{DrawerHeader}>
                        <{DrawerTitle}>Move Goal</{DrawerTitle}>
                        <{DrawerDescription}>Set your daily activity goal.</{DrawerDescription}>
                    </{DrawerHeader}>
                    <div class="no-scrollbar overflow-y-auto px-4">
                        {[t'''
                            <p
                                key={index}
                                class="mb-4 leading-normal style-lyra:mb-2 style-lyra:leading-relaxed style-sera:leading-relaxed"
                            >
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                            </p>
                        ''' for index in range(10)]}
                    </div>
                    <{DrawerFooter}>
                        <{Button}>Submit</{Button}>
                        <{DrawerClose} asChild>
                            <{Button} variant="outline">Cancel</{Button}>
                        </{DrawerClose}>
                    </{DrawerFooter}>
                </{DrawerContent}>
            </{Drawer}>
        </{Example}>
    """
