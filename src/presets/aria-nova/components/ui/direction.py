from browser import window

__js__ = {"react-aria-components": ["I18nProvider", "useLocale"]}


def DirectionProvider(**props):
    # For compatibility with Radix / Base UI, if only a `direction` is provided and not a `locale`,
    # create a locale string that forces the direction by setting the script to arabic or latin.
    current_locale = useLocale().get("locale")
    locale = props.get("locale")
    if not locale and props.get("direction"):
        locale = str(window.Intl.Locale.new(current_locale, {"script": "Arab" if props.get("direction") == "rtl" else "Latn"}))

    return t"<{I18nProvider} ...{props} locale={locale} />"


def use_direction():
    direction = useLocale().get("direction")
    return direction
