from button import Button
from card import Card, CardContent, CardFooter
from field import Field, FieldGroup, FieldLabel
from native_select import NativeSelect, NativeSelectOption
from textarea import Textarea


def FeedbackForm():
    return t"""
        <{Card}>
            <{CardContent}>
                <form id="feedback-form">
                    <{FieldGroup}>
                        <{Field}>
                            <{FieldLabel} for="topic">Topic</{FieldLabel}>
                            <{NativeSelect} id="topic">
                                <{NativeSelectOption} value="">Select a topic</{NativeSelectOption}>
                                <{NativeSelectOption} value="ai">AI</{NativeSelectOption}>
                                <{NativeSelectOption} value="accounts-and-access-controls">
                                    Accounts and Access Controls
                                </{NativeSelectOption}>
                                <{NativeSelectOption} value="billing">Billing</{NativeSelectOption}>
                                <{NativeSelectOption} value="cdn">CDN (Firewall, Caching)</{NativeSelectOption}>
                                <{NativeSelectOption} value="ci-cd">
                                    CI/CD (Builds, Deployments, Environment Variables)
                                </{NativeSelectOption}>
                                <{NativeSelectOption} value="dashboard-interface">
                                    Dashboard Interface (Navigation, UI Issues)
                                </{NativeSelectOption}>
                                <{NativeSelectOption} value="domains">Domains</{NativeSelectOption}>
                                <{NativeSelectOption} value="frameworks">Frameworks</{NativeSelectOption}>
                                <{NativeSelectOption} value="marketplace-and-integrations">
                                    Marketplace and Integrations
                                </{NativeSelectOption}>
                                <{NativeSelectOption} value="observability">
                                    Observability (Observability, Logs, Monitoring)
                                </{NativeSelectOption}>
                                <{NativeSelectOption} value="storage">Storage</{NativeSelectOption}>
                            </{NativeSelect}>
                        </{Field}>
                        <{Field}>
                            <{FieldLabel} for="feedback">Feedback</{FieldLabel}>
                            <{Textarea} id="feedback" placeholder="Your feedback helps us improve..." />
                        </{Field}>
                    </{FieldGroup}>
                </form>
            </{CardContent}>
            <{CardFooter}>
                <{Button} type="submit" form="feedback-form" class="style-sera:w-full">Submit</{Button}>
            </{CardFooter}>
        </{Card}>
    """
