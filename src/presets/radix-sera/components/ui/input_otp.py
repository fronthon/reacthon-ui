from reacthon import use_context
from utils import cn

__js__ = {"input-otp": ["OTPInput", "OTPInputContext"], "lucide-react": ["MinusIcon"]}


def InputOTP(className=None, containerClassName=None, **props):
    return t"""
        <{OTPInput}
            data-slot="input-otp"
            containerClassName={cn("cn-input-otp flex items-center has-disabled:opacity-50", containerClassName)}
            spellCheck={False}
            class={cn("disabled:cursor-not-allowed", className)}
            ...{props}
        />
    """


def InputOTPGroup(className=None, **props):
    return t"""
        <div
            data-slot="input-otp-group"
            class={cn("flex items-center gap-1 rounded-none has-aria-invalid:border-b-destructive dark:has-aria-invalid:border-b-destructive/50", className)}
            ...{props}
        />
    """


def InputOTPSlot(index=None, className=None, **props):
    input_otp_context = use_context(OTPInputContext)
    slot = input_otp_context["slots"][index] if input_otp_context["slots"][index] is not None else {}
    char, has_fake_caret, is_active = slot.get("char"), slot.get("hasFakeCaret"), slot.get("isActive")

    div = t"""
        <div class="pointer-events-none absolute inset-0 flex items-center justify-center">
            <div class="h-4 w-px animate-caret-blink bg-foreground duration-1000" />
        </div>
    """

    return t"""
        <div
            data-slot="input-otp-slot"
            data-active={is_active}
            class={cn("relative flex size-10 items-center justify-center border border-transparent border-b-input bg-transparent text-sm transition-[color,border-color] outline-none first:rounded-none last:rounded-none aria-invalid:border-b-destructive data-[active=true]:z-10 data-[active=true]:border-b-ring dark:aria-invalid:border-b-destructive/50", className)}
            ...{props}
        >
            {char}
            {has_fake_caret and div}
        </div>
    """


def InputOTPSeparator(**props):
    return t"""
        <div
            data-slot="input-otp-separator"
            class="flex items-center [&_svg:not([class*='size-'])]:size-3.5"
            role="separator"
            ...{props}
        >
            <{MinusIcon} />
        </div>
    """
