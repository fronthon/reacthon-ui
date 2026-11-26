from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldLabel
from input import Input
from input_group import InputGroup, InputGroupAddon, InputGroupButton, InputGroupInput
from select import Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue
from separator import Separator

__js__ = {"lucide-react": ["CopyIcon", "PlusIcon"]}


def InviteTeam():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Invite Team</{CardTitle}>
                <{CardDescription}>Add members to your workspace</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <div class="flex flex-col gap-3">
                    {[t'''
                        <div key={invite["email"]} class="flex items-center gap-2">
                            <{Input} defaultValue={invite["email"]} class="flex-1" />
                            <{Select} defaultValue={invite["role"].lower()}>
                                <{SelectTrigger} class="w-24">
                                    <{SelectValue} />
                                </{SelectTrigger}>
                                <{SelectContent} placement="bottom end">
                                    <{SelectGroup}>
                                        <{SelectItem} id="admin">Admin</{SelectItem}>
                                        <{SelectItem} id="editor">Editor</{SelectItem}>
                                        <{SelectItem} id="viewer">Viewer</{SelectItem}>
                                    </{SelectGroup}>
                                </{SelectContent}>
                            </{Select}>
                        </div>
                    ''' for invite in [{"email": "alex@example.com", "role": "Editor"}, {"email": "sam@example.com", "role": "Viewer"}]]}
                </div>
                <{Button} variant="outline">
                    <{PlusIcon} data-icon="inline-start" />
                    Add another
                </{Button}>
                <{Separator} />
                <{Field}>
                    <{FieldLabel} for="invite-link">Or share invite link</{FieldLabel}>
                    <{InputGroup}>
                        <{InputGroupInput} id="invite-link" defaultValue="https://app.co/invite/x8f2k" readOnly />
                        <{InputGroupAddon} align="inline-end">
                            <{InputGroupButton} size="icon-xs" aria-label="Copy link">
                                <{CopyIcon} />
                            </{InputGroupButton}>
                        </{InputGroupAddon}>
                    </{InputGroup}>
                </{Field}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">Send Invites</{Button}>
            </{CardFooter}>
        </{Card}>
    """
