from settings_dialog import SettingsDialog


def Page():
    return t"""
        <div class="flex h-svh items-center justify-center">
            <{SettingsDialog} />
        </div>
    """
