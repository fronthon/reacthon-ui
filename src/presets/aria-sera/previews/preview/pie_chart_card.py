from browser import window
from javascript import Math, NULL
from badge import Badge
from card import Card, CardAction, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from chart import ChartContainer, ChartLegend, ChartLegendContent, ChartTooltip, ChartTooltipContent
from progress import Progress
from utils import reduce

__js__ = {"recharts": ["Label", "Pie", "PieChart"]}

pie_chart_data = [
    {"browser": "chrome", "visitors": 275, "fill": "var(--color-chrome)"},
    {"browser": "safari", "visitors": 200, "fill": "var(--color-safari)"},
    {"browser": "firefox", "visitors": 287, "fill": "var(--color-firefox)"},
    {"browser": "edge", "visitors": 173, "fill": "var(--color-edge)"},
]

pie_chart_config = {
    "visitors": {"label": "Visitors"},
    "chrome": {"label": "Chrome", "color": "var(--chart-1)"},
    "safari": {"label": "Safari", "color": "var(--chart-2)"},
    "firefox": {"label": "Firefox", "color": "var(--chart-3)"},
    "edge": {"label": "Edge", "color": "var(--chart-4)"},
}


def PieChartCard():
    total_visitors = sum((item["visitors"] for item in pie_chart_data), 0)
    top_browser = reduce(lambda max_, item: item if item["visitors"] > max_["visitors"] else max_, pie_chart_data)
    top_browser_share = Math.round(top_browser["visitors"] / total_visitors * 100)
    top_browser_label = pie_chart_config.get(top_browser["browser"])["label"] if pie_chart_config.get(top_browser["browser"]) else None
    if top_browser_label in (None, NULL):
        top_browser_label = "Top"

    def content(props):
        view_box = props.get("viewBox")

        if view_box and "cx" in view_box and "cy" in view_box:
            return t"""
                <text x={view_box["cx"]} y={view_box["cy"]} textAnchor="middle" dominantBaseline="middle" fill="red">
                    <tspan x={view_box["cx"]} y={view_box["cy"] - 16} class="fill-foreground text-2xl font-bold">
                        {window.Number.prototype.toLocaleString.call(total_visitors)}
                    </tspan>
                    <tspan x={view_box["cx"]} y={(view_box["cy"] or 0) + 4} class="fill-muted-foreground text-xs">
                        Visitors
                    </tspan>
                </text>
            """

    return t"""
        <{Card}>
            <{CardHeader} class="pb-0">
                <{CardTitle}>Browser Share</{CardTitle}>
                <{CardDescription}>January - June 2026</{CardDescription}>
                <{CardAction}>
                    <{Badge} variant="outline">{top_browser_label}</{Badge}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent} class="pt-0">
                <{ChartContainer} config={pie_chart_config} class="mx-auto aspect-square max-h-[190px]">
                    <{PieChart}>
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel />'} />
                        <{Pie}
                            data={pie_chart_data}
                            dataKey="visitors"
                            nameKey="browser"
                            innerRadius={50}
                            strokeWidth={5}
                        >
                            <{Label} content={content} />
                        </{Pie}>
                        <{ChartLegend} content={t'<{ChartLegendContent} nameKey="browser" />'} class="translate-y-2" />
                    </{PieChart}>
                </{ChartContainer}>
            </{CardContent}>
            <{CardFooter} class="flex-col items-stretch gap-2">
                <div class="flex items-center text-xs">
                    <span class="font-medium">{top_browser_label}</span>
                    <span class="ml-auto text-muted-foreground tabular-nums">{top_browser_share}%</span>
                </div>
                <{Progress} value={top_browser_share} class="**:data-[slot=progress-indicator]:bg-chart-3" />
            </{CardFooter}>
        </{Card}>
    """
