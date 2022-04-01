"""
The main brain of this package (and what
really matters) is here.
"""

import os
import runpy

import pyxel

from . import utils


class PyxelAppRunner:
    "The class to run the Diddi Platforms app."

    def __init__(
        self,
        app_type="pyxapp",
        title="Diddi Platforms",
        init_width=100,
        init_height=100,
        **kwargs,
    ):
        self.app_type = app_type
        self.levels_path = os.path.join(utils.get_user_ubication(), "levels")

        os.chdir(self.levels_path)

        if self.app_type == "pyxapp":
            if "pyxapp_file" not in kwargs:
                raise ValueError("Keyword argument 'pyxapp_file' not found")
            self.run_pyxapp(kwargs["pyxapp_file"])
        elif self.app_type == "py":
            if "py_file" not in kwargs:
                raise ValueError("Keyword argument 'py_file' not found")
            try:
                if kwargs["no_pyxel_init"] is False:
                    self.pyxel_init(init_width, init_height, title)
            except KeyError:
                pass
            self.run_py(kwargs["py_file"])
        elif self.app_type not in ("pyxapp", "py"):
            raise ValueError(
                f"Expected 'app_type' to be one of ('pyxapp', 'py'), got '{self.app_type}'"
            )

    def pyxel_init(self, w, h, t):
        # NOTE: We set capture_sec to 30
        # to enable video screenshots :)
        pyxel.init(w, h, t, capture_sec=30)

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

    def run_py(self, file, configfile):
        """
        Given the Python file, run the app.
        """
        runpy.run_path(file + ".py")
