"Module for starting up."

import os

import pyxel

from . import variables
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


def initialize():
    "The primary function that runs everything!"
