from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldDescription, FieldGroup, FieldLabel
from input import Input
from native_select import NativeSelect, NativeSelectOption
from textarea import Textarea


def GithubProfile():
    return t"""
        <{Card} class="mx-auto w-full max-w-md">
            <{CardHeader}>
                <{CardTitle}>Profile</{CardTitle}>
                <{CardDescription}>Manage your profile information.</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <form id="profile">
                    <{FieldGroup}>
                        <{Field}>
                            <{FieldLabel} for="name">Name</{FieldLabel}>
                            <{Input} id="name" placeholder="Taylor" />
                            <{FieldDescription}>
                                Your name may appear around GitHub where you contribute or are mentioned. You can remove it at any time.
                            </{FieldDescription}>
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="email">Public Email</{FieldLabel}>
                            <{NativeSelect} id="email">
                                <{NativeSelectOption} value="taylor@example.com">
                                    taylor@example.com
                                </{NativeSelectOption}>
                                <{NativeSelectOption} value="work@example.com">work@example.com</{NativeSelectOption}>
                            </{NativeSelect}>
                            <{FieldDescription}>
                                You can manage verified email addresses in your{" "}
                                <a href="#email-settings">email settings</a>.
                            </{FieldDescription}>
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="bio">Bio</{FieldLabel}>
                            <{Textarea} id="bio" placeholder="Tell us a little bit about yourself" />
                            <{FieldDescription}>
                                You can <span>@mention</span> other users and organizations to link to them.
                            </{FieldDescription}>
                        </{Field}>
                    </{FieldGroup}>
                </form>
            </{CardContent}>
            <{CardFooter}>
                <{Button} form="profile" class="style-sera:w-full">Save Profile</{Button}>
            </{CardFooter}>
        </{Card}>
    """
