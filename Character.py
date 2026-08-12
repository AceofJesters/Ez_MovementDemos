class Character:

    def __init__(self, pos=(0, 0)):
        self.pos = pos

    def move(self, dir):
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
        return f"Player character moved to {self.pos}"