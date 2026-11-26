from badge import Badge
from button import Button
from card import Card, CardContent, CardDescription, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent

__js__ = {"recharts": ["Bar", "BarChart", "XAxis"]}

activity_data = [
    {"month": "Jan", "amount": 40},
    {"month": "Feb", "amount": 55},
    {"month": "Mar", "amount": 35},
    {"month": "Apr", "amount": 60},
    {"month": "May", "amount": 45},
    {"month": "Jun", "amount": 50},
    {"month": "Jul", "amount": 65},
    {"month": "Aug", "amount": 40},
    {"month": "Sep", "amount": 55},
    {"month": "Oct", "amount": 70},
    {"month": "Nov", "amount": 45},
    {"month": "Dec", "amount": 80},
]

chart_config = {"amount": {"label": "Activity", "color": "var(--chart-2)"}}


def CardOverview():
    return t"""
        <div class="grid grid-cols-2 gap-3">
            <{Card}>
                <{CardContent}>
                    <{CardDescription}>Card Balance</{CardDescription}>
                    <{CardTitle} class="text-2xl tabular-nums">US$12.94</{CardTitle}>
                    <{CardDescription} class="tabular-nums">US$11,337.06 Available</{CardDescription}>
                </{CardContent}>
            </{Card}>
            <{Card} class="flex flex-col justify-between">
                <{CardContent} class="flex flex-1 flex-col justify-between">
                    <div class="flex flex-col gap-1">
                        <{CardDescription}>Payment Due</{CardDescription}>
                        <{CardTitle} class="text-2xl">1 Apr</{CardTitle}>
                    </div>
                    <{Button} variant="outline" size="sm" class="mt-3 w-full">Pay Early</{Button}>
                </{CardContent}>
            </{Card}>
            <{Card} class="col-span-2">
                <{CardContent} class="flex flex-col gap-2">
                    <div class="flex items-center justify-between">
                        <{CardDescription}>Yearly Activity</{CardDescription}>
                        <{Badge} variant="secondary">+US$0.25 Daily Cash</{Badge}>
                    </div>
                    <{ChartContainer} config={chart_config} class="h-20 w-full">
                        <{BarChart} data={activity_data} margin={ {"top": 4, "right": 0, "bottom": 0, "left": 0} }>
                            <{XAxis}
                                dataKey="month"
                                tickLine={False}
                                tickMargin={4}
                                axisLine={False}
                                tickFormatter={(lambda v: str(v)[0:1])}
                                class="text-[10px]"
                            />
                            <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel />'} />
                            <{Bar} dataKey="amount" fill="var(--color-amount)" radius={[3, 3, 0, 0]} />
                        </{BarChart}>
                    </{ChartContainer}>
                </{CardContent}>
            </{Card}>
        </div>
    """
