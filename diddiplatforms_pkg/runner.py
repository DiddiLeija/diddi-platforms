"""
The main brain of this package (and what
really matters) is here.
"""

import os

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
        if app_type == "pyxapp" and "pyxapp_file" not in kwargs:
            raise ValueError("Keyword argument 'pyxapp_file' not found")
        elif app_type == "py" and "json_config" not in kwargs:
            raise ValueError("Keyword argument 'json_config' not found")
        elif app_type not in ("pyxapp", "py"):
            raise ValueError(
                f"Expected 'app_type' to be one of ('pyxapp', 'py'), got '{app_type}'"
            )

        self.levels_path = os.path.join(utils.get_user_ubication(), "levels")

        self.pyxel_init(init_width, init_height, title)

    def pyxel_init(self, w, h, t):
        # NOTE: We set capture_sec to 30
        # to enable video screenshots :)
        pyxel.init(w, h, t, capture_sec=30)
