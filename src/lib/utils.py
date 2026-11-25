"""The helpers the components share: cn() merges Tailwind classes, a later one
winning over an earlier one it conflicts with, cva() names a component's
classes after its variants, and closest() finds an element's ancestor."""

__js__ = {"cn": ["cn"]}


def _key(value):
    # cva reads a boolean variant by its JavaScript text.
    return ("true" if value else "false") if isinstance(value, bool) else value


def cva(base, variants=None, default_variants=None, compound_variants=None):
    """class-variance-authority's cva(): a function of the chosen variants and
    of a className, which hands back the classes they make."""
    variants = variants or {}
    default_variants = default_variants or {}

    def classes(className=None, **chosen):
        def value(name):
            given = chosen.get(name)
            return _key(default_variants.get(name) if given is None else given)

        picked = [options[value(name)] for name, options in variants.items() if value(name) in options]
        for compound in compound_variants or []:
            wanted = {name: one for name, one in compound.items() if name not in ("class", "className")}
            if all(value(name) in (one if isinstance(one, list) else [_key(one)]) for name, one in wanted.items()):
                picked += [compound.get("class"), compound.get("className")]
        return cn(base, *picked, className)

    return classes


def closest(element, selector):
    """The DOM's closest(): the element or its nearest ancestor that matches the
    selector, None where none does, as JavaScript's null; Brython's raises
    KeyError."""
    try:
        return element.closest(selector)
    except KeyError:
        return None
