from javascript import NULL
from reacthon import create_context, use_context, use_id, use_memo
from utils import cn

__js__ = {"recharts": ["* as RechartsPrimitive"]}

THEMES = {"light": "", "dark": ".dark"}

INITIAL_DIMENSION = {"width": 320, "height": 200}

ChartContext = create_context(NULL)


def use_chart():
    context = use_context(ChartContext)

    if not context:
        raise RuntimeError("useChart must be used within a <ChartContainer />")

    return context


def ChartContainer(id=None, className=None, children=None, config=None, initialDimension=INITIAL_DIMENSION, **props):
    unique_id = use_id()
    chart_id = f"chart-{id if id not in (None, NULL) else unique_id.replace(":", "")}"

    return t"""
        <{ChartContext.Provider} value={ {
            "config": config,
        } }>
            <div
                data-slot="chart"
                data-chart={chart_id}
                class={cn("flex aspect-video justify-center text-xs [&_.recharts-cartesian-axis-tick_text]:fill-muted-foreground [&_.recharts-cartesian-grid_line[stroke='#ccc']]:stroke-border/50 [&_.recharts-curve.recharts-tooltip-cursor]:stroke-border [&_.recharts-dot[stroke='#fff']]:stroke-transparent [&_.recharts-layer]:outline-hidden [&_.recharts-polar-grid_[stroke='#ccc']]:stroke-border [&_.recharts-radial-bar-background-sector]:fill-muted [&_.recharts-rectangle.recharts-tooltip-cursor]:fill-muted [&_.recharts-reference-line_[stroke='#ccc']]:stroke-border [&_.recharts-sector]:outline-hidden [&_.recharts-sector[stroke='#fff']]:stroke-transparent [&_.recharts-surface]:outline-hidden", className)}
                ...{props}
            >
                <{ChartStyle} id={chart_id} config={config} />
                <{RechartsPrimitive.ResponsiveContainer} initialDimension={initialDimension}>
                    {children}
                </{RechartsPrimitive.ResponsiveContainer}>
            </div>
        </{ChartContext.Provider}>
    """


def ChartStyle(id=None, config=None):
    color_config = [(_, config) for _, config in config.items() if (config.get("theme") if config.get("theme") not in (None, NULL) else config.get("color"))]

    if not color_config:
        return None

    def render_key(key, item_config, theme):
        color = item_config.get("theme").get(theme) if item_config.get("theme") else None
        if color in (None, NULL):
            color = item_config.get("color")
        return f"  --color-{key}: {color};" if color else NULL

    return t"""
        <style dangerouslySetInnerHTML={ {
            "__html": "\n".join([f"\n{prefix} [data-chart={id}] {{\n{"\n".join([render_key(key, item_config, theme) for key, item_config in color_config])}\n}}\n" for theme, prefix in THEMES.items()]),
        } } />
    """


ChartTooltip = RechartsPrimitive.Tooltip


