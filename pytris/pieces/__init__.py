import pygame
from pytris import utils
from pytris.const import *


class Piece:
    def __init__(self):
        self.origin = (4, 1)
        self.orientation = 0

    def draw(self, screen):
        for offset in self.shapes[self.orientation]:
            mino = utils.make_mino(self.origin, offset, SCALE)
            color = utils.get_color(self.id)
            pygame.draw.rect(screen, color, mino)

    def rotate(self, amount):
        self.orientation = (self.orientation + amount) % 4

class I(Piece):
    def __init__(self):
        super(I, self).__init__()
        self.shapes = [
            [(-1, -1), (0, -1), (1, -1), (2, -1)],
            [(1, -2), (1, -1), (1, 0), (1, 1)],
            [(-1, 0), (0, 0), (1, 0), (2, 0)],
            [(0, -2), (0, -1), (0, 0), (0, 1)]
        ]
        self.id = "i"

class Z(Piece):
    def __init__(self):
        super(Z, self).__init__()
        self.shapes = [
            [(-1, -1), (0, -1), (0, 0), (1, 0)],
            [(1, -1), (1, 0), (0, 0), (0, 1)],
            [(-1, 0), (0, 0), (0, 1), (1, 1)],
            [(0, -1), (0, 0), (-1, 0), (-1, 1)]
        ]
        self.id = "z"

class J(Piece):
    def __init__(self):
        super(J, self).__init__()
        self.shapes = [
            [(-1, -1), (-1, 0), (0, 0), (1, 0)],
            [(1, -1), (0, -1), (0, 0), (0, 1)],
            [(-1, 0), (0, 0), (1, 0), (1, 1)],
            [(-1, 1), (0, 1), (0, 0), (0, -1)]
        ]
        self.id = "j"

class S(Piece):
    def __init__(self):
        super(S, self).__init__()
        self.shapes = [
            [(-1, 0), (0, 0), (0, -1), (1, -1)],
            [(0, -1), (0, 0), (1, 0), (1, 1)],
            [(-1, 1), (0, 1), (0, 0), (1, 0)],
            [(-1, -1), (-1, 0), (0, 0), (0, 1)]
        ]
        self.id = "s"

class O(Piece):
    def __init__(self):
        super(O, self).__init__()
        shape = [(0, -1), (0, 0), (1, -1), (1, 0)]
        self.shapes = [shape, shape, shape, shape]
        self.id = "o"

class L(Piece):
    def __init__(self):
        super(L, self).__init__()
        self.shapes = [
            [(1, -1), (-1, 0), (0, 0), (1, 0)],
            [(0, -1), (0, 0), (0, 1), (1, 1)],
            [(-1, 1), (-1, 0), (0, 0), (1, 0)],
            [(-1, -1), (0, -1), (0, 0), (0, 1)]
        ]
        self.id = "l"

class T(Piece):
    def __init__(self):
        super(T, self).__init__()
        self.shapes = [
            [(-1, 0), (0, 0), (1, 0), (0, -1)],
            [(0, 1), (0, 0), (0, -1), (1, 0)],
            [(-1, 0), (0, 0), (1, 0), (0, 1)],
            [(0, 1), (0, 0), (0, -1), (-1, 0)]
        ]
        self.id = "t"
