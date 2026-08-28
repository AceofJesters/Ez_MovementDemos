import pygame
from Character import Character
from Monster import Monster
from Board import Board

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

Ezekiel = Character(pos=(2, 2))
Monster = Monster(pos=(4, 4))
Board = Board(player_pos=Ezekiel.pos, monster_pos=Monster.pos, width=40, height=30)

running = True
while running:
    
    moved = False
    if not moved:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print(Ezekiel.move("up"))
                elif event.key == pygame.K_s:
                    print(Ezekiel.move("down"))
                elif event.key == pygame.K_a:
                    print(Ezekiel.move("left"))
                elif event.key == pygame.K_d:
                    print(Ezekiel.move("right"))
                elif event.key == pygame.K_c:
                    running = False

                # Monster movement

            Board.draw_board(screen)

    pygame.display.update()

pygame.quit()