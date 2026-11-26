from example import Example, ExampleWrapper
from attachment import (
    Attachment,
    AttachmentAction,
    AttachmentActions,
    AttachmentContent,
    AttachmentDescription,
    AttachmentGroup,
    AttachmentMedia,
    AttachmentTitle,
)
from avatar import Avatar, AvatarFallback, AvatarImage
from bubble import Bubble, BubbleContent, BubbleGroup, BubbleReactions
from button import Button
from marker import Marker, MarkerContent, MarkerIcon
from message import Message, MessageAvatar, MessageContent, MessageFooter, MessageGroup, MessageHeader
from spinner import Spinner

__js__ = {
    "@/lib/ai": ["createChat"],
    "lucide-react": [
        "FileTextIcon",
        "DownloadIcon",
        "PresentationIcon",
        "FileArchiveIcon",
        "CopyIcon",
        "RefreshCcwIcon",
        "ThumbsUpIcon",
        "ThumbsDownIcon",
    ],
}


def callback(props):
    writer = props.get("writer")

    writer.reasoning(
        "The user included an image and asked for deployment status, so I should inspect the screenshot context and call the deployment health tool before answering.",
    )

    deployment = writer.tool(
        "getDeploymentHealth",
        {"title": "Checking deployment health", "input": {"project": "checkout", "region": "iad1"}},
    )

    deployment.output(
        {
            "status": "healthy",
            "p95": 186,
            "errors": 2,
            "recommendation": "Keep the deployment live and monitor error rate.",
        },
    )

    writer.data(
        {
            "type": "data-deployment",
            "id": "deployment-health",
            "data": {"status": "healthy", "region": "iad1", "latency": 186},
        },
    )
    writer.text(
        "The deployment looks healthy. P95 latency is **186ms** with **2 recent errors**, so I would keep it live and monitor error rate for the next 15 minutes.",
    )
    writer.sourceUrl(
        {
            "sourceId": "source-deployment-docs",
            "title": "Deployment health checks",
            "url": "https://vercel.com/docs/deployments",
        },
    )
    writer.sourceDocument(
        {
            "sourceId": "source-runbook",
            "title": "Checkout release runbook",
            "filename": "checkout-release-runbook.md",
            "mediaType": "text/markdown",
        },
    )


message_parts_chat = createChat(
    callback,
)

message_parts_messages = message_parts_chat.get()


def MessageExample():
    return t"""
        <{ExampleWrapper}>
            <{MessageDefault} />
            <{MessageWithAvatar} />
            <{MessageGroupExample} />
            <{MessageGroupChat} />
            <{MessageHeaderFooter} />
            <{MessageActions} />
            <{MessageAttachment} />
            <{MessageAttachmentGroup} />
        </{ExampleWrapper}>
    """


def MessageTextPart(part=None, message=None, **_):
    if part.type != "text":
        return None

    return t"""
        <{Bubble}
            align={"end" if message.role == "user" else "start"}
            variant={"default" if message.role == "user" else "ghost"}
        >
            <{BubbleContent}>
                <span class="whitespace-pre-wrap">{part.text}</span>
            </{BubbleContent}>
        </{Bubble}>
    """


