from example import Example, ExampleWrapper
from field import Field, FieldDescription, FieldLabel
from native_select import NativeSelect, NativeSelectOptGroup, NativeSelectOption


def NativeSelectExample():
    return t"""
        <{ExampleWrapper}>
            <{NativeSelectBasic} />
            <{NativeSelectWithGroups} />
            <{NativeSelectSizes} />
            <{NativeSelectWithField} />
            <{NativeSelectDisabled} />
            <{NativeSelectInvalid} />
        </{ExampleWrapper}>
    """


def NativeSelectBasic():
    return t"""
        <{Example} title="Basic">
            <{NativeSelect}>
                <{NativeSelectOption} value="">Select a fruit</{NativeSelectOption}>
                <{NativeSelectOption} value="apple">Apple</{NativeSelectOption}>
                <{NativeSelectOption} value="banana">Banana</{NativeSelectOption}>
                <{NativeSelectOption} value="blueberry">Blueberry</{NativeSelectOption}>
                <{NativeSelectOption} value="grapes" disabled>Grapes</{NativeSelectOption}>
                <{NativeSelectOption} value="pineapple">Pineapple</{NativeSelectOption}>
            </{NativeSelect}>
        </{Example}>
    """


def NativeSelectWithGroups():
    return t"""
        <{Example} title="With Groups">
            <{NativeSelect}>
                <{NativeSelectOption} value="">Select a food</{NativeSelectOption}>
                <{NativeSelectOptGroup} label="Fruits">
                    <{NativeSelectOption} value="apple">Apple</{NativeSelectOption}>
                    <{NativeSelectOption} value="banana">Banana</{NativeSelectOption}>
                    <{NativeSelectOption} value="blueberry">Blueberry</{NativeSelectOption}>
                </{NativeSelectOptGroup}>
                <{NativeSelectOptGroup} label="Vegetables">
                    <{NativeSelectOption} value="carrot">Carrot</{NativeSelectOption}>
                    <{NativeSelectOption} value="broccoli">Broccoli</{NativeSelectOption}>
                    <{NativeSelectOption} value="spinach">Spinach</{NativeSelectOption}>
                </{NativeSelectOptGroup}>
            </{NativeSelect}>
        </{Example}>
    """


def NativeSelectSizes():
    return t"""
        <{Example} title="Sizes">
            <div class="flex flex-col gap-4">
                <{NativeSelect} size="sm">
                    <{NativeSelectOption} value="">Select a fruit</{NativeSelectOption}>
                    <{NativeSelectOption} value="apple">Apple</{NativeSelectOption}>
                    <{NativeSelectOption} value="banana">Banana</{NativeSelectOption}>
                    <{NativeSelectOption} value="blueberry">Blueberry</{NativeSelectOption}>
                </{NativeSelect}>
                <{NativeSelect} size="default">
                    <{NativeSelectOption} value="">Select a fruit</{NativeSelectOption}>
                    <{NativeSelectOption} value="apple">Apple</{NativeSelectOption}>
                    <{NativeSelectOption} value="banana">Banana</{NativeSelectOption}>
                    <{NativeSelectOption} value="blueberry">Blueberry</{NativeSelectOption}>
                </{NativeSelect}>
            </div>
        </{Example}>
    """


def NativeSelectWithField():
    return t"""
        <{Example} title="With Field">
            <{Field}>
                <{FieldLabel} for="native-select-country">Country</{FieldLabel}>
                <{NativeSelect} id="native-select-country">
                    <{NativeSelectOption} value="">Select a country</{NativeSelectOption}>
                    <{NativeSelectOption} value="us">United States</{NativeSelectOption}>
                    <{NativeSelectOption} value="uk">United Kingdom</{NativeSelectOption}>
                    <{NativeSelectOption} value="ca">Canada</{NativeSelectOption}>
                    <{NativeSelectOption} value="au">Australia</{NativeSelectOption}>
                </{NativeSelect}>
                <{FieldDescription}>Select your country of residence.</{FieldDescription}>
            </{Field}>
        </{Example}>
    """


def NativeSelectDisabled():
    return t"""
        <{Example} title="Disabled">
            <{NativeSelect} disabled>
                <{NativeSelectOption} value="">Disabled</{NativeSelectOption}>
                <{NativeSelectOption} value="apple">Apple</{NativeSelectOption}>
                <{NativeSelectOption} value="banana">Banana</{NativeSelectOption}>
                <{NativeSelectOption} value="blueberry">Blueberry</{NativeSelectOption}>
            </{NativeSelect}>
        </{Example}>
    """


def NativeSelectInvalid():
    return t"""
        <{Example} title="Invalid">
            <{NativeSelect} aria-invalid="true">
                <{NativeSelectOption} value="">Error state</{NativeSelectOption}>
                <{NativeSelectOption} value="apple">Apple</{NativeSelectOption}>
                <{NativeSelectOption} value="banana">Banana</{NativeSelectOption}>
                <{NativeSelectOption} value="blueberry">Blueberry</{NativeSelectOption}>
            </{NativeSelect}>
        </{Example}>
    """
