from example import Example, ExampleWrapper
from breadcrumb import (
    Breadcrumb, BreadcrumbEllipsis, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage, BreadcrumbSeparator,
)
from button import Button
from dropdown_menu import DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger

__js__ = {"next/link": ["default as Link"]}


def BreadcrumbExample():
    return t"""
        <{ExampleWrapper}>
            <{BreadcrumbBasic} />
            <{BreadcrumbWithDropdown} />
            <{BreadcrumbWithLink} />
        </{ExampleWrapper}>
    """


def BreadcrumbBasic():
    return t"""
        <{Example} title="Basic" class="items-center justify-center">
            <{Breadcrumb}>
                <{BreadcrumbList}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#">Home</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#">Components</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbPage}>Breadcrumb</{BreadcrumbPage}>
                    </{BreadcrumbItem}>
                </{BreadcrumbList}>
            </{Breadcrumb}>
        </{Example}>
    """


def BreadcrumbWithDropdown():
    return t"""
        <{Example} title="With Dropdown" class="items-center justify-center">
            <{Breadcrumb}>
                <{BreadcrumbList}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#">Home</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{DropdownMenu}>
                            <{DropdownMenuTrigger} render={t'<{Button} size="icon-sm" variant="ghost" />'}>
                                <{BreadcrumbEllipsis} />
                                <span class="sr-only">Toggle menu</span>
                            </{DropdownMenuTrigger}>
                            <{DropdownMenuContent} align="start">
                                <{DropdownMenuItem}>Documentation</{DropdownMenuItem}>
                                <{DropdownMenuItem}>Themes</{DropdownMenuItem}>
                                <{DropdownMenuItem}>GitHub</{DropdownMenuItem}>
                            </{DropdownMenuContent}>
                        </{DropdownMenu}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#">Components</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbPage}>Breadcrumb</{BreadcrumbPage}>
                    </{BreadcrumbItem}>
                </{BreadcrumbList}>
            </{Breadcrumb}>
        </{Example}>
    """


def BreadcrumbWithLink():
    return t"""
        <{Example} title="With Link" class="items-center justify-center">
            <{Breadcrumb}>
                <{BreadcrumbList}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} render={t'<{Link} href="#">Home</{Link}>'} />
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbEllipsis} />
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} render={t'<{Link} href="#">Components</{Link}>'} />
                    </{BreadcrumbItem}>
                    <{BreadcrumbSeparator} />
                    <{BreadcrumbItem}>
                        <{BreadcrumbPage}>Breadcrumb</{BreadcrumbPage}>
                    </{BreadcrumbItem}>
                </{BreadcrumbList}>
            </{Breadcrumb}>
        </{Example}>
    """
