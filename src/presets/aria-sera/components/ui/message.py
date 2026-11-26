from utils import cn


def MessageGroup(className=None, **props):
    return t'<div data-slot="message-group" class={cn("flex min-w-0 flex-col gap-2", className)} ...{props} />'


def Message(className=None, align="start", **props):
    return t"""
        <div
            data-slot="message"
            data-align={align}
            class={cn("group/message relative flex w-full min-w-0 gap-2 text-sm data-[align=end]:flex-row-reverse", className)}
            ...{props}
        />
    """


def MessageAvatar(className=None, **props):
    return t"""
        <div
            data-slot="message-avatar"
            class={cn("flex w-fit min-w-8 shrink-0 items-center justify-center self-end overflow-hidden rounded-full bg-muted group-has-data-[slot=message-footer]/message:-translate-y-8", className)}
            ...{props}
        />
    """


def MessageContent(className=None, **props):
    return t"""
        <div
            data-slot="message-content"
            class={cn("flex w-full min-w-0 flex-col gap-2.5 wrap-break-word group-data-[align=end]/message:*:data-slot:self-end", className)}
            ...{props}
        />
    """


def MessageHeader(className=None, **props):
    return t"""
        <div
            data-slot="message-header"
            class={cn("flex max-w-full min-w-0 items-center px-4 text-xs font-medium tracking-wide text-muted-foreground uppercase group-has-data-[variant=ghost]/message:px-0", className)}
            ...{props}
        />
    """


def MessageFooter(className=None, **props):
    return t"""
        <div
            data-slot="message-footer"
            class={cn("flex max-w-full min-w-0 items-center px-4 text-xs font-medium tracking-wide text-muted-foreground uppercase group-has-data-[variant=ghost]/message:px-0 group-data-[align=end]/message:justify-end", className)}
            ...{props}
        />
    """
