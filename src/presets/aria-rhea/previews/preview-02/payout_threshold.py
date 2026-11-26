from reacthon import use_state
from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldDescription, FieldGroup, FieldLabel
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from slider import Slider
from textarea import Textarea

__js__ = {"lucide-react": ["XIcon"]}

CURRENCIES = [
    {"label": "USD — United States Dollar", "value": "usd"},
    {"label": "EUR — Euro", "value": "eur"},
    {"label": "GBP — British Pound", "value": "gbp"},
    {"label": "JPY — Japanese Yen", "value": "jpy"},
]


def PayoutThreshold():
    amount, set_amount = use_state([2500])

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Payout Threshold</{CardTitle}>
                <{CardDescription}>Set the minimum balance required before a payout is triggered.</{CardDescription}>
                <{CardAction}>
                    <{Button} variant="ghost" size="icon-sm" class="bg-muted">
                        <{XIcon} />
                    </{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="preferred-currency">Preferred Currency</{FieldLabel}>
                        <{Select} defaultValue="usd">
                            <{SelectTrigger} id="preferred-currency" class="w-full">
                                <{SelectValue} />
                            </{SelectTrigger}>
                            <{SelectContent}>
                                <{SelectGroup}>
                                    {[t'''
                                        <{SelectItem}
                                            key={item["value"]}
                                            id={item["value"]}
                                        >
                                            {item["label"]}
                                        </{SelectItem}>
                                    ''' for item in CURRENCIES]}
                                </{SelectGroup}>
                            </{SelectContent}>
                        </{Select}>
                    </{Field}>
                    <{Field}>
                        <div class="flex items-baseline justify-between">
                            <{FieldLabel} for="min-payout">Minimum Payout Amount</{FieldLabel}>
                            <span class="text-2xl font-semibold tabular-nums">${format(amount[0], f".{2}f")}</span>
                        </div>
                        <{Slider}
                            id="min-payout"
                            value={amount}
                            onChange={(lambda value: set_amount(list(value) if isinstance(value, list) else [value]))}
                            minValue={50}
                            maxValue={10000}
                            step={50}
                        />
                        <div class="flex items-center justify-between">
                            <{FieldDescription}>$50 (MIN)</{FieldDescription}>
                            <{FieldDescription}>$10,000 (MAX)</{FieldDescription}>
                        </div>
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="payout-notes">Notes</{FieldLabel}>
                        <{Textarea}
                            id="payout-notes"
                            placeholder="Add any notes for this payout configuration..."
                            class="min-h-[100px]"
                        />
                    </{Field}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">Save Threshold</{Button}>
            </{CardFooter}>
        </{Card}>
    """
