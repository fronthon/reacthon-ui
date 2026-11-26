// The icons of a registry item written in Python, Lucide's, in the library a
// project's components.json names, as shadcn's CLI writes its TSX ones for it:
// each icon in its place, the item's `meta.icons` listing a file's icons in
// its order with their names in each library, the same Lucide icon another
// one elsewhere in the file; its import and its tag as the CLI's templates
// have them (@shadcn/registry's iconLibraries), and as its transform reads
// them: a template's own attributes only where it wraps the icon, Hugeicons',
// and none the element has already.
const LIBRARIES = {
  tabler: { from: "@tabler/icons-react", packages: ["@tabler/icons-react"] },
  hugeicons: {
    from: "@hugeicons/core-free-icons",
    packages: ["@hugeicons/react", "@hugeicons/core-free-icons"],
    wrapper: ["@hugeicons/react", "HugeiconsIcon"],
  },
  phosphor: { from: "@phosphor-icons/react", packages: ["@phosphor-icons/react"] },
  remixicon: { from: "@remixicon/react", packages: ["@remixicon/react"] },
}

export const iconLibraries = ["lucide", ...Object.keys(LIBRARIES)]

function rewritten(text, icons, library) {
  const { from, wrapper } = LIBRARIES[library]
  const lucide = new Set(icons.map((one) => one.lucide))
  const seen = {}
  const used = []
  // The next one of this Lucide icon in the file, in the library.
  const next = (name) => {
    const at = (seen[name] = (seen[name] ?? -1) + 1)
    const one = icons.filter((icon) => icon.lucide === name)[at]?.[library]

    if (!one) throw new Error(`no ${library} icon for the ${at + 1}th ${name}`)
    if (!used.includes(one)) used.push(one)
    return one
  }
  const tags = text.replace(/<(\/?)\{(\w+)\}/g, (whole, closing, name, at) => {
    if (!lucide.has(name)) return whole
    if (closing) return `</{${wrapper ? wrapper[1] : name}}`

    const one = next(name)
    const own = text.slice(at, text.indexOf("/>", at))

    return wrapper ? `<{${wrapper[1]}} icon={${one}}${/\bstrokeWidth=/.test(own) ? "" : " strokeWidth={2}"}` : `<{${one}}`
  })
  const entry = `${JSON.stringify(from)}: [${used.map((one) => JSON.stringify(one)).join(", ")}]`

  return tags.replace(/"lucide-react": \[[^\]]*\]/, wrapper ? `${JSON.stringify(wrapper[0])}: [${JSON.stringify(wrapper[1])}], ${entry}` : entry)
}

export function withIcons(item, library) {
  if (library === "lucide" || !item.meta?.icons) return item
  if (!LIBRARIES[library]) throw new Error(`no icon library ${library}, only ${iconLibraries.join(", ")}`)

  const dependencies = (item.dependencies ?? []).filter((one) => one !== "lucide-react")

  return {
    ...item,
    dependencies: [...new Set([...dependencies, ...LIBRARIES[library].packages])].sort(),
    files: item.files.map((file) => (item.meta.icons[file.target] ? { ...file, content: rewritten(file.content, item.meta.icons[file.target], library) } : file)),
  }
}
