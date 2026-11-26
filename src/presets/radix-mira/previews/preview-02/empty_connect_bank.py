from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyMedia, EmptyTitle

__js__ = {"lucide-react": ["CreditCardIcon"]}


def EmptyConnectBank():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Empty} class="p-4">
                    <{EmptyMedia} variant="icon">
                        <{CreditCardIcon} />
                    </{EmptyMedia}>
                    <{EmptyHeader}>
                        <{EmptyTitle}>Connect Bank</{EmptyTitle}>
                        <{EmptyDescription}>
                            Link your payout method to receive monthly royalty distributions automatically.
                        </{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button}>Set Up Payouts</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
