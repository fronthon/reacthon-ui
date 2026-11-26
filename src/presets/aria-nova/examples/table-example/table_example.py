from example import Example, ExampleWrapper
from button import Button
from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger
from input import Input
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from table import Table, TableBody, TableCaption, TableCell, TableFooter, TableHead, TableHeader, TableRow

__js__ = {"lucide-react": ["MoreHorizontalIcon"]}

invoices = [
    {"invoice": "INV001", "paymentStatus": "Paid", "totalAmount": "$250.00", "paymentMethod": "Credit Card"},
    {"invoice": "INV002", "paymentStatus": "Pending", "totalAmount": "$150.00", "paymentMethod": "PayPal"},
    {"invoice": "INV003", "paymentStatus": "Unpaid", "totalAmount": "$350.00", "paymentMethod": "Bank Transfer"},
    {"invoice": "INV004", "paymentStatus": "Paid", "totalAmount": "$450.00", "paymentMethod": "Credit Card"},
    {"invoice": "INV005", "paymentStatus": "Paid", "totalAmount": "$550.00", "paymentMethod": "PayPal"},
    {"invoice": "INV006", "paymentStatus": "Pending", "totalAmount": "$200.00", "paymentMethod": "Bank Transfer"},
    {"invoice": "INV007", "paymentStatus": "Unpaid", "totalAmount": "$300.00", "paymentMethod": "Credit Card"},
]


def TableExample():
    return t"""
        <{ExampleWrapper}>
            <{TableBasic} />
            <{TableWithFooter} />
            <{TableSimple} />
            <{TableWithBadges} />
            <{TableWithActions} />
            <{TableWithSelect} />
            <{TableWithInput} />
        </{ExampleWrapper}>
    """


def TableBasic():
    return t"""
        <{Example} title="Basic">
            <figure>
                <{Table}>
                    <{TableHeader}>
                        <{TableHead} isRowHeader class="w-[100px]">Invoice</{TableHead}>
                        <{TableHead}>Status</{TableHead}>
                        <{TableHead}>Method</{TableHead}>
                        <{TableHead} class="text-right">Amount</{TableHead}>
                    </{TableHeader}>
                    <{TableBody}>
                        {[t'''
                            <{TableRow} key={invoice["invoice"]}>
                                <{TableCell} class="font-medium">{invoice["invoice"]}</{TableCell}>
                                <{TableCell}>{invoice["paymentStatus"]}</{TableCell}>
                                <{TableCell}>{invoice["paymentMethod"]}</{TableCell}>
                                <{TableCell} class="text-right">{invoice["totalAmount"]}</{TableCell}>
                            </{TableRow}>
                        ''' for invoice in invoices[0:3]]}
                    </{TableBody}>
                </{Table}>
                <{TableCaption}>A list of your recent invoices.</{TableCaption}>
            </figure>
        </{Example}>
    """


def TableWithFooter():
    return t"""
        <{Example} title="With Footer">
            <figure>
                <{Table}>
                    <{TableHeader}>
                        <{TableHead} isRowHeader class="w-[100px]">Invoice</{TableHead}>
                        <{TableHead}>Status</{TableHead}>
                        <{TableHead}>Method</{TableHead}>
                        <{TableHead} class="text-right">Amount</{TableHead}>
                    </{TableHeader}>
                    <{TableBody}>
                        {[t'''
                            <{TableRow} key={invoice["invoice"]}>
                                <{TableCell} class="font-medium">{invoice["invoice"]}</{TableCell}>
                                <{TableCell}>{invoice["paymentStatus"]}</{TableCell}>
                                <{TableCell}>{invoice["paymentMethod"]}</{TableCell}>
                                <{TableCell} class="text-right">{invoice["totalAmount"]}</{TableCell}>
                            </{TableRow}>
                        ''' for invoice in invoices[0:3]]}
                    </{TableBody}>
                    <{TableFooter}>
                        <{TableRow}>
                            <{TableCell} colSpan={3}>Total</{TableCell}>
                            <{TableCell} class="text-right">$2,500.00</{TableCell}>
                        </{TableRow}>
                    </{TableFooter}>
                </{Table}>
                <{TableCaption}>A list of your recent invoices.</{TableCaption}>
            </figure>
        </{Example}>
    """


