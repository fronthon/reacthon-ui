"use client"

import { PlusIcon } from "lucide-react"
import * as React from "react"

import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Combobox,
  ComboboxChip,
  ComboboxChipList,
  ComboboxChips,
  ComboboxChipsInput,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxItem,
  ComboboxList,
} from "@/components/ui/combobox"
import { Tooltip, TooltipTrigger } from "@/components/ui/tooltip"

// Users available for assignment.
const users = [
  "shadcn",
  "maxleiter",
  "evilrabbit",
  "pranathip",
  "jorgezreik",
  "shuding",
  "rauchg",
]

export function AssignIssue() {
  return (
    <Card className="w-full max-w-sm" size="sm">
      <CardHeader className="border-b">
        <CardTitle className="text-sm">Assign Issue</CardTitle>
        <CardDescription className="text-sm">
          Select users to assign to this issue.
        </CardDescription>
        <CardAction>
          <TooltipTrigger>
            <Button variant="outline" size="icon-xs">
              <PlusIcon
              />
            </Button>
            <Tooltip>Add user</Tooltip>
          </TooltipTrigger>
        </CardAction>
      </CardHeader>
      <CardContent>
        <Combobox
          selectionMode="multiple"
          defaultValue={[users[0]]}
          allowsEmptyCollection
        >
          <ComboboxChips>
            <ComboboxChipList<{ username: string }>>
              {(value: { username: string }) => (
                <ComboboxChip id={value.username}>
                  <Avatar className="size-4">
                    <AvatarImage
                      src={`https://github.com/${value.username}.png`}
                      alt={value.username}
                    />
                    <AvatarFallback>{value.username.charAt(0)}</AvatarFallback>
                  </Avatar>
                  {value.username}
                </ComboboxChip>
              )}
            </ComboboxChipList>
            <ComboboxChipsInput placeholder="Select a item..." />
          </ComboboxChips>
          <ComboboxContent>
            <ComboboxList
              renderEmptyState={() => (
                <ComboboxEmpty>No users found.</ComboboxEmpty>
              )}
            >
              {users.map((username) => (
                <ComboboxItem
                  key={username}
                  id={username}
                  value={{ username }}
                  textValue={username}
                >
                  <Avatar className="size-5">
                    <AvatarImage
                      src={`https://github.com/${username}.png`}
                      alt={username}
                    />
                    <AvatarFallback>{username.charAt(0)}</AvatarFallback>
                  </Avatar>
                  {username}
                </ComboboxItem>
              ))}
            </ComboboxList>
          </ComboboxContent>
        </Combobox>
      </CardContent>
    </Card>
  )
}
