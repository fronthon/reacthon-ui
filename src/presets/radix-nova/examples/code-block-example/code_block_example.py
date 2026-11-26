from browser import document, window
from javascript import NULL
from reacthon import use_effect, use_id, use_state
from example import Example, ExampleWrapper
from bubble import Bubble, BubbleContent
from button import Button
from card import Card, CardContent, CardDescription, CardHeader, CardTitle
from code_block import (
    CodeBlock,
    CodeBlockActions,
    CodeBlockContent,
    CodeBlockCopyButton,
    CodeBlockFooter,
    CodeBlockHeader,
    CodeBlockLine,
    CodeBlockTitle,
)
from dialog import Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger
from message import Message, MessageContent
from tabs import Tabs, TabsContent, TabsList, TabsTrigger
from trace import (
    Trace, TraceCollapsible, TraceCollapsibleContent, TraceCollapsibleTrigger, TraceIcon, TraceLine, TraceTitle,
)

__js__ = {
    "streamdown": ["Streamdown", "useIsCodeFenceIncomplete"],
    "@/hooks/use-highlighted-code": ["useHighlightedCode"],
    "lucide-react": ["TerminalIcon", "FileCodeIcon", "WrapTextIcon", "DownloadIcon", "ChevronDownIcon"],
}

build = "$ pnpm build\n> next build\n\n   ▲ Next.js 16.0.0\n   Creating an optimized production build ...\n ✓ Compiled successfully in 4.2s\n ✓ Generating static pages (12/12)\n\nRoute (app)                Size  First Load JS\n┌ ○ /                    1.9 kB         112 kB\n├ ○ /_not-found           993 B         103 kB\n└ ƒ /api/chat             141 B         102 kB"

install = "$ pnpm add ai @ai-sdk/react zod\nProgress: resolved 412, reused 398, downloaded 14, added 14, done\ndependencies:\n+ @ai-sdk/react 3.0.12\n+ ai 6.0.12\n+ zod 4.1.12\nDone in 2.8s using pnpm v10.18.0"

error = "TypeError: Cannot read properties of undefined (reading 'map')\n    at MessageList (components/message-list.tsx:18:22)\n    at renderWithHooks (react-dom.development.js:16305:18)\n    at mountIndeterminateComponent (react-dom.development.js:20069:13)"

source = "import { streamText } from \"ai\"\n\nexport async function POST(request: Request) {\n  const { messages } = await request.json()\n\n  const result = streamText({\n    model: \"anthropic/claude-sonnet-4.5\",\n    messages,\n  })\n\n  return result.toUIMessageStreamResponse()\n}"

chat = "\"use client\"\n\nimport * as React from \"react\"\nimport { useChat } from \"@ai-sdk/react\"\n\nimport { Button } from \"@/components/ui/button\"\nimport { Input } from \"@/components/ui/input\"\n\nexport function Chat() {\n  const [input, setInput] = React.useState(\"\")\n  const { messages, sendMessage, status } = useChat()\n\n  return (\n    <div className=\"flex flex-col gap-4\">\n      {messages.map((message) => (\n        <div key={message.id}>\n          {message.parts.map((part, index) =>\n            part.type === \"text\" ? <p key={index}>{part.text}</p> : null\n          )}\n        </div>\n      ))}\n      <form\n        onSubmit={(event) => {\n          event.preventDefault()\n          sendMessage({ text: input })\n          setInput(\"\")\n        }}\n      >\n        <Input value={input} onChange={(event) => setInput(event.target.value)} placeholder=\"Ask anything\" />\n        <Button disabled={status !== \"ready\"}>Send</Button>\n      </form>\n    </div>\n  )\n}"

diff = [
    {"variant": "default", "text": "export function Greeting({ name }: Props) {"},
    {"variant": "removed", "text": "  return <p>Hello, {name}</p>"},
    {"variant": "added", "text": "  return <p className=\"text-sm\">Hello, {name}!</p>"},
    {"variant": "default", "text": "}"},
]

