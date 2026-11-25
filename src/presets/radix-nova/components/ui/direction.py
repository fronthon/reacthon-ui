__js__ = {"radix-ui": ["Direction"]}


def DirectionProvider(dir=None, direction=None, children=None):
    return t"""
        <{Direction.DirectionProvider} dir={direction if direction is not None else dir}>
            {children}
        </{Direction.DirectionProvider}>
    """


use_direction = Direction.useDirection
