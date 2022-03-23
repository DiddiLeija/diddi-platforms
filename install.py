"""
Handy script to install the 'Diddi Platforms'
into 'usr/.diddiplatforms'. The current user
is used to install the game.
"""

import sys

if sys.version_info < (3, 7):
    sys.exit(f"Unsupported Python: {sys.version}")

import os
import platform
import shutil

try:
    from diddiplatforms_pkg.find_path import get_user_ubication
except ImportError:

    def get_user_ubication():
        plat = platform.system()
        if plat == "Windows":
            if "USERPROFILE" not in os.environ:
                sys.exit(
                    "Could not get the USERPROFILE variable, so we couldn't find a place to install."
                )
            return os.path.expandvars("%USERPROFILE%/.diddiplatforms")
        elif plat == ("Darwin", "Linux"):
            if "HOME" not in os.environ:
                sys.exit(
                    "Could not get the HOME variable, so we couldn't find a place to install."
                )
            return os.path.expandvars("$HOME/.diddiplatforms")
        else:
            sys.exit(f"Unsupported platform: {plat}")


print("Looking for the destination path...")
dest_path = get_user_ubication()

if not os.path.exists(dest_path):
    print(
        f"Destination path {dest_path} doesn't seem to exist. It will be created in a moment."
    )
else:
    print(
        f"Destination path {dest_path} already exists. If you want to re-install, "
        "please run the uninstall script first. Aborting..."
    )
    sys.exit(0)

try:
    print("Copying the contents...")
    shutil.copytree("./diddiplatforms", dest_path)
except Exception as exc:
    sys.exit(f"Error while installing: {type(exc).__name__}: {str(exc)}")

print("All done!")
