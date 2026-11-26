from browser import window
from javascript import Math
from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from chart import ChartContainer, ChartLegend, ChartLegendContent, ChartTooltip, ChartTooltipContent
from design_system import use_design_system_search_params

__js__ = {"recharts": ["Bar", "BarChart", "CartesianGrid", "XAxis"]}

bar_chart_data = [
    {"month": "January", "desktop": 186, "mobile": 80},
    {"month": "February", "desktop": 305, "mobile": 200},
    {"month": "March", "desktop": 237, "mobile": 120},
    {"month": "April", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "June", "desktop": 214, "mobile": 140},
]

bar_chart_config = {
    "desktop": {"label": "Desktop", "color": "var(--chart-1)"},
    "mobile": {"label": "Mobile", "color": "var(--chart-2)"},
}

desktop_total = sum((item["desktop"] for item in bar_chart_data), 0)

mobile_total = sum((item["mobile"] for item in bar_chart_data), 0)

desktop_delta = Math.round((desktop_total - mobile_total) / mobile_total * 100)

desktop_delta_prefix = "+" if desktop_delta > 0 else ""


def BarChartCard():
    params = use_design_system_search_params()[0]
    is_rounded = not params["style"] in ["lyra", "sera"]
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle} class="text-lg">Traffic channels</{CardTitle}>
                <{CardDescription} class="line-clamp-2 text-sm leading-snug">
                    Monthly desktop and mobile traffic for the last six months, compare volume and mix across platforms and devices at a glance.
                </{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4 pt-0">
                <{ChartContainer} config={bar_chart_config} class="max-h-[180px] w-full">
                    <{BarChart}
                        accessibilityLayer
                        data={bar_chart_data}
                        margin={ {"left": 0, "right": 0, "top": 8, "bottom": 0} }
                    >
                        <{CartesianGrid} vertical={False} strokeDasharray="3 3" />
                        <{XAxis}
                            dataKey="month"
                            tickLine={False}
                            tickMargin={8}
                            axisLine={False}
                            tickFormatter={(lambda value: str(value)[0:3])}
                        />
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} indicator="dashed" />'} />
                        <{ChartLegend} content={t'<{ChartLegendContent} />'} />
                        <{Bar} dataKey="desktop" fill="var(--color-desktop)" radius={[6, 6, 0, 0] if is_rounded else 0} />
                        <{Bar} dataKey="mobile" fill="var(--color-mobile)" radius={[6, 6, 0, 0] if is_rounded else 0} />
                    </{BarChart}>
                </{ChartContainer}>
                <div class="grid w-full grid-cols-3 divide-x divide-border/60">
                    <div class="px-2 text-center">
                        <div class="text-[0.65rem] text-muted-foreground uppercase">Desktop</div>
                        <div class="text-sm font-medium tabular-nums">
                            {window.Number.prototype.toLocaleString.call(desktop_total)}
                        </div>
                    </div>
                    <div class="px-2 text-center">
                        <div class="text-[0.65rem] text-muted-foreground uppercase">Mobile</div>
                        <div class="text-sm font-medium tabular-nums">
                            {window.Number.prototype.toLocaleString.call(mobile_total)}
                        </div>
                    </div>
                    <div class="px-2 text-center">
                        <div class="text-[0.65rem] text-muted-foreground uppercase">Mix Delta</div>
                        <div class="text-sm font-medium tabular-nums">
                            {desktop_delta_prefix}
                            {desktop_delta}%
                        </div>
                    </div>
                </div>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">View report</{Button}>
            </{CardFooter}>
        </{Card}>
    """
