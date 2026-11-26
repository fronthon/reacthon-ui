import colors from "./colors.json"

// shadcn/ui's colors, which the demo's toolbar picks: a gray's variables, or a
// color's over neutral, the gray its CLI starts from, light and dark, in a
// style after the stylesheet's own; kept for the next page, which may be
// another preset's build.
const KEY = "reacthon-ui-color"
const NEUTRAL = colors.find((one) => one.name === "neutral")!

export const choices = colors.map(({ name, title, gray }) => ({ name, title, gray }))

export function saved(): string {
  try {
    return localStorage.getItem(KEY) ?? NEUTRAL.name
  } catch {
    return NEUTRAL.name
  }
}

// The color's variables, its radius aside, which the style sets.
const variables = (values: Record<string, string>) =>
  Object.entries(values)
    .filter(([name]) => name !== "radius")
    .map(([name, value]) => `--${name}: ${value};`)
    .join(" ")

export function paint(name: string) {
  const chosen = colors.find((one) => one.name === name) ?? NEUTRAL
  const [light, dark] = chosen.gray ? [chosen.light, chosen.dark] : [{ ...NEUTRAL.light, ...chosen.light }, { ...NEUTRAL.dark, ...chosen.dark }]
  let style = document.getElementById("demo-color")

  if (!style) {
    style = document.createElement("style")
    style.id = "demo-color"
    document.head.append(style)
  }
  style.textContent = `:root { ${variables(light)} } .dark { ${variables(dark)} }`
  try {
    localStorage.setItem(KEY, chosen.name)
  } catch {
    // A page that keeps nothing paints the same.
  }
}
