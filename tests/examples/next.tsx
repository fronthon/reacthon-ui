// Next.js's image and link, which shadcn/ui's examples take, as the page
// renders them where Next.js is not: an image and a link.
import { createElement } from "react"

export default function Next({ href, src, fill, priority, ...props }: Record<string, unknown>) {
  return href === undefined ? createElement("img", { src, ...props }) : createElement("a", { href, ...props })
}
