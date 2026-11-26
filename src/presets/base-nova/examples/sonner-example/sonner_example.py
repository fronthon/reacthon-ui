from example import Example, ExampleWrapper
from button import Button

__js__ = {"sonner": ["toast"]}


def SonnerExample():
    return t"""
        <{ExampleWrapper}>
            <{SonnerBasic} />
            <{SonnerWithDescription} />
        </{ExampleWrapper}>
    """


def SonnerBasic():
    return t"""
        <{Example} title="Basic" class="items-center justify-center">
            <{Button} onClick={(lambda: toast("Event has been created"))} variant="outline" class="w-fit">
                Show Toast
            </{Button}>
        </{Example}>
    """


def SonnerWithDescription():
    return t"""
        <{Example} title="With Description" class="items-center justify-center">
            <{Button}
                onClick={(lambda: toast("Event has been created", {"description": "Monday, January 3rd at 6:00pm"}))}
                variant="outline"
                class="w-fit"
            >
                Show Toast
            </{Button}>
        </{Example}>
    """
