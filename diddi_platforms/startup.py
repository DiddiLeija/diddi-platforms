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
    player = None

    def __init__(self, w=128, h=128, title="Default"):
        pyxel.init(w, h, title=f"Diddi Platforms: {title}")
        load_pyxres()
        self.setup()
        pyxel.run(self.update, self.draw)

    def setup(self):
        self.player = variables.PLAYER_OBJECT()

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.camera()
        if self.player.alive:
            pyxel.bltm(0, 0, 0, mechanics.SCROLL_X, 0, 128, 128, 0)
            pyxel.camera(mechanics.SCROLL_X, 0)
            self.player.draw()
