import pygame
import time
import pieces
import board
import sys
from pytris.const import *
import random

pieces = [pieces.T, pieces.S, pieces.J, pieces.L, pieces.Z, pieces.I, pieces.O]

#board = board.Board()
pygame.init()
screen = pygame.display.set_mode((10*SCALE, 20*SCALE))
while True:
    current_piece = random.choice(pieces)()
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 0))
    current_piece.draw(screen)
    #board.draw(screen)
    pygame.display.flip()
    time.sleep(0.3)