def MessageDefault():
    return t"""
        <{Example} title="Message">
            <div class="flex w-full max-w-md min-w-0 flex-col gap-10">
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble}>
                            <{BubbleContent}>Deploying to prod real quick.</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>It's 4:55 PM. On a Friday.</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble}>
                            <{BubbleContent}>It's a one-line change.</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageContent}>
                        <{BubbleGroup}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>
                                    It's always a one-line change 😭. Make sure to run the tests this time.
                                </{BubbleContent}>
                            </{Bubble}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>Alright, go for it.</{BubbleContent}>
                            </{Bubble}>
                        </{BubbleGroup}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def MessageWithAvatar():
    return t"""
        <{Example} title="Avatar">
            <div class="flex w-full max-w-md flex-col gap-10">
                <{Message}>
                    <{MessageAvatar}>
                        <{Avatar}>
                            <{AvatarImage} src="https://github.com/shadcn.png" alt="@shadcn" class="grayscale" />
                            <{AvatarFallback}>CN</{AvatarFallback}>
                        </{Avatar}>
                    </{MessageAvatar}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>Something went wrong. Any idea?</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageAvatar}>
                        <{Avatar}>
                            <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                            <{AvatarFallback}>ER</{AvatarFallback}>
                        </{Avatar}>
                    </{MessageAvatar}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>
                                I checked the latest deployment and found the build failed during dependency installation.
                            </{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="end">
                    <{MessageAvatar}>
                        <{Avatar}>
                            <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                            <{AvatarFallback}>ER</{AvatarFallback}>
                        </{Avatar}>
                    </{MessageAvatar}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>Something went wrong. Any idea?</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageAvatar}>
                        <{Avatar}>
                            <{AvatarImage} src="https://avatar.vercel.sh/shadcn" alt="@shadcn" />
                            <{AvatarFallback}>CN</{AvatarFallback}>
                        </{Avatar}>
                    </{MessageAvatar}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent} class="space-y-2">
                                <div>
                                    I checked the latest deployment and found the build failed during dependency installation.
                                </div>
                                <div>Can you share the exact error message from the logs?</div>
                            </{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageAvatar}>
                        <{Avatar}>
                            <{AvatarFallback}>CN</{AvatarFallback}>
                        </{Avatar}>
                    </{MessageAvatar}>
                    <{MessageContent}>
                        <{Bubble} variant="destructive">
                            <{BubbleContent}>Something went wrong. Any idea?</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def MessageGroupExample():
    return t"""
        <{Example} title="Group">
            <div class="flex w-full max-w-md flex-col gap-10">
                <{MessageGroup}>
                    <{Message}>
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>I checked the registry addresses.</{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                    <{Message}>
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>
                                    The component and example JSON now live under the UI registry.
                                </{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                </{MessageGroup}>
                <{MessageGroup}>
                    <{Message} align="end">
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>I checked the registry addresses.</{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                    <{Message} align="end">
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>
                                    The component and example JSON now live under the UI registry.
                                </{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                </{MessageGroup}>
                <{MessageGroup}>
                    <{Message} align="end">
                        <{MessageAvatar} />
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>I checked the registry addresses.</{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                    <{Message} align="end">
                        <{MessageAvatar}>
                            <{Avatar}>
                                <{AvatarImage} src="https://avatar.vercel.sh/shadcn" alt="@shadcn" />
                                <{AvatarFallback}>CN</{AvatarFallback}>
                            </{Avatar}>
                        </{MessageAvatar}>
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>
                                    The component and example JSON now live under the UI registry.
                                </{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                </{MessageGroup}>
                <{MessageGroup}>
                    <{Message}>
                        <{MessageAvatar} />
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>I checked the registry addresses.</{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                    <{Message}>
                        <{MessageAvatar}>
                            <{Avatar}>
                                <{AvatarImage} src="https://avatar.vercel.sh/shadcn" alt="@shadcn" />
                                <{AvatarFallback}>CN</{AvatarFallback}>
                            </{Avatar}>
                        </{MessageAvatar}>
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>
                                    The component and example JSON now live under the UI registry.
                                </{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                </{MessageGroup}>
            </div>
        </{Example}>
    """


