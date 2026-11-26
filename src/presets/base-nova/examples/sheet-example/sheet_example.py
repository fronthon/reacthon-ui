from example import Example, ExampleWrapper
from button import Button
from field import Field, FieldGroup, FieldLabel
from input import Input
from sheet import Sheet, SheetClose, SheetContent, SheetDescription, SheetFooter, SheetHeader, SheetTitle, SheetTrigger


def SheetExample():
    return t"""
        <{ExampleWrapper}>
            <{SheetWithForm} />
            <{SheetNoCloseButton} />
            <{SheetWithSides} />
        </{ExampleWrapper}>
    """


def SheetWithForm():
    return t"""
        <{Example} title="With Form">
            <{Sheet}>
                <{SheetTrigger} render={t'<{Button} variant="outline" />'}>Open</{SheetTrigger}>
                <{SheetContent}>
                    <{SheetHeader}>
                        <{SheetTitle}>Edit profile</{SheetTitle}>
                        <{SheetDescription}>
                            Make changes to your profile here. Click save when you're done.
                        </{SheetDescription}>
                    </{SheetHeader}>
                    <div class="style-vega:px-4 style-nova:px-4 style-lyra:px-4 style-maia:px-6 style-mira:px-6 style-luma:px-6 style-rhea:px-6">
                        <{FieldGroup}>
                            <{Field}>
                                <{FieldLabel} for="sheet-demo-name">Name</{FieldLabel}>
                                <{Input} id="sheet-demo-name" defaultValue="Pedro Duarte" />
                            </{Field}>
                            <{Field}>
                                <{FieldLabel} for="sheet-demo-username">Username</{FieldLabel}>
                                <{Input} id="sheet-demo-username" defaultValue="@peduarte" />
                            </{Field}>
                        </{FieldGroup}>
                    </div>
                    <{SheetFooter}>
                        <{Button} type="submit">Save changes</{Button}>
                        <{SheetClose} render={t'<{Button} variant="outline" />'}>Close</{SheetClose}>
                    </{SheetFooter}>
                </{SheetContent}>
            </{Sheet}>
        </{Example}>
    """


def SheetNoCloseButton():
    return t"""
        <{Example} title="No Close Button">
            <{Sheet}>
                <{SheetTrigger} render={t'<{Button} variant="outline" />'}>No Close Button</{SheetTrigger}>
                <{SheetContent} showCloseButton={False}>
                    <{SheetHeader}>
                        <{SheetTitle}>No Close Button</{SheetTitle}>
                        <{SheetDescription}>
                            This sheet doesn't have a close button in the top-right corner. You can only close it using the button below.
                        </{SheetDescription}>
                    </{SheetHeader}>
                </{SheetContent}>
            </{Sheet}>
        </{Example}>
    """


SHEET_SIDES = ["top", "right", "bottom", "left"]


def SheetWithSides():
    return t"""
        <{Example} title="Sides">
            <div class="flex flex-wrap gap-2">
                {[t'''
                    <{Sheet} key={side}>
                        <{SheetTrigger} render={t"""<{Button} variant="outline" class="capitalize" />"""}>
                            {side}
                        </{SheetTrigger}>
                        <{SheetContent} side={side} class="data-[side=bottom]:max-h-[50vh] data-[side=top]:max-h-[50vh]">
                            <{SheetHeader}>
                                <{SheetTitle}>Edit profile</{SheetTitle}>
                                <{SheetDescription}>
                                    Make changes to your profile here. Click save when you're done.
                                </{SheetDescription}>
                            </{SheetHeader}>
                            <div class="no-scrollbar overflow-y-auto style-vega:px-4 style-nova:px-4 style-lyra:px-4 style-maia:px-6 style-mira:px-6 style-luma:px-6 style-rhea:px-6">
                                {[t"""
                                    <p
                                        key={index}
                                        class="mb-4 leading-normal style-lyra:mb-2 style-lyra:leading-relaxed"
                                    >
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                                    </p>
                                """ for index in range(10)]}
                            </div>
                            <{SheetFooter}>
                                <{Button} type="submit">Save changes</{Button}>
                                <{SheetClose} render={t"""<{Button} variant="outline" />"""}>Cancel</{SheetClose}>
                            </{SheetFooter}>
                        </{SheetContent}>
                    </{Sheet}>
                ''' for side in SHEET_SIDES]}
            </div>
        </{Example}>
    """
