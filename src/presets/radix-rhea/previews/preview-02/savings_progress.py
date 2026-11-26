from card import Card, CardContent, CardFooter
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from separator import Separator

__js__ = {"recharts": ["Label", "Pie", "PieChart"]}

chart_data = [
    {"name": "saved", "value": 24000, "fill": "var(--color-saved)"},
    {"name": "remaining", "value": 6000, "fill": "var(--color-remaining)"},
]

chart_config = {
    "saved": {"label": "Saved", "color": "var(--chart-2)"},
    "remaining": {"label": "Remaining", "color": "var(--chart-1)"},
}


def SavingsProgress():
    def content(props):
        view_box = props.get("viewBox")

        if view_box and "cx" in view_box and "cy" in view_box:
            return t"""
                <text x={view_box["cx"]} y={view_box["cy"]} textAnchor="middle" dominantBaseline="middle">
                    <tspan x={view_box["cx"]} y={(view_box["cy"] or 0) - 12} class="fill-foreground text-2xl font-bold">
                        $24,000
                    </tspan>
                    <tspan x={view_box["cx"]} y={(view_box["cy"] or 0) + 12} class="fill-muted-foreground text-xs">
                        80% of $30,000
                    </tspan>
                </text>
            """

    return t"""
        <{Card}>
            <{CardContent}>
                <{ChartContainer} config={chart_config} class="mx-auto aspect-square max-h-[220px]">
                    <{PieChart}>
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel />'} />
                        <{Pie}
                            data={chart_data}
                            dataKey="value"
                            nameKey="name"
                            innerRadius={70}
                            outerRadius={95}
                            strokeWidth={0}
                            startAngle={90}
                            endAngle={-270}
                        >
                            <{Label} content={content} />
                        </{Pie}>
                    </{PieChart}>
                </{ChartContainer}>
            </{CardContent}>
            <{CardFooter} class="flex-col gap-0">
                <div class="flex w-full items-center justify-between py-3">
                    <span class="text-sm text-muted-foreground">Projected Finish</span>
                    <span class="text-sm font-semibold">October 2024</span>
                </div>
                <{Separator} />
                <div class="flex w-full items-center justify-between py-3">
                    <span class="text-sm text-muted-foreground">Monthly Average</span>
                    <span class="text-sm font-semibold tabular-nums">$1,250</span>
                </div>
                <{Separator} />
                <div class="flex w-full items-center justify-between py-3">
                    <span class="text-sm text-muted-foreground">Top Contributor</span>
                    <span class="text-sm font-semibold">Auto-Transfer</span>
                </div>
            </{CardFooter}>
        </{Card}>
    """
