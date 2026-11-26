from utils import cn

__js__ = {"react-aria-components": ["composeRenderProps", "Input as InputPrimitive"]}


def Input(className=None, type=None, **props):
    return t"""
        <{InputPrimitive}
            type={type}
            data-slot="input"
            class={composeRenderProps(className, lambda class_name: cn("h-10 w-full min-w-0 border border-transparent border-b-input bg-transparent px-0 py-1 text-base transition-[color,border-color] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:border-b-ring disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-b-destructive md:text-sm dark:aria-invalid:border-b-destructive/50", class_name))}
            ...{props}
        />
    """
