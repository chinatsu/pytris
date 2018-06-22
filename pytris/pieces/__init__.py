import pygame
from pytris import utils
from pytris.const import *
import random
import math

class Piece:
    def __init__(self):
        self.origin = (math.floor(WIDTH/2)-1, HEIGHT-2)
        print(self.origin)
        self.orientation = 0
        self.das = 0
        self.das_limit = DAS_LIMIT
        self.randomizer = bag.Randomizer()


    def set_randomizer(self, randomizer):
        self.randomizer = randomizer

    def charge_das(self):
        if self.das < self.das_limit:
            self.das += 1
        if self.das == self.das_limit:
            return True
        else: return False

    def reset_das(self):
        self.das = 0

    def new(self):
        self.origin = (math.floor(WIDTH/2)-1, HEIGHT-2)
        self.orientation = 0
        new_piece = self.randomizer.next()()
        self.shapes = new_piece.shapes
        self.id = new_piece.id

    def draw(self, screen):
        for offset in self.shapes[self.orientation]:
            mino = utils.make_mino(utils.add_coordinates(self.origin, offset))
            color = utils.get_color(self.id)
            pygame.draw.rect(screen, color, mino)

    def draw_ghost(self, screen, board):
        temp_origin = self.origin
        reached_bottom = False
        while not reached_bottom:
            for cell in self.shapes[self.orientation]:
                if not board.is_free(utils.add_coordinates(temp_origin, cell)):
                    reached_bottom = True
            if reached_bottom:
                temp_origin = utils.add_coordinates(temp_origin, (0, 1)) # this is stupid and hacky
                break
            temp_origin = utils.add_coordinates(temp_origin, (0, -1))
        for offset in self.shapes[self.orientation]:
            mino = utils.make_mino(utils.add_coordinates(temp_origin, offset))
            color = (100, 100, 100)
            pygame.draw.rect(screen, color, mino)

    def rotate(self, amount, board):
        for check in CHECKS:
            new_orientation = (self.orientation + amount) % 4
            new_origin = utils.add_coordinates(self.origin, check)
            if self.valid_position(new_origin, new_orientation, board):
                self.orientation = new_orientation
                self.origin = new_origin
                return



    def move(self, offset, board, ignore_das=False):
        if self.valid_position(utils.add_coordinates(self.origin, offset), self.orientation, board):
            self.origin = utils.add_coordinates(self.origin, offset)

    def hard_drop(self, board):
        while self.valid_position(utils.add_coordinates(self.origin, (0, -1)), self.orientation, board):
            self.origin = utils.add_coordinates(self.origin, (0, -1))


    def valid_position(self, point, orientation, board):
        for cell in self.shapes[orientation]:
            coordinate = utils.add_coordinates(point, cell)
            if coordinate[1] >= HEIGHT or coordinate[1] < 0:
                return False
            elif coordinate[0] >= WIDTH or coordinate[0] < 0:
                return False
            elif board.matrix[coordinate[1]][coordinate[0]] != 'x':
                return False
        return True

class I(Piece):
    def __init__(self):
        super(I, self).__init__()
        self.shapes = [
            [(-1, 0), (0, 0), (1, 0), (2, 0)],
            [(0, -2), (0, -1), (0, 0), (0, 1)],
            [(-1, -1), (0, -1), (1, -1), (2, -1)],
            [(1, -2), (1, -1), (1, 0), (1, 1)]

        ]
        self.id = "i"

class Z(Piece):
    def __init__(self):
        super(Z, self).__init__()
        self.shapes = [
            [(-1, 1), (0, 1), (0, 0), (1, 0)],
            [(-1, -1), (-1, 0), (0, 0), (0, 1)],
            [(-1, 0), (0, 0), (0, -1), (1, -1)],
            [(0, -1), (0, 0), (1, 0), (1, 1)]
        ]
        self.id = "z"

class J(Piece):
    def __init__(self):
        super(J, self).__init__()
        self.shapes = [
            [(-1, 0), (0, 0), (1, 0), (1, 1)],
            [(-1, 1), (0, 1), (0, 0), (0, -1)],
            [(-1, -1), (-1, 0), (0, 0), (1, 0)],
            [(1, -1), (0, -1), (0, 0), (0, 1)]

        ]
        self.id = "j"

class S(Piece):
    def __init__(self):
        super(S, self).__init__()
        self.shapes = [
            [(-1, 0), (0, 0), (0, 1), (1, 1)],
            [(0, -1), (0, 0), (-1, 0), (-1, 1)],
            [(-1, -1), (0, -1), (0, 0), (1, 0)],
            [(1, -1), (1, 0), (0, 0), (0, 1)]

        ]
        self.id = "s"

class O(Piece):
    def __init__(self):
        super(O, self).__init__()
        shape = [(0, 1), (0, 0), (1, 1), (1, 0)]
        self.shapes = [shape, shape, shape, shape]
        self.id = "o"

class L(Piece):
    def __init__(self):
        super(L, self).__init__()
        self.shapes = [
            [(-1, 1), (-1, 0), (0, 0), (1, 0)],
            [(-1, -1), (0, -1), (0, 0), (0, 1)],
            [(1, -1), (-1, 0), (0, 0), (1, 0)],
            [(0, -1), (0, 0), (0, 1), (1, 1)]
        ]
        self.id = "l"

class T(Piece):
    def __init__(self):
        super(T, self).__init__()
        self.shapes = [
            [(-1, 0), (0, 0), (1, 0), (0, 1)],
            [(0, 1), (0, 0), (0, -1), (-1, 0)],
            [(-1, 0), (0, 0), (1, 0), (0, -1)],
            [(0, 1), (0, 0), (0, -1), (1, 0)]
        ]
        self.id = "t"

from pytris.randomizer import bag
