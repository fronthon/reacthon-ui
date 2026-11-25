"""The two helpers the components share: cn() merges Tailwind classes, a later
one winning over an earlier one it conflicts with, and cva() names a
component's classes after its variants."""

__js__ = {"cn": ["cn"]}


def cva(base, variants=None, default_variants=None):
    """class-variance-authority's cva(): a function of the chosen variants and
    of a className, which hands back the classes they make."""
    variants = variants or {}
    default_variants = default_variants or {}

    def classes(className=None, **chosen):
        picked = []
        for name, options in variants.items():
            value = chosen.get(name)
            if value is None:
                value = default_variants.get(name)
            if value in options:
                picked.append(options[value])
        return cn(base, *picked, className)

    return classes
