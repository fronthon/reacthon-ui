from button import Button
from card import Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter
from input import Input
from label import Label
from checkbox import Checkbox
from tabs import Tabs, TabsList, TabsTrigger, TabsContent
from dialog import Dialog, DialogTrigger, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogFooter
from select import Select, SelectTrigger, SelectValue, SelectContent, SelectItem
from dropdown_menu import (
    DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator,
)
from accordion import Accordion, AccordionItem, AccordionTrigger, AccordionContent

FRUITS = ["apple", "pear", "plum"]


def App():
    name = ""
    subscribed = False
    plan = "free"
    shown = False
    picked = []

    def edit(event):
        name := event.target.value

    def toggle(checked):
        subscribed := checked is True

    def choose(value):
        plan := value

    def show(value):
        shown := value

    def close(event):
        shown := False

    def pick(fruit):
        return lambda event: picked.append(fruit)

    summary = f"{name or 'nobody'}, {plan}, {'subscribed' if subscribed else 'not subscribed'}"

    return t"""
        <div class="flex min-h-svh flex-col items-center gap-6 p-6">
            <{Card} class="w-full max-w-md">
                <{CardHeader}>
                    <{CardTitle}>Reacthon and shadcn/ui</{CardTitle}>
                    <{CardDescription}>Python components, shadcn/ui's own Radix parts.</{CardDescription}>
                </{CardHeader}>
                <{CardContent} class="flex flex-col gap-4">
                    <div class="flex flex-col gap-2">
                        <{Label} for="name">Name</{Label}>
                        <{Input} id="name" value={name} onChange={edit} placeholder="your name" />
                    </div>
                    <div class="flex items-center gap-2">
                        <{Checkbox} id="news" checked={subscribed} onCheckedChange={toggle} />
                        <{Label} for="news">Subscribe</{Label}>
                    </div>
                    <{Select} value={plan} onValueChange={choose}>
                        <{SelectTrigger} class="w-40" id="plan"><{SelectValue} placeholder="plan" /></{SelectTrigger}>
                        <{SelectContent}>
                            <{SelectItem} value="free">Free</{SelectItem}>
                            <{SelectItem} value="pro">Pro</{SelectItem}>
                        </{SelectContent}>
                    </{Select}>
                    <p id="summary">{summary}</p>
                </{CardContent}>
                <{CardFooter} class="flex gap-2">
                    <{Dialog} open={shown} onOpenChange={show}>
                        <{DialogTrigger} asChild><{Button} id="open">open the dialog</{Button}></{DialogTrigger}>
                        <{DialogContent}>
                            <{DialogHeader}>
                                <{DialogTitle}>Hello {name or "nobody"}</{DialogTitle}>
                                <{DialogDescription}>A Radix dialog, opened from Python state.</{DialogDescription}>
                            </{DialogHeader}>
                            <{DialogFooter}><{Button} id="close" onClick={close}>close</{Button}></{DialogFooter}>
                        </{DialogContent}>
                    </{Dialog}>
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} asChild>
                            <{Button} id="fruits" variant="outline">fruits ({len(picked)})</{Button}>
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent}>
                            <{DropdownMenuLabel}>Pick a fruit</{DropdownMenuLabel}>
                            <{DropdownMenuSeparator} />
                            {[t'<{DropdownMenuItem} key={fruit} id="fruit-{fruit}" onSelect={pick(fruit)}>{fruit}</{DropdownMenuItem}>' for fruit in FRUITS]}
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                </{CardFooter}>
            </{Card}>
            <{Tabs} defaultValue="python" class="w-full max-w-md">
                <{TabsList}>
                    <{TabsTrigger} value="python">Python</{TabsTrigger}>
                    <{TabsTrigger} value="react">React</{TabsTrigger}>
                </{TabsList}>
                <{TabsContent} value="python">picked: {", ".join(picked) or "nothing"}</{TabsContent}>
                <{TabsContent} value="react">the same parts, written in TSX</{TabsContent}>
            </{Tabs}>
            <{Accordion} type="single" collapsible class="w-full max-w-md">
                <{AccordionItem} value="why">
                    <{AccordionTrigger}>Why Python?</{AccordionTrigger}>
                    <{AccordionContent}>Because the component is yours to read.</{AccordionContent}>
                </{AccordionItem}>
            </{Accordion}>
        </div>
    """
