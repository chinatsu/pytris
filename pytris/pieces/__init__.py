import pygame
from pytris import utils
from pytris.const import *
import random


class Piece:
    def __init__(self):
        self.origin = (4, 20)
        self.orientation = 0

    def new(self):
        pieces = [T, S, J, L, Z, I, O]
        self.origin = (4, 20)
        self.orientation = 0
        new_piece = random.choice(pieces)()
        self.shapes = new_piece.shapes
        self.id = new_piece.id

    def draw(self, screen):
        for offset in self.shapes[self.orientation]:
            mino = utils.make_mino(utils.add_coordinates(self.origin, offset))
            color = utils.get_color(self.id)
            pygame.draw.rect(screen, color, mino)

    def draw_ghost(self, screen):
        temp_origin = self.origin
        while True:
            temp_origin = utils.add_coordinates(temp_origin, (0, -1))
            for cell self.shapes[self.orientation]:
                if not matrix.is_free(utils.add_coordinates(temp_origin, cell)):
                    break
        for offset in self.shapes[self.orientation]:
            mino = utils.make_mino(temp_origin)
            color = (244, 244, 244)
            pygame.draw.rect(screen, color, mino)

    def rotate(self, amount):
        self.orientation = (self.orientation + amount) % 4

    def move(self, offset, matrix):
        if self.can_move(offset, matrix):
            self.origin = utils.add_coordinates(self.origin, offset)

    def hard_drop(self, matrix):
        while self.can_move((0, -1), matrix):
            self.origin = utils.add_coordinates(self.origin, (0, -1))
        matrix.commit(self)

    def can_move(self, offset, matrix):
        temp_origin = utils.add_coordinates(self.origin, offset)
        for cell in self.shapes[self.orientation]:
            if not matrix.is_free(utils.add_coordinates(temp_origin, cell)):
                return False
        return True

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
