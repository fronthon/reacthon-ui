from browser import window
from badge import Badge
from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from table import Table, TableBody, TableCell, TableHead, TableHeader, TableRow

INVOICE_ITEMS = [
    {"item": "Design System License", "qty": 1, "unitPrice": 499},
    {"item": "Priority Support", "qty": 12, "unitPrice": 99},
    {"item": "Custom Components", "qty": 3, "unitPrice": 250},
]

subtotal = sum((row["qty"] * row["unitPrice"] for row in INVOICE_ITEMS), 0)

tax = 0

total_due = subtotal + tax


def format_currency(value):
    return window.Intl.NumberFormat.new("en-US", {"style": "currency", "currency": "USD", "maximumFractionDigits": 2}).format(value)


def Invoice():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Invoice #INV-2847</{CardTitle}>
                <{CardDescription}>Due March 30, 2026</{CardDescription}>
                <{CardAction}>
                    <{Badge} variant="secondary">Pending</{Badge}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{Table}>
                    <{TableHeader}>
                        <{TableRow}>
                            <{TableHead}>Item</{TableHead}>
                            <{TableHead} class="text-right">Qty</{TableHead}>
                            <{TableHead} class="text-right">Rate</{TableHead}>
                            <{TableHead} class="text-right">Amount</{TableHead}>
                        </{TableRow}>
                    </{TableHeader}>
                    <{TableBody}>
                        {[t'''
                            <{TableRow} key={row["item"]}>
                                <{TableCell}>{row["item"]}</{TableCell}>
                                <{TableCell} class="text-right tabular-nums">{row["qty"]}</{TableCell}>
                                <{TableCell} class="text-right tabular-nums">
                                    {format_currency(row["unitPrice"])}
                                </{TableCell}>
                                <{TableCell} class="text-right tabular-nums">
                                    {format_currency(row["qty"] * row["unitPrice"])}
                                </{TableCell}>
                            </{TableRow}>
                        ''' for row in INVOICE_ITEMS]}
                        <{TableRow}>
                            <{TableCell} colSpan={3} class="text-right">Subtotal</{TableCell}>
                            <{TableCell} class="text-right tabular-nums">{format_currency(subtotal)}</{TableCell}>
                        </{TableRow}>
                        <{TableRow}>
                            <{TableCell} colSpan={3} class="text-right">Tax</{TableCell}>
                            <{TableCell} class="text-right tabular-nums">$0.00</{TableCell}>
                        </{TableRow}>
                        <{TableRow}>
                            <{TableCell} colSpan={3} class="text-right">Total Due</{TableCell}>
                            <{TableCell} class="text-right tabular-nums">{format_currency(total_due)}</{TableCell}>
                        </{TableRow}>
                    </{TableBody}>
                </{Table}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} variant="outline" size="sm">Download PDF</{Button}>
                <{Button} size="sm" class="ml-auto">Pay Now</{Button}>
            </{CardFooter}>
        </{Card}>
    """
