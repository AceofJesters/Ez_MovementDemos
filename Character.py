class Character:

    def __init__(self, pos=(0, 0)):
        self.pos = pos

    def move(self, dir):
        old_pos = self.pos
        dx, dy = 0, 0
        if dir == "up":
            dy = -25
        elif dir == "down":
            dy = 25
        elif dir == "left":
            dx = -25
        elif dir == "right":
            dx = 25
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        if self.pos[0] not in range(0, 800):
            self.pos = (old_pos[0], self.pos[1])
        if self.pos[1] not in range(0, 600):
            self.pos = (self.pos[0], old_pos[1])
        return f"Player character moved to {self.pos}"