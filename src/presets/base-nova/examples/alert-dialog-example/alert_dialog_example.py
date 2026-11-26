from example import Example, ExampleWrapper
from alert_dialog import (
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogMedia,
    AlertDialogTitle,
    AlertDialogTrigger,
)
from button import Button
from dialog import Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger

__js__ = {"lucide-react": ["BluetoothIcon", "Trash2Icon"]}


def AlertDialogExample():
    return t"""
        <{ExampleWrapper}>
            <{AlertDialogBasic} />
            <{AlertDialogSmall} />
            <{AlertDialogWithMedia} />
            <{AlertDialogSmallWithMedia} />
            <{AlertDialogDestructive} />
            <{AlertDialogInDialog} />
        </{ExampleWrapper}>
    """


def AlertDialogBasic():
    return t"""
        <{Example} title="Basic" class="items-center">
            <{AlertDialog}>
                <{AlertDialogTrigger} render={t'<{Button} variant="outline">Default</{Button}>'} />
                <{AlertDialogContent}>
                    <{AlertDialogHeader}>
                        <{AlertDialogTitle}>Are you absolutely sure?</{AlertDialogTitle}>
                        <{AlertDialogDescription}>
                            This action cannot be undone. This will permanently delete your account and remove your data from our servers.
                        </{AlertDialogDescription}>
                    </{AlertDialogHeader}>
                    <{AlertDialogFooter}>
                        <{AlertDialogCancel}>Cancel</{AlertDialogCancel}>
                        <{AlertDialogAction}>Continue</{AlertDialogAction}>
                    </{AlertDialogFooter}>
                </{AlertDialogContent}>
            </{AlertDialog}>
        </{Example}>
    """


def AlertDialogSmall():
    return t"""
        <{Example} title="Small" class="items-center">
            <{AlertDialog}>
                <{AlertDialogTrigger} render={t'<{Button} variant="outline">Small</{Button}>'} />
                <{AlertDialogContent} size="sm">
                    <{AlertDialogHeader}>
                        <{AlertDialogTitle}>Allow accessory to connect?</{AlertDialogTitle}>
                        <{AlertDialogDescription}>
                            Do you want to allow the USB accessory to connect to this device?
                        </{AlertDialogDescription}>
                    </{AlertDialogHeader}>
                    <{AlertDialogFooter}>
                        <{AlertDialogCancel}>Don't allow</{AlertDialogCancel}>
                        <{AlertDialogAction}>Allow</{AlertDialogAction}>
                    </{AlertDialogFooter}>
                </{AlertDialogContent}>
            </{AlertDialog}>
        </{Example}>
    """


def AlertDialogWithMedia():
    return t"""
        <{Example} title="With Media" class="items-center">
            <{AlertDialog}>
                <{AlertDialogTrigger} render={t'<{Button} variant="outline">Default (Media)</{Button}>'} />
                <{AlertDialogContent}>
                    <{AlertDialogHeader}>
                        <{AlertDialogMedia}>
                            <{BluetoothIcon} />
                        </{AlertDialogMedia}>
                        <{AlertDialogTitle}>Are you absolutely sure?</{AlertDialogTitle}>
                        <{AlertDialogDescription}>
                            This will permanently delete your account and remove your data from our servers.
                        </{AlertDialogDescription}>
                    </{AlertDialogHeader}>
                    <{AlertDialogFooter}>
                        <{AlertDialogCancel}>Cancel</{AlertDialogCancel}>
                        <{AlertDialogAction}>Continue</{AlertDialogAction}>
                    </{AlertDialogFooter}>
                </{AlertDialogContent}>
            </{AlertDialog}>
        </{Example}>
    """


def AlertDialogSmallWithMedia():
    return t"""
        <{Example} title="Small With Media" class="items-center">
            <{AlertDialog}>
                <{AlertDialogTrigger} render={t'<{Button} variant="outline">Small (Media)</{Button}>'} />
                <{AlertDialogContent} size="sm">
                    <{AlertDialogHeader}>
                        <{AlertDialogMedia}>
                            <{BluetoothIcon} />
                        </{AlertDialogMedia}>
                        <{AlertDialogTitle}>Allow accessory to connect?</{AlertDialogTitle}>
                        <{AlertDialogDescription}>
                            Do you want to allow the USB accessory to connect to this device?
                        </{AlertDialogDescription}>
                    </{AlertDialogHeader}>
                    <{AlertDialogFooter}>
                        <{AlertDialogCancel}>Don't allow</{AlertDialogCancel}>
                        <{AlertDialogAction}>Allow</{AlertDialogAction}>
                    </{AlertDialogFooter}>
                </{AlertDialogContent}>
            </{AlertDialog}>
        </{Example}>
    """


def AlertDialogDestructive():
    return t"""
        <{Example} title="Destructive" class="items-center">
            <{AlertDialog}>
                <{AlertDialogTrigger} render={t'<{Button} variant="destructive">Delete Chat</{Button}>'} />
                <{AlertDialogContent} size="sm">
                    <{AlertDialogHeader}>
                        <{AlertDialogMedia} class="bg-destructive/10 text-destructive dark:bg-destructive/20 dark:text-destructive">
                            <{Trash2Icon} />
                        </{AlertDialogMedia}>
                        <{AlertDialogTitle}>Delete chat?</{AlertDialogTitle}>
                        <{AlertDialogDescription}>
                            This will permanently delete this chat conversation. View{" "}
                            <a href="#">Settings</a> delete any memories saved during this chat.
                        </{AlertDialogDescription}>
                    </{AlertDialogHeader}>
                    <{AlertDialogFooter}>
                        <{AlertDialogCancel} variant="ghost">Cancel</{AlertDialogCancel}>
                        <{AlertDialogAction} variant="destructive">Delete</{AlertDialogAction}>
                    </{AlertDialogFooter}>
                </{AlertDialogContent}>
            </{AlertDialog}>
        </{Example}>
    """


def AlertDialogInDialog():
    return t"""
        <{Example} title="In Dialog" class="items-center">
            <{Dialog}>
                <{DialogTrigger} render={t'<{Button} variant="outline" />'}>Open Dialog</{DialogTrigger}>
                <{DialogContent}>
                    <{DialogHeader}>
                        <{DialogTitle}>Alert Dialog Example</{DialogTitle}>
                        <{DialogDescription}>Click the button below to open an alert dialog.</{DialogDescription}>
                    </{DialogHeader}>
                    <{DialogFooter}>
                        <{AlertDialog}>
                            <{AlertDialogTrigger} render={t'<{Button} />'}>Open Alert Dialog</{AlertDialogTrigger}>
                            <{AlertDialogContent} size="sm">
                                <{AlertDialogHeader}>
                                    <{AlertDialogTitle}>Are you absolutely sure?</{AlertDialogTitle}>
                                    <{AlertDialogDescription}>
                                        This action cannot be undone. This will permanently delete your account and remove your data from our servers.
                                    </{AlertDialogDescription}>
                                </{AlertDialogHeader}>
                                <{AlertDialogFooter}>
                                    <{AlertDialogCancel}>Cancel</{AlertDialogCancel}>
                                    <{AlertDialogAction}>Continue</{AlertDialogAction}>
                                </{AlertDialogFooter}>
                            </{AlertDialogContent}>
                        </{AlertDialog}>
                    </{DialogFooter}>
                </{DialogContent}>
            </{Dialog}>
        </{Example}>
    """
