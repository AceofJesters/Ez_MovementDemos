import pygame

class Board:
    def __init__(self, PIXEL_SIZE, units, sprite_group, width=40, height=30):
        self.PIXEL_SIZE = PIXEL_SIZE
        self.units = units
        self.sprite_group = sprite_group
        self.width = width
        self.height = height
        self.grid = self.set_positions()
        
    def set_positions(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for obj in self.units:
            self.grid[obj.get_position()[1]][obj.get_position()[0]] = obj
        return self.grid


    def draw_board(self, screen):
        screen.fill((0, 0, 0))
        for i in range(self.height):
            for j in range(self.width):
                rect = pygame.Rect(j * self.PIXEL_SIZE, i * self.PIXEL_SIZE, self.PIXEL_SIZE, self.PIXEL_SIZE)

                # A more formal system that doesn't rely on hardcoded variables or indices would make this easier, but we're doing this for now.
                # Assume Ezzy is always units[0] and the Monster is always units[1]
                if self.grid[i][j] == self.units[0]:
                    pygame.draw.rect(screen, (0, 0, 255), rect)
                elif self.grid[i][j] == self.units[1]:
                    pygame.draw.rect(screen, (255, 0, 0), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect, 1)
        self.sprite_group.draw(screen)

    
    def move_entity(self, destination):
        if destination[0] in range(self.width) and destination[1] in range(self.height):
            self.set_positions()
            return True
        else:
            return False