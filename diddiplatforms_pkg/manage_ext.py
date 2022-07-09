"""
Find and manage the extensions.
"""

import os
import shutil

from . import utils


def install_extension(file, no_pyxapp=False):
    dest = os.path.join(utils.get_user_ubication(), "levels")
    if no_pyxapp:
        if not file.endswith(".py"):
            raise ValueError(
                f"Expected a single Python file, but the given file ('{file}') does not look like one."
            )
        shutil.copy2(file, os.path.join(dest, file[len(os.path.dirname(file)) :]))
    else:
        if not file.endswith(".pyxapp"):
            raise ValueError(
                f"Expected a Pyxel packaged app, but the file name ('{file}') does not look like one."
            )
        shutil.copy2(file, os.path.join(dest, file[len(os.path.dirname(file)) :]))
