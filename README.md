# Reacthon UI

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

## Add a component

In a React project with shadcn/ui and [Reacthon](https://github.com/svelthon/reacthon):

```sh
npx reacthon-ui add dialog
```

copies `dialog.py`, and the `button.py` and `lib/utils.py` it needs, as
`npx shadcn add dialog` copies `dialog.tsx`: shadcn's own CLI does the copying,
from the registry the package carries for the project's preset, which its
`components.json` names. Their icons are in the library it names too, Lucide,
Tabler, Hugeicons, Phosphor or Remix Icon, each written in its place as
shadcn's CLI writes it in the TSX. Reacthon finds them by the folders it is
given:

```js
// vite.config.ts
plugins: [reacthon({ path: ["src/lib", "src/components/ui"] }), react(), tailwindcss()]
```

```python
from dialog import Dialog, DialogTrigger, DialogContent, DialogTitle
```

## Translated from shadcn/ui's own

A preset of shadcn/ui is a style on a base, the library its components behave
by. All 24 of them: the eight styles, Vega, Nova, Maia, Lyra, Mira, Luma,
Rhea and Sera, on each of the three bases, Radix, Base UI and React Aria,
`base-nova` being the preset `npx shadcn init --defaults` makes. Their Python
is written with Lucide's icons, and `icons.json` holds each icon of each file
in the other libraries, as shadcn's registry has them for its CLI, in the
file's order: `bin/icons.js` writes them in the project's library. Each
stands in its own folder of `src/presets`, laid out as a project of that
preset: `components/ui`, `hooks`, `lib` and the blocks, the helpers of
`src/lib` aside, which every preset shares. `tools/preset.js` fetches its TSX
as shadcn's CLI writes it.

`tools/tsx2py.js` writes each component file's Python from shadcn/ui's TSX,
with TypeScript's own parser and checker, as one writes
it by hand: its imports, its `cva` tables, its props, its JSX as a t-string,
React's hooks as Reacthon's, its handlers and effects as functions of their
own, its own names in snake_case. TypeScript's types tell it what each value
is: plain data, which Brython hands Python as a dict, or an object. What it
cannot translate it names, and leaves the file out. `lib/utils.py` holds
`cn()`, shadcn/ui's own package, `cva()`, written in Python, `closest()`, the
DOM's, which Brython's raises where it finds nothing, and `sort()`,
JavaScript's, by a function that compares two items.

In each preset, all the components of `npx shadcn add --all` are translated, 63
on Radix and on Base UI, 61 on React Aria, the sidebar, the carousel, the
calendar and the chart included.

So are shadcn/ui's blocks, whole pages made of its components, each in its own
folder of the preset's `blocks`, its page beside its own components, as
shadcn's CLI writes them. All 27 of each preset are translated: the logins,
the signups, the 16 sidebars and the dashboard, its chart, and its table on
TanStack's with rows dragged by dnd-kit.

## Tested against shadcn/ui's own

The twins run on each preset, a Vitest project of its own, where `@` is the
preset's folder: 4,888 of them. The trees and the scenes were written for
Radix's components; one that React Aria's TSX cannot render either, a dialog
of other parts, a calendar not react-day-picker's, says nothing of the Python,
and is skipped as such: 5 a preset of React Aria, 40 in all.

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
  sidebar's group opened, a mail picked, the dashboard's rows selected, its
  next page and its form sent: the same page after each step, and the same
  errors.
- `tests/icons.test.tsx` writes every component's icons in each of the four
  other libraries, each found, none of Lucide's left. The pages were twinned,
  once for each library and each base, against the TSX shadcn's CLI writes
  for it: the same pages.
- The demo, `src/App.py`, runs on the Python ones alone; in Chrome, Radix's
  focus, keyboard and portals behave as with the TSX ones.

```sh
npm install
npm test               # the twins, on each preset
npm run preset radix-nova   # its components and blocks, from shadcn/ui
npm run translate      # each preset's components/ui/*.tsx into their .py
npm run translate:blocks
npm run dev            # the demo, on radix-nova
npm run registry       # a registry a preset, built into public/r/<preset>/
```

## Licence

Reacthon UI is MIT, the licence of shadcn/ui, whose components it writes in
Python. See `LICENSE`.
