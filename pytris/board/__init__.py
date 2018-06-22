import pygame
from pytris.const import SCALE, WIDTH, HEIGHT
from pytris import utils

class Board:
    def __init__(self):
        self.matrix = [['x' for x in range(WIDTH)] for y in range(HEIGHT)]

    def draw(self, screen):
        for y, _ in enumerate(self.matrix):
            for x, b in enumerate(self.matrix[y]):
                mino = utils.make_mino((x, y))
                color = utils.get_color(b)
                if color:
                    pygame.draw.rect(screen, color, mino)

    def commit(self, piece):
        for cell in piece.shapes[piece.orientation]:
            absolute = utils.add_coordinates(piece.origin, cell)
            self.matrix[absolute[1]][absolute[0]] = piece.id
        piece.new()
        return self.clear_lines()

    def clear_lines(self):
        cleared = 0
        for idx, row in reversed(list(enumerate(self.matrix))):
            if not 'x' in row:
                cleared += 1
                del self.matrix[idx]
                self.matrix.append(['x'] * WIDTH)
        return cleared


    def is_free(self, coordinate):
        if coordinate[1] >= HEIGHT or coordinate[1] < 0:
            return False
        elif coordinate[0] >= WIDTH or coordinate[0] < 0:
            return False
        elif self.matrix[coordinate[1]][coordinate[0]] != 'x':
            return False
        else:
            return True
