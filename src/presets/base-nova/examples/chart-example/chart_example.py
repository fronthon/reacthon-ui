from browser import window
from reacthon import use_memo
from example import Example, ExampleWrapper
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent

__js__ = {
    "recharts": [
        "Area",
        "AreaChart",
        "Bar",
        "BarChart",
        "CartesianGrid",
        "Label",
        "Line",
        "LineChart",
        "Pie",
        "PieChart",
        "PolarAngleAxis",
        "PolarGrid",
        "PolarRadiusAxis",
        "Radar",
        "RadarChart",
        "RadialBar",
        "RadialBarChart",
        "XAxis",
    ],
    "lucide-react": ["TrendingUpIcon"],
}

area_chart_data = [
    {"month": "January", "desktop": 186},
    {"month": "February", "desktop": 305},
    {"month": "March", "desktop": 237},
    {"month": "April", "desktop": 73},
    {"month": "May", "desktop": 209},
    {"month": "June", "desktop": 214},
]

area_chart_config = {"desktop": {"label": "Desktop", "color": "var(--chart-1)"}}


def ChartExample():
    return t"""
        <{ExampleWrapper}>
            <{ChartAreaExample} />
            <{ChartBarExample} />
            <{ChartLineExample} />
            <{ChartPieExample} />
            <{ChartRadialExample} />
            <{ChartRadarExample} />
        </{ExampleWrapper}>
    """


def ChartAreaExample():
    return t"""
        <{Example} title="Area Chart">
            <{Card} class="w-full">
                <{CardHeader}>
                    <{CardTitle}>Area Chart</{CardTitle}>
                    <{CardDescription}>Showing total visitors for the last 6 months</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <{ChartContainer} config={area_chart_config}>
                        <{AreaChart} accessibilityLayer data={area_chart_data} margin={ {"left": 12, "right": 12} }>
                            <{CartesianGrid} vertical={False} />
                            <{XAxis}
                                dataKey="month"
                                tickLine={False}
                                axisLine={False}
                                tickMargin={8}
                                tickFormatter={(lambda value: value.slice(0, 3))}
                            />
                            <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} indicator="line" />'} />
                            <{Area}
                                dataKey="desktop"
                                type="natural"
                                fill="var(--color-desktop)"
                                fillOpacity={0.4}
                                stroke="var(--color-desktop)"
                            />
                        </{AreaChart}>
                    </{ChartContainer}>
                </{CardContent}>
                <{CardFooter}>
                    <div class="flex w-full items-start gap-2">
                        <div class="grid gap-2">
                            <div class="flex items-center gap-2 leading-none font-medium">
                                Trending up by 5.2% this month{" "}
                                <{TrendingUpIcon} class="size-4" />
                            </div>
                            <div class="flex items-center gap-2 leading-none text-muted-foreground">
                                January - June 2024
                            </div>
                        </div>
                    </div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


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


def ChartBarExample():
    return t"""
        <{Example} title="Bar Chart">
            <{Card} class="w-full">
                <{CardHeader}>
                    <{CardTitle}>Bar Chart - Multiple</{CardTitle}>
                    <{CardDescription}>January - June 2024</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <{ChartContainer} config={bar_chart_config}>
                        <{BarChart} accessibilityLayer data={bar_chart_data}>
                            <{CartesianGrid} vertical={False} />
                            <{XAxis}
                                dataKey="month"
                                tickLine={False}
                                tickMargin={10}
                                axisLine={False}
                                tickFormatter={(lambda value: value.slice(0, 3))}
                            />
                            <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} indicator="dashed" />'} />
                            <{Bar} dataKey="desktop" fill="var(--color-desktop)" radius={4} />
                            <{Bar} dataKey="mobile" fill="var(--color-mobile)" radius={4} />
                        </{BarChart}>
                    </{ChartContainer}>
                </{CardContent}>
                <{CardFooter} class="flex-col items-start gap-2">
                    <div class="flex gap-2 leading-none font-medium">
                        Trending up by 5.2% this month{" "}
                        <{TrendingUpIcon} class="size-4" />
                    </div>
                    <div class="leading-none text-muted-foreground">Showing total visitors for the last 6 months</div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


line_chart_data = [
    {"month": "January", "desktop": 186, "mobile": 80},
    {"month": "February", "desktop": 305, "mobile": 200},
    {"month": "March", "desktop": 237, "mobile": 120},
    {"month": "April", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "June", "desktop": 214, "mobile": 140},
]

