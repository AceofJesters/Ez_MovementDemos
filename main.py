import pygame
from Character import Character
from Monster import Monster

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

Ezekiel = Character(pos=(100, 100))
Monster = Monster(pos=(400, 300))

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
                monster_dir = Monster.select_destination(SCREEN_WIDTH, SCREEN_HEIGHT)
                if monster_dir:
                    print(Monster.move(monster_dir))

                if Ezekiel.pos == Monster.pos:
                    print("Ezekiel has encountered the Monster!")

    screen.fill((255/2, 255/2, 255/2))
    pygame.draw.rect(screen, (0, 0, 225), (Ezekiel.pos[0], Ezekiel.pos[1], 50, 50))
    pygame.draw.rect(screen, (225, 0, 0), (Monster.pos[0], Monster.pos[1], 50, 50))

    pygame.display.update()

pygame.quit()