def MessageGroupChat():
    return t"""
        <{Example} title="Group Chat">
            <div class="flex w-full max-w-md flex-col gap-10">
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble} variant="tinted">
                            <{BubbleContent}>Why is the dashboard showing zero users</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{MessageGroup}>
                    <{Message}>
                        <{MessageAvatar} />
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>Define "zero."</{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                    <{Message}>
                        <{MessageAvatar}>
                            <{Avatar}>
                                <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                                <{AvatarFallback}>ER</{AvatarFallback}>
                            </{Avatar}>
                        </{MessageAvatar}>
                        <{MessageContent}>
                            <{Bubble} variant="muted">
                                <{BubbleContent}>What do you mean?</{BubbleContent}>
                            </{Bubble}>
                        </{MessageContent}>
                    </{Message}>
                </{MessageGroup}>
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble} variant="tinted">
                            <{BubbleContent}>
                                <span class="font-medium">@eve</span> can you check?
                            </{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{Marker} role="status">
                        <{MarkerIcon}>
                            <{Spinner} />
                        </{MarkerIcon}>
                        <{MarkerContent}>Checking the logs...</{MarkerContent}>
                    </{Marker}>
                </{Message}>
                <{Message}>
                    <{MessageContent}>
                        <{MessageHeader}>Eve</{MessageHeader}>
                        <{Bubble} variant="ghost">
                            <{BubbleContent}>
                                <span class="whitespace-pre-wrap">
                                    {"I found the following error in the logs:\n\n- Error: No users found\n- Stack trace:\n  - at src/users/services/user-service.ts:123\n  - at src/users/services/get-user.ts:230\n\nCan you check if the users are being created?"}
                                </span>
                            </{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def MessageHeaderFooter():
    return t"""
        <{Example} title="Header and Footer">
            <div class="flex w-full max-w-md flex-col gap-12">
                <{Message} align="end">
                    <{MessageContent}>
                        <{MessageHeader} class="justify-end">You</{MessageHeader}>
                        <{Bubble}>
                            <{BubbleContent}>Can we keep this style quiet and send the update today?</{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter} class="gap-2">
                            <span>Delivered</span>
                            <{Button} variant="ghost" size="xs">Undo</{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="start">
                    <{MessageContent}>
                        <{MessageHeader}>
                            <span>Olivia</span>
                            <span class="ml-auto font-normal">1m ago</span>
                        </{MessageHeader}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>
                                I checked the logs. The retry finished and the missing invoices are included now.
                            </{BubbleContent}>
                            <{BubbleReactions}>
                                <{Button} variant="ghost" size="xs">Thanks</{Button}>
                            </{BubbleReactions}>
                        </{Bubble}>
                        <{MessageFooter} class="gap-2">
                            <span>From Support queue</span>
                            <{Button} variant="ghost" size="xs">Copy</{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="end">
                    <{MessageContent}>
                        <{MessageHeader}>Marina</{MessageHeader}>
                        <{Bubble} variant="outline">
                            <{BubbleContent}>
                                I drafted the reply with the exact filter path and a link to the export history.
                            </{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter} class="gap-2">
                            <span>Draft ready</span>
                            <{Button} variant="outline" size="xs">Review</{Button}>
                            <{Button} size="xs">Send</{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="start">
                    <{MessageContent}>
                        <{MessageHeader}>Assistant note</{MessageHeader}>
                        <{Bubble} variant="ghost">
                            <{BubbleContent}>
                                Ghost messages keep long-form assistant notes aligned with the surrounding text instead of adding a frame.
                            </{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter} class="gap-2">
                            <span>Internal only</span>
                            <{Button} variant="ghost" size="xs">Pin</{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="end">
                    <{MessageContent}>
                        <{MessageHeader} class="justify-end">Automation warning</{MessageHeader}>
                        <{Bubble} variant="destructive">
                            <{BubbleContent}>
                                The old export link expires in 10 minutes. Regenerate before sending this transcript externally.
                            </{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter} class="gap-2">
                            <span>Needs action</span>
                            <{Button} variant="destructive" size="xs">Regenerate</{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def MessageAttachment():
    return t"""
        <{Example} title="Attachment">
            <div class="flex w-full max-w-sm flex-col gap-8">
                <{Message} align="end">
                    <{MessageContent}>
                        <{Attachment} orientation="vertical">
                            <{AttachmentMedia} variant="image">
                                <img
                                    src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80"
                                    alt="Workspace"
                                />
                            </{AttachmentMedia}>
                        </{Attachment}>
                        <{Bubble}>
                            <{BubbleContent}>
                                Here's the image. Can you add it to the PDF? Use it for the cover page.
                            </{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>
                                Done. Here's the PDF with the image added as the cover page.
                            </{BubbleContent}>
                        </{Bubble}>
                        <{Attachment}>
                            <{AttachmentMedia}>
                                <{FileTextIcon} />
                            </{AttachmentMedia}>
                            <{AttachmentContent}>
                                <{AttachmentTitle}>sales-dashboard.pdf</{AttachmentTitle}>
                                <{AttachmentDescription}>PDF · 2.4 MB</{AttachmentDescription}>
                            </{AttachmentContent}>
                            <{AttachmentActions}>
                                <{AttachmentAction}
                                    type="button"
                                    aria-label="Download"
                                    size="icon-sm"
                                    variant="secondary"
                                >
                                    <{DownloadIcon} />
                                </{AttachmentAction}>
                            </{AttachmentActions}>
                        </{Attachment}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble}>
                            <{BubbleContent}>Thanks. Looks good.</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def MessageAttachmentGroup():
    return t"""
        <{Example} title="Attachment Group">
            <div class="flex w-full max-w-sm flex-col gap-8">
                <{Message} align="end">
                    <{MessageContent}>
                        <{AttachmentGroup} class="w-[80%]">
                            <{Attachment} orientation="vertical">
                                <{AttachmentMedia} variant="image">
                                    <img
                                        src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=900&auto=format&fit=crop&q=80"
                                        alt="Workspace"
                                    />
                                </{AttachmentMedia}>
                            </{Attachment}>
                            <{Attachment} orientation="vertical">
                                <{AttachmentMedia} variant="image">
                                    <img
                                        src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=900&auto=format&fit=crop&q=80"
                                        alt="Desk"
                                    />
                                </{AttachmentMedia}>
                            </{Attachment}>
                            <{Attachment} orientation="vertical">
                                <{AttachmentMedia} variant="image">
                                    <img
                                        src="https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=900&auto=format&fit=crop&q=80"
                                        alt="Office"
                                    />
                                </{AttachmentMedia}>
                            </{Attachment}>
                        </{AttachmentGroup}>
                        <{Bubble}>
                            <{BubbleContent}>Here are the brand photos. Can you add them to the deck?</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>Done. Here's the draft deck and the exported assets.</{BubbleContent}>
                        </{Bubble}>
                        <{AttachmentGroup} class="w-full">
                            <{Attachment} class="w-64">
                                <{AttachmentMedia}>
                                    <{FileTextIcon} />
                                </{AttachmentMedia}>
                                <{AttachmentContent}>
                                    <{AttachmentTitle}>brand-deck.pdf</{AttachmentTitle}>
                                    <{AttachmentDescription}>PDF · 3.1 MB</{AttachmentDescription}>
                                </{AttachmentContent}>
                                <{AttachmentActions}>
                                    <{AttachmentAction}
                                        type="button"
                                        aria-label="Download brand-deck.pdf"
                                        size="icon-sm"
                                        variant="secondary"
                                    >
                                        <{DownloadIcon} />
                                    </{AttachmentAction}>
                                </{AttachmentActions}>
                            </{Attachment}>
                            <{Attachment} class="w-64">
                                <{AttachmentMedia}>
                                    <{PresentationIcon} />
                                </{AttachmentMedia}>
                                <{AttachmentContent}>
                                    <{AttachmentTitle}>brand-deck.key</{AttachmentTitle}>
                                    <{AttachmentDescription}>Keynote · 9 MB</{AttachmentDescription}>
                                </{AttachmentContent}>
                                <{AttachmentActions}>
                                    <{AttachmentAction}
                                        type="button"
                                        aria-label="Download brand-deck.key"
                                        size="icon-sm"
                                        variant="secondary"
                                    >
                                        <{DownloadIcon} />
                                    </{AttachmentAction}>
                                </{AttachmentActions}>
                            </{Attachment}>
                            <{Attachment} class="w-64">
                                <{AttachmentMedia}>
                                    <{FileArchiveIcon} />
                                </{AttachmentMedia}>
                                <{AttachmentContent}>
                                    <{AttachmentTitle}>brand-assets.zip</{AttachmentTitle}>
                                    <{AttachmentDescription}>ZIP · 4.2 MB</{AttachmentDescription}>
                                </{AttachmentContent}>
                                <{AttachmentActions}>
                                    <{AttachmentAction}
                                        type="button"
                                        aria-label="Download brand-assets.zip"
                                        size="icon-sm"
                                        variant="secondary"
                                    >
                                        <{DownloadIcon} />
                                    </{AttachmentAction}>
                                </{AttachmentActions}>
                            </{Attachment}>
                        </{AttachmentGroup}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def MessageActions():
    return t"""
        <{Example} title="Actions">
            <div class="flex w-full max-w-md flex-col gap-10">
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble}>
                            <{BubbleContent}>What is the status of the deployment?</{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter}>
                            <{Button} variant="ghost" size="icon" aria-label="Copy">
                                <{CopyIcon} />
                            </{Button}>
                            <{Button} variant="ghost" size="icon" aria-label="Retry">
                                <{RefreshCcwIcon} />
                            </{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageAvatar}>
                        <{Avatar}>
                            <{AvatarImage} src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
                            <{AvatarFallback}>ER</{AvatarFallback}>
                        </{Avatar}>
                    </{MessageAvatar}>
                    <{MessageContent}>
                        <{Bubble} variant="muted">
                            <{BubbleContent}>
                                The install failure is coming from the workspace package. I can open the exact log line or retry the deployment.
                            </{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter}>
                            <{Button} variant="ghost" size="icon" aria-label="Copy">
                                <{CopyIcon} />
                            </{Button}>
                            <{Button} variant="ghost" size="icon" aria-label="Like: thumbs up">
                                <{ThumbsUpIcon} />
                            </{Button}>
                            <{Button} variant="ghost" size="icon" aria-label="Like: thumbs down">
                                <{ThumbsDownIcon} />
                            </{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble}>
                            <{BubbleContent}>Okay drop me a link. I'll check it out.</{BubbleContent}>
                        </{Bubble}>
                        <{MessageFooter} class="gap-2">
                            <span class="font-normal text-destructive">Failed to send</span>
                            <{Button} variant="secondary" size="xs">Retry</{Button}>
                        </{MessageFooter}>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """
