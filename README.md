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
npx shadcn add <registry>/r/dialog.json
```

copies `dialog.py`, and the `button.py` and `lib/utils.py` it needs, as
`npx shadcn add dialog` copies `dialog.tsx`. Reacthon finds them by the folders it
is given:

```js
// vite.config.ts
plugins: [reacthon({ path: ["src/lib", "src/components/ui"] }), react(), tailwindcss()]
```

```python
from dialog import Dialog, DialogTrigger, DialogContent, DialogTitle
```

## Written so far

Button, Card, Input, Label, Checkbox, Dialog, Tabs, Select, Dropdown menu and
Accordion, each line for line from shadcn/ui's own (style `radix-nova`).
`lib/utils.py` holds `cn()`, shadcn/ui's own package, and `cva()`, written in
Python.

## Tested against shadcn/ui's own

`tests/twin.test.tsx` renders each component written in Python and shadcn/ui's
TSX one with the same props, open and closed, every variant and size, and
compares the two pages to the character: 87 of them. The demo, `src/App.py`,
runs on the Python ones alone; in Chrome, Radix's focus, keyboard and portals
behave as with the TSX ones.

## Translated from TSX

`tools/tsx2py.js` writes a component file's Python from shadcn/ui's TSX, with
TypeScript's own parser: its imports, its `cva` tables, its props, its JSX as a
t-string. What it cannot translate it names, and leaves the file out.

- The ten above, translated, pass the same twin: 87 of 87.
- Of the 63 components of `npx shadcn add --all`, 50 are translated. Rendered
  alone against their TSX ones, 154 components give the same page; the others
  need their context to render, in TSX as well.
- The 13 left out use React's hooks, block-bodied functions or JavaScript's own
  library (`Array.from`, `.map`, a context read as an object): the next step.

```sh
npm install
npm test               # the twin
npm run translate      # src/components/ui/*.tsx into generated/
npm run test:translated
npm run dev            # the demo
npm run registry       # the registry, built into public/r/
```

## Licence

Reacthon UI is MIT, the licence of shadcn/ui, whose components it writes in
Python. See `LICENSE`.
