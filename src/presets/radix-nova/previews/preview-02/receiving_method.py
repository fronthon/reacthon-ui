from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldLegend, FieldSet, FieldTitle
from input import Input
from radio_group import RadioGroup, RadioGroupItem

__js__ = {"lucide-react": ["XIcon"]}


def ReceivingMethod():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardDescription}>Payout Preferences</{CardDescription}>
                <{CardTitle}>Receiving Method</{CardTitle}>
                <{CardAction}>
                    <{Button} variant="ghost" size="icon-sm" class="bg-muted">
                        <{XIcon} />
                    </{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="account-holder">Account Holder Name</{FieldLabel}>
                        <{Input} id="account-holder" defaultValue="Synthetic Horizons Music LLC" />
                    </{Field}>
                    <{FieldSet}>
                        <{FieldLegend} variant="label">Receiving Method</{FieldLegend}>
                        <{RadioGroup}
                            defaultValue="bank"
                            class="grid grid-cols-1 items-start gap-3 md:grid-cols-2 style-sera:grid-cols-1"
                        >
                            <{FieldLabel} for="method-bank">
                                <{Field} orientation="horizontal" class="pb-2.5">
                                    <{RadioGroupItem} value="bank" id="method-bank" />
                                    <{FieldContent}>
                                        <{FieldTitle}>Bank Transfer</{FieldTitle}>
                                        <{FieldDescription}>SWIFT / IBAN</{FieldDescription}>
                                    </{FieldContent}>
                                </{Field}>
                            </{FieldLabel}>
                            <{FieldLabel} for="method-paypal">
                                <{Field} orientation="horizontal" class="pb-2.5">
                                    <{RadioGroupItem} value="paypal" id="method-paypal" />
                                    <{FieldContent}>
                                        <{FieldTitle}>PayPal</{FieldTitle}>
                                        <{FieldDescription} class="line-clamp-1">Instant Payout</{FieldDescription}>
                                    </{FieldContent}>
                                </{Field}>
                            </{FieldLabel}>
                        </{RadioGroup}>
                    </{FieldSet}>
                    <{Field}>
                        <{FieldLabel} for="iban">IBAN / Account Number</{FieldLabel}>
                        <{Input} id="iban" placeholder="DE89 3704 0044 ...." />
                    </{Field}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full" disabled>Save Payout Settings</{Button}>
            </{CardFooter}>
        </{Card}>
    """
