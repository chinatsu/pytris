from pygame import Rect
from pytris.const import COLORS

def make_mino(origin, offset, scale):
    return Rect(
        (origin[0]+offset[0])*scale,
        (origin[1]+offset[1])*scale,
        scale,
        scale
    )

def get_color(id):
    if not id in COLORS:
        return False
    else:
        return COLORS[id]
