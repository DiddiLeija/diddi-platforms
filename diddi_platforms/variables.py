"""
The bunch of variables and data
required to start up Diddi Platforms.

You may customize this module's variables
before invoking the game, to extend or
customize its features, like the textures,
maps, or even adding new behavior.
"""

from . import mechanics, objs

# This "default.pyxres" is the Pyxel
# resource found in the repo.
RESOURCE_FILE = r"..\default.pyxres"

# TODO: Fill these variables with our
#       beloved character/mob/block objects!
PLAYER_OBJECT = objs.Diddi
MOB_OBJECTS = []


def add_floor_tiles(x, y):
    """
    Add a tuple to '.mechanics.TILES_FLOOR'.

    This function is actually a workaround to the
    complexity around '.objs', '.mechanics' and
    '.variables' itself.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        mechanics.TILES_FLOOR.append((x, y))
