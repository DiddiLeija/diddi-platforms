"""
Find and manage the extensions.
"""

from . import find_path, utils

import os
import shutil
import zipfile


class DiscouragedMethod(Warning):
    pass


class UnexpectedFilename(Warning):
    pass


def install_extension(file, no_pyxapp=False):
    dest = os.path.join(find_path.get_user_ubication(), "levels")
    if no_pyxapp:
        utils.warn("Levels that are not packaged as Pyxel apps are discouraged when not in the standard levels.", DiscouragedMethod)
        if not file.endswith(".zip"):
            utils.warn(f"Expected zip files, but the file name ('{file}') does not look like one.", UnexpectedFilename)
        dest_file = zipfile.ZipFile(file)
        # A Zip needs to be unpacked, so we
        # use the provided method directly
        dest_file.extractall(dest)
    else:
        if not file.endswith(".pyxapp"):
            utils.warn(f"Expected a Pyxel packaged app, but the file name ('{file}') does not look like one.", UnexpectedFilename)
        shutil.copy2(file, os.path.join(dest, file[len(os.path.dirname(file)):]))
