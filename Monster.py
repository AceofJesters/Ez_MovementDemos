import random
from pathfind import pathfind

MON_KEY = 2

class Monster:

    def __init__(self, pos=(0, 0)):
        self.pos = pos
        self.dest = pos
        self.path = []

    def move(self, Board):

        print("monpos is " + str(self.pos))
        print("mondest is " + str(self.dest))
        if self.pos != self.dest:
            # increment position along path by a random number between 1 and 3
            print(f"Monster is moving towards {self.dest}")
            return self.dest
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

            self.path = pathfind()


    def check_detection(self, player_pos):

        detection_range = 10

        # find distance between player and monster
        distance = ((self.pos[0] - player_pos[0]) ** 2 + (self.pos[1] - player_pos[1]) ** 2) ** 0.5

        if distance <= detection_range:
            self.dest = player_pos