from account_access import AccountAccess
from card_overview import CardOverview
from claimable_balance import ClaimableBalance
from contribution_history import ContributionHistory
from cover_art import CoverArt
from dividend_income import DividendIncome
from empty_connect_bank import EmptyConnectBank
from empty_distribute_track import EmptyDistributeTrack
from empty_explore_catalog import EmptyExploreCatalog
from faq import Faq
from front_door import FrontDoor
from index_investing import IndexInvesting
from kitchen_island import KitchenIsland
from loading_card import LoadingCard
from new_milestone import NewMilestone
from notification_settings import NotificationSettings
from payments import Payments
from payout_threshold import PayoutThreshold
from power_usage import PowerUsage
from preferences import Preferences
from qr_connect import QrConnect
from receiving_method import ReceivingMethod
from recent_transactions import RecentTransactions
from release_catalog import ReleaseCatalog
from roller_shades import RollerShades
from savings_progress import SavingsProgress
from savings_targets import SavingsTargets
from sidebar_nav import SidebarNav
from social_links import SocialLinks
from stock_performance import StockPerformance
from syncing_state import SyncingState
from transfer_funds import TransferFunds
from upcoming_payments import UpcomingPayments


def Preview02Example():
    return t"""
        <div class="overflow-x-auto overflow-y-hidden bg-muted contain-[paint] [--gap:--spacing(4)] 3xl:[--gap:--spacing(12)] md:[--gap:--spacing(10)] dark:bg-background style-lyra:md:[--gap:--spacing(6)] style-mira:md:[--gap:--spacing(6)]">
            <div class="flex w-full min-w-max justify-center">
                <div
                    class="grid w-[2400px] grid-cols-7 items-start gap-(--gap) bg-muted p-(--gap) md:w-[3000px] dark:bg-background style-lyra:md:w-[2600px] style-mira:md:w-[2600px] *:[div]:gap-(--gap)"
                    data-slot="capture-target"
                >
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{ContributionHistory} />
                        <{EmptyDistributeTrack} />
                        <{QrConnect} />
                        <{DividendIncome} />
                        <{IndexInvesting} />
                        <{SyncingState} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{PayoutThreshold} />
                        <{ClaimableBalance} />
                        <{Preferences} />
                        <{SavingsProgress} />
                        <{KitchenIsland} />
                    </div>
                    <div class="col-span-2 flex flex-col p-1 [contain-intrinsic-size:760px_1200px] [content-visibility:auto]">
                        <{SavingsTargets} />
                        <{RecentTransactions} />
                        <div class="grid grid-cols-2 items-start gap-(--gap)">
                            <div class="flex flex-col gap-(--gap)">
                                <{SidebarNav} />
                                <{Faq} />
                            </div>
                            <div class="flex flex-col gap-(--gap)">
                                <{Payments} />
                                <{FrontDoor} />
                            </div>
                        </div>
                        <{ReleaseCatalog} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{AccountAccess} />
                        <{CardOverview} />
                        <{TransferFunds} />
                        <{CoverArt} />
                        <{LoadingCard} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{ReceivingMethod} />
                        <{PowerUsage} />
                        <{EmptyConnectBank} />
                        <{UpcomingPayments} />
                        <{RollerShades} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{StockPerformance} />
                        <{EmptyExploreCatalog} />
                        <{NewMilestone} />
                        <{SocialLinks} />
                        <{NotificationSettings} />
                    </div>
                </div>
            </div>
        </div>
    """
