"""
This submodule is the toolkit for those
who create Diddi Platforms levels.
"""

import random
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
        blocks) or False if it could overlap and interact
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
        and the size. That's returned in a (img, coords, size)
        tuple. There, 'coords' should be a (x, y, r) tuple,
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


class Diddi(Object):
    """
    The main object behind a character. In most of the
    cases, Diddi is the main character of the game and
    doesn't need to be replaced (in most of the cases).
    """

    def __init__(self, x=None, y=None):
        """
        We ignored 'x' and 'y', though they
        can be passed like any other object.
        Anyway, we are starting from (0, 0).

        ---

        We also define a 'self.state'. It is
        a tuple that describes the state of the
        character. The first value can mean:

        - 0: Right
        - 1: Left

        And the second value can mean:

        - 0: In the air
        - 1: Not in the air

        The initial value of 'state' is (0, 0),
        which means "right oriented, in the air",
        and is what we need when starting.

        ---

        Finally, 'shooting' is a boolean that tells
        if the player is sending a bullet or not.
        """
        self.x, self.y = 0, 0
        self.state = (0, 0)
        self.shooting = False

    @property
    def role(self):
        return 0

    @property
    def is_solid(self):
        return False

    @abstractmethod
    def get_aspect_ubication(self):
        """
        To identify which aspect we'll
        use, we need to compare some
        "state values" first.
        """
        orientation, not_flying = self.state
        if orientation == 0:
            # Right oriented
            x, y = 32, 0
            if not_flying:
                # Select one of the "walking"
                # aspects defined for right orientation
                x, y = random.choice([(16, 0), (24, 0)])
                if self.shooting:
                    x, y = 16, 16
        else:
            # Left oriented
            x, y = 32, 8
            if not_flying:
                # Select one of the "walking"
                # aspects defined for left orientation
                x, y = random.choice([(16, 8), (24, 8)])
            if self.shooting:
                x, y = 24, 16
        return (
            (
                x,
                y,
                0,
            ),
            8,
        )

    def update(self):
        "The update method."
        self.horizontal_move()
        self.check_shooting()

    def horizontal_move(self):
        "Move in the 'x' axis"
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.x = min(self.x + 2, 10)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.x = max(self.x - 2, 10)

    def check_shooting(self):
        "The shooting startegy."
        if pyxel.btnp(pyxel.KEY_SPACE):
            # Time to shoot
            pass


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
