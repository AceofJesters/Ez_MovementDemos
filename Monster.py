from collections import deque

from pathfind import pathfind
from WorldObject import WorldObject

class Monster(WorldObject):

    def __init__(self, pos=(0, 0)):
        super().__init__(pos)
        self.dest = pos
        self.path = deque

    def move(self, Board):
        # Multiple movements is handled in the main loop. This is just the logic for individual movements.

        print("monpos is " + str(self.pos))
        print("mondest is " + str(self.dest))
        if self.pos != self.dest:

            if len(self.path) != 0:
                self.pos = self.path.pop()
                if(Board.move_entity(self.pos)):
                    print(f"Monster has moved to {self.dest}") 

            
            return self.dest

    
    def select_destination(self, Board, world_object):
            
            target = world_object.get_position()
            print("monster targetting " + str(target))

            self.dest = (target[0], target[1])

            self.path = pathfind(self.pos, self.dest)
            print(str(self.path))



    def check_detection(self, player_pos):

        detection_range = 10

        # find distance between player and monster
        distance = ((self.pos[0] - player_pos[0]) ** 2 + (self.pos[1] - player_pos[1]) ** 2) ** 0.5

        if distance <= detection_range:
            self.dest = player_pos