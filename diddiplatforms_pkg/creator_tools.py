"""
This submodule is the toolkit for those
who create Diddi Platforms levels.
"""

from abc import ABC, abstractmethod

import pyxel


class Object(ABC):
    """
    This is the base class for those classes
    that represent 'objects' that are drawed in
    the screen. In other words, an 'object' can
    be a block, a character, a power-up or the
    player itself.
    """

    x = 0
    y = 0

    def __init__(self):
        pass

    @property
    @abstractmethod
    def role(self):
        """
        These are the accepted numbers to provide:

        - 0: The Player itself!
        - 1: An unoffensive block.
        - 2: An unoffensive character.
        - 3: A hostile character.

        At this base class, we return -1 to avoid
        fitting in anyone of the above classifications.
        """
        return -1

    @abstractmethod
    def get_aspect_ubication(self):
        """
        This method is the way to find where to find
        the object's sprite in the Pyxel resource,
        and the size. That's returned in a (coords, size)
        tuple. Also, 'coords' should be a (x, y, r) tuple,
        where 'x' and 'y' are the coordinates, and 'r' is
        the resource number (as far as Pyxel has stated, 0-2).
        And 'size' is the size in pixels (usually, it's 8).

        This base class has provided an example.
        """
        return ((0, 0, 0), 8)

    @abstractmethod
    def update(self):
        "The update method."

    def draw(self):
        """
        The draw method, that uses Pyxel.
        This method is not abstract, but could
        be overridden when needed.
        """
        aspect, size = self.get_aspect_ubication()
        pyxel.blt(self.x, self.y, aspect[2], aspect[0], aspect[1], size, size)
