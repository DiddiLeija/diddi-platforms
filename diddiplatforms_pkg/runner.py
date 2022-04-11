"""
The main brain of this package (and what
really matters) is here.
"""

import os
import runpy

import pyxel

from . import utils


class AppRunner:
    """
    The class to run the Diddi Platforms app.
    It is a basic Pyxel app, that works as the
    'main operations room'. The levels are run
    in a separate window, as a unique Pyxel app.
    """

    def __init__(self):
        self.reset_values()
        pyxel.init(100, 100, "Diddi Platforms -- Welcome")
        pyxel.run(self.update, self.draw)

    def reset_values(self):
        self.levels_path = os.path.join(utils.get_user_ubication(), "levels")
        os.chdir(self.levels_path)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, 100, 7, 5)
        pyxel.text(1, 0, "Diddi Platforms", 1)
        pyxel.text(0, 0, "Diddi Platforms", 7)

    def run_file(
        self,
        app_type="pyxapp",
        **kwargs,
    ):
        self.app_type = app_type

        if self.app_type == "pyxapp":
            if "pyxapp_file" not in kwargs:
                raise ValueError("Keyword argument 'pyxapp_file' not found")
            self.run_pyxapp(kwargs["pyxapp_file"])
        elif self.app_type == "py":
            if "py_file" not in kwargs:
                raise ValueError("Keyword argument 'py_file' not found")
            self.run_py(kwargs["py_file"])
        else:
            raise ValueError(
                f"Expected 'app_type' to be one of ('pyxapp', 'py'), got '{self.app_type}'"
            )

    def run_pyxapp(self, file):
        """
        Run a pyxapp, given the file name,
        using part of the Pyxel's strategy for
        running these packaged apps.
        """
        # WARNING: We are using an internal function
        # of Pyxel to run the pyxapps. The Pyxel version
        # **should** keep pinned for safety reasons.
        pyxel.cli._play_pyxel_app(file + ".pyxapp")

    def run_py(self, file):
        """
        Given the Python file, run the app.
        """
        runpy.run_path(file + ".py")
