"use client"

import * as React from "react"

import {
  DropdownMenu,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"
import { GalleryVerticalEndIcon, ChevronsUpDownIcon, CheckIcon } from "lucide-react"

export function VersionSwitcher({
  versions,
  defaultVersion,
}: {
  versions: string[]
  defaultVersion: string
}) {
  const [selectedVersion, setSelectedVersion] = React.useState(defaultVersion)
  return (
    <SidebarMenu>
      <SidebarMenuItem>
        <DropdownMenuTrigger>
          <SidebarMenuButton
            size="lg"
            className="aria-expanded:bg-sidebar-accent aria-expanded:text-sidebar-accent-foreground"
          >
            <div className="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
              <GalleryVerticalEndIcon className="size-4" />
            </div>
            <div className="flex flex-col gap-0.5 leading-none">
              <span className="font-medium">Documentation</span>
              <span className="">v{selectedVersion}</span>
            </div>
            <ChevronsUpDownIcon className="ml-auto" />
          </SidebarMenuButton>
          <DropdownMenu placement="bottom start">
            {versions.map((version) => (
              <DropdownMenuItem
                key={version}
                onAction={() => setSelectedVersion(version)}
              >
                v{version}{" "}
                {version === selectedVersion && (
                  <CheckIcon className="ml-auto" />
                )}
              </DropdownMenuItem>
            ))}
          </DropdownMenu>
        </DropdownMenuTrigger>
      </SidebarMenuItem>
    </SidebarMenu>
  )
}

