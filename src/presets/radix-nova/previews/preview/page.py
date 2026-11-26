from activate_agent_dialog import ActivateAgentDialog
from analytics_card import AnalyticsCard
from anomaly_alert import AnomalyAlert
from bar_chart_card import BarChartCard
from book_appointment import BookAppointment
from codespaces_card import CodespacesCard
from contributions_activity import ContributionsActivity
from contributors import Contributors
from environment_variables import EnvironmentVariables
from feedback_form import FeedbackForm
from file_upload import FileUpload
from github_profile import GithubProfile
from invite_team import InviteTeam
from invoice import Invoice
from live_waveform import LiveWaveformCard
from no_team_members import NoTeamMembers
from not_found import NotFound
from observability_card import ObservabilityCard
from pie_chart_card import PieChartCard
from report_bug import ReportBug
from shipping_address import ShippingAddress
from shortcuts import Shortcuts
from skeleton_loading import SkeletonLoading
from sleep_report import SleepReport
from ui_elements import UIElements
from usage_card import UsageCard
from visitors import Visitors
from weekly_fitness_summary import WeeklyFitnessSummary


def PreviewExample():
    return t"""
        <div class="overflow-x-auto overflow-y-hidden bg-muted contain-[paint] [--gap:--spacing(4)] 3xl:[--gap:--spacing(12)] md:[--gap:--spacing(10)] dark:bg-background style-lyra:md:[--gap:--spacing(6)] style-mira:md:[--gap:--spacing(6)]">
            <div class="flex w-full min-w-max justify-center">
                <div
                    class="grid w-[2400px] grid-cols-7 items-start gap-(--gap) bg-muted p-(--gap) md:w-[3000px] dark:bg-background style-lyra:md:w-[2600px] style-mira:md:w-[2600px] *:[div]:gap-(--gap)"
                    data-slot="capture-target"
                >
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <div class="md:hidden">
                            <{UIElements} />
                        </div>
                        <{CodespacesCard} />
                        <{Invoice} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <div class="hidden w-full md:flex">
                            <{UIElements} />
                        </div>
                        <{ObservabilityCard} />
                        <{ShippingAddress} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{EnvironmentVariables} />
                        <{BarChartCard} />
                        <{InviteTeam} />
                        <{ActivateAgentDialog} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{SkeletonLoading} />
                        <{PieChartCard} />
                        <{NoTeamMembers} />
                        <{ReportBug} />
                        <{Contributors} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{FeedbackForm} />
                        <{BookAppointment} />
                        <{SleepReport} />
                        <{GithubProfile} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{WeeklyFitnessSummary} />
                        <{FileUpload} />
                        <{AnalyticsCard} />
                        <{UsageCard} />
                        <{Shortcuts} />
                    </div>
                    <div class="flex flex-col p-1 [contain-intrinsic-size:380px_1200px] [content-visibility:auto]">
                        <{AnomalyAlert} />
                        <{LiveWaveformCard} />
                        <{Visitors} />
                        <{ContributionsActivity} />
                        <{NotFound} />
                    </div>
                </div>
            </div>
        </div>
    """
