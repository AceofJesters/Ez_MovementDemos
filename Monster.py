import random

class Monster:

    def __init__(self, pos=(0, 0)):
        self.pos = pos
        self.dest = pos

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

    
    def pathfind(self, target_pos):
        if self.pos[0] < target_pos[0]:
            return "right"
        elif self.pos[0] > target_pos[0]:
            return "left"
        elif self.pos[1] < target_pos[1]:
            return "down"
        elif self.pos[1] > target_pos[1]:
            return "up"
        else:
            return None


    def find_direction(self):
        dir = random.choice(["up", "down", "left", "right"])
        return dir

    
    def select_destination(self, SCREEN_WIDTH=800, SCREEN_HEIGHT=600):

        if self.pos != self.dest:
            print(f"Monster is moving towards {self.dest}")
            return self.dest

        else:

            wbound = SCREEN_WIDTH - 50
            hbound = SCREEN_HEIGHT - 50

            destx = random.randint(0, wbound)
            desty = random.randint(0, hbound)

            dir = self.find_direction()
            return dir


    def check_detection(self, player_pos):

        detection_range = 10

        # find distance between player and monster
        distance = ((self.pos[0] - player_pos[0]) ** 2 + (self.pos[1] - player_pos[1]) ** 2) ** 0.5

        if distance <= detection_range:
            self.dest = player_pos