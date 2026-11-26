"""The helpers the components share: cn() merges Tailwind classes, a later one
winning over an earlier one it conflicts with, cva() names a component's
classes after its variants, closest() finds an element's ancestor, sort()
sorts by a function that compares two items and reduce() combines them."""

from browser import window
from javascript import NULL

__js__ = {"cn": ["cn"]}


def _key(value):
    # cva reads a boolean variant by its JavaScript text.
    return ("true" if value else "false") if isinstance(value, bool) else value


def _joined(*values):
    # clsx(), by which cva joins its classes: the truthy ones, a list's in its
    # place, none merged as cn() merges them.
    parts = []
    for value in values:
        if isinstance(value, (list, tuple)):
            value = _joined(*value)
        if value:
            parts.append(str(value))
    return " ".join(parts)


def cva(base, variants=None, default_variants=None, compound_variants=None):
    """class-variance-authority's cva(): a function of the chosen variants and
    of a className, which hands back the classes they make, joined as they
    come, cn() merging them where the component asks it to."""
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
        return _joined(base, *picked, className)

    return classes


def closest(element, selector):
    """The DOM's closest(): the element or its nearest ancestor that matches the
    selector, javascript.NULL where none does, JavaScript's null; Brython's
    raises KeyError."""
    try:
        return element.closest(selector)
    except KeyError:
        return NULL


def sort(items, compare):
    """JavaScript's sort(): the list sorted in place by a function that compares
    two items, negative where the first comes first, and handed back. Sorted by
    JavaScript's own, on the items' places: a function that answers at random,
    a shuffle, leaves them as JavaScript leaves them."""
    order = window.Array.new()
    for at in range(len(items)):
        order.push(at)
    order.sort(lambda one, other: compare(items[one], items[other]))
    items[:] = [items[at] for at in order]
    return items


def reduce(combine, items, *initial):
    """JavaScript's reduce(), as Python's functools.reduce, which Brython does
    not ship: each item combined with what the ones before it made, from the
    first item where no initial value is given; none, and no item, is
    JavaScript's TypeError."""
    rest = list(items)
    if initial:
        made = initial[0]
    elif rest:
        made = rest.pop(0)
    else:
        raise TypeError("Reduce of empty array with no initial value")
    for item in rest:
        made = combine(made, item)
    return made
