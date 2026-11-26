from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from item import Item, ItemContent, ItemDescription
from design_system import use_design_system_search_params

__js__ = {"recharts": ["Bar", "BarChart", "XAxis"]}

chart_data = [
    {"month": "Dec", "amount": 800},
    {"month": "Jan", "amount": 1100},
    {"month": "Feb", "amount": 900},
    {"month": "Mar", "amount": 1300},
    {"month": "Apr", "amount": 750},
    {"month": "May", "amount": 1400},
]

chart_config = {"amount": {"label": "Contribution", "color": "var(--chart-2)"}}


def ContributionHistory():
    params = use_design_system_search_params()[0]
    is_rounded = not params["style"] in ["lyra", "sera"]
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Contribution History</{CardTitle}>
                <{CardDescription}>Last 6 months of activity</{CardDescription}>
            </{CardHeader}>
            <{CardContent}>
                <{ChartContainer} config={chart_config} class="h-[200px] w-full">
                    <{BarChart}
                        accessibilityLayer
                        data={chart_data}
                        margin={ {"left": 0, "right": 0, "top": 8, "bottom": 0} }
                    >
                        <{XAxis} dataKey="month" tickLine={False} tickMargin={8} axisLine={False} />
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel class="min-w-40" />'} />
                        <{Bar}
                            dataKey="amount"
                            fill="var(--color-amount)"
                            radius={[6, 6, 0, 0] if is_rounded else 0}
                            maxBarSize={40}
                        />
                    </{BarChart}>
                </{ChartContainer}>
            </{CardContent}>
            <{CardContent}>
                <div class="grid w-full grid-cols-1 gap-3 md:grid-cols-2">
                    <{Item} variant="muted" class="flex-col items-stretch">
                        <{ItemContent} class="gap-1">
                            <{ItemDescription} class="text-xs font-medium tracking-wider text-muted-foreground uppercase">
                                Upcoming
                            </{ItemDescription}>
                            <span class="cn-font-heading text-lg font-semibold">May 25, 2024</span>
                            <span class="text-sm text-muted-foreground">$1,000 scheduled</span>
                        </{ItemContent}>
                    </{Item}>
                    <{Item} variant="muted" class="flex-col items-stretch">
                        <{ItemContent} class="gap-1">
                            <{ItemDescription} class="text-xs font-medium tracking-wider text-muted-foreground uppercase">
                                Auto-Save Plan
                            </{ItemDescription}>
                            <span class="cn-font-heading text-lg font-semibold">Accelerated</span>
                            <span class="text-sm text-muted-foreground">Recurring weekly</span>
                        </{ItemContent}>
                    </{Item}>
                </div>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">View Full Report</{Button}>
            </{CardFooter}>
        </{Card}>
    """
