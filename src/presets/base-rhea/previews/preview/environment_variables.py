from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle


def EnvironmentVariables():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Environment Variables</{CardTitle}>
                <{CardDescription}>Production · 8 variables</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-2">
                {[t'''
                    <div
                        key={env["key"]}
                        class="flex items-center gap-2 rounded-md px-2.5 py-2 font-mono text-xs ring ring-border"
                    >
                        <span class="font-medium">{env["key"]}</span>
                        <span class="ml-auto text-muted-foreground">
                            {"••••••••" if env["masked"] else "https://api.example.com"}
                        </span>
                    </div>
                ''' for env in [{
                    "key": "DATABASE_URL",
                    "masked": True,
                }, {
                    "key": "NEXT_PUBLIC_API",
                    "masked": False,
                }, {
                    "key": "STRIPE_SECRET",
                    "masked": True,
                }]]}
            </{CardContent}>
            <{CardFooter}>
                <{Button} variant="outline">Edit</{Button}>
                <{Button} class="ml-auto">Deploy</{Button}>
            </{CardFooter}>
        </{Card}>
    """
