import pygame

EZ_KEY = 1
MON_KEY = 2

class Board:
    def __init__(self, PIXEL_SIZE, player_pos, monster_pos, width=40, height=30):
        self.PIXEL_SIZE = PIXEL_SIZE
        self.player_pos = player_pos
        self.monster_pos = monster_pos
        self.width = width
        self.height = height
        self.grid = self.set_positions()


    def set_positions(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.grid[self.player_pos[1]][self.player_pos[0]] = 1
        self.grid[self.monster_pos[1]][self.monster_pos[0]] = 2
        return self.grid


    def draw_board(self, screen):
        screen.fill((0, 0, 0))
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(j * self.PIXEL_SIZE, i * self.PIXEL_SIZE, self.PIXEL_SIZE, self.PIXEL_SIZE)

                if self.grid[i][j] == EZ_KEY:
                    pygame.draw.rect(screen, (0, 0, 255), rect)
                elif self.grid[i][j] == MON_KEY:
                    pygame.draw.rect(screen, (255, 0, 0), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    
    def move_entity(self, entity_key, destination):

        if destination[0] in range(self.width) and destination[1] in range(self.height):
            if entity_key == EZ_KEY:
                self.player_pos = destination
            self.set_positions()
            return True
        else:
            return False