from example import Example, ExampleWrapper
from scroll_area import ScrollArea
from separator import Separator

__js__ = {"next/image": ["default as Image"], "react": ["Fragment"]}

tags = [f"v1.2.0-beta.{len(a) - i}" for i in range(50)]

works = [
    {
        "artist": "Ornella Binni",
        "art": "https://images.unsplash.com/photo-1465869185982-5a1a7522cbcb?auto=format&fit=crop&w=300&q=80",
    },
    {
        "artist": "Tom Byrom",
        "art": "https://images.unsplash.com/photo-1548516173-3cabfa4607e9?auto=format&fit=crop&w=300&q=80",
    },
    {
        "artist": "Vladimir Malyav",
        "art": "https://images.unsplash.com/photo-1494337480532-3725c85fd2ab?auto=format&fit=crop&w=300&q=80",
    },
]


def ScrollAreaExample():
    return t"""
        <{ExampleWrapper}>
            <{ScrollAreaVertical} />
            <{ScrollAreaHorizontal} />
        </{ExampleWrapper}>
    """


def ScrollAreaVertical():
    return t"""
        <{Example} title="Vertical">
            <{ScrollArea} class="mx-auto h-72 w-48 rounded-md border style-luma:rounded-2xl style-rhea:rounded-2xl">
                <div class="p-4">
                    <h4 class="mb-4 text-sm leading-none font-medium">Tags</h4>
                    {[t'''
                        <{Fragment} key={tag}>
                            <div class="text-sm">{tag}</div>
                            <{Separator} class="my-2" />
                        </{Fragment}>
                    ''' for tag in tags]}
                </div>
            </{ScrollArea}>
        </{Example}>
    """


def ScrollAreaHorizontal():
    return t"""
        <{Example} title="Horizontal">
            <{ScrollArea} class="mx-auto w-full max-w-96 rounded-md border p-4 style-luma:rounded-2xl style-rhea:rounded-2xl">
                <div class="flex gap-4">
                    {[t'''
                        <figure key={artwork["artist"]} class="shrink-0">
                            <div class="overflow-hidden rounded-md">
                                <{Image}
                                    src={artwork["art"]}
                                    alt={f"Photo by {artwork["artist"]}"}
                                    class="aspect-[3/4] h-fit w-fit object-cover"
                                    width={300}
                                    height={400}
                                />
                            </div>
                            <figcaption class="pt-2 text-xs text-muted-foreground">
                                Photo by{" "}
                                <span class="font-semibold text-foreground">{artwork["artist"]}</span>
                            </figcaption>
                        </figure>
                    ''' for artwork in works]}
                </div>
            </{ScrollArea}>
        </{Example}>
    """
