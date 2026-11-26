from example import Example, ExampleWrapper
from button import Button
from dropdown_menu import (
    DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger,
)
from input import Input
from tabs import Tabs, TabsContent, TabsList, TabsTrigger

__js__ = {"lucide-react": ["AppWindowIcon", "CodeIcon", "HomeIcon", "SearchIcon", "SettingsIcon", "MoreHorizontalIcon"]}


def TabsExample():
    return t"""
        <{ExampleWrapper}>
            <{TabsBasic} />
            <{TabsLine} />
            <{TabsVariantsComparison} />
            <{TabsDisabled} />
            <{TabsWithIcons} />
            <{TabsIconOnly} />
            <{TabsMultiple} />
            <{TabsWithContent} />
            <{TabsLineWithContent} />
            <{TabsLineDisabled} />
            <{TabsWithDropdown} />
            <{TabsVertical} />
            <{TabsWithInputAndButton} />
        </{ExampleWrapper}>
    """


def TabsBasic():
    return t"""
        <{Example} title="Basic">
            <{Tabs} defaultValue="home">
                <{TabsList}>
                    <{TabsTrigger} value="home">Home</{TabsTrigger}>
                    <{TabsTrigger} value="settings">Settings</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsLine():
    return t"""
        <{Example} title="Line">
            <{Tabs} defaultValue="overview">
                <{TabsList} variant="line">
                    <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                    <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                    <{TabsTrigger} value="reports">Reports</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsVariantsComparison():
    return t"""
        <{Example} title="Variants Alignment">
            <div class="flex gap-4">
                <{Tabs} defaultValue="overview">
                    <{TabsList}>
                        <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                    </{TabsList}>
                </{Tabs}>
                <{Tabs} defaultValue="overview">
                    <{TabsList} variant="line">
                        <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                    </{TabsList}>
                </{Tabs}>
            </div>
        </{Example}>
    """


def TabsDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Tabs} defaultValue="home">
                <{TabsList}>
                    <{TabsTrigger} value="home">Home</{TabsTrigger}>
                    <{TabsTrigger} value="settings" disabled>Disabled</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{Tabs} defaultValue="preview">
                <{TabsList}>
                    <{TabsTrigger} value="preview">
                        <{AppWindowIcon} />
                        Preview
                    </{TabsTrigger}>
                    <{TabsTrigger} value="code">
                        <{CodeIcon} />
                        Code
                    </{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsIconOnly():
    return t"""
        <{Example} title="Icon Only">
            <{Tabs} defaultValue="home">
                <{TabsList}>
                    <{TabsTrigger} value="home">
                        <{HomeIcon} />
                    </{TabsTrigger}>
                    <{TabsTrigger} value="search">
                        <{SearchIcon} />
                    </{TabsTrigger}>
                    <{TabsTrigger} value="settings">
                        <{SettingsIcon} />
                    </{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsMultiple():
    return t"""
        <{Example} title="Multiple">
            <{Tabs} defaultValue="overview">
                <{TabsList}>
                    <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                    <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                    <{TabsTrigger} value="reports">Reports</{TabsTrigger}>
                    <{TabsTrigger} value="settings">Settings</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsWithContent():
    return t"""
        <{Example} title="With Content">
            <{Tabs} defaultValue="account">
                <{TabsList}>
                    <{TabsTrigger} value="account">Account</{TabsTrigger}>
                    <{TabsTrigger} value="password">Password</{TabsTrigger}>
                    <{TabsTrigger} value="notifications">Notifications</{TabsTrigger}>
                </{TabsList}>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} value="account">
                        Manage your account preferences and profile information.
                    </{TabsContent}>
                    <{TabsContent} value="password">Update your password to keep your account secure.</{TabsContent}>
                    <{TabsContent} value="notifications">
                        Configure how you receive notifications and alerts.
                    </{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsLineWithContent():
    return t"""
        <{Example} title="Line With Content">
            <{Tabs} defaultValue="account">
                <{TabsList} variant="line">
                    <{TabsTrigger} value="account">Account</{TabsTrigger}>
                    <{TabsTrigger} value="password">Password</{TabsTrigger}>
                    <{TabsTrigger} value="notifications">Notifications</{TabsTrigger}>
                </{TabsList}>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} value="account">
                        Manage your account preferences and profile information.
                    </{TabsContent}>
                    <{TabsContent} value="password">Update your password to keep your account secure.</{TabsContent}>
                    <{TabsContent} value="notifications">
                        Configure how you receive notifications and alerts.
                    </{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsLineDisabled():
    return t"""
        <{Example} title="Line Disabled">
            <{Tabs} defaultValue="overview">
                <{TabsList} variant="line">
                    <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                    <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                    <{TabsTrigger} value="reports" disabled>Reports</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsWithDropdown():
    return t"""
        <{Example} title="With Dropdown">
            <{Tabs} defaultValue="overview">
                <div class="flex items-center justify-between">
                    <{TabsList}>
                        <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                        <{TabsTrigger} value="reports">Reports</{TabsTrigger}>
                    </{TabsList}>
                    <{DropdownMenu}>
                        <{DropdownMenuTrigger} render={t'<{Button} variant="ghost" size="icon" class="size-8" />'}>
                            <{MoreHorizontalIcon} />
                            <span class="sr-only">More options</span>
                        </{DropdownMenuTrigger}>
                        <{DropdownMenuContent} align="end">
                            <{DropdownMenuItem}>Settings</{DropdownMenuItem}>
                            <{DropdownMenuItem}>Export</{DropdownMenuItem}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuItem}>Archive</{DropdownMenuItem}>
                        </{DropdownMenuContent}>
                    </{DropdownMenu}>
                </div>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} value="overview">
                        View your dashboard metrics and key performance indicators.
                    </{TabsContent}>
                    <{TabsContent} value="analytics">Detailed analytics and insights about your data.</{TabsContent}>
                    <{TabsContent} value="reports">Generate and view custom reports.</{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsVertical():
    return t"""
        <{Example} title="Vertical">
            <{Tabs} defaultValue="account" orientation="vertical">
                <{TabsList}>
                    <{TabsTrigger} value="account">Account</{TabsTrigger}>
                    <{TabsTrigger} value="password">Password</{TabsTrigger}>
                    <{TabsTrigger} value="notifications">Notifications</{TabsTrigger}>
                </{TabsList}>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} value="account">
                        Manage your account preferences and profile information.
                    </{TabsContent}>
                    <{TabsContent} value="password">
                        Update your password to keep your account secure. Use a strong password with a mix of letters, numbers, and symbols.
                    </{TabsContent}>
                    <{TabsContent} value="notifications">
                        Configure how you receive notifications and alerts. Choose which types of notifications you want to receive and how you want to receive them.
                    </{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsWithInputAndButton():
    return t"""
        <{Example} title="With Input and Button" containerClassName="col-span-full">
            <{Tabs} defaultValue="overview" class="mx-auto w-full max-w-lg">
                <div class="flex items-center gap-4">
                    <{TabsList}>
                        <{TabsTrigger} value="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} value="analytics">Analytics</{TabsTrigger}>
                    </{TabsList}>
                    <div class="ml-auto flex items-center gap-2">
                        <{Input} placeholder="Search..." class="w-44" />
                        <{Button}>Action</{Button}>
                    </div>
                </div>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} value="overview">
                        View your dashboard metrics and key performance indicators.
                    </{TabsContent}>
                    <{TabsContent} value="analytics">Detailed analytics and insights about your data.</{TabsContent}>
                    <{TabsContent} value="reports">Generate and view custom reports.</{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """
