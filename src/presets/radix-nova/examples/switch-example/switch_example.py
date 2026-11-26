from example import Example, ExampleWrapper
from field import Field, FieldContent, FieldDescription, FieldLabel, FieldTitle
from label import Label
from switch import Switch


def SwitchExample():
    return t"""
        <{ExampleWrapper}>
            <{SwitchBasic} />
            <{SwitchWithDescription} />
            <{SwitchWithLabel} />
            <{SwitchDisabled} />
            <{SwitchSizes} />
        </{ExampleWrapper}>
    """


def SwitchBasic():
    return t"""
        <{Example} title="Basic">
            <{Field} orientation="horizontal">
                <{Switch} id="switch-basic" />
                <{FieldLabel} for="switch-basic">Airplane Mode</{FieldLabel}>
            </{Field}>
        </{Example}>
    """


def SwitchWithLabel():
    return t"""
        <{Example} title="With Label">
            <div class="flex items-center gap-2">
                <{Switch} id="switch-bluetooth" defaultChecked />
                <{Label} for="switch-bluetooth">Bluetooth</{Label}>
            </div>
        </{Example}>
    """


def SwitchWithDescription():
    return t"""
        <{Example} title="With Description">
            <{FieldLabel} for="switch-focus-mode">
                <{Field} orientation="horizontal">
                    <{FieldContent}>
                        <{FieldTitle}>Share across devices</{FieldTitle}>
                        <{FieldDescription}>
                            Focus is shared across devices, and turns off when you leave the app.
                        </{FieldDescription}>
                    </{FieldContent}>
                    <{Switch} id="switch-focus-mode" />
                </{Field}>
            </{FieldLabel}>
        </{Example}>
    """


def SwitchDisabled():
    return t"""
        <{Example} title="Disabled">
            <div class="flex flex-col gap-12">
                <div class="flex items-center gap-2">
                    <{Switch} id="switch-disabled-unchecked" disabled />
                    <{Label} for="switch-disabled-unchecked">Disabled (Unchecked)</{Label}>
                </div>
                <div class="flex items-center gap-2">
                    <{Switch} id="switch-disabled-checked" defaultChecked disabled />
                    <{Label} for="switch-disabled-checked">Disabled (Checked)</{Label}>
                </div>
            </div>
        </{Example}>
    """


def SwitchSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-12">
                <div class="flex items-center gap-2">
                    <{Switch} id="switch-size-sm" size="sm" />
                    <{Label} for="switch-size-sm">Small</{Label}>
                </div>
                <div class="flex items-center gap-2">
                    <{Switch} id="switch-size-default" size="default" />
                    <{Label} for="switch-size-default">Default</{Label}>
                </div>
            </div>
        </{Example}>
    """
