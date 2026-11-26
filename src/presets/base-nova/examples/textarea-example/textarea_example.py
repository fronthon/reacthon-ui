from example import Example, ExampleWrapper
from field import Field, FieldDescription, FieldLabel
from textarea import Textarea


def TextareaExample():
    return t"""
        <{ExampleWrapper}>
            <{TextareaBasic} />
            <{TextareaInvalid} />
            <{TextareaWithLabel} />
            <{TextareaWithDescription} />
            <{TextareaDisabled} />
        </{ExampleWrapper}>
    """


def TextareaBasic():
    return t"""
        <{Example} title="Basic">
            <{Textarea} placeholder="Type your message here." />
        </{Example}>
    """


def TextareaInvalid():
    return t"""
        <{Example} title="Invalid">
            <{Textarea} placeholder="Type your message here." aria-invalid="true" />
        </{Example}>
    """


def TextareaWithLabel():
    return t"""
        <{Example} title="With Label">
            <{Field}>
                <{FieldLabel} for="textarea-demo-message">Message</{FieldLabel}>
                <{Textarea} id="textarea-demo-message" placeholder="Type your message here." rows={6} />
            </{Field}>
        </{Example}>
    """


def TextareaWithDescription():
    return t"""
        <{Example} title="With Description">
            <{Field}>
                <{FieldLabel} for="textarea-demo-message-2">Message</{FieldLabel}>
                <{Textarea} id="textarea-demo-message-2" placeholder="Type your message here." rows={6} />
                <{FieldDescription}>Type your message and press enter to send.</{FieldDescription}>
            </{Field}>
        </{Example}>
    """


def TextareaDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Field}>
                <{FieldLabel} for="textarea-demo-disabled">Message</{FieldLabel}>
                <{Textarea} id="textarea-demo-disabled" placeholder="Type your message here." disabled />
            </{Field}>
        </{Example}>
    """
