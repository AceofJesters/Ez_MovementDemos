import pygame

class Board:
    def __init__(self, player_pos, monster_pos, width=40, height=30):
        self.player_pos = player_pos
        self.monster_pos = monster_pos
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.grid[player_pos[1]][player_pos[0]] = 1
        self.grid[monster_pos[1]][monster_pos[0]] = 2


    def draw_board(self, screen):
        screen.fill((0, 0, 0))
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(j * 50, i * 50, 50, 50)

                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (0, 0, 255), rect)
                elif self.grid[i][j] == 2:
                    pygame.draw.rect(screen, (255, 0, 0), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    
    def move_entity(self, entity, destination):

        if destination[0] in range(self.width) and destination[1] in range(self.height):
            entity.pos = destination
            return True
        else:
            return False