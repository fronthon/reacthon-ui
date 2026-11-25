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
from the registry the package carries. Reacthon finds them by the folders it is
given:

```js
// vite.config.ts
plugins: [reacthon({ path: ["src/lib", "src/components/ui"] }), react(), tailwindcss()]
```

```python
from dialog import Dialog, DialogTrigger, DialogContent, DialogTitle
```

## Translated from shadcn/ui's own

`tools/tsx2py.js` writes each component file's Python from shadcn/ui's TSX
(style `radix-nova`), with TypeScript's own parser and checker, as one writes
it by hand: its imports, its `cva` tables, its props, its JSX as a t-string,
React's hooks as Reacthon's, its handlers and effects as functions of their
own, its own names in snake_case. TypeScript's types tell it what each value
is: plain data, which Brython hands Python as a dict, or an object. What it
cannot translate it names, and leaves the file out. `lib/utils.py` holds
`cn()`, shadcn/ui's own package, `cva()`, written in Python, `closest()`, the
DOM's, which Brython's raises where it finds nothing, and `sort()`,
JavaScript's, by a function that compares two items.

All 63 components of `npx shadcn add --all` are translated, the sidebar, the
carousel, the calendar and the chart included.

So are shadcn/ui's blocks, whole pages made of its components: `tools/blocks.js`
fetches each into its own folder of `src/blocks`, its page beside its own
components, as shadcn's CLI writes them. 26 of the 27 are translated, the
logins, the signups and the 16 sidebars; the dashboard's data table is not yet.

## Tested against shadcn/ui's own

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
- The demo, `src/App.py`, runs on the Python ones alone; in Chrome, Radix's
  focus, keyboard and portals behave as with the TSX ones.

```sh
npm install
npm test               # the twins
npm run translate      # src/components/ui/*.tsx into their .py
npm run blocks         # shadcn/ui's blocks into src/blocks/
npm run translate:blocks
npm run dev            # the demo
npm run registry       # the registry, built into public/r/
```

## Licence

Reacthon UI is MIT, the licence of shadcn/ui, whose components it writes in
Python. See `LICENSE`.