log = "\n".join(
    "\n",
)


def CodeBlockExample():
    return t"""
        <{ExampleWrapper} class="md:grid-cols-1">
            <{CodeBlockPlain} />
            <{CodeBlockWrap} />
            <{CodeBlockLineNumbers} />
            <{CodeBlockWithHeader} />
            <{CodeBlockWithActions} />
            <{CodeBlockDestructive} />
            <{CodeBlockDiff} />
            <{CodeBlockHighlightedLines} />
            <{CodeBlockHeight} />
            <{CodeBlockShowMore} />
            <{CodeBlockShowMoreScroll} />
            <{CodeBlockHighlighted} />
            <{CodeBlockEmpty} />
            <{CodeBlockSmall} />
            <{CodeBlockSmallDestructive} />
            <{CodeBlockTrace} />
            <{CodeBlockTypeset} />
            <{CodeBlockWrapLineNumbers} />
            <{CodeBlockStartLine} />
            <{CodeBlockDiffWrap} />
            <{CodeBlockHeaderEdges} />
            <{CodeBlockSmallest} />
            <{CodeBlockSmallCombinations} />
            <{CodeBlockStreamed} />
            <{CodeBlockMarkdown} />
            <{CodeBlockLanguages} />
            <{CodeBlockInCard} />
            <{CodeBlockInMessage} />
            <{CodeBlockTabs} />
            <{CodeBlockRtl} />
        </{ExampleWrapper}>
    """


