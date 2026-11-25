from label import Label
from sidebar import SidebarInput

__js__ = {"lucide-react": ["SearchIcon"]}


def SearchForm(**props):
    return t"""
        <form ...{props}>
            <div class="relative">
                <{Label} for="search" class="sr-only">Search</{Label}>
                <{SidebarInput} id="search" placeholder="Type to search..." class="h-8 pl-7" />
                <{SearchIcon} class="pointer-events-none absolute top-1/2 left-2 size-4 -translate-y-1/2 opacity-50 select-none" />
            </div>
        </form>
    """
