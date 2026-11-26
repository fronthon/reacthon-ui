from utils import cn

__js__ = {"react-aria-components": ["composeRenderProps", "Input as InputPrimitive"]}


def Input(className=None, type=None, **props):
    return t"""
        <{InputPrimitive}
            type={type}
            data-slot="input"
            class={composeRenderProps(className, lambda class_name: cn("h-8 w-full min-w-0 rounded-none border border-input bg-transparent px-2.5 py-1 text-xs transition-colors outline-none file:inline-flex file:h-6 file:border-0 file:bg-transparent file:text-xs file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-1 focus-visible:ring-ring/50 disabled:pointer-events-none disabled:cursor-not-allowed disabled:bg-input/50 disabled:opacity-50 aria-invalid:border-destructive aria-invalid:ring-1 aria-invalid:ring-destructive/20 md:text-xs dark:bg-input/30 dark:disabled:bg-input/80 dark:aria-invalid:border-destructive/50 dark:aria-invalid:ring-destructive/40", class_name))}
            ...{props}
        />
    """
