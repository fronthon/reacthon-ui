from reacthon import use_state
from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from checkbox import Checkbox
from field import Field, FieldContent, FieldDescription, FieldGroup, FieldLabel

NOTIFICATIONS = [
    {
        "id": "transactions",
        "label": "Transaction alerts",
        "description": "Deposits, withdrawals, and transfers.",
        "defaultChecked": True,
    },
    {
        "id": "security",
        "label": "Security alerts",
        "description": "Login attempts and account changes.",
        "defaultChecked": True,
    },
    {
        "id": "goals",
        "label": "Goal milestones",
        "description": "Updates at 25%, 50%, 75%, and 100%.",
        "defaultChecked": False,
    },
    {
        "id": "market",
        "label": "Market updates",
        "description": "Daily portfolio summary and price alerts.",
        "defaultChecked": False,
    },
]


def NotificationSettings():
    checked, set_checked = use_state(dict([[n["id"], n["defaultChecked"]] for n in NOTIFICATIONS]))

    all_checked = all(checked.get(n["id"]) for n in NOTIFICATIONS)
    some_checked = any(checked.get(n["id"]) for n in NOTIFICATIONS) and not all_checked

    def handle_select_all(value):
        set_checked(dict([[n["id"], value] for n in NOTIFICATIONS]))

    def handle_toggle(id_, value):
        set_checked(lambda prev: {**prev, id_: value})

    def render_n(n):
        return t"""
            <{Field} key={n["id"]} orientation="horizontal">
                <{Checkbox}
                    id={f"notify-{n["id"]}"}
                    checked={checked.get(n["id"])}
                    onCheckedChange={(lambda v: handle_toggle(n["id"], bool(v)))}
                />
                <{FieldContent}>
                    <{FieldLabel} for={f"notify-{n["id"]}"}>{n["label"]}</{FieldLabel}>
                    <{FieldDescription}>{n["description"]}</{FieldDescription}>
                </{FieldContent}>
            </{Field}>
        """

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Notifications</{CardTitle}>
                <{CardDescription}>Choose what you want to be notified about.</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field} orientation="horizontal">
                        <{Checkbox}
                            id="notify-all"
                            checked={all_checked}
                            indeterminate={some_checked}
                            onCheckedChange={(lambda v: handle_select_all(bool(v)))}
                        />
                        <{FieldContent}>
                            <{FieldLabel} for="notify-all">Select all</{FieldLabel}>
                        </{FieldContent}>
                    </{Field}>
                    {[render_n(n) for n in NOTIFICATIONS]}
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">Save Preferences</{Button}>
            </{CardFooter}>
        </{Card}>
    """
