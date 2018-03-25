import pygame
from pytris.const import SCALE
from pytris import utils

class Board:
    def __init__(self):
        self.matrix = [[0 for x in range(10)] for y in range(22)]

    def draw(self, screen):
        for y, _ in enumerate(self.matrix):
            for x, b in enumerate(self.matrix[y]):
                mino = utils.make_mino((y, x), (0, 0), SCALE)
                color = utils.get_color(b)
                if color:
                    pygame.draw.rect(screen, color, mino)
