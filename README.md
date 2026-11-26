# Reacthon UI

<div align="center">
    <img src="img/reacthon-ui-512.png" alt="Reacthon UI" width="172"/>
</div>

**shadcn/ui's components, written in Python, for Reacthon.**

```python
from utils import cva

__js__ = {"radix-ui": ["Slot"]}

button_variants = cva("inline-flex items-center …", {"variant": {"default": "…", "outline": "…"}})


def Button(className=None, variant="default", size="default", asChild=False, **props):
    Comp = Slot.Root if asChild else "button"

    return t"""
        <{Comp}
            data-slot="button"
            class={button_variants(variant=variant, size=size, className=className)}
            ...{props}
        />
    """
```

shadcn/ui hands you the source of each component rather than a library, so that
you read it and change it. Here that source is Python: the same Radix parts
underneath, the same Tailwind classes, the same props, and a component a
Python developer owns.

## Add a component or a block

In a React project with shadcn/ui and [Reacthon](https://github.com/fronthon/reacthon):

```sh
npx reacthon-ui add dialog
```

copies `dialog.py`, and the `button.py` and `lib/utils.py` it needs, as
`npx shadcn add dialog` copies `dialog.tsx`: shadcn's own CLI does the copying,
from the registry the package carries for the project's preset, which its
`components.json` names. Their icons are in the library it names too, Lucide,
Tabler, Hugeicons, Phosphor or Remix Icon, each written in its place as
shadcn's CLI writes it in the TSX.

```sh
npx reacthon-ui add dashboard-01
```

copies a block's own components, `app_sidebar.py`, `data_table.py` and the
others, into `components`, with those of `components/ui` they take, as
`npx shadcn add dashboard-01` copies its TSX. Its page, shadcn's CLI writes
only where a page is a file of the app's routes, as in Next.js, there
`app/dashboard/page.py`. A Vite project, Reacthon's, has none, its root
showing what it chooses: the CLI writes no page there, of TSX as of Python,
and the block's page is its `page.py` in this repository, to write in one's
own, `App.py` say.

Reacthon finds them all by the folders it is given:

```js
// vite.config.ts
plugins: [reacthon({ path: ["src/lib", "src/components/ui", "src/components"] }), react(), tailwindcss()]
```

```python
from dialog import Dialog, DialogTrigger, DialogContent, DialogTitle
from app_sidebar import AppSidebar
```

## Convert your own

```sh
npx reacthon-ui convert src/components/team-card.tsx src/app
```

writes each TSX file it is given, or finds in a folder, a component or a page,
in Python beside it, `team_card.py`, by the converter that writes Reacthon UI's
components from shadcn/ui's, with the project's own `tsconfig`. An import of a
file of the project that is Python, converted with it or before it, is
Python's, `from team_card import TeamCard`, and `@/components/ui/dialog` the
`dialog.py` that `reacthon-ui add` writes, which it names if the project has
not added it yet, with the command that does; a library's stays JavaScript's,
in `__js__`. A `.py` already there is kept, as one may have changed it, unless
`--overwrite` says. What it cannot convert it names, and leaves the file out.

## Translated from shadcn/ui's own

A preset of shadcn/ui is a style on a base, the library its components behave
by. All 24 of them: the eight styles, Vega, Nova, Maia, Lyra, Mira, Luma,
Rhea and Sera, on each of the three bases, Radix, Base UI and React Aria,
`base-nova` being the preset `npx shadcn init --defaults` makes. Their Python
is written with Lucide's icons, and `icons.json` holds each icon of each file
in the other libraries, as shadcn's registry has them for its CLI, in the
file's order: `bin/icons.js` writes them in the project's library.
`items.json` holds what shadcn's registry says of each component and block
beside its files: the packages and the items it takes, which its CLI installs
whether its code imports them or not, at their versions, and where a block's
page and data go; `tools/registry.js` gives our items all of it. Each preset
stands in its own folder of `src/presets`, laid out as a project of that
preset: `components/ui`, `hooks`, `lib` and the blocks, the helpers of
`src/lib` aside, which every preset shares. `tools/preset.js` fetches its TSX
as shadcn's CLI writes it.

`tools/tsx2py.js` writes each component file's Python from shadcn/ui's TSX,
with TypeScript's own parser and checker, as one writes
it by hand: its imports, its `cva` tables, its props, its JSX as a t-string,
React's hooks as Reacthon's, its handlers and effects as functions of their
own, its own names in snake_case, JavaScript's `null` as `javascript.NULL` and
`undefined` as `None`, as Brython hands them, and `None` where React renders
either alike, a child or what a component returns. A component takes `**_`,
the props it is handed and does not take, and a function one of them calls
`*_`, the arguments it does not read, which JavaScript's leave as they come.
TypeScript's types tell it what each value is: plain data, which Brython hands
Python as a dict, or an object. What Python writes its own way it writes so: a
`switch` as an `if` and its `elif`s, an `async` function as an `async def`,
which `aio.run()` starts where JavaScript calls it without awaiting it, a `try`
and its `catch`, a `forEach` as a loop, a closure's write of an outer name with
`nonlocal`, `forwardRef` as a component that takes `ref` among its props, as
React 19 hands it; and what Brython's DOM answers its own way, `canvas.width`
the style's, by JavaScript's. What it cannot translate it names, and leaves the
file out. `lib/utils.py` holds `cn()`, shadcn/ui's own package, `cva()`,
written in Python, `closest()`, the DOM's, which Brython's raises where it
finds nothing, `sort()`, JavaScript's, by a function that compares two items,
and `reduce()`, functools', which Brython does not ship.

In each preset, all the components of `npx shadcn add --all` are translated, 63
on Radix and on Base UI, 61 on React Aria, the sidebar, the carousel, the
calendar and the chart included; and on Base UI the sonner `--all` leaves out
there, beside Base UI's own toast, which a block takes.

So are shadcn/ui's blocks, whole pages made of its components, each in its own
folder of the preset's `blocks`, its page beside its own components, as
shadcn's CLI writes them. All 27 of each preset are translated: the logins,
the signups, the 16 sidebars and the dashboard, its chart, and its table on
TanStack's with rows dragged by dnd-kit.

So are shadcn/ui's showcases, the canvas of its site's create page, `preview`
and `preview-02`, 61 cards of its components put to use, on every preset, each
in its folder of the preset's `previews`: the page its registry has for the
preset, and its cards, which the registry leaves out, from shadcn's
repository, where each is written once for each base and each style dresses it
by its components, its icons Lucide's. The three that read shadcn's site, its
fonts and its icons, are left out of the page.

## Tested against shadcn/ui's own

The twins run on each preset, a Vitest project of its own, where `@` is the
preset's folder: 4,936 of them, none skipped. Each tree and each scene is
written with the parts of its preset's base, as shadcn's own examples write
them there: React Aria's dialog opens from its trigger, its calendar takes
`@internationalized/date`'s dates, Base UI's select its `items`. Each says
what shadcn's page must show, and each step of a scene changes that page, so
that none passes by rendering nothing on either side.

- `tests/twin.test.tsx` renders ten of them and shadcn/ui's TSX ones with the
  same props, open and closed, every variant and size, and compares the two
  pages to the character: 87 of them.
- `tests/alone.test.tsx` renders every component alone against its TSX one:
  the same page wherever the TSX one renders by itself.
- `tests/hooks.test.tsx` renders the ones of React's hooks in their trees, then
  clicks and types in both alike: the sidebar's trigger, rail and Ctrl+B and
  its cookie, the carousel's keys and `setApi`, the toggle group, the OTP
  input, the calendar's days and months, the chart's tooltip and legend, the
  code block's copy button: the same page after each step, 26 scenes.
- `tests/blocks.test.tsx` renders each translated block's page against its TSX
  one: the same page, to the character.
- `tests/block-scenes.test.tsx` uses three of them as one does, both alike: a
  sidebar's group opened and a team picked from its menu, a mail picked, the
  dashboard's rows selected, its next page and its form sent, its toast shown
  in the application's toaster: the same page after each step, and the same
  errors.
- `tests/examples/examples.test.tsx` converts the pages of shadcn/ui's site, as
  `reacthon-ui convert` converts a project's own TSX: its two showcases on
  every preset, and its examples, which show each component, on Nova on each
  base, 187 of them; each converted, its Python page the same as its TSX one,
  to the character. `npm run preset radix-nova -- --previews` fetches the
  showcases, and `-- --examples` the examples as shadcn's CLI writes them,
  leaving out one that imports a file of shadcn's site, which works in no
  project.
- `tests/icons.test.tsx` writes every component's and block's icons in each
  of the four other libraries, each found, none of Lucide's left. The pages
  were twinned, once for each library and each base, against the TSX shadcn's
  CLI writes for it: the same pages; and blocks, written by the two CLIs into
  a Next.js project, the TSX by shadcn's and the Python by `reacthon-ui add`:
  the same pages.
- The demo shows the showcases and the 27 blocks, each page at `#/<name>` in
  Python and its TSX twin at `#/<name>/tsx`, under a toolbar written in Python
  with the preset's components: the page, the style and the base, each of the
  24 presets a build of its own, which `npm run build:demo` builds side by
  side; the colors of shadcn's create page, its 7 grays and its 17 colors over
  neutral, painted at once on any preset, which `npm run colors` fetches;
  Python or TSX, and the theme.
- `tests/browser/blocks.test.ts` builds the demo and opens each page in
  Chrome, where a page is laid out, its Python page against its TSX twin, the
  toolbar aside: the same page as it loads and after a mouse collapses the
  sidebar, hovers a menu's button and the chart, and drags a row of the
  dashboard's table, and nothing thrown. jsdom renders neither recharts'
  tooltip nor a drag.

```sh
npm install
npm test               # the twins, on each preset
npm run preset radix-nova   # its components and blocks, from shadcn/ui
npm run convert        # each preset's components/ui/*.tsx into their .py
npm run convert:blocks
npm run convert:examples
npm run dev            # the demo, on radix-nova, or the preset DEMO_PRESET names
npm run build:demo     # the demo of every preset, into dist/
npm run registry       # a registry a preset, its components and blocks, built into public/r/<preset>/
```

## Licence

Reacthon UI is MIT, the licence of shadcn/ui, whose components it writes in
Python. See `LICENSE`.