def ChartTooltipContent(active=None, payload=None, className=None, indicator="dot", hideLabel=False, hideIndicator=False, label=None, labelFormatter=None, labelClassName=None, formatter=None, color=None, nameKey=None, labelKey=None):
    config = use_chart().get("config")

    def tooltip_label():
        if hideLabel or not payload:
            return NULL

        item = payload[0]
        key = f"{labelKey if labelKey not in (None, NULL) else item.get("dataKey") if item.get("dataKey") not in (None, NULL) else item.get("name") if item.get("name") not in (None, NULL) else "value"}"
        item_config = get_payload_config_from_payload(config, item, key)
        value = ((config.get(label).get("label") if config.get(label) else None) if (config.get(label).get("label") if config.get(label) else None) not in (None, NULL) else label) if not labelKey and isinstance(label, str) else item_config.get("label") if item_config else None

        if labelFormatter:
            return t"<div class={cn("font-medium", labelClassName)}>{labelFormatter(value, payload)}</div>"

        if not value:
            return NULL

        return t"<div class={cn("font-medium", labelClassName)}>{value}</div>"

    tooltip_label = use_memo(tooltip_label, [label, labelFormatter, payload, hideLabel, labelClassName, config, labelKey])

    if not active or not payload:
        return None

    nest_label = len(payload) == 1 and indicator != "dot"

    def render_item(item, index):
        key = f"{nameKey if nameKey not in (None, NULL) else item.get("name") if item.get("name") not in (None, NULL) else item.get("dataKey") if item.get("dataKey") not in (None, NULL) else "value"}"
        item_config = get_payload_config_from_payload(config, item, key)
        indicator_color = color if color not in (None, NULL) else item.get("payload").get("fill") if item.get("payload") else None
        if indicator_color in (None, NULL):
            indicator_color = item.get("color")

        return t"""
            <div
                key={index}
                class={cn("flex w-full flex-wrap items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5 [&>svg]:text-muted-foreground", indicator == "dot" and "items-center")}
            >
                {formatter(item.get("value"), item.get("name"), item, index, item.get("payload")) if formatter and item.get("value") is not None and item.get("name") else t'''
                    {t"<{item_config.get("icon")} />" if (item_config.get("icon") if item_config else None) else not hideIndicator and t"""
                        <div
                            class={cn("shrink-0 rounded-[2px] border-(--color-border) bg-(--color-bg)", {
                                "h-2.5 w-2.5": indicator == "dot",
                                "w-1": indicator == "line",
                                "w-0 border-[1.5px] border-dashed bg-transparent": indicator == "dashed",
                                "my-0.5": nest_label and indicator == "dashed",
                            })}
                            style={ {
                                "--color-bg": indicator_color,
                                "--color-border": indicator_color,
                            } }
                        />
                    """}
                    <div class={cn(
                        "flex flex-1 justify-between leading-none",
                        "items-end" if nest_label else "items-center",
                    )}>
                        <div class="grid gap-1.5">
                            {tooltip_label if nest_label else None}
                            <span class="text-muted-foreground">
                                {(item_config.get("label") if item_config else None) if (item_config.get("label") if item_config else None) not in (None, NULL) else item.get("name")}
                            </span>
                        </div>
                        {item.get("value") not in (None, NULL) and t"""
                            <span class="font-mono font-medium text-foreground tabular-nums">
                                {format(item.get("value"), ",") if isinstance(item.get("value"), (int, float)) else str(item.get("value"))}
                            </span>
                        """}
                    </div>
                '''}
            </div>
        """

    return t"""
        <div class={cn("grid min-w-32 items-start gap-1.5 rounded-none border border-border/50 bg-background px-2.5 py-1.5 text-xs shadow-xl", className)}>
            {tooltip_label if not nest_label else None}
            <div class="grid gap-1.5">
                {[render_item(item, index) for index, item in enumerate(item for item in payload if item.get("type") != "none")]}
            </div>
        </div>
    """


ChartLegend = RechartsPrimitive.Legend


def ChartLegendContent(className=None, hideIcon=False, payload=None, verticalAlign="bottom", nameKey=None):
    config = use_chart().get("config")

    if not payload:
        return None

    def render_item(item, index):
        key = f"{nameKey if nameKey not in (None, NULL) else item.get("dataKey") if item.get("dataKey") not in (None, NULL) else "value"}"
        item_config = get_payload_config_from_payload(config, item, key)

        return t"""
            <div
                key={index}
                class={cn("flex items-center gap-1.5 [&>svg]:h-3 [&>svg]:w-3 [&>svg]:text-muted-foreground")}
            >
                {t'<{item_config.get("icon")} />' if (item_config.get("icon") if item_config else None) and not hideIcon else t'''
                    <div
                        class="h-2 w-2 shrink-0 rounded-[2px]"
                        style={ {
                            "backgroundColor": item.get("color"),
                        } }
                    />
                '''}
                {item_config.get("label") if item_config else None}
            </div>
        """

    return t"""
        <div class={cn("flex items-center justify-center gap-4", "pb-3" if verticalAlign == "top" else "pt-3", className)}>
            {[render_item(item, index) for index, item in enumerate(item for item in payload if item.get("type") != "none")]}
        </div>
    """


def get_payload_config_from_payload(config, payload, key):
    if not isinstance(payload, dict) or payload is NULL:
        return None

    payload_payload = payload["payload"] if "payload" in payload and isinstance(payload["payload"], dict) and payload["payload"] is not NULL else None

    config_label_key = key

    if key in payload and isinstance(payload.get(key), str):
        config_label_key = payload.get(key)
    elif payload_payload and key in payload_payload and isinstance(payload_payload.get(key), str):
        config_label_key = payload_payload.get(key)

    return config.get(config_label_key) if config_label_key in config else config.get(key)
