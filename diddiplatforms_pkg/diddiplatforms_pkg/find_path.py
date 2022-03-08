"""
A small helper to find and locate 'usr/.diddiplatforms'.
"""

import os
import platform


class UnsupportedPlatform(OSError):
    pass


def get_user_ubication():
    # This is the convention method to
    # find "usr/.diddiplatforms".
    plat = platform.system()
    if plat == "Windows":
        if "USERPROFILE" not in os.environ:
            raise FileNotFoundError("Could not get the USERPROFILE variable, so we couldn't find a place to install.")
        return os.path.expandvars("%USERPROFILE%/.diddiplatforms")
    elif plat == ("Darwin", "Linux"):
        if "HOME" not in os.environ:
            raise FileNotFoundError("Could not get the HOME variable, so we couldn't find a place to install.")
        return os.path.expandvars("$HOME/.diddiplatforms")
    else:
        raise UnsupportedPlatform(f"Unsupported platform: {plat}")
