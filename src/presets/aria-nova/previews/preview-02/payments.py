from breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage
from button import Button
from card import Card, CardContent, CardHeader
from dropdown_menu import DropdownMenu, DropdownMenuGroup, DropdownMenuItem, DropdownMenuTrigger
from item import Item, ItemContent, ItemDescription, ItemGroup, ItemMedia, ItemTitle

__js__ = {
    "lucide-react": [
        "CalendarIcon",
        "ChevronRightIcon",
        "GaugeIcon",
        "MoreHorizontalIcon",
        "RefreshCwIcon",
        "RepeatIcon",
    ],
}


def Payments():
    return t"""
        <{Card}>
            <{CardHeader} class="flex flex-col gap-3">
                <{Breadcrumb}>
                    <{BreadcrumbList}>
                        <{BreadcrumbItem}>
                            <{BreadcrumbLink} href="#">Home</{BreadcrumbLink}>
                        </{BreadcrumbItem}>
                        <{BreadcrumbItem}>
                            <{DropdownMenuTrigger}>
                                <{Button} size="icon-sm" variant="ghost">
                                    <{MoreHorizontalIcon} />
                                    <span class="sr-only">Account options</span>
                                </{Button}>
                                <{DropdownMenu} placement="bottom start">
                                    <{DropdownMenuGroup}>
                                        <{DropdownMenuItem}>Profile</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Statements</{DropdownMenuItem}>
                                        <{DropdownMenuItem}>Documents</{DropdownMenuItem}>
                                    </{DropdownMenuGroup}>
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{BreadcrumbItem}>
                        <{BreadcrumbItem}>
                            <{BreadcrumbPage}>Payments</{BreadcrumbPage}>
                        </{BreadcrumbItem}>
                    </{BreadcrumbList}>
                </{Breadcrumb}>
            </{CardHeader}>
            <{CardContent}>
                <{ItemGroup}>
                    <{Item} variant="muted" href="#">
                        <{ItemMedia} variant="icon">
                            <{GaugeIcon} />
                        </{ItemMedia}>
                        <{ItemContent}>
                            <{ItemTitle}>Change transfer limit</{ItemTitle}>
                            <{ItemDescription}>Adjust how much you can send from your balance.</{ItemDescription}>
                        </{ItemContent}>
                        <{ChevronRightIcon} class="size-4 shrink-0 text-muted-foreground" />
                    </{Item}>
                    <{Item} variant="muted" href="#">
                        <{ItemMedia} variant="icon">
                            <{CalendarIcon} />
                        </{ItemMedia}>
                        <{ItemContent}>
                            <{ItemTitle}>Scheduled transfers</{ItemTitle}>
                            <{ItemDescription}>Set up a transfer to send at a later date.</{ItemDescription}>
                        </{ItemContent}>
                        <{ChevronRightIcon} class="size-4 shrink-0 text-muted-foreground" />
                    </{Item}>
                    <{Item} variant="muted" href="#">
                        <{ItemMedia} variant="icon">
                            <{RepeatIcon} />
                        </{ItemMedia}>
                        <{ItemContent}>
                            <{ItemTitle}>Direct Debits</{ItemTitle}>
                            <{ItemDescription}>Set up and manage regular payments.</{ItemDescription}>
                        </{ItemContent}>
                        <{ChevronRightIcon} class="size-4 shrink-0 text-muted-foreground" />
                    </{Item}>
                    <{Item} variant="muted" href="#">
                        <{ItemMedia} variant="icon">
                            <{RefreshCwIcon} />
                        </{ItemMedia}>
                        <{ItemContent}>
                            <{ItemTitle}>Recurring card payments</{ItemTitle}>
                            <{ItemDescription}>Manage your repeated card transactions.</{ItemDescription}>
                        </{ItemContent}>
                        <{ChevronRightIcon} class="size-4 shrink-0 text-muted-foreground" />
                    </{Item}>
                </{ItemGroup}>
            </{CardContent}>
        </{Card}>
    """
