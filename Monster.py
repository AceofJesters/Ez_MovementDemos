import random

class Monster:

    def __init__(self, pos=(0, 0)):
        self.pos = pos

    def move(self, dir):
        old_pos = self.pos
        dx, dy = 0, 0
        if dir == "up":
            dy = -50
        elif dir == "down":
            dy = 50
        elif dir == "left":
            dx = -50
        elif dir == "right":
            dx = 50
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        if self.pos[0] not in range(0, 800 - 50):
            self.pos = (old_pos[0], self.pos[1])
        if self.pos[1] not in range(0, 600 - 50):
            self.pos = (self.pos[0], old_pos[1])
        return f"Monster moved to {self.pos}"
    
    def select_destination(self, SCREEN_WIDTH=800, SCREEN_HEIGHT=600):
        wbound = SCREEN_WIDTH - 50
        hbound = SCREEN_HEIGHT - 50

        dir = random.choice(["up", "down", "left", "right"])
        return dir