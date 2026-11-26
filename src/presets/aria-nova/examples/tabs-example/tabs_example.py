from example import Example, ExampleWrapper
from button import Button
from dropdown_menu import DropdownMenu, DropdownMenuItem, DropdownMenuSeparator, DropdownMenuTrigger
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
            <{Tabs} defaultSelectedKey="home">
                <{TabsList}>
                    <{TabsTrigger} id="home">Home</{TabsTrigger}>
                    <{TabsTrigger} id="settings">Settings</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsLine():
    return t"""
        <{Example} title="Line">
            <{Tabs} defaultSelectedKey="overview">
                <{TabsList} variant="line">
                    <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                    <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                    <{TabsTrigger} id="reports">Reports</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsVariantsComparison():
    return t"""
        <{Example} title="Variants Alignment">
            <div class="flex gap-4">
                <{Tabs} defaultSelectedKey="overview">
                    <{TabsList}>
                        <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                    </{TabsList}>
                </{Tabs}>
                <{Tabs} defaultSelectedKey="overview">
                    <{TabsList} variant="line">
                        <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                    </{TabsList}>
                </{Tabs}>
            </div>
        </{Example}>
    """


def TabsDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Tabs} defaultSelectedKey="home">
                <{TabsList}>
                    <{TabsTrigger} id="home">Home</{TabsTrigger}>
                    <{TabsTrigger} id="settings" isDisabled>Disabled</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsWithIcons():
    return t"""
        <{Example} title="With Icons">
            <{Tabs} defaultSelectedKey="preview">
                <{TabsList}>
                    <{TabsTrigger} id="preview">
                        <{AppWindowIcon} />
                        Preview
                    </{TabsTrigger}>
                    <{TabsTrigger} id="code">
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
            <{Tabs} defaultSelectedKey="home">
                <{TabsList}>
                    <{TabsTrigger} id="home">
                        <{HomeIcon} />
                    </{TabsTrigger}>
                    <{TabsTrigger} id="search">
                        <{SearchIcon} />
                    </{TabsTrigger}>
                    <{TabsTrigger} id="settings">
                        <{SettingsIcon} />
                    </{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsMultiple():
    return t"""
        <{Example} title="Multiple">
            <{Tabs} defaultSelectedKey="overview">
                <{TabsList}>
                    <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                    <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                    <{TabsTrigger} id="reports">Reports</{TabsTrigger}>
                    <{TabsTrigger} id="settings">Settings</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsWithContent():
    return t"""
        <{Example} title="With Content">
            <{Tabs} defaultSelectedKey="account">
                <{TabsList}>
                    <{TabsTrigger} id="account">Account</{TabsTrigger}>
                    <{TabsTrigger} id="password">Password</{TabsTrigger}>
                    <{TabsTrigger} id="notifications">Notifications</{TabsTrigger}>
                </{TabsList}>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} id="account">Manage your account preferences and profile information.</{TabsContent}>
                    <{TabsContent} id="password">Update your password to keep your account secure.</{TabsContent}>
                    <{TabsContent} id="notifications">
                        Configure how you receive notifications and alerts.
                    </{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsLineWithContent():
    return t"""
        <{Example} title="Line With Content">
            <{Tabs} defaultSelectedKey="account">
                <{TabsList} variant="line">
                    <{TabsTrigger} id="account">Account</{TabsTrigger}>
                    <{TabsTrigger} id="password">Password</{TabsTrigger}>
                    <{TabsTrigger} id="notifications">Notifications</{TabsTrigger}>
                </{TabsList}>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} id="account">Manage your account preferences and profile information.</{TabsContent}>
                    <{TabsContent} id="password">Update your password to keep your account secure.</{TabsContent}>
                    <{TabsContent} id="notifications">
                        Configure how you receive notifications and alerts.
                    </{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsLineDisabled():
    return t"""
        <{Example} title="Line Disabled">
            <{Tabs} defaultSelectedKey="overview">
                <{TabsList} variant="line">
                    <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                    <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                    <{TabsTrigger} id="reports" isDisabled>Reports</{TabsTrigger}>
                </{TabsList}>
            </{Tabs}>
        </{Example}>
    """


def TabsWithDropdown():
    return t"""
        <{Example} title="With Dropdown">
            <{Tabs} defaultSelectedKey="overview">
                <div class="flex items-center justify-between">
                    <{TabsList}>
                        <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                        <{TabsTrigger} id="reports">Reports</{TabsTrigger}>
                    </{TabsList}>
                    <{DropdownMenuTrigger}>
                        <{Button} variant="ghost" size="icon" class="size-8">
                            <{MoreHorizontalIcon} />
                            <span class="sr-only">More options</span>
                        </{Button}>
                        <{DropdownMenu} placement="bottom end">
                            <{DropdownMenuItem}>Settings</{DropdownMenuItem}>
                            <{DropdownMenuItem}>Export</{DropdownMenuItem}>
                            <{DropdownMenuSeparator} />
                            <{DropdownMenuItem}>Archive</{DropdownMenuItem}>
                        </{DropdownMenu}>
                    </{DropdownMenuTrigger}>
                </div>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} id="overview">
                        View your dashboard metrics and key performance indicators.
                    </{TabsContent}>
                    <{TabsContent} id="analytics">Detailed analytics and insights about your data.</{TabsContent}>
                    <{TabsContent} id="reports">Generate and view custom reports.</{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsVertical():
    return t"""
        <{Example} title="Vertical">
            <{Tabs} defaultSelectedKey="account" orientation="vertical">
                <{TabsList}>
                    <{TabsTrigger} id="account">Account</{TabsTrigger}>
                    <{TabsTrigger} id="password">Password</{TabsTrigger}>
                    <{TabsTrigger} id="notifications">Notifications</{TabsTrigger}>
                </{TabsList}>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} id="account">Manage your account preferences and profile information.</{TabsContent}>
                    <{TabsContent} id="password">
                        Update your password to keep your account secure. Use a strong password with a mix of letters, numbers, and symbols.
                    </{TabsContent}>
                    <{TabsContent} id="notifications">
                        Configure how you receive notifications and alerts. Choose which types of notifications you want to receive and how you want to receive them.
                    </{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """


def TabsWithInputAndButton():
    return t"""
        <{Example} title="With Input and Button" containerClassName="col-span-full">
            <{Tabs} defaultSelectedKey="overview" class="mx-auto w-full max-w-lg">
                <div class="flex items-center gap-4">
                    <{TabsList}>
                        <{TabsTrigger} id="overview">Overview</{TabsTrigger}>
                        <{TabsTrigger} id="analytics">Analytics</{TabsTrigger}>
                    </{TabsList}>
                    <div class="ml-auto flex items-center gap-2">
                        <{Input} placeholder="Search..." class="w-44" />
                        <{Button}>Action</{Button}>
                    </div>
                </div>
                <div class="border style-vega:rounded-lg style-vega:p-6 style-nova:rounded-lg style-nova:p-4 style-lyra:rounded-none style-lyra:p-4 style-maia:rounded-xl style-maia:p-6 style-mira:rounded-md style-mira:p-4 style-luma:rounded-xl style-luma:p-6 style-rhea:rounded-xl style-rhea:p-6">
                    <{TabsContent} id="overview">
                        View your dashboard metrics and key performance indicators.
                    </{TabsContent}>
                    <{TabsContent} id="analytics">Detailed analytics and insights about your data.</{TabsContent}>
                    <{TabsContent} id="reports">Generate and view custom reports.</{TabsContent}>
                </div>
            </{Tabs}>
        </{Example}>
    """
