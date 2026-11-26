from reacthon import create_context, use_context
from utils import cn
from toggle import toggle_variants

__js__ = {"radix-ui": ["ToggleGroup as ToggleGroupPrimitive"]}

ToggleGroupContext = create_context(
    {"size": "default", "variant": "default", "spacing": 2, "orientation": "horizontal"},
)


def ToggleGroup(className=None, variant=None, size=None, spacing=2, orientation="horizontal", children=None, **props):
    return t"""
        <{ToggleGroupPrimitive.Root}
            data-slot="toggle-group"
            data-variant={variant}
            data-size={size}
            data-spacing={spacing}
            data-orientation={orientation}
            style={ {
                "--gap": spacing,
            } }
            class={cn("group/toggle-group flex w-fit flex-row items-center gap-[--spacing(var(--gap))] rounded-none data-[size=sm]:rounded-none data-vertical:flex-col data-vertical:items-stretch", className)}
            ...{props}
        >
            <{ToggleGroupContext.Provider} value={ {
                "variant": variant,
                "size": size,
                "spacing": spacing,
                "orientation": orientation,
            } }>
                {children}
            </{ToggleGroupContext.Provider}>
        </{ToggleGroupPrimitive.Root}>
    """


def ToggleGroupItem(className=None, children=None, variant="default", size="default", **props):
    context = use_context(ToggleGroupContext)

    return t"""
        <{ToggleGroupPrimitive.Item}
            data-slot="toggle-group-item"
            data-variant={context.get("variant") or variant}
            data-size={context.get("size") or size}
            data-spacing={context.get("spacing")}
            class={cn(
                "shrink-0 group-data-[spacing=0]/toggle-group:rounded-none group-data-[spacing=0]/toggle-group:px-2 focus:z-10 focus-visible:z-10 group-data-[spacing=0]/toggle-group:has-data-[icon=inline-end]:pr-1.5 group-data-[spacing=0]/toggle-group:has-data-[icon=inline-start]:pl-1.5 group-data-horizontal/toggle-group:data-[spacing=0]:first:rounded-none group-data-vertical/toggle-group:data-[spacing=0]:first:rounded-none group-data-horizontal/toggle-group:data-[spacing=0]:last:rounded-none group-data-vertical/toggle-group:data-[spacing=0]:last:rounded-none group-data-horizontal/toggle-group:data-[spacing=0]:data-[variant=outline]:border-l-0 group-data-vertical/toggle-group:data-[spacing=0]:data-[variant=outline]:border-t-0 group-data-horizontal/toggle-group:data-[spacing=0]:data-[variant=outline]:first:border-l group-data-vertical/toggle-group:data-[spacing=0]:data-[variant=outline]:first:border-t",
                toggle_variants(variant=context.get("variant") or variant, size=context.get("size") or size),
                className,
            )}
            ...{props}
        >
            {children}
        </{ToggleGroupPrimitive.Item}>
    """
