from browser import window
from example import Example, ExampleWrapper
from button import Button
from toast import toast


def ToastExample():
    return t"""
        <{ExampleWrapper}>
            <{ToastBasic} />
            <{ToastWithAction} />
            <{ToastPromise} />
        </{ExampleWrapper}>
    """


def ToastBasic():
    def on_click():
        return toast.add({"title": "Event created", "description": "Sunday, December 3 at 9:00 AM"})

    return t"""
        <{Example} title="Basic" class="items-center justify-center">
            <{Button} variant="outline" class="w-fit" onClick={on_click}>Show Toast</{Button}>
        </{Example}>
    """


def ToastWithAction():
    def show_toast():
        def on_click():
            toast.close(id_)
            toast.add({"description": "Event creation undone."})

        id_ = toast.add(
            {
                "title": "Event created",
                "description": "You can undo this action.",
                "actionProps": {"children": "Undo", "onClick": on_click},
            },
        )

    return t"""
        <{Example} title="With Action" class="items-center justify-center">
            <{Button} variant="outline" class="w-fit" onClick={show_toast}>Show Toast</{Button}>
        </{Example}>
    """


def ToastPromise():
    def show_toast():
        def callback(resolve):
            window.setTimeout(lambda: resolve({"name": "Event"}), 2000)

        toast.promise(
            window.Promise.new(callback),
            {
                "loading": "Creating event…",
                "success": lambda data: f"{data["name"]} created.",
                "error": "Could not create event.",
            },
        )

    return t"""
        <{Example} title="Promise" class="items-center justify-center">
            <{Button} variant="outline" class="w-fit" onClick={show_toast}>Create Event</{Button}>
        </{Example}>
    """
