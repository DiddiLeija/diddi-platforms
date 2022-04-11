"""
Handy script to install the 'Diddi Platforms'
into 'usr/.diddiplatforms'. The current user
is used to install the game.
"""

import sys

if sys.version_info < (3, 7):
    sys.exit(f"Unsupported Python: {sys.version}")

import os

try:
    from diddiplatforms_pkg.find_path import get_user_ubication
except ImportError:
    sys.exit("Please get the 'diddiplatforms_pkg' package to continue")


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
    os.makedirs(os.path.join(dest_path, "levels"), exist_ok=True)
except Exception as exc:
    sys.exit(f"Error while installing: {type(exc).__name__}: {str(exc)}")

print("All done!")
