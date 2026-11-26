"use client"

import {
  DropdownMenu,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  SidebarGroup,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/components/ui/sidebar"
import { MoreHorizontalIcon } from "lucide-react"

export function NavMain({
  items,
}: {
  items: {
    title: string
    url: string
    icon?: React.ReactNode
    isActive?: boolean
    items?: {
      title: string
      url: string
    }[]
  }[]
}) {
  const { isMobile } = useSidebar()
  return (
    <SidebarGroup>
      <SidebarMenu>
        {items.map((item) => (
          <SidebarMenuItem key={item.title}>
            <DropdownMenuTrigger>
              <SidebarMenuButton className="aria-expanded:bg-muted">
                {item.title}{" "}
                <MoreHorizontalIcon className="ml-auto" />
              </SidebarMenuButton>
              {item.items?.length ? (
                <DropdownMenu
                  placement={isMobile ? "bottom end" : "right top"}
                  className="min-w-56 rounded-lg"
                >
                  {item.items.map((item) => (
                    <DropdownMenuItem key={item.title} href={item.url}>
                      {item.title}
                    </DropdownMenuItem>
                  ))}
                </DropdownMenu>
              ) : null}
            </DropdownMenuTrigger>
          </SidebarMenuItem>
        ))}
      </SidebarMenu>
    </SidebarGroup>
  )
}

