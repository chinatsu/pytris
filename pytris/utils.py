from pygame import Rect
from pytris.const import COLORS, HEIGHT, SCALE

def make_mino(coordinate):
    coords = to_pygame(coordinate)
    return Rect(
        (coords[0])*SCALE,
        (coords[1]-1)*SCALE, # off by one error? :(
        SCALE,
        SCALE
    )

def get_color(id):
    if not id in COLORS:
        return False
    else:
        return COLORS[id]

def to_pygame(coords):
    """Convert coordinates into pygame coordinates (lower-left => top left)."""
    return (coords[0], HEIGHT - coords[1])

def add_coordinates(a, b):
    return tuple(map(sum, zip(a, b)))
