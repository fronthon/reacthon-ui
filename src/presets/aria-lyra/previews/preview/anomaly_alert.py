from button import Button
from card import Card, CardContent
from empty import Empty, EmptyContent, EmptyDescription, EmptyHeader, EmptyTitle


def AnomalyAlert():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Empty} class="h-48">
                    <{EmptyHeader}>
                        <{EmptyTitle}>Get alerted for anomalies</{EmptyTitle}>
                        <{EmptyDescription}>
                            Automatically monitor your projects for anomalies and get notified.
                        </{EmptyDescription}>
                    </{EmptyHeader}>
                    <{EmptyContent}>
                        <{Button}>Upgrade to Observability Plus</{Button}>
                    </{EmptyContent}>
                </{Empty}>
            </{CardContent}>
        </{Card}>
    """
