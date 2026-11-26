from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldSeparator
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from switch import Switch

__js__ = {"lucide-react": ["XIcon"]}

CURRENCIES = [
    {"label": "USD — United States Dollar", "value": "usd"},
    {"label": "EUR — Euro", "value": "eur"},
    {"label": "GBP — British Pound", "value": "gbp"},
    {"label": "JPY — Japanese Yen", "value": "jpy"},
]


def Preferences():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Preferences</{CardTitle}>
                <{CardDescription}>Manage your account settings and notifications.</{CardDescription}>
                <{CardAction}>
                    <{Button} variant="ghost" size="icon-sm" class="bg-muted">
                        <{XIcon} />
                    </{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="default-currency">Default Currency</{FieldLabel}>
                        <{Select} items={CURRENCIES} defaultValue="usd">
                            <{SelectTrigger} id="default-currency" class="w-full">
                                <{SelectValue} />
                            </{SelectTrigger}>
                            <{SelectContent}>
                                <{SelectGroup}>
                                    {[t'''
                                        <{SelectItem}
                                            key={item["value"]}
                                            value={item["value"]}
                                        >
                                            {item["label"]}
                                        </{SelectItem}>
                                    ''' for item in CURRENCIES]}
                                </{SelectGroup}>
                            </{SelectContent}>
                        </{Select}>
                    </{Field}>
                    <{FieldSeparator} class="-my-4 style-sera:hidden" />
                    <{Field} orientation="horizontal">
                        <{FieldContent}>
                            <{FieldLabel} for="public-statistics">Public Statistics</{FieldLabel}>
                            <{FieldDescription}>
                                Allow others to see your total stream count and listening activity
                            </{FieldDescription}>
                        </{FieldContent}>
                        <{Switch} id="public-statistics" defaultChecked />
                    </{Field}>
                    <{FieldSeparator} class="-my-4 style-sera:hidden" />
                    <{Field} orientation="horizontal">
                        <{FieldContent}>
                            <{FieldLabel} for="email-notifications">Email Notifications</{FieldLabel}>
                            <{FieldDescription}>Monthly royalty reports and distribution updates</{FieldDescription}>
                        </{FieldContent}>
                        <{Switch} id="email-notifications" defaultChecked />
                    </{Field}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} variant="outline">Reset</{Button}>
                <{Button} class="ml-auto">Save Preferences</{Button}>
            </{CardFooter}>
        </{Card}>
    """
