from button import Button
from card import Card, CardContent, CardFooter, CardHeader, CardTitle
from field import Field, FieldGroup, FieldLabel
from input_group import InputGroup, InputGroupAddon, InputGroupInput

__js__ = {"lucide-react": ["CameraIcon", "CirclePlusIcon", "CloudIcon", "GlobeIcon"]}


def SocialLinks():
    return t"""
        <{Card}>
            <{CardHeader}>
                <{CardTitle}>Social Links</{CardTitle}>
            </{CardHeader}>
            <{CardContent}>
                <{FieldGroup}>
                    <{Field}>
                        <{FieldLabel} for="spotify-url">Spotify Artist URL</{FieldLabel}>
                        <{InputGroup}>
                            <{InputGroupAddon}>
                                <{CirclePlusIcon} />
                            </{InputGroupAddon}>
                            <{InputGroupInput} id="spotify-url" defaultValue="spotify.com/artist/3j...2k" />
                        </{InputGroup}>
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="instagram-handle">Instagram Handle</{FieldLabel}>
                        <{InputGroup}>
                            <{InputGroupAddon}>
                                <{CameraIcon} />
                            </{InputGroupAddon}>
                            <{InputGroupInput} id="instagram-handle" defaultValue="@julianduryea_music" />
                        </{InputGroup}>
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="soundcloud-url">SoundCloud URL</{FieldLabel}>
                        <{InputGroup}>
                            <{InputGroupAddon}>
                                <{CloudIcon} />
                            </{InputGroupAddon}>
                            <{InputGroupInput} id="soundcloud-url" placeholder="soundcloud.com/username" />
                        </{InputGroup}>
                    </{Field}>
                    <{Field}>
                        <{FieldLabel} for="website-url">Website</{FieldLabel}>
                        <{InputGroup}>
                            <{InputGroupAddon}>
                                <{GlobeIcon} />
                            </{InputGroupAddon}>
                            <{InputGroupInput} id="website-url" placeholder="https://yoursite.com" />
                        </{InputGroup}>
                    </{Field}>
                </{FieldGroup}>
            </{CardContent}>
            <{CardFooter} class="justify-end gap-2 style-sera:justify-center">
                <{Button} variant="secondary" class="style-sera:flex-1">Discard</{Button}>
                <{Button} class="style-sera:flex-1">Save Changes</{Button}>
            </{CardFooter}>
        </{Card}>
    """
