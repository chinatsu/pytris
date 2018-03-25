import pygame
import time
import pieces
import board
import sys
from pytris.const import *
import random



board = board.Board()
pygame.init()
screen = pygame.display.set_mode((WIDTH*SCALE, HEIGHT*SCALE))
current_piece = pieces.Piece()
current_piece.new()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_piece.hard_drop(board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            current_piece.move((-1, 0), board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            current_piece.move((1, 0), board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            current_piece.move((0, -1), board)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            current_piece.rotate(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            current_piece.rotate(3)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                        current_piece.rotate(2)

    screen.fill((0, 0, 0))
    current_piece.draw(screen)
    current_piece.draw_ghost(screen, board)
    board.draw(screen)
    pygame.display.flip()
