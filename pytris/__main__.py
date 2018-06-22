import pygame
import time

from pytris import pieces, board, utils
import sys
from pytris.const import *
import random
import math

class Game:
    def __init__(self):
        self.piece = pieces.Piece()
        self.piece.new()
        self.board = board.Board()
        self.game_over = False
        self.screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
        self.lines = 0
        self.level = 0
        self.frame = 0
        self.gravity = False
        self.dasing = False
        self.direction = 0

game = Game()
pygame.init()
clock = pygame.time.Clock()


table = {
0: 48,
1: 43,
2: 38,
3: 33,
4: 28,
5: 23,
6: 18,
7: 13,
8: 8,
9: 6,
10: 5,
11: 5,
12: 5,
13: 4,
14: 4,
15: 4,
16: 3,
17: 3,
18: 3,
19: 2,
20: 2,
21: 2,
22: 2,
23: 2,
24: 2,
25: 2,
26: 2,
27: 2,
28: 2,
29: 1
}

while not game.game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game.game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.piece.hard_drop(game.board)
            l = game.board.commit(game.piece)
            if l > 0:
                game.lines += l
                game.level = game.lines//10
                print(game.level)

        if event.type == pygame.KEYDOWN and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            game.dasing = True
        elif event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            print("yeah")
            game.piece.reset_das()
            game.dasing = False
            game.direction = "none"

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            game.direction = "left"
            game.piece.move((-1, 0), game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            game.direction = "right"
            game.piece.move((1, 0), game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            game.piece.move((0, -1), game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            game.piece.rotate(1, game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            game.piece.rotate(3, game.board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            game.piece.rotate(2, game.board)

    if game.dasing:
        charged = game.piece.charge_das()

    if game.direction == "left" and charged:
        game.piece.move((-1, 0), game.board)
    if game.direction == "right" and charged:
        game.piece.move((1, 0), game.board)
    if game.frame >= table[game.level]:
        print(game.frame)
        game.piece.move((0, -1), game.board, ignore_das=True)
        game.frame = 0
    game.screen.fill((0, 0, 0))
    coords = utils.to_pygame((math.floor(WIDTH/2)-1, HEIGHT-1))
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
    game.frame += 1
    clock.tick(30)
