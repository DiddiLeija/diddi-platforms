"Module for starting up."

import os

import pyxel

from . import mechanics, variables
from .utils import ResourceNotFound


def load_pyxres():
    """
    Load the Pyxel resource (specified in
    'diddi_platofrms.variables.RESOURCE_FILE').
    """
    if os.path.exists(variables.RESOURCE_FILE):
        pyxel.load(variables.RESOURCE_FILE)
    else:
        raise ResourceNotFound(f"File '{variables.RESOURCE_FILE}' does not exist.")


class App:
    "The primary class that runs everything!"

    def __init__(self, w, h, title="Default"):
        pyxel.init(w, h, title=f"Diddi Platforms: {title}")
        load_pyxres()
        pyxel.run(self.update, self.run)

    def update(self):
        variables.PLAYER_OBJECT.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        if variables.PLAYER_OBJECT.alive:
            # WARNING: I hope the global "scroll_x"
            # defined in "diddi_platofrms.objs"
            # is available here. If not, an error will come.
            #
            # TODO: Find out a cleaner way to control this.
            pyxel.bltm(0, 0, 1, mechanics.SCROLL_X, 0, 128, 128, 0)
            pyxel.camera(mechanics.SCROLL_X, 0)
            variables.PLAYER_OBJECT.draw()