line_chart_config = {
    "desktop": {"label": "Desktop", "color": "var(--chart-1)"},
    "mobile": {"label": "Mobile", "color": "var(--chart-2)"},
}


def ChartLineExample():
    return t"""
        <{Example} title="Line Chart">
            <{Card} class="w-full">
                <{CardHeader}>
                    <{CardTitle}>Line Chart - Multiple</{CardTitle}>
                    <{CardDescription}>January - June 2024</{CardDescription}>
                </{CardHeader}>
                <{CardContent}>
                    <{ChartContainer} config={line_chart_config}>
                        <{LineChart} accessibilityLayer data={line_chart_data} margin={ {"left": 12, "right": 12} }>
                            <{CartesianGrid} vertical={False} />
                            <{XAxis}
                                dataKey="month"
                                tickLine={False}
                                axisLine={False}
                                tickMargin={8}
                                tickFormatter={(lambda value: value.slice(0, 3))}
                            />
                            <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} />'} />
                            <{Line}
                                dataKey="desktop"
                                type="monotone"
                                stroke="var(--color-desktop)"
                                strokeWidth={2}
                                dot={False}
                            />
                            <{Line}
                                dataKey="mobile"
                                type="monotone"
                                stroke="var(--color-mobile)"
                                strokeWidth={2}
                                dot={False}
                            />
                        </{LineChart}>
                    </{ChartContainer}>
                </{CardContent}>
                <{CardFooter}>
                    <div class="flex w-full items-start gap-2">
                        <div class="grid gap-2">
                            <div class="flex items-center gap-2 leading-none font-medium">
                                Trending up by 5.2% this month{" "}
                                <{TrendingUpIcon} class="size-4" />
                            </div>
                            <div class="flex items-center gap-2 leading-none text-muted-foreground">
                                Showing total visitors for the last 6 months
                            </div>
                        </div>
                    </div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


pie_chart_data = [
    {"browser": "chrome", "visitors": 275, "fill": "var(--color-chrome)"},
    {"browser": "safari", "visitors": 200, "fill": "var(--color-safari)"},
    {"browser": "firefox", "visitors": 287, "fill": "var(--color-firefox)"},
    {"browser": "edge", "visitors": 173, "fill": "var(--color-edge)"},
    {"browser": "other", "visitors": 190, "fill": "var(--color-other)"},
]

pie_chart_config = {
    "visitors": {"label": "Visitors"},
    "chrome": {"label": "Chrome", "color": "var(--chart-1)"},
    "safari": {"label": "Safari", "color": "var(--chart-2)"},
    "firefox": {"label": "Firefox", "color": "var(--chart-3)"},
    "edge": {"label": "Edge", "color": "var(--chart-4)"},
    "other": {"label": "Other", "color": "var(--chart-5)"},
}


def ChartPieExample():
    total_visitors = use_memo(lambda: sum((curr["visitors"] for curr in pie_chart_data), 0), [])

    def content(props):
        view_box = props.get("viewBox")

        if view_box and "cx" in view_box and "cy" in view_box:
            return t"""
                <text x={view_box["cx"]} y={view_box["cy"]} textAnchor="middle" dominantBaseline="middle">
                    <tspan x={view_box["cx"]} y={view_box["cy"]} class="fill-foreground text-3xl font-bold">
                        {window.Number.prototype.toLocaleString.call(total_visitors)}
                    </tspan>
                    <tspan x={view_box["cx"]} y={(view_box["cy"] or 0) + 24} class="fill-muted-foreground">
                        Visitors
                    </tspan>
                </text>
            """

    return t"""
        <{Example} title="Pie Chart">
            <{Card} class="w-full">
                <{CardHeader} class="items-center pb-0">
                    <{CardTitle}>Pie Chart - Donut with Text</{CardTitle}>
                    <{CardDescription}>January - June 2024</{CardDescription}>
                </{CardHeader}>
                <{CardContent} class="flex-1 pb-0">
                    <{ChartContainer} config={pie_chart_config} class="mx-auto aspect-square max-h-[250px]">
                        <{PieChart}>
                            <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel />'} />
                            <{Pie}
                                data={pie_chart_data}
                                dataKey="visitors"
                                nameKey="browser"
                                innerRadius={60}
                                strokeWidth={5}
                            >
                                <{Label} content={content} />
                            </{Pie}>
                        </{PieChart}>
                    </{ChartContainer}>
                </{CardContent}>
                <{CardFooter} class="flex-col gap-2">
                    <div class="flex items-center gap-2 leading-none font-medium">
                        Trending up by 5.2% this month{" "}
                        <{TrendingUpIcon} class="size-4" />
                    </div>
                    <div class="leading-none text-muted-foreground">Showing total visitors for the last 6 months</div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


