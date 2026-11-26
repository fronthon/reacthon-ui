from reacthon import use_state
from example import Example, ExampleWrapper
from checkbox import Checkbox
from field import Field, FieldContent, FieldDescription, FieldGroup, FieldLabel, FieldTitle
from table import Table, TableBody, TableCell, TableHead, TableHeader, TableRow


def CheckboxExample():
    return t"""
        <{ExampleWrapper}>
            <{CheckboxBasic} />
            <{CheckboxWithDescription} />
            <{CheckboxInvalid} />
            <{CheckboxDisabled} />
            <{CheckboxWithTitle} />
            <{CheckboxInTable} />
            <{CheckboxGroup} />
        </{ExampleWrapper}>
    """


def CheckboxBasic():
    return t"""
        <{Example} title="Basic">
            <{Field} orientation="horizontal">
                <{Checkbox} id="terms" />
                <{FieldLabel} for="terms">Accept terms and conditions</{FieldLabel}>
            </{Field}>
        </{Example}>
    """


def CheckboxWithDescription():
    return t"""
        <{Example} title="With Description">
            <{Field} orientation="horizontal">
                <{Checkbox} id="terms-2" defaultChecked />
                <{FieldContent}>
                    <{FieldLabel} for="terms-2">Accept terms and conditions</{FieldLabel}>
                    <{FieldDescription}>
                        By clicking this checkbox, you agree to the terms and conditions.
                    </{FieldDescription}>
                </{FieldContent}>
            </{Field}>
        </{Example}>
    """


def CheckboxInvalid():
    return t"""
        <{Example} title="Invalid">
            <{Field} orientation="horizontal" data-invalid>
                <{Checkbox} id="terms-3" aria-invalid />
                <{FieldLabel} for="terms-3">Accept terms and conditions</{FieldLabel}>
            </{Field}>
        </{Example}>
    """


def CheckboxDisabled():
    return t"""
        <{Example} title="Disabled">
            <{Field} orientation="horizontal">
                <{Checkbox} id="toggle" disabled />
                <{FieldLabel} for="toggle">Enable notifications</{FieldLabel}>
            </{Field}>
        </{Example}>
    """


def CheckboxWithTitle():
    return t"""
        <{Example} title="With Title">
            <{FieldGroup}>
                <{FieldLabel} for="toggle-2">
                    <{Field} orientation="horizontal">
                        <{Checkbox} id="toggle-2" defaultChecked />
                        <{FieldContent}>
                            <{FieldTitle}>Enable notifications</{FieldTitle}>
                            <{FieldDescription}>
                                You can enable or disable notifications at any time.
                            </{FieldDescription}>
                        </{FieldContent}>
                    </{Field}>
                </{FieldLabel}>
                <{FieldLabel} for="toggle-4">
                    <{Field} orientation="horizontal" data-disabled>
                        <{Checkbox} id="toggle-4" disabled />
                        <{FieldContent}>
                            <{FieldTitle}>Enable notifications</{FieldTitle}>
                            <{FieldDescription}>
                                You can enable or disable notifications at any time.
                            </{FieldDescription}>
                        </{FieldContent}>
                    </{Field}>
                </{FieldLabel}>
            </{FieldGroup}>
        </{Example}>
    """


table_data = [
    {"id": "1", "name": "Sarah Chen", "email": "sarah.chen@example.com", "role": "Admin"},
    {"id": "2", "name": "Marcus Rodriguez", "email": "marcus.rodriguez@example.com", "role": "User"},
    {"id": "3", "name": "Priya Patel", "email": "priya.patel@example.com", "role": "User"},
    {"id": "4", "name": "David Kim", "email": "david.kim@example.com", "role": "Editor"},
]


def CheckboxInTable():
    selected_rows, set_selected_rows = use_state(Set.new(["1"]))

    select_all = selected_rows.size == len(table_data)

    def handle_select_all(checked):
        if checked:
            set_selected_rows(Set.new([row["id"] for row in table_data]))
        else:
            set_selected_rows(Set.new())

    def handle_select_row(id_, checked):
        new_selected = Set.new(selected_rows)
        if checked:
            new_selected.add(id_)
        else:
            new_selected.delete(id_)
        set_selected_rows(new_selected)

    def render_row(row):
        return t"""
            <{TableRow} key={row["id"]} data-state={"selected" if selected_rows.has(row["id"]) else None}>
                <{TableCell}>
                    <{Checkbox}
                        id={f"row-{row["id"]}"}
                        checked={selected_rows.has(row["id"])}
                        onCheckedChange={(lambda checked: handle_select_row(row["id"], checked == True))}
                    />
                </{TableCell}>
                <{TableCell} class="font-medium">{row["name"]}</{TableCell}>
                <{TableCell}>{row["email"]}</{TableCell}>
                <{TableCell}>{row["role"]}</{TableCell}>
            </{TableRow}>
        """

    return t"""
        <{Example} title="In Table">
            <{Table}>
                <{TableHeader}>
                    <{TableRow}>
                        <{TableHead} class="w-8">
                            <{Checkbox} id="select-all" checked={select_all} onCheckedChange={handle_select_all} />
                        </{TableHead}>
                        <{TableHead}>Name</{TableHead}>
                        <{TableHead}>Email</{TableHead}>
                        <{TableHead}>Role</{TableHead}>
                    </{TableRow}>
                </{TableHeader}>
                <{TableBody}>{[render_row(row) for row in table_data]}</{TableBody}>
            </{Table}>
        </{Example}>
    """


def CheckboxGroup():
    return t"""
        <{Example} title="Group">
            <{Field}>
                <{FieldLabel}>Show these items on the desktop:</{FieldLabel}>
                <{Field} orientation="horizontal">
                    <{Checkbox} id="finder-pref-9k2-hard-disks-ljj" />
                    <{FieldLabel} for="finder-pref-9k2-hard-disks-ljj" class="font-normal">Hard disks</{FieldLabel}>
                </{Field}>
                <{Field} orientation="horizontal">
                    <{Checkbox} id="finder-pref-9k2-external-disks-1yg" />
                    <{FieldLabel} for="finder-pref-9k2-external-disks-1yg" class="font-normal">
                        External disks
                    </{FieldLabel}>
                </{Field}>
                <{Field} orientation="horizontal">
                    <{Checkbox} id="finder-pref-9k2-cds-dvds-fzt" />
                    <{FieldLabel} for="finder-pref-9k2-cds-dvds-fzt" class="font-normal">
                        CDs, DVDs, and iPods
                    </{FieldLabel}>
                </{Field}>
                <{Field} orientation="horizontal">
                    <{Checkbox} id="finder-pref-9k2-connected-servers-6l2" />
                    <{FieldLabel} for="finder-pref-9k2-connected-servers-6l2" class="font-normal">
                        Connected servers
                    </{FieldLabel}>
                </{Field}>
            </{Field}>
        </{Example}>
    """