def CodeBlockPlain():
    return t"""
        <{Example} title="Plain">
            <{CodeBlock}>
                <{CodeBlockContent}>{build}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockWrap():
    return t"""
        <{Example} title="Wrap">
            <{CodeBlock}>
                <{CodeBlockContent} wrap>{error}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockLineNumbers():
    lines = useHighlightedCode(source, "ts")

    return t"""
        <{Example} title="Line Numbers">
            <{CodeBlock}>
                <{CodeBlockContent} lineNumbers>
                    {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockWithHeader():
    return t"""
        <{Example} title="Header">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>
                        <{TerminalIcon} />
                        Terminal
                    </{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={install} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent}>{install}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockDestructive():
    return t"""
        <{Example} title="Destructive">
            <{CodeBlock} variant="destructive">
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>Error</{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={error} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} wrap>{error}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockDiff():
    lines = useHighlightedCode("\n".join([line["text"] for line in diff]), "tsx")

    return t"""
        <{Example} title="Diff">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>components/greeting.tsx</{CodeBlockTitle}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} lineNumbers>
                    {[t'''
                        <{CodeBlockLine}
                            key={index}
                            variant={diff[index]["variant"]}
                        >
                            {line}
                        </{CodeBlockLine}>
                    ''' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockHighlightedLines():
    lines = useHighlightedCode(source, "ts")

    return t"""
        <{Example} title="Highlighted Lines">
            <{CodeBlock}>
                <{CodeBlockContent} lineNumbers>
                    {[t'''
                        <{CodeBlockLine}
                            key={index}
                            variant={"highlighted" if index >= 5 and index <= 8 else "default"}
                        >
                            {line}
                        </{CodeBlockLine}>
                    ''' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockHeight():
    return t"""
        <{Example} title="Height">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>Logs</{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={log} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} class="max-h-48 scroll-fade-y">{log}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockHighlighted():
    lines = useHighlightedCode(source, "ts")

    return t"""
        <{Example} title="Syntax Highlighting">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>
                        <{FileCodeIcon} />
                        app/api/chat/route.ts
                    </{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={source} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} lineNumbers>
                    {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockEmpty():
    return t"""
        <{Example} title="Empty">
            <{CodeBlock}>
                <{CodeBlockContent}>{""}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockSmall():
    return t"""
        <{Example} title="Small">
            <{CodeBlock} size="sm">
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>
                        <{TerminalIcon} />
                        pnpm add ai @ai-sdk/react zod
                    </{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={install} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} wrap>{install}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockSmallDestructive():
    return t"""
        <{Example} title="Small Destructive">
            <{CodeBlock} size="sm" variant="destructive">
                <{CodeBlockContent} wrap>{error}</{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockTrace():
    return t"""
        <{Example} title="Trace">
            <{Trace}>
                <{TraceCollapsible} defaultOpen>
                    <{TraceCollapsibleTrigger}>
                        <{TraceLine}>
                            <{TraceIcon}>
                                <{TerminalIcon} />
                            </{TraceIcon}>
                            <{TraceTitle}>Ran pnpm add ai @ai-sdk/react zod</{TraceTitle}>
                        </{TraceLine}>
                    </{TraceCollapsibleTrigger}>
                    <{TraceCollapsibleContent}>
                        <{CodeBlock} size="sm">
                            <{CodeBlockContent} wrap class="max-h-64">{install}</{CodeBlockContent}>
                        </{CodeBlock}>
                    </{TraceCollapsibleContent}>
                </{TraceCollapsible}>
                <{TraceCollapsible} defaultOpen>
                    <{TraceCollapsibleTrigger}>
                        <{TraceLine} status="error">
                            <{TraceIcon}>
                                <{TerminalIcon} />
                            </{TraceIcon}>
                            <{TraceTitle}>Failed to run pnpm dev</{TraceTitle}>
                        </{TraceLine}>
                    </{TraceCollapsibleTrigger}>
                    <{TraceCollapsibleContent}>
                        <{CodeBlock} size="sm" variant="destructive">
                            <{CodeBlockContent} wrap class="max-h-64">{error}</{CodeBlockContent}>
                        </{CodeBlock}>
                    </{TraceCollapsibleContent}>
                </{TraceCollapsible}>
            </{Trace}>
        </{Example}>
    """


def CodeBlockTypeset():
    lines = useHighlightedCode(source, "ts")
    command = useHighlightedCode("pnpm add ai @ai-sdk/react zod", "bash")

    return t"""
        <{Example} title="Typeset">
            <div class="typeset max-w-2xl">
                <h3>Stream a response</h3>
                <p>
                    Create a route handler that calls <code>streamText</code> and returns the stream to the client. The <code>useChat</code> hook reads it on the other side.
                </p>
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>
                            <{FileCodeIcon} />
                            app/api/chat/route.ts
                        </{CodeBlockTitle}>
                        <{CodeBlockActions}>
                            <{CodeBlockCopyButton} value={source} />
                        </{CodeBlockActions}>
                    </{CodeBlockHeader}>
                    <{CodeBlockContent} lineNumbers>
                        {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                    </{CodeBlockContent}>
                </{CodeBlock}>
                <p>Then install the packages the route uses.</p>
                <{CodeBlock}>
                    <{CodeBlockContent}>
                        {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(command)]}
                    </{CodeBlockContent}>
                </{CodeBlock}>
                <p>The model streams text parts as they arrive, so the answer renders while it is written.</p>
            </div>
        </{Example}>
    """


def CodeBlockWithActions():
    wrap, set_wrap = use_state(False)
    lines = useHighlightedCode(source, "ts")

    return t"""
        <{Example} title="Actions">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>app/api/chat/route.ts</{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{Button}
                            variant="ghost"
                            size="icon-xs"
                            aria-label="Wrap lines"
                            aria-pressed={wrap}
                            class="aria-pressed:text-foreground"
                            onClick={(lambda: set_wrap(not wrap))}
                        >
                            <{WrapTextIcon} />
                        </{Button}>
                        <{Button}
                            variant="ghost"
                            size="icon-xs"
                            aria-label="Download"
                            onClick={(lambda: download(source, "route.ts"))}
                        >
                            <{DownloadIcon} />
                        </{Button}>
                        <{CodeBlockCopyButton} value={source} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} wrap={wrap} lineNumbers>
                    {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def download(code, filename):
    url = window.URL.createObjectURL(window.Blob.new([code], {"type": "text/plain"}))
    link = document.createElement("a")
    link.href = url
    link.download = filename
    link.click()
    window.URL.revokeObjectURL(url)


def CodeBlockShowMore():
    expanded, set_expanded = use_state(False)
    lines = useHighlightedCode(chat, "tsx")
    id_ = use_id()

    return t"""
        <{Example} title="Show More">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>components/chat.tsx</{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={chat} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent}
                    id={id_}
                    lineNumbers
                    class={None if expanded else "max-h-64 scroll-fade-y overflow-y-hidden"}
                >
                    {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
                <{CodeBlockFooter} class="justify-center">
                    <{Button}
                        variant="ghost"
                        size="xs"
                        aria-expanded={expanded}
                        aria-controls={id_}
                        onClick={(lambda: set_expanded(not expanded))}
                    >
                        <{ChevronDownIcon} class="transition-transform in-aria-expanded:rotate-180 aria-expanded:rotate-180" />
                        {"Show less" if expanded else "Show more"}
                    </{Button}>
                </{CodeBlockFooter}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockShowMoreScroll():
    expanded, set_expanded = use_state(False)
    lines = useHighlightedCode(chat, "tsx")
    id_ = use_id()

    return t"""
        <{Example} title="Show More with Max Height">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>components/chat.tsx</{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={chat} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
                <{CodeBlockContent}
                    id={id_}
                    lineNumbers
                    class={"max-h-96 scroll-fade-y" if expanded else "max-h-64 scroll-fade-y overflow-y-hidden"}
                >
                    {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
                <{CodeBlockFooter} class="justify-center">
                    <{Button}
                        variant="ghost"
                        size="xs"
                        aria-expanded={expanded}
                        aria-controls={id_}
                        onClick={(lambda: set_expanded(not expanded))}
                    >
                        <{ChevronDownIcon} class="transition-transform in-aria-expanded:rotate-180 aria-expanded:rotate-180" />
                        {"Show less" if expanded else "Show more"}
                    </{Button}>
                </{CodeBlockFooter}>
            </{CodeBlock}>
        </{Example}>
    """


middle = "  if (!session) {\n    redirect(\"/login\")\n  }\n\n  const projects = await db.project.findMany({\n    where: { ownerId: session.user.id },\n    orderBy: { updatedAt: \"desc\" },\n  })\n\n  return <ProjectList projects={projects} />\n}"

long_diff = [
    {"variant": "default", "text": "export async function GET(request: Request) {"},
    {
        "variant": "removed",
        "text": "  const { searchParams } = new URL(request.url, \"http://localhost:3000/api/projects?include=owner,members\")",
    },
    {
        "variant": "added",
        "text": "  const { searchParams } = new URL(request.url, process.env.NEXT_PUBLIC_APP_URL ?? request.headers.get(\"origin\") ?? undefined)",
    },
    {"variant": "added", "text": "  const include = searchParams.get(\"include\")?.split(\",\") ?? []"},
    {"variant": "default", "text": "  return Response.json(await getProjects({ include }))"},
    {"variant": "default", "text": "}"},
]

samples = [
    {
        "language": "json",
        "title": "package.json",
        "code": "{\n  \"name\": \"acme-chat\",\n  \"scripts\": { \"dev\": \"next dev --turbopack\" },\n  \"dependencies\": { \"ai\": \"^6.0.12\", \"zod\": \"^4.1.12\" }\n}",
    },
    {
        "language": "css",
        "title": "app/globals.css",
        "code": "@import \"tailwindcss\";\n\n:root {\n  --radius: 0.625rem;\n}",
    },
    {
        "language": "python",
        "title": "main.py",
        "code": "def greet(name: str) -> str:\n    return f\"Hello, {name}!\"",
    },
    {"language": "text", "title": "notes.txt", "code": "An unknown language renders as plain lines."},
]

ansi = "$ pnpm test\n\u001b[32m✓\u001b[39m src/format.test.ts \u001b[2m(4 tests)\u001b[22m\n\u001b[31m✗\u001b[39m src/stream.test.ts \u001b[2m(3 tests | 1 failed)\u001b[22m\n\nTests  \u001b[31m1 failed\u001b[39m | \u001b[32m6 passed\u001b[39m (7)"

answer = "Wrap the input in a `useDebounce` hook:\n\n```tsx\nexport function useDebounce<T>(value: T, delay = 300) {\n  const [debounced, setDebounced] = React.useState(value)\n\n  React.useEffect(() => {\n    const timeout = setTimeout(() => setDebounced(value), delay)\n    return () => clearTimeout(timeout)\n  }, [value, delay])\n\n  return debounced\n}\n```\n\nThen install it:\n\n```bash\npnpm dlx shadcn@latest add use-debounce\n```"

files = [
    {"id": "route", "title": "app/api/chat/route.ts", "language": "ts", "code": source},
    {"id": "chat", "title": "components/chat.tsx", "language": "tsx", "code": chat},
    {"id": "env", "title": ".env.local", "language": "bash", "code": "AI_GATEWAY_API_KEY=your-api-key"},
]


def Highlighted(code=None, language=None, **props):
    lines = useHighlightedCode(code, language)

    return t"""
        <{CodeBlockContent} ...{props}>
            {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
        </{CodeBlockContent}>
    """


def CodeBlockWrapLineNumbers():
    return t"""
        <{Example} title="Wrap and Line Numbers">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>components/chat.tsx</{CodeBlockTitle}>
                </{CodeBlockHeader}>
                <{Highlighted} code={chat} language="tsx" wrap lineNumbers />
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockStartLine():
    return t"""
        <{Example} title="Start Line">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>app/dashboard/page.tsx</{CodeBlockTitle}>
                </{CodeBlockHeader}>
                <{Highlighted} code={middle} language="tsx" lineNumbers startLine={995} />
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockDiffWrap():
    lines = useHighlightedCode("\n".join([line["text"] for line in long_diff]), "ts")

    return t"""
        <{Example} title="Diff, Wrap and Highlighting">
            <{CodeBlock}>
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>app/api/projects/route.ts</{CodeBlockTitle}>
                </{CodeBlockHeader}>
                <{CodeBlockContent} wrap lineNumbers startLine={12}>
                    {[t'''
                        <{CodeBlockLine}
                            key={index}
                            variant={long_diff[index]["variant"]}
                        >
                            {line}
                        </{CodeBlockLine}>
                    ''' for index, line in enumerate(lines)]}
                </{CodeBlockContent}>
            </{CodeBlock}>
        </{Example}>
    """


def CodeBlockHeaderEdges():
    return t"""
        <{Example} title="Header Edges">
            <div class="flex flex-col gap-4">
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>Title only</{CodeBlockTitle}>
                    </{CodeBlockHeader}>
                    <{CodeBlockContent}>{"console.log(\"title, no actions\")"}</{CodeBlockContent}>
                </{CodeBlock}>
                <{CodeBlock}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={install} />
                    </{CodeBlockActions}>
                    <{CodeBlockContent}>{install}</{CodeBlockContent}>
                </{CodeBlock}>
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>
                            <{FileCodeIcon} />
                            apps/web/app/(dashboard)/settings/organizations/[organizationId]/members/invitations/page.tsx
                        </{CodeBlockTitle}>
                        <{CodeBlockActions}>
                            <{CodeBlockCopyButton} value={source} />
                        </{CodeBlockActions}>
                    </{CodeBlockHeader}>
                    <{CodeBlockContent}>{"export default function Page() {}"}</{CodeBlockContent}>
                </{CodeBlock}>
            </div>
        </{Example}>
    """


def CodeBlockSmallest():
    return t"""
        <{Example} title="Single Line and Empty">
            <div class="flex flex-col gap-4">
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>Install</{CodeBlockTitle}>
                        <{CodeBlockActions}>
                            <{CodeBlockCopyButton} value="pnpm dlx shadcn@latest add code-block" />
                        </{CodeBlockActions}>
                    </{CodeBlockHeader}>
                    <{Highlighted} code="pnpm dlx shadcn@latest add code-block" language="bash" />
                </{CodeBlock}>
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>output.log</{CodeBlockTitle}>
                    </{CodeBlockHeader}>
                    <{CodeBlockContent}>{""}</{CodeBlockContent}>
                </{CodeBlock}>
                <{CodeBlock}>
                    <{Highlighted} code="pnpm dev" language="bash" />
                </{CodeBlock}>
            </div>
        </{Example}>
    """


def CodeBlockSmallCombinations():
    lines = useHighlightedCode("\n".join([line["text"] for line in diff]), "tsx")

    return t"""
        <{Example} title="Small Combinations">
            <div class="flex flex-col gap-4">
                <{CodeBlock} size="sm">
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>components/greeting.tsx</{CodeBlockTitle}>
                        <{CodeBlockActions}>
                            <{CodeBlockCopyButton} value={source} />
                        </{CodeBlockActions}>
                    </{CodeBlockHeader}>
                    <{CodeBlockContent} lineNumbers>
                        {[t'''
                            <{CodeBlockLine}
                                key={index}
                                variant={diff[index]["variant"]}
                            >
                                {line}
                            </{CodeBlockLine}>
                        ''' for index, line in enumerate(lines)]}
                    </{CodeBlockContent}>
                </{CodeBlock}>
                <{CodeBlock} size="sm">
                    <{Highlighted} code={source} language="ts" lineNumbers startLine={995} />
                </{CodeBlock}>
            </div>
        </{Example}>
    """


streamed = [
    {
        "title": "app/api/chat/route.ts",
        "language": "ts",
        "lineNumbers": True,
        "highlight": [5, 6, 7, 8],
        "code": source,
    },
    {"language": "bash", "code": "pnpm dlx shadcn@latest add code-block"},
    {
        "title": "components/search.tsx",
        "language": "tsx",
        "lineNumbers": True,
        "diff": True,
        "code": " export function Search() {\n   const [query, setQuery] = React.useState(\"\")\n-  const results = useSearch(query)\n+  const debounced = useDebounce(query, 300)\n+  const results = useSearch(debounced)\n \n   return <SearchResults results={results} />\n }",
    },
]

offsets = [streamed[0:index].reduce(lambda total, block: total + len(block["code"]), 0) for index, _ in enumerate(streamed)]

streamed_length = streamed.reduce(lambda sum_, block: sum_ + len(block["code"]), 0)


def StreamedBlock(block=None, code=None, **_):
    rows = code.split("\n")
    text = "\n".join([row[1:] for row in rows]) if block.get("diff") else code
    lines = useHighlightedCode(text, block["language"])

    return t"""
        <{CodeBlock}>
            {block.get("title") and t'''
                <{CodeBlockHeader}>
                    <{CodeBlockTitle}>{block.get("title")}</{CodeBlockTitle}>
                    <{CodeBlockActions}>
                        <{CodeBlockCopyButton} value={text} disabled={len(code) < len(block["code"])} />
                    </{CodeBlockActions}>
                </{CodeBlockHeader}>
            '''}
            <{CodeBlockContent} lineNumbers={block.get("lineNumbers", False)}>
                {[t'''
                    <{CodeBlockLine}
                        key={index}
                        variant={("added" if rows[index].startswith("+") else "removed" if rows[index].startswith("-") else "default") if block.get("diff") else "highlighted" if (index in block.get("highlight") if block.get("highlight") else None) else "default"}
                    >
                        {line}
                    </{CodeBlockLine}>
                ''' for index, line in enumerate(lines)]}
            </{CodeBlockContent}>
        </{CodeBlock}>
    """


def use_stream(length):
    position, set_position = use_state(length)

    def effect():
        if position >= length:
            return

        timeout = window.setTimeout(lambda: set_position(position + 3), 16)
        return lambda: window.clearTimeout(timeout)

    use_effect(effect, [position, length])

    return [position, lambda: set_position(0)]


def CodeBlockStreamed():
    position, replay = use_stream(streamed_length)

    return t"""
        <{Example} title="Streaming">
            <div class="flex flex-col gap-4">
                {[position > offsets[index] and t'''
                    <{StreamedBlock}
                        key={block["code"]}
                        block={block}
                        code={block["code"][0:position - offsets[index]]}
                    />
                ''' for index, block in enumerate(streamed)]}
                <{Button}
                    variant="outline"
                    size="sm"
                    class="self-start"
                    disabled={position < streamed_length}
                    onClick={replay}
                >
                    Replay
                </{Button}>
            </div>
        </{Example}>
    """


def MarkdownCode(node=None, className=None, children=None, **props):
    incomplete = useIsCodeFenceIncomplete()
    block = "data-block" in props
    code = children if isinstance(children, str) else ""
    language = window.RegExp.new("language-(\\S+)").exec(className if className not in (None, NULL) else "")[1] if window.RegExp.new("language-(\\S+)").exec(className if className not in (None, NULL) else "") else None
    if language in (None, NULL):
        language = ""
    lines = useHighlightedCode(code if block else "", language)

    if not block:
        return t'<code class="rounded-sm bg-muted px-1 py-0.5 font-mono text-[0.9em]">{children}</code>'

    return t"""
        <{CodeBlock} class="my-3">
            <{CodeBlockHeader}>
                <{CodeBlockTitle}>{language or "text"}</{CodeBlockTitle}>
                <{CodeBlockActions}>
                    <{CodeBlockCopyButton} value={code} disabled={incomplete} />
                </{CodeBlockActions}>
            </{CodeBlockHeader}>
            <{CodeBlockContent}>
                {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
            </{CodeBlockContent}>
        </{CodeBlock}>
    """


markdown_components = {"code": MarkdownCode}


def CodeBlockMarkdown():
    position, replay = use_stream(len(answer))

    return t"""
        <{Example} title="Markdown">
            <div class="flex flex-col gap-4 text-sm">
                <{Streamdown} components={markdown_components} controls={False} isAnimating={position < len(answer)}>
                    {answer[0:position]}
                </{Streamdown}>
                <{Button}
                    variant="outline"
                    size="sm"
                    class="self-start"
                    disabled={position < len(answer)}
                    onClick={replay}
                >
                    Replay
                </{Button}>
            </div>
        </{Example}>
    """


def CodeBlockLanguages():
    lines = useHighlightedCode(ansi, "ansi")

    return t"""
        <{Example} title="Languages">
            <div class="flex flex-col gap-4">
                {[t'''
                    <{CodeBlock} key={sample["language"]}>
                        <{CodeBlockHeader}>
                            <{CodeBlockTitle}>{sample["title"]}</{CodeBlockTitle}>
                        </{CodeBlockHeader}>
                        <{Highlighted} code={sample["code"]} language={sample["language"]} />
                    </{CodeBlock}>
                ''' for sample in samples]}
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>ANSI</{CodeBlockTitle}>
                    </{CodeBlockHeader}>
                    <{CodeBlockContent} wrap>
                        {[t'<{CodeBlockLine} key={index}>{line}</{CodeBlockLine}>' for index, line in enumerate(lines)]}
                    </{CodeBlockContent}>
                </{CodeBlock}>
            </div>
        </{Example}>
    """


def CodeBlockInCard():
    return t"""
        <{Example} title="Card and Dialog">
            <div class="flex flex-col items-start gap-4">
                <{Card} class="w-full">
                    <{CardHeader}>
                        <{CardTitle}>Install the AI SDK</{CardTitle}>
                        <{CardDescription}>Add the packages to your project.</{CardDescription}>
                    </{CardHeader}>
                    <{CardContent}>
                        <{CodeBlock}>
                            <{CodeBlockHeader}>
                                <{CodeBlockTitle}>Terminal</{CodeBlockTitle}>
                                <{CodeBlockActions}>
                                    <{CodeBlockCopyButton} value="pnpm add ai @ai-sdk/react zod" />
                                </{CodeBlockActions}>
                            </{CodeBlockHeader}>
                            <{Highlighted} code="pnpm add ai @ai-sdk/react zod" language="bash" />
                        </{CodeBlock}>
                    </{CardContent}>
                </{Card}>
                <{Dialog}>
                    <{DialogTrigger} asChild>
                        <{Button} variant="outline">View route</{Button}>
                    </{DialogTrigger}>
                    <{DialogContent} class="sm:max-w-xl">
                        <{DialogHeader}>
                            <{DialogTitle}>app/api/chat/route.ts</{DialogTitle}>
                            <{DialogDescription}>The route that streams the answer.</{DialogDescription}>
                        </{DialogHeader}>
                        <{CodeBlock}>
                            <{Highlighted} code={source} language="ts" lineNumbers />
                        </{CodeBlock}>
                    </{DialogContent}>
                </{Dialog}>
            </div>
        </{Example}>
    """


def CodeBlockInMessage():
    return t"""
        <{Example} title="Chat Answer">
            <div class="flex flex-col gap-4 text-sm">
                <{Message} align="end">
                    <{MessageContent}>
                        <{Bubble}>
                            <{BubbleContent}>How do I stream a response?</{BubbleContent}>
                        </{Bubble}>
                    </{MessageContent}>
                </{Message}>
                <{Message}>
                    <{MessageContent} class="gap-3">
                        <p>Create a route handler that returns the stream:</p>
                        <{CodeBlock}>
                            <{CodeBlockHeader}>
                                <{CodeBlockTitle}>app/api/chat/route.ts</{CodeBlockTitle}>
                                <{CodeBlockActions}>
                                    <{CodeBlockCopyButton} value={source} />
                                </{CodeBlockActions}>
                            </{CodeBlockHeader}>
                            <{Highlighted} code={source} language="ts" />
                        </{CodeBlock}>
                        <p>The client reads it with useChat.</p>
                    </{MessageContent}>
                </{Message}>
            </div>
        </{Example}>
    """


def CodeBlockTabs():
    return t"""
        <{Example} title="Tabs">
            <{Tabs} defaultValue="route">
                <{TabsList}>
                    {[t'''
                        <{TabsTrigger}
                            key={file["id"]}
                            value={file["id"]}
                        >
                            {file["title"].split("/").at(-1)}
                        </{TabsTrigger}>
                    ''' for file in files]}
                </{TabsList}>
                {[t'''
                    <{TabsContent} key={file["id"]} value={file["id"]}>
                        <{CodeBlock}>
                            <{CodeBlockHeader}>
                                <{CodeBlockTitle}>{file["title"]}</{CodeBlockTitle}>
                                <{CodeBlockActions}>
                                    <{CodeBlockCopyButton} value={file["code"]} />
                                </{CodeBlockActions}>
                            </{CodeBlockHeader}>
                            <{Highlighted} code={file["code"]} language={file["language"]} lineNumbers />
                        </{CodeBlock}>
                    </{TabsContent}>
                ''' for file in files]}
            </{Tabs}>
        </{Example}>
    """


def CodeBlockRtl():
    return t"""
        <{Example} title="RTL">
            <div dir="rtl" class="flex flex-col gap-3 text-sm">
                <p>أنشئ ملف المسار وأعد البث إلى العميل.</p>
                <{CodeBlock}>
                    <{CodeBlockHeader}>
                        <{CodeBlockTitle}>app/api/chat/route.ts</{CodeBlockTitle}>
                        <{CodeBlockActions}>
                            <{CodeBlockCopyButton} value={source} />
                        </{CodeBlockActions}>
                    </{CodeBlockHeader}>
                    <{Highlighted} code={source} language="ts" lineNumbers />
                </{CodeBlock}>
            </div>
        </{Example}>
    """
