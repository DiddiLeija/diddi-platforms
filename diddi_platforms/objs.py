"""
The module that provides all the
classes used in objects (player,
blocks, mobs, etc).
"""

import random

import pyxel

from . import mechanics


class BaseClass:
    "The base class for all the objects."
    # Edit these variables if needed
    x, y = 0, 0
    aspect = (0, 0)
    size = 8

    def update(self):
        # Fill this function at instances.
        pass

    def draw(self):
        # Basic draw: feel free to override
        # this if you need it.
        pyxel.bltm(
            self.x,
            self.y,
            # Assuming all "objects" can be found
            # at tilemap 0...
            0,
            self.aspect[0],
            self.aspect[1],
            0,
        )


# --- Player classes ---


class Diddi(BaseClass):
    """
    Diddi, our main player. In theory,
    you can replace Diddi with someone
    else's class, so the world would be
    saved by somebody else...
    """

    # TODO: The current code is based in the
    #       "Abandon the ship!" code, v1.0.0.
    #       We must get rid of that soon.

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.r_facing = True
        self.is_falling = False
        self.has_shooter = False
        # For debugging purposes only!
        self.is_invicible = False
        self.aspects = {
            # [D]eath
            "d": [(0, 0) for i in range(3)],
            # [R]ight-facing
            "r": ((16, 0), (24, 0), (32, 0)),
            # [L]eft-facing
            "l": ((16, 8), (24, 8), (32, 8)),
        }
        self.alive = True
        self.active = False

    def update(self):
        if not self.alive:
            return
        if not self.active:
            return
        # global scroll_x
        last_y = self.y
        if pyxel.btn(pyxel.KEY_LEFT):
            self.dx = -2
            self.r_facing = False
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.dx = 2
            self.r_facing = True
        self.dy = min(self.dy + 1, 3)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.dy = -6
            # pyxel.play(3, 8)
        self.x, self.y, self.dx, self.dy = mechanics.push_back(
            self.x, self.y, self.dx, self.dy
        )
        if self.x < mechanics.SCROLL_X:
            self.x = mechanics.SCROLL_X
        if self.y < 0:
            self.y = 0
        self.dx = int(self.dx * 0.8)
        self.is_falling = self.y > last_y

        if self.x > mechanics.SCROLL_X + mechanics.SCROLL_BORDER_X:
            # NOTE: The 'scroll_x' stuff and the enemy
            #       generation is here for a reason.
            last_scroll_x = mechanics.SCROLL_X
            mechanics.SCROLL_X = min(self.x - mechanics.SCROLL_BORDER_X, 240 * 8)
            mechanics.spawn_enemies(last_scroll_x + 128, mechanics.SCROLL_X + 127)

    def draw(self):
        if self.is_falling:
            situation = 2
        else:
            situation = random.choice([0, 1])
        if not self.alive:
            face = "d"
        elif self.r_facing:
            face = "r"
        else:
            face = "l"
        img_x, img_y = self.aspects[face][situation]
        pyxel.blt(self.x, self.y, 0, img_x, img_y, 8, 8, 0)
