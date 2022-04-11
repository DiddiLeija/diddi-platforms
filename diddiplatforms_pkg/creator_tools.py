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

    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    @property
    @abstractmethod
    def is_solid(self):
        """
        Return True if the block is 100% solid (e.g.
        blocks) or True if it could overlap and interact
        with other elements.

        This base class gives None, but that's not
        officially 'allowed'.
        """
        return None

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


class BaseBlock(Object):
    """
    A basic 'block' object. All those objects
    considered as 'blocks' should be instances
    of this object.
    """

    @property
    def role(self):
        return 1

    @property
    def is_solid(self):
        return True

    def draw(self):
        """
        Actually, blocks doesn't need to be drawn
        (in most of the cases), since they're already
        on the tilemap!
        """
        pass


class Dirt(BaseBlock):
    """
    Dirt is a basic block, with no available interactions
    with the users, it is totally solid.
    """

    def get_aspect_ubication(self):
        return ((24, 24), 8)

    def update(self):
        pass


class Grass1(Dirt):
    "Light grass."

    def get_aspect_ubication(self):
        return ((24, 16), 8)


class Grass2(Dirt):
    "Thick grass."

    def get_aspect_ubication(self):
        return ((16, 16), 8)


class Stone(BaseBlock):
    "Stone. Again, no interactions are allowed."

    def get_aspect_ubication(self):
        return ((16, 24), 8)
