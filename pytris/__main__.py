import pygame
import time
import pieces

import board
import sys
from pytris.const import *
from pytris import utils
import random

class Game:
    def __init__(self):
        self.piece = pieces.Piece()
        self.piece.new()
        self.board = board.Board()
        self.game_over = False
        self.screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))

game = Game()
pygame.init()

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game.game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.piece.hard_drop(game.board)
            print(list(reversed([x.__name__ for x in game.piece.randomizer.pile])))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            game.piece.move((-1, 0), game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            game.piece.move((1, 0), game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            game.piece.move((0, -1), game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            game.piece.rotate(1, game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            game.piece.rotate(3, game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            game.piece.rotate(2, game.board)

    game.screen.fill((0, 0, 0))
    coords = utils.to_pygame((3, 21))
    bounding = pygame.Rect(
        (coords[0])*SCALE,
        (coords[1]-1)*SCALE, # off by one error? :(
        3*SCALE,
        3*SCALE
    )
    pygame.draw.rect(game.screen, (55, 55, 55), bounding)
    game.board.draw(game.screen)
    game.piece.draw_ghost(game.screen, game.board)
    game.piece.draw(game.screen)

    pygame.display.flip()