def TableSimple():
    return t"""
        <{Example} title="Simple">
            <{Table}>
                <{TableHeader}>
                    <{TableHead} isRowHeader>Name</{TableHead}>
                    <{TableHead}>Email</{TableHead}>
                    <{TableHead} class="text-right">Role</{TableHead}>
                </{TableHeader}>
                <{TableBody}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Alex Morgan</{TableCell}>
                        <{TableCell}>alex@example.com</{TableCell}>
                        <{TableCell} class="text-right">Admin</{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Jordan Lee</{TableCell}>
                        <{TableCell}>jordan@example.com</{TableCell}>
                        <{TableCell} class="text-right">User</{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Taylor Kim</{TableCell}>
                        <{TableCell}>taylor@example.com</{TableCell}>
                        <{TableCell} class="text-right">User</{TableCell}>
                    </{TableRow}>
                </{TableBody}>
            </{Table}>
        </{Example}>
    """


def TableWithBadges():
    return t"""
        <{Example} title="With Badges">
            <{Table}>
                <{TableHeader}>
                    <{TableHead} isRowHeader>Task</{TableHead}>
                    <{TableHead}>Status</{TableHead}>
                    <{TableHead} class="text-right">Priority</{TableHead}>
                </{TableHeader}>
                <{TableBody}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Design homepage</{TableCell}>
                        <{TableCell}>
                            <span class="inline-flex items-center rounded-full bg-green-500/10 px-2 py-1 text-xs font-medium text-green-700 dark:text-green-400">
                                Completed
                            </span>
                        </{TableCell}>
                        <{TableCell} class="text-right">
                            <span class="inline-flex items-center rounded-full bg-blue-500/10 px-2 py-1 text-xs font-medium text-blue-700 dark:text-blue-400">
                                High
                            </span>
                        </{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Implement API</{TableCell}>
                        <{TableCell}>
                            <span class="inline-flex items-center rounded-full bg-yellow-500/10 px-2 py-1 text-xs font-medium text-yellow-700 dark:text-yellow-400">
                                In Progress
                            </span>
                        </{TableCell}>
                        <{TableCell} class="text-right">
                            <span class="inline-flex items-center rounded-full bg-gray-500/10 px-2 py-1 text-xs font-medium text-gray-700 dark:text-gray-400">
                                Medium
                            </span>
                        </{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Write tests</{TableCell}>
                        <{TableCell}>
                            <span class="inline-flex items-center rounded-full bg-gray-500/10 px-2 py-1 text-xs font-medium text-gray-700 dark:text-gray-400">
                                Pending
                            </span>
                        </{TableCell}>
                        <{TableCell} class="text-right">
                            <span class="inline-flex items-center rounded-full bg-gray-500/10 px-2 py-1 text-xs font-medium text-gray-700 dark:text-gray-400">
                                Low
                            </span>
                        </{TableCell}>
                    </{TableRow}>
                </{TableBody}>
            </{Table}>
        </{Example}>
    """


def TableWithActions():
    return t"""
        <{Example} title="With Actions">
            <{Table}>
                <{TableHeader}>
                    <{TableHead} isRowHeader>Product</{TableHead}>
                    <{TableHead}>Price</{TableHead}>
                    <{TableHead} class="text-right">Actions</{TableHead}>
                </{TableHeader}>
                <{TableBody}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Wireless Mouse</{TableCell}>
                        <{TableCell}>$29.99</{TableCell}>
                        <{TableCell} class="text-right">
                            <{DropdownMenuTrigger}>
                                <{Button} variant="ghost" size="icon" class="size-8">
                                    <{MoreHorizontalIcon} />
                                    <span class="sr-only">Open menu</span>
                                </{Button}>
                                <{DropdownMenu} placement="bottom end">
                                    <{DropdownMenuItem}>Edit</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Duplicate</{DropdownMenuItem}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuItem} variant="destructive">Delete</{DropdownMenuItem}>
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Mechanical Keyboard</{TableCell}>
                        <{TableCell}>$129.99</{TableCell}>
                        <{TableCell} class="text-right">
                            <{DropdownMenuTrigger}>
                                <{Button} variant="ghost" size="icon" class="size-8">
                                    <{MoreHorizontalIcon} />
                                    <span class="sr-only">Open menu</span>
                                </{Button}>
                                <{DropdownMenu} placement="bottom end">
                                    <{DropdownMenuItem}>Edit</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Duplicate</{DropdownMenuItem}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuItem} variant="destructive">Delete</{DropdownMenuItem}>
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">USB-C Hub</{TableCell}>
                        <{TableCell}>$49.99</{TableCell}>
                        <{TableCell} class="text-right">
                            <{DropdownMenuTrigger}>
                                <{Button} variant="ghost" size="icon" class="size-8">
                                    <{MoreHorizontalIcon} />
                                    <span class="sr-only">Open menu</span>
                                </{Button}>
                                <{DropdownMenu} placement="bottom end">
                                    <{DropdownMenuItem}>Edit</{DropdownMenuItem}>
                                    <{DropdownMenuItem}>Duplicate</{DropdownMenuItem}>
                                    <{DropdownMenuSeparator} />
                                    <{DropdownMenuItem} variant="destructive">Delete</{DropdownMenuItem}>
                                </{DropdownMenu}>
                            </{DropdownMenuTrigger}>
                        </{TableCell}>
                    </{TableRow}>
                </{TableBody}>
            </{Table}>
        </{Example}>
    """


