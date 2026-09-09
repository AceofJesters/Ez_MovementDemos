from WorldObject import WorldObject

class Character(WorldObject):

    def __init__(self, pos=(0, 0)):
        super().__init__(pos)

    def move(self, Board, dir):
        old_pos = self.pos
        dx, dy = 0, 0
        if dir == "up":
            dy = -1
        elif dir == "down":
            dy = 1
        elif dir == "left":
            dx = -1
        elif dir == "right":
            dx = 1

        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

        if Board.move_entity(self.pos):
            return f"Player character moved to {self.pos}"
        else:
            self.pos = old_pos
            return old_pos