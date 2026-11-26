from javascript import NULL

__js__ = {"radix-ui": ["Direction"]}


def DirectionProvider(dir=None, direction=None, children=None, **_):
    return t"""
        <{Direction.DirectionProvider} dir={direction if direction not in (None, NULL) else dir}>
            {children}
        </{Direction.DirectionProvider}>
    """


use_direction = Direction.useDirection
