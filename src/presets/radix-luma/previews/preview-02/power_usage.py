from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from progress import Progress
from separator import Separator
from design_system import use_design_system_search_params

__js__ = {"recharts": ["Bar", "BarChart", "XAxis"]}

chart_data = [
    {"hour": "6a", "usage": 1.2},
    {"hour": "8a", "usage": 2.8},
    {"hour": "10a", "usage": 3.1},
    {"hour": "12p", "usage": 2.4},
    {"hour": "2p", "usage": 3.4},
    {"hour": "4p", "usage": 2.9},
    {"hour": "6p", "usage": 3.8},
    {"hour": "8p", "usage": 3.2},
]

chart_config = {"usage": {"label": "Usage (kW)", "color": "var(--chart-2)"}}


def PowerUsage():
    params = use_design_system_search_params()[0]
    is_rounded = not params["style"] in ["lyra", "sera"]

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Power Usage</{CardTitle}>
                <{CardDescription}>Whole Home</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <{ChartContainer} config={chart_config} class="h-[140px] w-full">
                    <{BarChart} data={chart_data} margin={ {"left": 0, "right": 0, "top": 4, "bottom": 0} }>
                        <{XAxis} dataKey="hour" tickLine={False} tickMargin={6} axisLine={False} class="text-xs" />
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel />'} />
                        <{Bar} dataKey="usage" fill="var(--color-usage)" radius={[4, 4, 0, 0] if is_rounded else 0} />
                    </{BarChart}>
                </{ChartContainer}>
                <{Separator} />
                <div class="grid grid-cols-2 gap-4">
                    <div class="flex flex-col gap-0.5">
                        <span class="text-sm text-muted-foreground">Currently Using</span>
                        <span class="text-lg font-semibold tabular-nums">3.4 kW</span>
                    </div>
                    <div class="flex flex-col gap-0.5">
                        <span class="text-sm text-muted-foreground">Solar Gen</span>
                        <span class="text-lg font-semibold text-chart-1 tabular-nums">+1.2 kW</span>
                    </div>
                </div>
            </{CardContent}>
            <{CardFooter} class="flex-col items-start gap-1">
                <span class="text-sm text-muted-foreground">Battery Level</span>
                <div class="flex w-full items-center gap-2">
                    <{Progress} value={85} class="flex-1" />
                    <span class="text-sm font-medium tabular-nums">85%</span>
                </div>
            </{CardFooter}>
        </{Card}>
    """
