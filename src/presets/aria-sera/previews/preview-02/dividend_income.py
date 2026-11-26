from button import Button
from card import Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from item import Item, ItemContent, ItemDescription, ItemGroup, ItemTitle
from design_system import use_design_system_search_params

__js__ = {"lucide-react": ["XIcon"], "recharts": ["Bar", "BarChart"]}

HOLDINGS = [
    {
        "name": "Vanguard VIG",
        "shares": "450 Shares",
        "amount": "$1,842.10",
        "data": [
            {"q": "Q1", "value": 380},
            {"q": "Q2", "value": 420},
            {"q": "Q3", "value": 390},
            {"q": "Q4", "value": 652},
        ],
    },
    {
        "name": "S&P 500 VOO",
        "shares": "112 Shares",
        "amount": "$928.40",
        "data": [
            {"q": "Q1", "value": 180},
            {"q": "Q2", "value": 210},
            {"q": "Q3", "value": 320},
            {"q": "Q4", "value": 218},
        ],
    },
    {
        "name": "Apple AAPL",
        "shares": "85 Shares",
        "amount": "$340.00",
        "data": [
            {"q": "Q1", "value": 60},
            {"q": "Q2", "value": 70},
            {"q": "Q3", "value": 120},
            {"q": "Q4", "value": 90},
        ],
    },
    {
        "name": "Realty Income",
        "shares": "320 Shares",
        "amount": "$1,139.50",
        "data": [
            {"q": "Q1", "value": 240},
            {"q": "Q2", "value": 260},
            {"q": "Q3", "value": 280},
            {"q": "Q4", "value": 360},
        ],
    },
]

mini_chart_config = {"value": {"label": "Dividend", "color": "var(--chart-2)"}}


def DividendIncome():
    params = use_design_system_search_params()[0]
    is_rounded = not params["style"] in ["lyra", "sera"]
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Q2 Dividend Income</{CardTitle}>
                <{CardDescription}>Quarterly dividend payouts across your portfolio holdings.</{CardDescription}>
                <{CardAction}>
                    <{Button} variant="ghost" size="icon-sm" class="bg-muted">
                        <{XIcon} />
                    </{Button}>
                </{CardAction}>
            </{CardHeader}>
            <{CardContent}>
                <{ItemGroup}>
                    {[t'''
                        <{Item} key={holding["name"]} variant="muted">
                            <{ItemContent}>
                                <{ItemTitle}>{holding["name"]}</{ItemTitle}>
                                <{ItemDescription}>{holding["shares"]}</{ItemDescription}>
                            </{ItemContent}>
                            <{ChartContainer} config={mini_chart_config} class="hidden h-8 w-24 md:block">
                                <{BarChart}
                                    data={holding["data"]}
                                    margin={ {"top": 0, "right": 0, "bottom": 0, "left": 0} }
                                >
                                    <{ChartTooltip} cursor={False} content={t"<{ChartTooltipContent} hideLabel />"} />
                                    <{Bar}
                                        dataKey="value"
                                        fill="var(--color-value)"
                                        radius={[3, 3, 0, 0] if is_rounded else 0}
                                    />
                                </{BarChart}>
                            </{ChartContainer}>
                            <span class="hidden text-sm font-semibold tabular-nums md:block">{holding["amount"]}</span>
                        </{Item}>
                    ''' for holding in HOLDINGS]}
                </{ItemGroup}>
            </{CardContent}>
        </{Card}>
    """
