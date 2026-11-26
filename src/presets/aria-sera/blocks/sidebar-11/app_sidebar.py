from collapsible import Collapsible, CollapsibleContent
from sidebar import (
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarGroupLabel,
    SidebarMenu,
    SidebarMenuBadge,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarMenuSub,
    SidebarRail,
)

__js__ = {"lucide-react": ["FileIcon", "ChevronRightIcon", "FolderIcon"]}

data = {
    "changes": [
        {"file": "README.md", "state": "M"},
        {"file": "api/hello/route.ts", "state": "U"},
        {"file": "app/layout.tsx", "state": "M"},
    ],
    "tree": [
        ["app", ["api", ["hello", ["route.ts"]], "page.tsx", "layout.tsx", ["blog", ["page.tsx"]]]],
        ["components", ["ui", "button.tsx", "card.tsx"], "header.tsx", "footer.tsx"],
        ["lib", ["util.ts"]],
        ["public", "favicon.ico", "vercel.svg"],
        ".eslintrc.json",
        ".gitignore",
        "next.config.js",
        "tailwind.config.js",
        "package.json",
        "README.md",
    ],
}


def AppSidebar(**props):
    return t"""
        <{Sidebar} ...{props}>
            <{SidebarContent}>
                <{SidebarGroup}>
                    <{SidebarGroupLabel}>Changes</{SidebarGroupLabel}>
                    <{SidebarGroupContent}>
                        <{SidebarMenu}>
                            {[t'''
                                <{SidebarMenuItem} key={index}>
                                    <{SidebarMenuButton}>
                                        <{FileIcon} />
                                        {item["file"]}
                                    </{SidebarMenuButton}>
                                    <{SidebarMenuBadge}>{item["state"]}</{SidebarMenuBadge}>
                                </{SidebarMenuItem}>
                            ''' for index, item in enumerate(data["changes"])]}
                        </{SidebarMenu}>
                    </{SidebarGroupContent}>
                </{SidebarGroup}>
                <{SidebarGroup}>
                    <{SidebarGroupLabel}>Files</{SidebarGroupLabel}>
                    <{SidebarGroupContent}>
                        <{SidebarMenu}>
                            {[t'<{Tree} key={index} item={item} />' for index, item in enumerate(data["tree"])]}
                        </{SidebarMenu}>
                    </{SidebarGroupContent}>
                </{SidebarGroup}>
            </{SidebarContent}>
            <{SidebarRail} />
        </{Sidebar}>
    """


def Tree(item=None, **_):
    name, *items = item if isinstance(item, list) else [item]
    if not items:
        return t"""
            <{SidebarMenuButton} isActive={name == "button.tsx"} class="data-[active=true]:bg-transparent">
                <{FileIcon} />
                {name}
            </{SidebarMenuButton}>
        """
    return t"""
        <{SidebarMenuItem}>
            <{Collapsible}
                class="group/collapsible [&[data-expanded]>button>svg:first-child]:rotate-90"
                defaultExpanded={name == "components" or name == "ui"}
            >
                <{SidebarMenuButton} slot="trigger">
                    <{ChevronRightIcon} class="transition-transform" />
                    <{FolderIcon} />
                    {name}
                </{SidebarMenuButton}>
                <{CollapsibleContent}>
                    <{SidebarMenuSub}>
                        {[t'<{Tree} key={index} item={sub_item} />' for index, sub_item in enumerate(items)]}
                    </{SidebarMenuSub}>
                </{CollapsibleContent}>
            </{Collapsible}>
        </{SidebarMenuItem}>
    """
