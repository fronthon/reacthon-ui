from example import Example, ExampleWrapper
from breadcrumb import Breadcrumb, BreadcrumbEllipsis, BreadcrumbItem, BreadcrumbLink, BreadcrumbList, BreadcrumbPage
from button import Button
from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuTrigger

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
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#">Components</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
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
                    <{BreadcrumbItem}>
                        <{DropdownMenuTrigger}>
                            <{Button} size="icon-sm" variant="ghost">
                                <{BreadcrumbEllipsis} />
                                <span class="sr-only">Toggle menu</span>
                            </{Button}>
                            <{DropdownMenu} placement="bottom start">
                                <{DropdownMenuItem}>Documentation</{DropdownMenuItem}>
                                <{DropdownMenuItem}>Themes</{DropdownMenuItem}>
                                <{DropdownMenuItem}>GitHub</{DropdownMenuItem}>
                            </{DropdownMenu}>
                        </{DropdownMenuTrigger}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#">Components</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbPage}>Breadcrumb</{BreadcrumbPage}>
                    </{BreadcrumbItem}>
                </{BreadcrumbList}>
            </{Breadcrumb}>
        </{Example}>
    """


def BreadcrumbWithLink():
    def render(props):
        return t"<{Link} ...{props} />" if "href" in props else t"<span ...{props} />"

    def render_2(props):
        return t"<{Link} ...{props} />" if "href" in props else t"<span ...{props} />"

    return t"""
        <{Example} title="With Link" class="items-center justify-center">
            <{Breadcrumb}>
                <{BreadcrumbList}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#" render={render}>Home</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbEllipsis} />
                    </{BreadcrumbItem}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbLink} href="#" render={render_2}>Components</{BreadcrumbLink}>
                    </{BreadcrumbItem}>
                    <{BreadcrumbItem}>
                        <{BreadcrumbPage}>Breadcrumb</{BreadcrumbPage}>
                    </{BreadcrumbItem}>
                </{BreadcrumbList}>
            </{Breadcrumb}>
        </{Example}>
    """
