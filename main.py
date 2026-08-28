import pygame
from Character import Character
from Monster import Monster
from Board import Board

pygame.init()

GRID_WIDTH = 20
GRID_HEIGHT = 15
PIXEL_SIZE = 50
SCREEN_WIDTH = (GRID_WIDTH+1) * PIXEL_SIZE
SCREEN_HEIGHT = (GRID_HEIGHT+1) * PIXEL_SIZE
EZ_KEY = 1
MON_KEY = 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ezzie <3")

Ezekiel = Character(pos=(2, 2))
Monster = Monster(pos=(4, 4))
Board = Board(PIXEL_SIZE=PIXEL_SIZE, player_pos=Ezekiel.pos, monster_pos=Monster.pos, width=40, height=30)

running = True
while running:
    
    moved = False
    if not moved:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print(Ezekiel.move(Board, "up"))
                elif event.key == pygame.K_s:
                    print(Ezekiel.move(Board, "down"))
                elif event.key == pygame.K_a:
                    print(Ezekiel.move(Board, "left"))
                elif event.key == pygame.K_d:
                    print(Ezekiel.move(Board, "right"))
                elif event.key == pygame.K_c:
                    running = False
                Board.move_entity(EZ_KEY, Ezekiel.pos)
                Board.move_entity(MON_KEY, Monster.pos)

            Board.draw_board(screen)

    pygame.display.update()

pygame.quit()