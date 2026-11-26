import * as React from "react"
import type { Selection } from "react-aria-components"

import {
  Example,
  ExampleWrapper,
} from "./example"
import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import {
  DropdownMenu,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { UserIcon, CreditCardIcon, SettingsIcon, LogOutIcon, LayoutIcon, ActivityIcon, PanelLeftIcon, ArrowUpIcon, ArrowDownIcon, ArrowRightIcon, MailIcon, MessageSquareIcon, BellIcon, WalletIcon, Building2Icon, PencilIcon, ShareIcon, ArchiveIcon, TrashIcon, BadgeCheckIcon, ChevronsUpDownIcon, CopyIcon, ScissorsIcon, ClipboardPasteIcon, UsersIcon, PlusCircleIcon, HelpCircleIcon } from "lucide-react"

export default function DropdownMenuExample() {
  return (
    <ExampleWrapper>
      <DropdownMenuBasic />
      <DropdownMenuComplex />
      <DropdownMenuSides />
      <DropdownMenuWithIcons />
      <DropdownMenuWithShortcuts />
      <DropdownMenuWithSubmenu />
      <DropdownMenuWithCheckboxes />
      <DropdownMenuWithCheckboxesIcons />
      <DropdownMenuWithRadio />
      <DropdownMenuWithRadioIcons />
      <DropdownMenuWithDestructive />
      <DropdownMenuWithAvatar />
      <DropdownMenuInDialog />
      <DropdownMenuWithInset />
    </ExampleWrapper>
  )
}

function DropdownMenuBasic() {
  return (
    <Example title="Basic">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Open
        </Button>
        <DropdownMenu>
          <DropdownMenuGroup>
            <DropdownMenuLabel>My Account</DropdownMenuLabel>
            <DropdownMenuItem>Profile</DropdownMenuItem>
            <DropdownMenuItem>Billing</DropdownMenuItem>
            <DropdownMenuItem>Settings</DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>GitHub</DropdownMenuItem>
          <DropdownMenuItem>Support</DropdownMenuItem>
          <DropdownMenuItem isDisabled>API</DropdownMenuItem>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuSides() {
  return (
    <Example title="Sides" containerClassName="col-span-2">
      <div className="flex flex-wrap justify-center gap-2">
        {(
          [
            { label: "start", placement: "start top" },
            { label: "left", placement: "left top" },
            { label: "top", placement: "top start" },
            { label: "bottom", placement: "bottom start" },
            { label: "right", placement: "right top" },
            { label: "end", placement: "end top" },
          ] as const
        ).map(({ label, placement }) => (
          <DropdownMenuTrigger key={placement}>
            <Button variant="outline" className="w-fit capitalize">
              {label}
            </Button>
            <DropdownMenu placement={placement}>
              <DropdownMenuGroup>
                <DropdownMenuItem>Profile</DropdownMenuItem>
                <DropdownMenuItem>Billing</DropdownMenuItem>
                <DropdownMenuItem>Settings</DropdownMenuItem>
              </DropdownMenuGroup>
            </DropdownMenu>
          </DropdownMenuTrigger>
        ))}
      </div>
    </Example>
  )
}

function DropdownMenuWithIcons() {
  return (
    <Example title="With Icons">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Open
        </Button>
        <DropdownMenu>
          <DropdownMenuItem>
            <UserIcon
            />
            Profile
          </DropdownMenuItem>
          <DropdownMenuItem>
            <CreditCardIcon
            />
            Billing
          </DropdownMenuItem>
          <DropdownMenuItem>
            <SettingsIcon
            />
            Settings
          </DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem variant="destructive">
            <LogOutIcon
            />
            Log out
          </DropdownMenuItem>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithShortcuts() {
  return (
    <Example title="With Shortcuts">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Open
        </Button>
        <DropdownMenu>
          <DropdownMenuGroup>
            <DropdownMenuLabel>My Account</DropdownMenuLabel>
            <DropdownMenuItem>
              Profile
              <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              Billing
              <DropdownMenuShortcut>⌘B</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              Settings
              <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              Keyboard shortcuts
              <DropdownMenuShortcut>⌘K</DropdownMenuShortcut>
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            Log out
            <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
          </DropdownMenuItem>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithSubmenu() {
  return (
    <Example title="With Submenu">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Open
        </Button>
        <DropdownMenu>
          <DropdownMenuGroup>
            <DropdownMenuItem>Team</DropdownMenuItem>
            <DropdownMenuSub>
              <DropdownMenuSubTrigger>Invite users</DropdownMenuSubTrigger>

              <DropdownMenuSubContent>
                <DropdownMenuItem>Email</DropdownMenuItem>
                <DropdownMenuItem>Message</DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem>More...</DropdownMenuItem>
              </DropdownMenuSubContent>
            </DropdownMenuSub>
            <DropdownMenuItem>
              New Team
              <DropdownMenuShortcut>⌘+T</DropdownMenuShortcut>
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithCheckboxes() {
  const [selectedKeys, setSelectedKeys] = React.useState<Selection>(
    new Set(["status-bar"])
  )

  return (
    <Example title="With Checkboxes">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Checkboxes
        </Button>
        <DropdownMenu className="min-w-40">
          <DropdownMenuGroup
            selectionMode="multiple"
            selectedKeys={selectedKeys}
            onSelectionChange={setSelectedKeys}
          >
            <DropdownMenuLabel>Appearance</DropdownMenuLabel>
            <DropdownMenuItem id="status-bar">
              <LayoutIcon
              />
              Status Bar
            </DropdownMenuItem>
            <DropdownMenuItem id="activity-bar" isDisabled>
              <ActivityIcon
              />
              Activity Bar
            </DropdownMenuItem>
            <DropdownMenuItem id="panel">
              <PanelLeftIcon
              />
              Panel
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithRadio() {
  const [position, setPosition] = React.useState("bottom")

  return (
    <Example title="With Radio Group">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Radio Group
        </Button>
        <DropdownMenu>
          <DropdownMenuGroup
            selectionMode="single"
            selectedKeys={[position]}
            onSelectionChange={(keys) =>
              setPosition(
                keys === "all"
                  ? "bottom"
                  : (keys.values().next().value as string)
              )
            }
          >
            <DropdownMenuLabel>Panel Position</DropdownMenuLabel>
            <DropdownMenuItem id="top">
              <ArrowUpIcon
              />
              Top
            </DropdownMenuItem>
            <DropdownMenuItem id="bottom">
              <ArrowDownIcon
              />
              Bottom
            </DropdownMenuItem>
            <DropdownMenuItem id="right" isDisabled>
              <ArrowRightIcon
              />
              Right
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithCheckboxesIcons() {
  const [selectedKeys, setSelectedKeys] = React.useState<Selection>(
    new Set(["email", "push"])
  )

  return (
    <Example title="Checkboxes with Icons">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Notifications
        </Button>
        <DropdownMenu className="min-w-56">
          <DropdownMenuGroup
            selectionMode="multiple"
            selectedKeys={selectedKeys}
            onSelectionChange={setSelectedKeys}
          >
            <DropdownMenuLabel>Notification Preferences</DropdownMenuLabel>
            <DropdownMenuItem id="email">
              <MailIcon
              />
              Email notifications
            </DropdownMenuItem>
            <DropdownMenuItem id="sms">
              <MessageSquareIcon
              />
              SMS notifications
            </DropdownMenuItem>
            <DropdownMenuItem id="push">
              <BellIcon
              />
              Push notifications
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithRadioIcons() {
  const [paymentMethod, setPaymentMethod] = React.useState("card")

  return (
    <Example title="Radio with Icons">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Payment Method
        </Button>
        <DropdownMenu className="min-w-56">
          <DropdownMenuGroup
            selectionMode="single"
            selectedKeys={[paymentMethod]}
            onSelectionChange={(keys) =>
              setPaymentMethod(
                keys === "all" ? "card" : (keys.values().next().value as string)
              )
            }
          >
            <DropdownMenuLabel>Select Payment Method</DropdownMenuLabel>
            <DropdownMenuItem id="card">
              <CreditCardIcon
              />
              Credit Card
            </DropdownMenuItem>
            <DropdownMenuItem id="paypal">
              <WalletIcon
              />
              PayPal
            </DropdownMenuItem>
            <DropdownMenuItem id="bank">
              <Building2Icon
              />
              Bank Transfer
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithDestructive() {
  return (
    <Example title="With Destructive Items">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Actions
        </Button>
        <DropdownMenu>
          <DropdownMenuItem>
            <PencilIcon
            />
            Edit
          </DropdownMenuItem>
          <DropdownMenuItem>
            <ShareIcon
            />
            Share
          </DropdownMenuItem>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            <ArchiveIcon
            />
            Archive
          </DropdownMenuItem>
          <DropdownMenuItem variant="destructive">
            <TrashIcon
            />
            Delete
          </DropdownMenuItem>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuWithAvatar() {
  const menuContent = (
    <>
      <DropdownMenuGroup>
        <DropdownMenuItem>
          <BadgeCheckIcon
          />
          Account
        </DropdownMenuItem>
        <DropdownMenuItem>
          <CreditCardIcon
          />
          Billing
        </DropdownMenuItem>
        <DropdownMenuItem>
          <BellIcon
          />
          Notifications
        </DropdownMenuItem>
      </DropdownMenuGroup>
      <DropdownMenuSeparator />
      <DropdownMenuItem>
        <LogOutIcon
        />
        Sign Out
      </DropdownMenuItem>
    </>
  )

  return (
    <Example title="With Avatar">
      <div className="flex items-center justify-between gap-4">
        <DropdownMenuTrigger>
          <Button
            variant="outline"
            className="h-12 justify-start px-2 md:max-w-[200px] style-sera:font-normal style-sera:tracking-normal style-sera:normal-case"
          >
            <Avatar>
              <AvatarImage src="https://github.com/shadcn.png" alt="Shadcn" />
              <AvatarFallback className="rounded-lg">CN</AvatarFallback>
            </Avatar>
            <div className="grid flex-1 text-left text-sm leading-tight">
              <span className="truncate font-semibold">shadcn</span>
              <span className="truncate text-xs text-muted-foreground">
                shadcn@example.com
              </span>
            </div>
            <ChevronsUpDownIcon className="ml-auto text-muted-foreground" />
          </Button>
          <DropdownMenu className="w-(--anchor-width) min-w-56">
            {menuContent}
          </DropdownMenu>
        </DropdownMenuTrigger>

        <DropdownMenuTrigger>
          <Button variant="ghost" size="icon" className="rounded-full">
            <Avatar>
              <AvatarImage src="https://github.com/shadcn.png" alt="shadcn" />
              <AvatarFallback>LR</AvatarFallback>
            </Avatar>
          </Button>
          <DropdownMenu placement="top end">{menuContent}</DropdownMenu>
        </DropdownMenuTrigger>
      </div>
    </Example>
  )
}

function DropdownMenuInDialog() {
  return (
    <Example title="In Dialog">
      <DialogTrigger>
        <Button variant="outline">Open Dialog</Button>
        <Dialog>
          <DialogHeader>
            <DialogTitle>Dropdown Menu Example</DialogTitle>
            <DialogDescription>
              Click the button below to see the dropdown menu.
            </DialogDescription>
          </DialogHeader>

          <DropdownMenuTrigger>
            <Button variant="outline" className="w-fit">
              Open Menu
            </Button>
            <DropdownMenu>
              <DropdownMenuItem>
                <CopyIcon
                />
                Copy
              </DropdownMenuItem>
              <DropdownMenuItem>
                <ScissorsIcon
                />
                Cut
              </DropdownMenuItem>
              <DropdownMenuItem>
                <ClipboardPasteIcon
                />
                Paste
              </DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuSub>
                <DropdownMenuSubTrigger>More Options</DropdownMenuSubTrigger>

                <DropdownMenuSubContent>
                  <DropdownMenuItem>Save Page...</DropdownMenuItem>
                  <DropdownMenuItem>Create Shortcut...</DropdownMenuItem>
                  <DropdownMenuItem>Name Window...</DropdownMenuItem>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem>Developer Tools</DropdownMenuItem>
                </DropdownMenuSubContent>
              </DropdownMenuSub>
              <DropdownMenuSeparator />
              <DropdownMenuItem variant="destructive">
                <TrashIcon
                />
                Delete
              </DropdownMenuItem>
            </DropdownMenu>
          </DropdownMenuTrigger>
        </Dialog>
      </DialogTrigger>
    </Example>
  )
}

function DropdownMenuWithInset() {
  const [selectedKeys, setSelectedKeys] = React.useState<Selection>(
    new Set(["bookmarks"])
  )
  const [theme, setTheme] = React.useState("system")

  return (
    <Example title="With Inset">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Open
        </Button>
        <DropdownMenu className="w-44">
          <DropdownMenuGroup>
            <DropdownMenuLabel>Actions</DropdownMenuLabel>
            <DropdownMenuItem>
              <CopyIcon
              />
              Copy
            </DropdownMenuItem>
            <DropdownMenuItem>
              <ScissorsIcon
              />
              Cut
            </DropdownMenuItem>
            <DropdownMenuItem inset>Paste</DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup
            selectionMode="multiple"
            selectedKeys={selectedKeys}
            onSelectionChange={setSelectedKeys}
          >
            <DropdownMenuLabel inset>Appearance</DropdownMenuLabel>
            <DropdownMenuItem inset id="bookmarks">
              Bookmarks
            </DropdownMenuItem>
            <DropdownMenuItem inset id="urls">
              Full URLs
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup
            selectionMode="single"
            selectedKeys={[theme]}
            onSelectionChange={(keys) =>
              setTheme(
                keys === "all"
                  ? "system"
                  : (keys.values().next().value as string)
              )
            }
          >
            <DropdownMenuLabel inset>Theme</DropdownMenuLabel>
            <DropdownMenuItem inset id="light">
              Light
            </DropdownMenuItem>
            <DropdownMenuItem inset id="dark">
              Dark
            </DropdownMenuItem>
            <DropdownMenuItem inset id="system">
              System
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuSub>
            <DropdownMenuSubTrigger inset>More Options</DropdownMenuSubTrigger>

            <DropdownMenuSubContent>
              <DropdownMenuGroup>
                <DropdownMenuItem>Save Page...</DropdownMenuItem>
                <DropdownMenuItem>Create Shortcut...</DropdownMenuItem>
              </DropdownMenuGroup>
            </DropdownMenuSubContent>
          </DropdownMenuSub>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

function DropdownMenuComplex() {
  const [selectedKeys, setSelectedKeys] = React.useState<Selection>(
    new Set(["sidebar"])
  )

  return (
    <Example title="Complex">
      <DropdownMenuTrigger>
        <Button variant="outline" className="w-fit">
          Complex Menu
        </Button>
        <DropdownMenu className="w-56">
          <DropdownMenuGroup>
            <DropdownMenuLabel>My Account</DropdownMenuLabel>
            <DropdownMenuItem>
              <UserIcon
              />
              Profile
              <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <CreditCardIcon
              />
              Billing
              <DropdownMenuShortcut>⌘B</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <SettingsIcon
              />
              Settings
              <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup
            selectionMode="multiple"
            selectedKeys={selectedKeys}
            onSelectionChange={setSelectedKeys}
          >
            <DropdownMenuLabel>View</DropdownMenuLabel>
            <DropdownMenuItem id="sidebar">
              <PanelLeftIcon
              />
              Sidebar
            </DropdownMenuItem>
            <DropdownMenuItem id="status-bar">
              <LayoutIcon
              />
              Status Bar
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuSub>
              <DropdownMenuSubTrigger>
                <UsersIcon
                />
                Invite Users
              </DropdownMenuSubTrigger>

              <DropdownMenuSubContent>
                <DropdownMenuGroup>
                  <DropdownMenuItem>
                    <MailIcon
                    />
                    Email
                  </DropdownMenuItem>
                  <DropdownMenuItem>
                    <MessageSquareIcon
                    />
                    Message
                  </DropdownMenuItem>
                </DropdownMenuGroup>
                <DropdownMenuSeparator />
                <DropdownMenuGroup>
                  <DropdownMenuItem>
                    <PlusCircleIcon
                    />
                    More...
                  </DropdownMenuItem>
                </DropdownMenuGroup>
              </DropdownMenuSubContent>
            </DropdownMenuSub>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <HelpCircleIcon
              />
              Support
            </DropdownMenuItem>
            <DropdownMenuItem variant="destructive">
              <LogOutIcon
              />
              Sign Out
              <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
            </DropdownMenuItem>
          </DropdownMenuGroup>
        </DropdownMenu>
      </DropdownMenuTrigger>
    </Example>
  )
}

