from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle

__js__ = {"react-qr-code": ["default as QRCode"]}


def QrConnect():
    return t"""
        <{Card}>
            <{CardContent} class="flex justify-center pt-6">
                <div class="rounded-xl border bg-white p-4">
                    <{QRCode} value="https://ledger.app/connect/jd-4829" size={160} level="M" />
                </div>
            </{CardContent}>
            <{CardHeader} class="text-center">
                <{CardTitle}>Scan to connect your mobile device</{CardTitle}>
                <{CardDescription}>
                    Open the Ledger mobile app and scan this code to link your device.
                </{CardDescription}>
            </{CardHeader}>
            <{CardFooter}>
                <{Button} variant="secondary" class="w-full">Got it</{Button}>
            </{CardFooter}>
        </{Card}>
    """
