import random
from pathfind import pathfind

MON_KEY = 2

class Monster:

# TODO: Why are you moving down your path backwards that's fucked up stop that

    def __init__(self, pos=(0, 0), dest=(10, 10), Board=None):
        self.pos = pos
        self.dest = dest
        self.path = pathfind(self.pos, self.dest)

    def move(self, Board, player_pos):

        if self.check_detection(player_pos):
            self.dest = player_pos
            self.path = pathfind(self.pos, self.dest)
        if len(self.path) > 0:
            # increment position along path by a random number between 1 and 3
            print(f"Monster is moving towards {self.dest}")
            self.pos = self.path.pop()
            return self.pos
        else:
            self.select_destination(Board)

    
    def select_destination(self, Board):
            valid_pos = False

            while not valid_pos:
                destx = random.randint(0, Board.width)
                desty = random.randint(0, Board.height)
                if Board.move_entity(MON_KEY, self.pos):
                    valid_pos = True
                    self.dest = (destx, desty)

            self.path = pathfind(self.pos, self.dest)


    def check_detection(self, player_pos):

        detection_range = 10

        # find distance between player and monster
        distance = ((self.pos[0] - player_pos[0]) ** 2 + (self.pos[1] - player_pos[1]) ** 2) ** 0.5

        if distance <= detection_range:
            self.dest = player_pos