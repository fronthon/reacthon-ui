from example import Example, ExampleWrapper
from checkbox import Checkbox
from field import Field
from input import Input
from label import Label
from textarea import Textarea


def LabelExample():
    return t"""
        <{ExampleWrapper}>
            <{LabelWithCheckbox} />
            <{LabelWithInput} />
            <{LabelDisabled} />
            <{LabelWithTextarea} />
        </{ExampleWrapper}>
    """


def LabelWithCheckbox():
    return t"""
        <{Example} title="With Checkbox">
            <{Field} orientation="horizontal">
                <{Checkbox} id="label-demo-terms" />
                <{Label} for="label-demo-terms">Accept terms and conditions</{Label}>
            </{Field}>
        </{Example}>
    """


def LabelWithInput():
    return t"""
        <{Example} title="With Input">
            <{Field}>
                <{Label} for="label-demo-username">Username</{Label}>
                <{Input} id="label-demo-username" placeholder="Username" />
            </{Field}>
        </{Example}>
    """


def LabelDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Field} data-disabled={True}>
                <{Label} for="label-demo-disabled">Disabled</{Label}>
                <{Input} id="label-demo-disabled" placeholder="Disabled" disabled />
            </{Field}>
        </{Example}>
    """


def LabelWithTextarea():
    return t"""
        <{Example} title="With Textarea">
            <{Field}>
                <{Label} for="label-demo-message">Message</{Label}>
                <{Textarea} id="label-demo-message" placeholder="Message" />
            </{Field}>
        </{Example}>
    """
