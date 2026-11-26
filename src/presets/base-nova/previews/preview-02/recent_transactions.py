from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle
from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from table import Table, TableBody, TableCell, TableRow

__js__ = {"lucide-react": ["CarIcon", "CoffeeIcon", "MoreHorizontalIcon", "ShoppingCartIcon", "TvIcon", "WalletIcon"]}


def RecentTransactions():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Recent Transactions</{CardTitle}>
                <{CardDescription}>Your latest account activity.</{CardDescription}>
                <{CardAction}>
                    <{Button} variant="outline" size="sm">View All</{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{Table}>
                    <{TableBody}>
                        <{TableRow}>
                            <{TableCell} class="w-10">
                                <div class="flex size-10 items-center justify-center rounded-lg bg-muted">
                                    <{CoffeeIcon} class="size-4 shrink-0" />
                                </div>
                            </{TableCell}>
                            <{TableCell}>
                                <div class="flex flex-col">
                                    <span class="font-medium">Blue Bottle Coffee</span>
                                    <span class="text-sm text-muted-foreground">Food & Drink</span>
                                </div>
                            </{TableCell}>
                            <{TableCell} class="text-sm text-muted-foreground">Today, 10:24 AM</{TableCell}>
                            <{TableCell} class="text-right">
                                <span class="text-sm font-semibold tabular-nums">-$6.50</span>
                            </{TableCell}>
                            <{TableCell} class="w-8">
                                <{DropdownMenu}>
                                    <{DropdownMenuTrigger} render={t'<{Button} variant="ghost" size="icon-sm" />'}>
                                        <{MoreHorizontalIcon} />
                                    </{DropdownMenuTrigger}>
                                    <{DropdownMenuContent} align="end">
                                        <{DropdownMenuItem}>View details</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Add note</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Categorize</{DropdownMenuItem}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuItem}>Dispute</{DropdownMenuItem}>
                                    </{DropdownMenuContent}>
                                </{DropdownMenu}>
                            </{TableCell}>
                        </{TableRow}>
                        <{TableRow}>
                            <{TableCell} class="w-10">
                                <div class="flex size-10 items-center justify-center rounded-lg bg-muted">
                                    <{ShoppingCartIcon} class="size-4 shrink-0" />
                                </div>
                            </{TableCell}>
                            <{TableCell}>
                                <div class="flex flex-col">
                                    <span class="font-medium">Whole Foods Market</span>
                                    <span class="text-sm text-muted-foreground">Groceries</span>
                                </div>
                            </{TableCell}>
                            <{TableCell} class="text-sm text-muted-foreground">Yesterday</{TableCell}>
                            <{TableCell} class="text-right">
                                <span class="text-sm font-semibold tabular-nums">-$142.30</span>
                            </{TableCell}>
                            <{TableCell} class="w-8">
                                <{DropdownMenu}>
                                    <{DropdownMenuTrigger} render={t'<{Button} variant="ghost" size="icon-sm" />'}>
                                        <{MoreHorizontalIcon} />
                                    </{DropdownMenuTrigger}>
                                    <{DropdownMenuContent} align="end">
                                        <{DropdownMenuItem}>View details</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Add note</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Categorize</{DropdownMenuItem}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuItem}>Dispute</{DropdownMenuItem}>
                                    </{DropdownMenuContent}>
                                </{DropdownMenu}>
                            </{TableCell}>
                        </{TableRow}>
                        <{TableRow}>
                            <{TableCell} class="w-10">
                                <div class="flex size-10 items-center justify-center rounded-lg bg-muted">
                                    <{WalletIcon} class="size-4 shrink-0" />
                                </div>
                            </{TableCell}>
                            <{TableCell}>
                                <div class="flex flex-col">
                                    <span class="font-medium">Stripe Payout</span>
                                    <span class="text-sm text-muted-foreground">Income</span>
                                </div>
                            </{TableCell}>
                            <{TableCell} class="text-sm text-muted-foreground">Oct 12</{TableCell}>
                            <{TableCell} class="text-right">
                                <span class="text-sm font-semibold text-emerald-500 tabular-nums">+$4,200.00</span>
                            </{TableCell}>
                            <{TableCell} class="w-8">
                                <{DropdownMenu}>
                                    <{DropdownMenuTrigger} render={t'<{Button} variant="ghost" size="icon-sm" />'}>
                                        <{MoreHorizontalIcon} />
                                    </{DropdownMenuTrigger}>
                                    <{DropdownMenuContent} align="end">
                                        <{DropdownMenuItem}>View details</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Add note</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Categorize</{DropdownMenuItem}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuItem}>Dispute</{DropdownMenuItem}>
                                    </{DropdownMenuContent}>
                                </{DropdownMenu}>
                            </{TableCell}>
                        </{TableRow}>
                        <{TableRow}>
                            <{TableCell} class="w-10">
                                <div class="flex size-10 items-center justify-center rounded-lg bg-muted">
                                    <{CarIcon} class="size-4 shrink-0" />
                                </div>
                            </{TableCell}>
                            <{TableCell}>
                                <div class="flex flex-col">
                                    <span class="font-medium">Uber Technologies</span>
                                    <span class="text-sm text-muted-foreground">Transport</span>
                                </div>
                            </{TableCell}>
                            <{TableCell} class="text-sm text-muted-foreground">Oct 11</{TableCell}>
                            <{TableCell} class="text-right">
                                <span class="text-sm font-semibold tabular-nums">-$24.10</span>
                            </{TableCell}>
                            <{TableCell} class="w-8">
                                <{DropdownMenu}>
                                    <{DropdownMenuTrigger} render={t'<{Button} variant="ghost" size="icon-sm" />'}>
                                        <{MoreHorizontalIcon} />
                                    </{DropdownMenuTrigger}>
                                    <{DropdownMenuContent} align="end">
                                        <{DropdownMenuItem}>View details</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Add note</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Categorize</{DropdownMenuItem}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuItem}>Dispute</{DropdownMenuItem}>
                                    </{DropdownMenuContent}>
                                </{DropdownMenu}>
                            </{TableCell}>
                        </{TableRow}>
                        <{TableRow}>
                            <{TableCell} class="w-10">
                                <div class="flex size-10 items-center justify-center rounded-lg bg-muted">
                                    <{TvIcon} class="size-4 shrink-0" />
                                </div>
                            </{TableCell}>
                            <{TableCell}>
                                <div class="flex flex-col">
                                    <span class="font-medium">Netflix Subscription</span>
                                    <span class="text-sm text-muted-foreground">Entertainment</span>
                                </div>
                            </{TableCell}>
                            <{TableCell} class="text-sm text-muted-foreground">Oct 10</{TableCell}>
                            <{TableCell} class="text-right">
                                <span class="text-sm font-semibold tabular-nums">-$19.99</span>
                            </{TableCell}>
                            <{TableCell} class="w-8">
                                <{DropdownMenu}>
                                    <{DropdownMenuTrigger} render={t'<{Button} variant="ghost" size="icon-sm" />'}>
                                        <{MoreHorizontalIcon} />
                                    </{DropdownMenuTrigger}>
                                    <{DropdownMenuContent} align="end">
                                        <{DropdownMenuItem}>View details</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Add note</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Categorize</{DropdownMenuItem}>
                                        <{DropdownMenuSeparator} />
                                        <{DropdownMenuItem}>Dispute</{DropdownMenuItem}>
                                    </{DropdownMenuContent}>
                                </{DropdownMenu}>
                            </{TableCell}>
                        </{TableRow}>
                    </{TableBody}>
                </{Table}>
            </{CardContent}>
        </{Card}>
    """
