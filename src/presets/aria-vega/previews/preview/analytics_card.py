from badge import Badge
from button import Button
from card import Card, CardAction, CardDescription, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent

__js__ = {"recharts": ["Area", "AreaChart"]}

chart_data = [
    {"month": "January", "visitors": 186},
    {"month": "February", "visitors": 305},
    {"month": "March", "visitors": 237},
    {"month": "April", "visitors": 73},
    {"month": "May", "visitors": 209},
    {"month": "June", "visitors": 214},
]

chart_config = {"visitors": {"label": "Visitors", "color": "var(--chart-1)"}}


def AnalyticsCard():
    return t"""
        <{Card} class="mx-auto w-full max-w-sm data-[size=sm]:pb-0" size="sm">
            <{CardHeader}>
                <{CardTitle}>Analytics</{CardTitle}>
                <{CardDescription}>
                    418.2K Visitors <{Badge}>+10%</{Badge}>
                </{CardDescription}>
                <{CardAction}>
                    <{Button} variant="outline" size="sm">View Analytics</{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{ChartContainer} config={chart_config} class="aspect-[1/0.35]">
                <{AreaChart} accessibilityLayer data={chart_data} margin={ {"left": 0, "right": 0} }>
                    <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} indicator="line" hideLabel />'} />
                    <{Area}
                        dataKey="visitors"
                        type="linear"
                        fill="var(--color-visitors)"
                        fillOpacity={0.4}
                        stroke="var(--color-visitors)"
                    />
                </{AreaChart}>
            </{ChartContainer}>
        </{Card}>
    """
