from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from checkbox import Checkbox
from field import Field, FieldGroup, FieldLabel
from input import Input
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue


def ShippingAddress():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Shipping Address</{CardTitle}>
                <{CardDescription}>Where should we deliver?</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="shipping-street">Street address</{FieldLabel}>
                        <{Input} id="shipping-street" placeholder="123 Main Street" />
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="shipping-apt">Apt / Suite</{FieldLabel}>
                        <{Input} id="shipping-apt" placeholder="Apt 4B" />
                    </{Field}>
                    <{FieldGroup} class="grid grid-cols-2">
                        <{Field}>
                            <{FieldLabel} for="shipping-city">City</{FieldLabel}>
                            <{Input} id="shipping-city" placeholder="San Francisco" />
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="shipping-state">State</{FieldLabel}>
                            <{Select} defaultValue="CA">
                                <{SelectTrigger} id="shipping-state" class="w-full">
                                    <{SelectValue} />
                                </{SelectTrigger}>
                                <{SelectContent}>
                                    <{SelectGroup}>
                                        <{SelectItem} value="CA">California</{SelectItem}>
                                        <{SelectItem} value="NY">New York</{SelectItem}>
                                        <{SelectItem} value="TX">Texas</{SelectItem}>
                                    </{SelectGroup}>
                                </{SelectContent}>
                            </{Select}>
                        </{Field}>
                    </{FieldGroup}>
                    <{FieldGroup} class="grid grid-cols-2">
                        <{Field}>
                            <{FieldLabel} for="shipping-zip">ZIP Code</{FieldLabel}>
                            <{Input} id="shipping-zip" placeholder="94102" />
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="shipping-country">Country</{FieldLabel}>
                            <{Select} defaultValue="US">
                                <{SelectTrigger} id="shipping-country" class="w-full">
                                    <{SelectValue} />
                                </{SelectTrigger}>
                                <{SelectContent}>
                                    <{SelectGroup}>
                                        <{SelectItem} value="US">United States</{SelectItem}>
                                        <{SelectItem} value="CA">Canada</{SelectItem}>
                                        <{SelectItem} value="UK">United Kingdom</{SelectItem}>
                                    </{SelectGroup}>
                                </{SelectContent}>
                            </{Select}>
                        </{Field}>
                    </{FieldGroup}>
                    <{Field} orientation="horizontal">
                        <{Checkbox} id="shipping-save" defaultChecked />
                        <{FieldLabel} for="shipping-save" class="font-normal">Save as default address</{FieldLabel}>
                    </{Field}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} variant="outline" size="sm">Cancel</{Button}>
                <{Button} size="sm" class="ml-auto">Save Address</{Button}>
            </{CardFooter}>
        </{Card}>
    """
