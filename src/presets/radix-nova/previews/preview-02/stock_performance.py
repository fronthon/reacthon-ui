from javascript import NULL
from reacthon import use_state
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
from chart import ChartContainer, ChartTooltip, ChartTooltipContent
from combobox import Combobox, ComboboxContent, ComboboxEmpty, ComboboxInput, ComboboxItem, ComboboxList
from field import Field, FieldGroup, FieldLabel
from separator import Separator

__js__ = {"recharts": ["Area", "AreaChart", "CartesianGrid"]}

TICKERS = ["VOO", "VIG", "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

CHART_DATA = {
    "VOO": [
        {"month": "Jan", "price": 412},
        {"month": "Feb", "price": 438},
        {"month": "Mar", "price": 395},
        {"month": "Apr", "price": 450},
        {"month": "May", "price": 420},
        {"month": "Jun", "price": 462},
    ],
    "AAPL": [
        {"month": "Jan", "price": 185},
        {"month": "Feb", "price": 210},
        {"month": "Mar", "price": 172},
        {"month": "Apr", "price": 198},
        {"month": "May", "price": 178},
        {"month": "Jun", "price": 215},
    ],
}

DEFAULT_DATA = [
    {"month": "Jan", "price": 100},
    {"month": "Feb", "price": 118},
    {"month": "Mar", "price": 95},
    {"month": "Apr", "price": 125},
    {"month": "May", "price": 108},
    {"month": "Jun", "price": 130},
]

chart_config = {"price": {"label": "Price", "color": "var(--chart-1)"}}


def StockPerformance():
    ticker, set_ticker = use_state("VOO")

    data = CHART_DATA.get(ticker)
    if data in (None, NULL):
        data = DEFAULT_DATA

    def on_value_change(value):
        if value is not NULL:
            set_ticker(value)

    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Stock Performance</{CardTitle}>
                <{CardDescription}>6-month price history.</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="ticker-select">Ticker</{FieldLabel}>
                        <{Combobox} items={TICKERS} value={ticker} onValueChange={on_value_change}>
                            <{ComboboxInput} id="ticker-select" placeholder="Search ticker..." />
                            <{ComboboxContent}>
                                <{ComboboxEmpty}>No tickers found.</{ComboboxEmpty}>
                                <{ComboboxList}>
                                    {(lambda item: t'''
                                        <{ComboboxItem}
                                            key={item}
                                            value={item}
                                        >
                                            {item}
                                        </{ComboboxItem}>
                                    ''')}
                                </{ComboboxList}>
                            </{ComboboxContent}>
                        </{Combobox}>
                    </{Field}>
                </{FieldGroup}>
                <{Separator} class="style-sera:hidden" />
                <{ChartContainer} config={chart_config} class="h-[200px] w-full">
                    <{AreaChart} accessibilityLayer data={data} margin={ {"left": 0, "right": 0, "top": 8, "bottom": 0} }>
                        <defs>
                            <linearGradient id="fillPrice" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="0%" stopColor="var(--color-price)" stopOpacity={0.3} />
                                <stop offset="100%" stopColor="var(--color-price)" stopOpacity={0.05} />
                            </linearGradient>
                        </defs>
                        <{CartesianGrid} vertical={False} strokeDasharray="3 3" />
                        <{ChartTooltip} cursor={False} content={t'<{ChartTooltipContent} hideLabel />'} />
                        <{Area}
                            type="monotone"
                            dataKey="price"
                            stroke="var(--color-price)"
                            strokeWidth={2}
                            fill="url(#fillPrice)"
                        />
                    </{AreaChart}>
                </{ChartContainer}>
            </{CardContent}>
        </{Card}>
    """