people = [
    {"value": "sarah", "label": "Sarah Chen"},
    {"value": "marcus", "label": "Marc Rodriguez"},
    {"value": "emily", "label": "Emily Watson"},
    {"value": "david", "label": "David Kim"},
]

tasks = [
    {"task": "Design homepage", "assignee": "sarah", "status": "In Progress"},
    {"task": "Implement API", "assignee": "marcus", "status": "Pending"},
    {"task": "Write tests", "assignee": "emily", "status": "Not Started"},
]


def TableWithSelect():
    return t"""
        <{Example} title="With Select">
            <{Table}>
                <{TableHeader}>
                    <{TableHead} isRowHeader>Task</{TableHead}>
                    <{TableHead}>Assignee</{TableHead}>
                    <{TableHead}>Status</{TableHead}>
                </{TableHeader}>
                <{TableBody}>
                    {[t'''
                        <{TableRow} key={item["task"]}>
                            <{TableCell} class="font-medium">{item["task"]}</{TableCell}>
                            <{TableCell}>
                                <{Select} defaultValue={item["assignee"]}>
                                    <{SelectTrigger} class="w-40" size="sm">
                                        <{SelectValue} />
                                    </{SelectTrigger}>
                                    <{SelectContent}>
                                        <{SelectGroup}>
                                            {[t"""
                                                <{SelectItem}
                                                    key={person["value"]}
                                                    id={person["value"]}
                                                >
                                                    {person["label"]}
                                                </{SelectItem}>
                                            """ for person in people]}
                                        </{SelectGroup}>
                                    </{SelectContent}>
                                </{Select}>
                            </{TableCell}>
                            <{TableCell}>{item["status"]}</{TableCell}>
                        </{TableRow}>
                    ''' for item in tasks]}
                </{TableBody}>
            </{Table}>
        </{Example}>
    """


def TableWithInput():
    return t"""
        <{Example} title="With Input">
            <{Table}>
                <{TableHeader}>
                    <{TableHead} isRowHeader>Product</{TableHead}>
                    <{TableHead}>Quantity</{TableHead}>
                    <{TableHead}>Price</{TableHead}>
                </{TableHeader}>
                <{TableBody}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Wireless Mouse</{TableCell}>
                        <{TableCell}>
                            <{Input} type="number" defaultValue="1" class="h-8 w-20" min="0" />
                        </{TableCell}>
                        <{TableCell}>$29.99</{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">Mechanical Keyboard</{TableCell}>
                        <{TableCell}>
                            <{Input} type="number" defaultValue="2" class="h-8 w-20" min="0" />
                        </{TableCell}>
                        <{TableCell}>$129.99</{TableCell}>
                    </{TableRow}>
                    <{TableRow}>
                        <{TableCell} class="font-medium">USB-C Hub</{TableCell}>
                        <{TableCell}>
                            <{Input} type="number" defaultValue="1" class="h-8 w-20" min="0" />
                        </{TableCell}>
                        <{TableCell}>$49.99</{TableCell}>
                    </{TableRow}>
                </{TableBody}>
            </{Table}>
        </{Example}>
    """
