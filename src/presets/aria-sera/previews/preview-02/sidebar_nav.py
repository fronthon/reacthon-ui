from card import Card
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarProvider,
    SidebarSeparator,
)

__js__ = {
    "lucide-react": [
        "ActivityIcon",
        "ArrowLeftRightIcon",
        "BellIcon",
        "BookOpenIcon",
        "Building2Icon",
        "CircleHelpIcon",
        "CreditCardIcon",
        "FileBarChartIcon",
        "FileTextIcon",
        "LayoutDashboardIcon",
        "MessageSquareIcon",
        "PaintbrushIcon",
        "PieChartIcon",
        "ShieldIcon",
        "TargetIcon",
        "TrendingUpIcon",
        "UserIcon",
        "WalletIcon",
    ],
}


def SidebarNav():
    return t"""
        <div class="grid grid-cols-2 items-start gap-6">
            <{Card} class="overflow-hidden py-0">
                <{SidebarProvider} class="min-h-0">
                    <{Sidebar} collapsible="none" class="w-full bg-transparent">
                        <{SidebarContent} class="gap-0">
                            <{SidebarGroup} class="pb-1">
                                <{SidebarGroupLabel}>Overview</{SidebarGroupLabel}>
                                <{SidebarGroupContent}>
                                    <{SidebarMenu}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton} isActive>
                                                <{LayoutDashboardIcon} />
                                                Dashboard
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{ArrowLeftRightIcon} />
                                                Transactions
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{TrendingUpIcon} />
                                                Investments
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{Building2Icon} />
                                                Accounts
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{PieChartIcon} />
                                                Spending
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                    </{SidebarMenu}>
                                </{SidebarGroupContent}>
                            </{SidebarGroup}>
                            <{SidebarSeparator} class="w-auto!" />
                            <{SidebarGroup} class="pt-1">
                                <{SidebarGroupLabel}>Planning</{SidebarGroupLabel}>
                                <{SidebarGroupContent}>
                                    <{SidebarMenu}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{TargetIcon} />
                                                Goals
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{WalletIcon} />
                                                Budget
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{FileBarChartIcon} />
                                                Reports
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{FileTextIcon} />
                                                Documents
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                    </{SidebarMenu}>
                                </{SidebarGroupContent}>
                            </{SidebarGroup}>
                        </{SidebarContent}>
                    </{Sidebar}>
                </{SidebarProvider}>
            </{Card}>
            <{Card} class="overflow-hidden py-0">
                <{SidebarProvider} class="min-h-0">
                    <{Sidebar} collapsible="none" class="w-full bg-transparent">
                        <{SidebarContent} class="gap-0">
                            <{SidebarGroup} class="pb-1">
                                <{SidebarGroupLabel}>Account</{SidebarGroupLabel}>
                                <{SidebarGroupContent}>
                                    <{SidebarMenu}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{UserIcon} />
                                                Profile
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton} isActive>
                                                <{CreditCardIcon} />
                                                Billing
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{BellIcon} />
                                                Notifications
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{ShieldIcon} />
                                                Security
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{PaintbrushIcon} />
                                                Appearance
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                    </{SidebarMenu}>
                                </{SidebarGroupContent}>
                            </{SidebarGroup}>
                            <{SidebarSeparator} class="w-auto!" />
                            <{SidebarGroup} class="pt-1">
                                <{SidebarGroupLabel}>Support</{SidebarGroupLabel}>
                                <{SidebarGroupContent}>
                                    <{SidebarMenu}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{CircleHelpIcon} />
                                                Help Center
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{MessageSquareIcon} />
                                                Contact Us
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{BookOpenIcon} />
                                                Documentation
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                        <{SidebarMenuItem}>
                                            <{SidebarMenuButton}>
                                                <{ActivityIcon} />
                                                Status
                                            </{SidebarMenuButton}>
                                        </{SidebarMenuItem}>
                                    </{SidebarMenu}>
                                </{SidebarGroupContent}>
                            </{SidebarGroup}>
                        </{SidebarContent}>
                    </{Sidebar}>
                </{SidebarProvider}>
            </{Card}>
        </div>
    """