radar_chart_data = [
    {"month": "January", "desktop": 186, "mobile": 80},
    {"month": "February", "desktop": 305, "mobile": 200},
    {"month": "March", "desktop": 237, "mobile": 120},
    {"month": "April", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "June", "desktop": 214, "mobile": 140},
]

radar_chart_config = {
    "desktop": {"label": "Desktop", "color": "var(--chart-1)"},
    "mobile": {"label": "Mobile", "color": "var(--chart-2)"},
}


def ChartRadarExample():
    return t"""
        <{Example} title="Radar Chart">
            <{Card} class="w-full">
                <{CardHeader} class="items-center pb-4">
                    <{CardTitle}>Radar Chart - Multiple</{CardTitle}>
                    <{CardDescription}>Showing total visitors for the last 6 months</{CardDescription}>
                </{CardHeader}>
                <{CardContent} class="pb-0">
                    <{ChartContainer} config={radar_chart_config} class="mx-auto aspect-square max-h-[250px]">
                        <{RadarChart} data={radar_chart_data}>
                            <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} indicator="line" />'} />
                            <{PolarAngleAxis} dataKey="month" />
                            <{PolarGrid} />
                            <{Radar} dataKey="desktop" fill="var(--color-desktop)" fillOpacity={0.6} />
                            <{Radar} dataKey="mobile" fill="var(--color-mobile)" />
                        </{RadarChart}>
                    </{ChartContainer}>
                </{CardContent}>
                <{CardFooter} class="flex-col gap-2">
                    <div class="flex items-center gap-2 leading-none font-medium">
                        Trending up by 5.2% this month{" "}
                        <{TrendingUpIcon} class="size-4" />
                    </div>
                    <div class="flex items-center gap-2 leading-none text-muted-foreground">January - June 2024</div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """


radial_chart_data = [{"browser": "safari", "visitors": 1260, "fill": "var(--color-safari)"}]

radial_chart_config = {"visitors": {"label": "Visitors"}, "safari": {"label": "Safari", "color": "var(--chart-2)"}}


def ChartRadialExample():
    def content(props):
        view_box = props.get("viewBox")

        if view_box and "cx" in view_box and "cy" in view_box:
            return t"""
                <text x={view_box["cx"]} y={view_box["cy"]} textAnchor="middle" dominantBaseline="middle">
                    <tspan x={view_box["cx"]} y={view_box["cy"]} class="fill-foreground text-4xl font-bold">
                        {window.Number.prototype.toLocaleString.call(radial_chart_data[0]["visitors"])}
                    </tspan>
                    <tspan x={view_box["cx"]} y={(view_box["cy"] or 0) + 24} class="fill-muted-foreground">
                        Visitors
                    </tspan>
                </text>
            """

    return t"""
        <{Example} title="Radial Chart">
            <{Card} class="w-full">
                <{CardHeader}>
                    <{CardTitle}>Radial Chart - Shape</{CardTitle}>
                    <{CardDescription}>January - June 2024</{CardDescription}>
                </{CardHeader}>
                <{CardContent} class="flex-1 pb-0">
                    <{ChartContainer} config={radial_chart_config} class="mx-auto aspect-square max-h-[210px]">
                        <{RadialBarChart} data={radial_chart_data} endAngle={100} innerRadius={64} outerRadius={94}>
                            <{PolarGrid}
                                gridType="circle"
                                radialLines={False}
                                stroke="none"
                                class="first:fill-muted last:fill-background"
                                polarRadius={[86, 74]}
                            />
                            <{RadialBar} dataKey="visitors" background />
                            <{PolarRadiusAxis} tick={False} tickLine={False} axisLine={False}>
                                <{Label} content={content} />
                            </{PolarRadiusAxis}>
                        </{RadialBarChart}>
                    </{ChartContainer}>
                </{CardContent}>
                <{CardFooter} class="flex-col gap-2">
                    <div class="flex items-center gap-2 leading-none font-medium">
                        Trending up by 5.2% this month{" "}
                        <{TrendingUpIcon} class="size-4" />
                    </div>
                    <div class="leading-none text-muted-foreground">Showing total visitors for the last 6 months</div>
                </{CardFooter}>
            </{Card}>
        </{Example}>
    """
