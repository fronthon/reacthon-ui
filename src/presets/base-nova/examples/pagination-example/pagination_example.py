from example import Example, ExampleWrapper
from field import Field, FieldLabel
from pagination import (
    Pagination,
    PaginationContent,
    PaginationEllipsis,
    PaginationItem,
    PaginationLink,
    PaginationNext,
    PaginationPrevious,
)
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue


def PaginationExample():
    return t"""
        <{ExampleWrapper}>
            <{PaginationBasic} />
            <{PaginationSimple} />
            <{PaginationIconsOnly} />
        </{ExampleWrapper}>
    """


def PaginationBasic():
    return t"""
        <{Example} title="Basic">
            <{Pagination}>
                <{PaginationContent}>
                    <{PaginationItem}>
                        <{PaginationPrevious} href="#" />
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#">1</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#" isActive>2</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#">3</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationEllipsis} />
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationNext} href="#" />
                    </{PaginationItem}>
                </{PaginationContent}>
            </{Pagination}>
        </{Example}>
    """


def PaginationSimple():
    return t"""
        <{Example} title="Simple">
            <{Pagination}>
                <{PaginationContent}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#">1</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#" isActive>2</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#">3</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#">4</{PaginationLink}>
                    </{PaginationItem}>
                    <{PaginationItem}>
                        <{PaginationLink} href="#">5</{PaginationLink}>
                    </{PaginationItem}>
                </{PaginationContent}>
            </{Pagination}>
        </{Example}>
    """


def PaginationIconsOnly():
    return t"""
        <{Example} title="With Select">
            <div class="flex items-center justify-between gap-4">
                <{Field} orientation="horizontal" class="w-fit">
                    <{FieldLabel} for="select-rows-per-page">Rows per page</{FieldLabel}>
                    <{Select} defaultValue="25">
                        <{SelectTrigger} class="w-20" id="select-rows-per-page">
                            <{SelectValue} />
                        </{SelectTrigger}>
                        <{SelectContent} align="start">
                            <{SelectGroup}>
                                <{SelectItem} value="10">10</{SelectItem}>
                                <{SelectItem} value="25">25</{SelectItem}>
                                <{SelectItem} value="50">50</{SelectItem}>
                                <{SelectItem} value="100">100</{SelectItem}>
                            </{SelectGroup}>
                        </{SelectContent}>
                    </{Select}>
                </{Field}>
                <{Pagination} class="mx-0 w-auto">
                    <{PaginationContent}>
                        <{PaginationItem}>
                            <{PaginationPrevious} href="#" />
                        </{PaginationItem}>
                        <{PaginationItem}>
                            <{PaginationNext} href="#" />
                        </{PaginationItem}>
                    </{PaginationContent}>
                </{Pagination}>
            </div>
        </{Example}>
    """
