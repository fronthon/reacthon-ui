from accordion import Accordion, AccordionContent, AccordionItem, AccordionTrigger
from button import Button
from card import Card, CardContent, CardFooter
from tabs import Tabs, TabsContent, TabsList, TabsTrigger

GENERAL_QUESTIONS = [
    {
        "q": "How secure is my financial data with Ledger?",
        "a": "We use bank-level AES-256 encryption, SOC 2 Type II certified infrastructure, and never store your credentials. All connections use read-only access tokens. We are a SEC registered investment advisor.",
    },
    {
        "q": "How do I connect my bank or investment accounts?",
        "a": "Go to Settings > Linked Accounts and search for your institution. We support over 12,000 banks and brokerages via Plaid and MX.",
    },
    {
        "q": "Can I export my data for tax purposes?",
        "a": "Yes. Navigate to Reports > Tax Export to download a CSV or PDF summary of your transactions, dividends, and capital gains for any tax year.",
    },
]

BILLING_QUESTIONS = [
    {
        "q": "What is the difference between Basic and Pro pricing tiers?",
        "a": "Basic includes budgeting, goal tracking, and up to 3 linked accounts. Pro adds unlimited accounts, dividend tracking, portfolio analysis, and priority support.",
    },
    {
        "q": "How do I cancel my subscription?",
        "a": "Go to Settings > Billing > Manage Plan and click Cancel. Your access continues until the end of your current billing period.",
    },
    {
        "q": "Do you offer a free trial?",
        "a": "Yes. All new accounts start with a 14-day Pro trial. No credit card required.",
    },
]

GOALS_QUESTIONS = [
    {
        "q": "How do I set up a custom financial goal?",
        "a": "Click New Goal from the Savings Targets card. Choose a category, set a target amount and date, and we'll calculate the monthly contribution needed.",
    },
    {
        "q": "Can I track multiple goals at once?",
        "a": "Yes. Pro accounts can track unlimited goals. Basic accounts support up to 3 active goals.",
    },
    {
        "q": "How are monthly contributions calculated?",
        "a": "We divide the remaining amount by the number of months until your target date, adjusted for your current savings rate and any auto-transfer schedules.",
    },
]


def QuestionList(questions=None, **_):
    return t"""
        <{Accordion}>
            {[t'''
                <{AccordionItem} key={index} id={f"question-{index}"}>
                    <{AccordionTrigger}>{item["q"]}</{AccordionTrigger}>
                    <{AccordionContent}>{item["a"]}</{AccordionContent}>
                </{AccordionItem}>
            ''' for index, item in enumerate(questions)]}
        </{Accordion}>
    """


def Faq():
    return t"""
        <{Card}>
            <{CardContent}>
                <{Tabs} defaultSelectedKey="general">
                    <{TabsList} class="w-full">
                        <{TabsTrigger} id="general" class="flex-1">General</{TabsTrigger}>
                        <{TabsTrigger} id="billing" class="flex-1">Billing</{TabsTrigger}>
                        <{TabsTrigger} id="goals" class="flex-1">Goals</{TabsTrigger}>
                    </{TabsList}>
                    <{TabsContent} id="general">
                        <{QuestionList} questions={GENERAL_QUESTIONS} />
                    </{TabsContent}>
                    <{TabsContent} id="billing">
                        <{QuestionList} questions={BILLING_QUESTIONS} />
                    </{TabsContent}>
                    <{TabsContent} id="goals">
                        <{QuestionList} questions={GOALS_QUESTIONS} />
                    </{TabsContent}>
                </{Tabs}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} variant="outline" class="w-full">Contact Support</{Button}>
                <{Button} variant="link" class="w-full">Learn More</{Button}>
            </{CardFooter}>
        </{Card}>
    """
