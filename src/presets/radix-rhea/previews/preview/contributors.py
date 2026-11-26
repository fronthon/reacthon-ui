from avatar import Avatar, AvatarFallback, AvatarImage
from badge import Badge
from card import Card, CardContent, CardFooter, CardHeader, CardTitle

usernames = [
    "shadcn",
    "vercel",
    "nextjs",
    "tailwindlabs",
    "typescript-lang",
    "eslint",
    "prettier",
    "babel",
    "webpack",
    "rollup",
    "parcel",
    "vite",
    "react",
    "vue",
    "angular",
    "solid",
]


def Contributors():
    return t"""
        <{Card} class="max-w-sm">
            <{CardHeader}>
                <{CardTitle}>
                    Contributors <{Badge} variant="secondary">312</{Badge}>
                </{CardTitle}>
            </{CardHeader}>
            <{CardContent}>
                <div class="flex flex-wrap gap-2">
                    {[t'''
                        <{Avatar} key={username} class="grayscale">
                            <{AvatarImage} src={f"https://github.com/{username}.png"} alt={username} />
                            <{AvatarFallback}>{username[:1]}</{AvatarFallback}>
                        </{Avatar}>
                    ''' for username in usernames]}
                </div>
            </{CardContent}>
            <{CardFooter}>
                <a href="#" class="text-sm underline underline-offset-4">+ 810 contributors</a>
            </{CardFooter}>
        </{Card}>
    """
