from avatar import Avatar, AvatarFallback, AvatarImage
from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle
from combobox import (
    Combobox,
    ComboboxChip,
    ComboboxChipList,
    ComboboxChips,
    ComboboxChipsInput,
    ComboboxContent,
    ComboboxEmpty,
    ComboboxItem,
    ComboboxList,
)
from tooltip import Tooltip, TooltipTrigger

__js__ = {"lucide-react": ["PlusIcon"]}

users = ["shadcn", "maxleiter", "evilrabbit", "pranathip", "jorgezreik", "shuding", "rauchg"]


def AssignIssue():
    return t"""
        <{Card} class="w-full max-w-sm" size="sm">
            <{CardHeader} class="border-b">
                <{CardTitle} class="text-sm">Assign Issue</{CardTitle}>
                <{CardDescription} class="text-sm">Select users to assign to this issue.</{CardDescription}>
                <{CardAction}>
                    <{TooltipTrigger}>
                        <{Button} variant="outline" size="icon-xs">
                            <{PlusIcon} />
                        </{Button}>
                        <{Tooltip}>Add user</{Tooltip}>
                    </{TooltipTrigger}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{Combobox} selectionMode="multiple" defaultValue={[users[0]]} allowsEmptyCollection>
                    <{ComboboxChips}>
                        <{ComboboxChipList}>
                            {(lambda value: t'''
                                <{ComboboxChip} id={value["username"]}>
                                    <{Avatar} class="size-4">
                                        <{AvatarImage}
                                            src={f"https://github.com/{value["username"]}.png"}
                                            alt={value["username"]}
                                        />
                                        <{AvatarFallback}>{value["username"][:1]}</{AvatarFallback}>
                                    </{Avatar}>
                                    {value["username"]}
                                </{ComboboxChip}>
                            ''')}
                        </{ComboboxChipList}>
                        <{ComboboxChipsInput} placeholder="Select a item..." />
                    </{ComboboxChips}>
                    <{ComboboxContent}>
                        <{ComboboxList} renderEmptyState={(lambda: t'<{ComboboxEmpty}>No users found.</{ComboboxEmpty}>')}>
                            {[t'''
                                <{ComboboxItem}
                                    key={username}
                                    id={username}
                                    value={ {
                                        "username": username,
                                    } }
                                    textValue={username}
                                >
                                    <{Avatar} class="size-5">
                                        <{AvatarImage} src={f"https://github.com/{username}.png"} alt={username} />
                                        <{AvatarFallback}>{username[:1]}</{AvatarFallback}>
                                    </{Avatar}>
                                    {username}
                                </{ComboboxItem}>
                            ''' for username in users]}
                        </{ComboboxList}>
                    </{ComboboxContent}>
                </{Combobox}>
            </{CardContent}>
        </{Card}>
    """
