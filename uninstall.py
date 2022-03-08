"""
Handy script for reverting the install
script. It only verifies that the installation
exists, and tries to remove it.
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
                sys.exit("Could not get the USERPROFILE variable, so we couldn't find a place to install.")
            return os.path.expandvars("%USERPROFILE%/.diddiplatforms")
        elif plat == ("Darwin", "Linux"):
            if "HOME" not in os.environ:
                sys.exit("Could not get the HOME variable, so we couldn't find a place to install.")
            return os.path.expandvars("$HOME/.diddiplatforms")
        else:
            sys.exit(f"Unsupported platform: {plat}")

print("Looking for the destination path...")
dest_path = get_user_ubication()

if not os.path.exists(dest_path):
    print(f"Destination path {dest_path} does not exist. Aborting...")
    sys.exit(0)

if input(f"Do you want to remove: {dest_path}? (y/n) ") not in ("y", "yes", "ye", "yeah"):
    print("Aborting...")
    sys.exit(0)

try:
    print("Removing...")
    shutil.rmtree(dest_path)
except Exception as exc:
    sys.exit(f"Error while installing: {type(exc).__name__}: {str(exc)}")

print("All done!")
