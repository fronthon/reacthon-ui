from javascript import Math, NULL
from badge import Badge
from card import Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent

__js__ = {"recharts": ["Area", "AreaChart", "XAxis"]}

area_chart_data = [
    {"month": "January", "desktop": 186},
    {"month": "February", "desktop": 305},
    {"month": "March", "desktop": 237},
    {"month": "April", "desktop": 73},
    {"month": "May", "desktop": 209},
    {"month": "June", "desktop": 214},
]

area_chart_config = {"desktop": {"label": "Desktop", "color": "var(--chart-1)"}}


value = area_chart_data[len(area_chart_data) - 1]["desktop"]


latest_visitors = value if value not in (None, NULL) else 0


value_2 = area_chart_data[len(area_chart_data) - 2]["desktop"]


previous_visitors = value_2 if value_2 not in (None, NULL) else latest_visitors

trend_percent = 0 if previous_visitors == 0 else Math.round((latest_visitors - previous_visitors) / previous_visitors * 100)

trend_prefix = "+" if trend_percent > 0 else ""


def Visitors():
    return t"""
        <{Card} class="pb-0">
            <{CardHeader}>
                <{CardTitle}>Visitors</{CardTitle}>
                <{CardDescription}>Last 6 months </{CardDescription}>
                <{CardAction}>
                    <{Badge} variant={"secondary" if trend_percent >= 0 else "destructive"}>
                        {trend_prefix}
                        {trend_percent}% vs last month
                    </{Badge}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent} class="px-0">
                <{ChartContainer} config={area_chart_config} class="h-48 w-full">
                    <{AreaChart}
                        accessibilityLayer
                        data={area_chart_data}
                        margin={ {"left": 0, "right": 0, "top": 6, "bottom": 0} }
                    >
                        <{XAxis}
                            dataKey="month"
                            tickLine={False}
                            hide
                            axisLine={False}
                            tickMargin={6}
                            tickFormatter={(lambda value: str(value)[0:3])}
                        />
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} indicator="line" />'} />
                        <{Area}
                            dataKey="desktop"
                            type="natural"
                            fill="var(--color-desktop)"
                            fillOpacity={0.15}
                            stroke="var(--color-desktop)"
                            strokeWidth={2}
                        />
                    </{AreaChart}>
                </{ChartContainer}>
            </{CardContent}>
        </{Card}>
    """
