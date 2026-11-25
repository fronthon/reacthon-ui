from browser import window
from javascript import NULL
from reacthon import use_effect, use_state
from utils import cn, cva
from button import Button

__js__ = {"lucide-react": ["CheckIcon", "CopyIcon"]}

code_block_variants = cva(
    "group/code-block relative flex w-full min-w-0 flex-col overflow-hidden rounded-lg text-sm has-[>[data-slot=code-block-content]:focus-visible]:ring-3 has-[>[data-slot=code-block-content]:focus-visible]:ring-ring/50 data-[size=sm]:text-xs",
    {
        "variant": {
            "default": "border border-input text-foreground has-[>[data-slot=code-block-content]:focus-visible]:border-ring dark:bg-input/30",
            "destructive": "border border-destructive/30 text-destructive dark:border-destructive/40",
        },
    },
    {"variant": "default"},
)


def CodeBlock(className=None, variant="default", size="default", **props):
    return t"""
        <div
            data-slot="code-block"
            data-variant={variant}
            data-size={size}
            class={cn(code_block_variants(variant=variant), className)}
            ...{props}
        />
    """


def CodeBlockHeader(className=None, **props):
    return t"""
        <div
            data-slot="code-block-header"
            class={cn("flex min-w-0 shrink-0 items-center gap-2 px-3 pt-3 text-muted-foreground group-data-[size=sm]/code-block:px-2.5 group-data-[size=sm]/code-block:pt-2.5 group-data-[variant=destructive]/code-block:text-destructive *:has-[>[data-slot=code-block-title]]:min-w-0", className)}
            ...{props}
        />
    """


def CodeBlockTitle(className=None, **props):
    return t"""
        <div
            data-slot="code-block-title"
            class={cn("min-w-0 truncate font-sans text-sm font-medium text-foreground group-data-[size=sm]/code-block:text-xs group-data-[variant=destructive]/code-block:text-destructive [&_svg]:pointer-events-none [&_svg]:inline-block [&_svg]:align-middle [&_svg:not([class*='size-'])]:size-3.5 *:[svg]:me-1.5", className)}
            ...{props}
        />
    """


def CodeBlockActions(className=None, **props):
    return t"""
        <div
            data-slot="code-block-actions"
            class={cn("-my-1 ms-auto -me-1.5 flex shrink-0 items-center gap-1 [[data-slot=code-block]>&]:absolute [[data-slot=code-block]>&]:end-2 [[data-slot=code-block]>&]:top-2 [[data-slot=code-block]>&]:z-10 [[data-slot=code-block]>&]:m-0 [[data-slot=code-block]>&]:opacity-0 [[data-slot=code-block]>&]:transition-opacity [[data-slot=code-block]>&]:group-focus-within/code-block:opacity-100 [[data-slot=code-block]>&]:group-hover/code-block:opacity-100 group-data-[size=sm]/code-block:[[data-slot=code-block]>&]:end-1.5 group-data-[size=sm]/code-block:[[data-slot=code-block]>&]:top-1.5 [[data-slot=code-block]>&]:pointer-coarse:opacity-100 [[data-slot=code-block]>&]:*:[button]:bg-background [[data-slot=code-block]>&]:*:[button]:ring-1 [[data-slot=code-block]>&]:*:[button]:ring-foreground/10", className)}
            ...{props}
        />
    """


def CodeBlockCopyButton(value=None, variant="ghost", size="icon-xs", className=None, onClick=None, **props):
    copied, set_copied = use_state(False)

    def effect():
        if not copied:
            return

        timeout = window.setTimeout(lambda: set_copied(False), 2000)
        return lambda: window.clearTimeout(timeout)

    use_effect(effect, [copied])

    def on_click(event):
        if onClick:
            onClick(event)
        window.navigator.clipboard.writeText(value).then(lambda: set_copied(True)).catch(lambda *args: None)

    return t"""
        <{Button}
            data-slot="code-block-copy-button"
            data-copied={copied or None}
            variant={variant}
            size={size}
            aria-label={"Copied" if copied else "Copy"}
            class={cn(className)}
            onClick={on_click}
            ...{props}
        >
            {t'<{CheckIcon} />' if copied else t'<{CopyIcon} />'}
        </{Button}>
        <span aria-live="polite" class="sr-only">{"Copied" if copied else ""}</span>
    """


def CodeBlockContent(className=None, children=None, style=None, wrap=False, lineNumbers=False, startLine=1, **props):
    return t"""
        <pre
            data-slot="code-block-content"
            data-wrap={wrap or None}
            data-numbered={lineNumbers or None}
            dir="ltr"
            tabIndex={0}
            style={ {
                "counterReset": f"line {startLine - 1}",
                **(style or {}),
            } }
            class={cn("min-h-0 min-w-0 scroll-fade-x scrollbar-thin overflow-auto px-3 py-3 text-start font-mono leading-relaxed outline-none group-has-data-[slot=code-block-footer]/code-block:pb-2 group-has-data-[slot=code-block-header]/code-block:pt-2 group-data-[size=sm]/code-block:px-2.5 group-data-[size=sm]/code-block:py-2.5 group-data-[size=sm]/code-block:group-has-data-[slot=code-block-header]/code-block:pt-1.5 data-wrap:scroll-fade-y data-wrap:wrap-break-word data-wrap:whitespace-pre-wrap", className)}
            ...{props}
        >
            <code
                data-slot="code-block-code"
                class="grid min-h-lh min-w-max content-start in-data-numbered:grid-cols-[auto_1fr] in-data-wrap:min-w-0"
            >
                {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(children.removesuffix("\n").split("\n"))] if lineNumbers and isinstance(children, str) else children}
            </code>
        </pre>
    """


code_block_line_variants = cva(
    "relative -mx-3 block min-h-lh px-3 group-data-[size=sm]/code-block:-mx-2.5 group-data-[size=sm]/code-block:px-2.5 before:min-w-6 before:text-end before:text-muted-foreground after:absolute after:start-1 after:top-0 after:text-muted-foreground after:select-none in-data-numbered:col-span-2 in-data-numbered:grid in-data-numbered:grid-cols-subgrid in-data-numbered:gap-x-3 in-data-numbered:[counter-increment:line] in-data-numbered:before:content-[counter(line)] in-data-numbered:before:select-none in-data-numbered:supports-[content:counter(line)_/_'']:before:content-[counter(line)_/_'']",
    {
        "variant": {
            "default": "",
            "added": "bg-muted after:content-['+']",
            "removed": "bg-destructive/10 after:text-destructive after:content-['−']",
            "highlighted": "bg-muted",
        },
    },
    {"variant": "default"},
)


def CodeBlockLine(className=None, variant="default", children=None, **props):
    # An empty line holds a newline so copying a selection keeps blank lines.
    empty = children is None or children is NULL or children == "" or isinstance(children, list) and len(children) == 0

    return t"""
        <span
            data-slot="code-block-line"
            data-variant={variant}
            class={cn(code_block_line_variants(variant=variant), className)}
            ...{props}
        >
            <span data-slot="code-block-line-content" class="min-w-0">{"\n" if empty else children}</span>
        </span>
    """


def CodeBlockFooter(className=None, **props):
    return t"""
        <div
            data-slot="code-block-footer"
            class={cn("flex min-w-0 shrink-0 items-center gap-2 px-3 pb-3 text-muted-foreground group-data-[size=sm]/code-block:px-2.5 group-data-[size=sm]/code-block:pb-2.5", className)}
            ...{props}
        />
    """
