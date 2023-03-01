"""
Collection of useful functions about
physics mechanics.
"""

import pyxel

WALL_TILE_X = 4
SCROLL_BORDER_X = 80
# NOTE: The "TILES_FLOOR" coordinates
# are represented as (x//8, y//8),
# where x and y are the coordinates
# in the tilemap.
TILES_FLOOR = [
    (2, 2),
    (3, 2),
    (2, 3),
    (3, 3),
    (4, 0),
    (4, 1),
    (6, 0),
    (6, 1),
    (7, 0),
    (7, 1),
]

SCROLL_X = 0


def get_tile(tile_x, tile_y):
    return pyxel.tilemap(1).pget(tile_x, tile_y)


def detect_collision(x, y, dy):
    x1 = x // 8
    y1 = y // 8
    x2 = (x + 8 - 1) // 8
    y2 = (y + 8 - 1) // 8
    for yi in range(y1, y2 + 1):
        for xi in range(x1, x2 + 1):
            if get_tile(xi, yi)[0] >= WALL_TILE_X:
                return True
    if dy > 0 and y % 8 == 1:
        for xi in range(x1, x2 + 1):
            if get_tile(xi, y1 + 1) in TILES_FLOOR:
                return True
    return False


def push_back(x, y, dx, dy):
    abs_dx = abs(dx)
    abs_dy = abs(dy)
    if abs_dx > abs_dy:
        sign = 1 if dx > 0 else -1
        for _ in range(abs_dx):
            if detect_collision(x + sign, y, dy):
                break
            x += sign
        sign = 1 if dy > 0 else -1
        for _ in range(abs_dy):
            if detect_collision(x, y + sign, dy):
                break
            y += sign
    else:
        sign = 1 if dy > 0 else -1
        for _ in range(abs_dy):
            if detect_collision(x, y + sign, dy):
                break
            y += sign
        sign = 1 if dx > 0 else -1
        for _ in range(abs_dx):
            if detect_collision(x + sign, y, dy):
                break
            x += sign
    return x, y, dx, dy


def spawn_enemies(left_x, right_x):
    # TODO: fixme
    pass
