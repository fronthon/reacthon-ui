import {
  DropdownMenu,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar,
} from "@/components/ui/sidebar"
import { MoreHorizontalIcon, StarOffIcon, LinkIcon, ArrowUpRightIcon, Trash2Icon } from "lucide-react"

export function NavFavorites({
  favorites,
}: {
  favorites: {
    name: string
    url: string
    emoji: string
  }[]
}) {
  const { isMobile } = useSidebar()
  return (
    <SidebarGroup className="group-data-[collapsible=icon]:hidden">
      <SidebarGroupLabel>Favorites</SidebarGroupLabel>
      <SidebarMenu>
        {favorites.map((item) => (
          <SidebarMenuItem key={item.name}>
            <SidebarMenuButton href={item.url} tooltip={item.name}>
              <span>{item.emoji}</span>
              <span>{item.name}</span>
            </SidebarMenuButton>

            <DropdownMenuTrigger>
              <SidebarMenuAction showOnHover className="aria-expanded:bg-muted">
                <MoreHorizontalIcon
                />
                <span className="sr-only">More</span>
              </SidebarMenuAction>
              <DropdownMenu
                className="w-56 rounded-lg"
                placement={isMobile ? "bottom end" : "right top"}
              >
                <DropdownMenuItem>
                  <StarOffIcon className="text-muted-foreground" />
                  <span>Remove from Favorites</span>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem>
                  <LinkIcon className="text-muted-foreground" />
                  <span>Copy Link</span>
                </DropdownMenuItem>
                <DropdownMenuItem>
                  <ArrowUpRightIcon className="text-muted-foreground" />
                  <span>Open in New Tab</span>
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem>
                  <Trash2Icon className="text-muted-foreground" />
                  <span>Delete</span>
                </DropdownMenuItem>
              </DropdownMenu>
            </DropdownMenuTrigger>
          </SidebarMenuItem>
        ))}
        <SidebarMenuItem>
          <SidebarMenuButton className="text-sidebar-foreground/70">
            <MoreHorizontalIcon
            />
            <span>More</span>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarGroup>
  )
}

