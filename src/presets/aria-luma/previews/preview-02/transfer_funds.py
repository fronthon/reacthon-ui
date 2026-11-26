from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldGroup, FieldLabel
from input_group import InputGroup, InputGroupAddon, InputGroupInput, InputGroupText
from item import Item, ItemContent
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from separator import Separator

__js__ = {"lucide-react": ["XIcon"]}

FROM_ACCOUNTS = [
    {"label": "Main Checking (··8402) — $12,450.00", "value": "checking"},
    {"label": "Business (··7731) — $8,920.00", "value": "business"},
]

TO_ACCOUNTS = [
    {"label": "High Yield Savings (··1192) — $42,100.00", "value": "savings"},
    {"label": "Investment (··3349) — $18,200.00", "value": "investment"},
]


def TransferFunds():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Transfer Funds</{CardTitle}>
                <{CardDescription}>Move money between your connected accounts.</{CardDescription}>
                <{CardAction}>
                    <{Button} variant="ghost" size="icon-sm" class="bg-muted">
                        <{XIcon} />
                    </{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="transfer-amount">Amount to Transfer</{FieldLabel}>
                        <{InputGroup}>
                            <{InputGroupAddon}>
                                <{InputGroupText}>$</{InputGroupText}>
                            </{InputGroupAddon}>
                            <{InputGroupInput} id="transfer-amount" defaultValue="1,200.00" />
                        </{InputGroup}>
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="from-account">From Account</{FieldLabel}>
                        <{Select} defaultValue="checking">
                            <{SelectTrigger} id="from-account" class="w-full">
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
                                    ''' for item in FROM_ACCOUNTS]}
                                </{SelectGroup}>
                            </{SelectContent}>
                        </{Select}>
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="to-account">To Account</{FieldLabel}>
                        <{Select} defaultValue="savings">
                            <{SelectTrigger} id="to-account" class="w-full">
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
                                    ''' for item in TO_ACCOUNTS]}
                                </{SelectGroup}>
                            </{SelectContent}>
                        </{Select}>
                    </{Field}>
                    <{Item} variant="muted" class="flex-col items-stretch">
                        <{ItemContent} class="gap-3">
                            <div class="flex items-center justify-between">
                                <span class="text-sm text-muted-foreground">Estimated arrival</span>
                                <span class="text-sm font-medium">Today, Apr 14</span>
                            </div>
                            <{Separator} />
                            <div class="flex items-center justify-between">
                                <span class="text-sm text-muted-foreground">Transaction fee</span>
                                <span class="text-sm font-medium tabular-nums">$0.00</span>
                            </div>
                            <{Separator} />
                            <div class="flex items-center justify-between">
                                <span class="text-sm font-medium">Total amount</span>
                                <span class="text-sm font-semibold tabular-nums">$1,200.00</span>
                            </div>
                        </{ItemContent}>
                    </{Item}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">Confirm Transfer</{Button}>
            </{CardFooter}>
        </{Card}>
    """
