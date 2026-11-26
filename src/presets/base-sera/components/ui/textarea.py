from utils import cn


def Textarea(className=None, **props):
    return t"""
        <textarea
            data-slot="textarea"
            class={cn("flex field-sizing-content min-h-16 w-full resize-none rounded-none border border-transparent border-b-input bg-transparent px-0 py-3 text-base transition-[color,border-color] outline-none placeholder:text-muted-foreground focus-visible:border-b-ring disabled:cursor-not-allowed disabled:opacity-50 aria-invalid:border-b-destructive md:text-sm dark:aria-invalid:border-b-destructive/50", className)}
            ...{props}
        />
    """
