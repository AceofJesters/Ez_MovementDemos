import pygame
import random
from Character import Character
from Monster import Monster
from Board import Board
from Marker import Marker

pygame.init()

GRID_WIDTH = 20
GRID_HEIGHT = 15
PIXEL_SIZE = 50
SCREEN_WIDTH = (GRID_WIDTH+1) * PIXEL_SIZE
SCREEN_HEIGHT = (GRID_HEIGHT+1) * PIXEL_SIZE

#Flag to indicate whether or not the monster should retarget ezzy
CHASE = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ezzie <3")

EZZY = Character(pos=(2, 2))
MONSTER = Monster(pos=(4, 4))
MARKER = Marker(pos=(0,0))

# Any new units can go here
units = [EZZY, MONSTER, MARKER]

sprite_group = pygame.sprite.Group()

# Anything with a sprite can go here
sprite_group.add(MARKER)


Board = Board(PIXEL_SIZE=PIXEL_SIZE, units=units, sprite_group=sprite_group, width=40, height=30)

running = True
while running:

    moved = False
    if not moved:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                ez_moved = False
                if event.key == pygame.K_w:
                    print(EZZY.move(Board, "up"))
                    ez_moved = True
                elif event.key == pygame.K_s:
                    print(EZZY.move(Board, "down"))
                    ez_moved = True
                elif event.key == pygame.K_a:
                    print(EZZY.move(Board, "left"))
                    ez_moved = True
                elif event.key == pygame.K_d:
                    print(EZZY.move(Board, "right"))
                    ez_moved = True
                # pass turn
                elif event.key == pygame.K_SPACE:
                    print(EZZY.move(Board, "neutral"))
                    ez_moved = True
                # Press '1' to have Monster target Ezzy
                elif event.key == pygame.K_1:
                    CHASE = True
                    print(MONSTER.select_destination(Board, EZZY))
                # Press '2' to have Monster target the Marker
                elif event.key == pygame.K_2:
                    CHASE = False
                    print(MONSTER.select_destination(Board, MARKER))
                # Press '0' to have the Monster target nothing (we'll use itself)
                elif event.key == pygame.K_0:
                    CHASE = False
                    print(MONSTER.select_destination(Board, MONSTER))
                elif event.key == pygame.K_c:
                    running = False

                if ez_moved:
                    # Retarget Ezzy
                    if CHASE:
                        MONSTER.select_destination(Board, EZZY)
                    
                    # Roll number of movement opportunities
                    mov_ops = random.randint(1, 3)
                    
                    for i in range(mov_ops):
                        MONSTER.move(Board)

                    
                Board.move_entity(EZZY.pos)
                Board.move_entity(MONSTER.pos)
                if EZZY.pos == MONSTER.pos:
                    print("ez got eaten :(")
                    running = False
                if MARKER.pos == MONSTER.pos:
                    print("the monster has found DOOM BWAWAWAWAWA")

            Board.draw_board(screen)

    pygame.display.update()

pygame.quit()