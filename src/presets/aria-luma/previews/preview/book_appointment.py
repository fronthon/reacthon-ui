from alert import Alert, AlertDescription, AlertTitle
from button import Button
from card import Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle
from field import Field, FieldGroup, FieldLabel
from toggle_group import ToggleGroup, ToggleGroupItem


def BookAppointment():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Book Appointment</{CardTitle}>
                <{CardDescription}>Dr. Sarah Chen · Cardiology</{CardDescription}>
            </{CardHeader}>
            <{CardContent} class="flex flex-col gap-4">
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel}>Available on March 18, 2026</{FieldLabel}>
                        <{ToggleGroup} spacing={2} defaultSelectedKeys={["slot-0"]}>
                            {[t'''
                                <{ToggleGroupItem}
                                    key={time}
                                    id={f"slot-{index}"}
                                >
                                    {time}
                                </{ToggleGroupItem}>
                            ''' for index, time in enumerate(["9:00 AM", "10:30 AM", "11:00 AM", "1:30 PM"])]}
                        </{ToggleGroup}>
                    </{Field}>
                </{FieldGroup}>
                <{Alert}>
                    <{AlertTitle}>New patient?</{AlertTitle}>
                    <{AlertDescription}>Please arrive 15 minutes early.</{AlertDescription}>
                </{Alert}>
            </{CardContent}>
            <{CardFooter}>
                <{Button} class="w-full">Book Appointment</{Button}>
            </{CardFooter}>
        </{Card}>
    """
