"""
Handy script for reverting the install
script. It only verifies that the installation
exists, and tries to remove it.
"""

import sys

if sys.version_info < (3, 7):
    sys.exit(f"Unsupported Python: {sys.version}")

import os
import shutil

try:
    from diddiplatforms_pkg.find_path import get_user_ubication
except ImportError:
    sys.exit("Please get the 'diddiplatforms_pkg' package to continue")


print("Looking for the destination path...")
dest_path = get_user_ubication()

if not os.path.exists(dest_path):
    print(f"Destination path {dest_path} does not exist. Aborting...")
    sys.exit(0)

if input(f"Do you want to remove: {dest_path}? (y/n) ") not in (
    "y",
    "yes",
    "ye",
    "yeah",
):
    print("Aborting...")
    sys.exit(0)

try:
    print("Removing...")
    shutil.rmtree(dest_path)
except Exception as exc:
    sys.exit(f"Error while installing: {type(exc).__name__}: {str(exc)}")

print("All done!")
