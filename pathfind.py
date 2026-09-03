def pathfind(start, goal):
    pass

    goaled = False
    current_node = Pathnode(start, None)

    while not goaled:
        pass

        
        # add each neighbour of current cell to open list w/ current node saved as parent
        neighbours_coords = get_neighbours(current_node.coords)
        # - for each neighbour
            # 	- ensure it's not on the open/closed list or a wall
            # 	- create new node with current node as parent, heuristic calculation, parent cost, and sum
            # 	- put neighbour in open list
        # put current cell in closed list
        # select cell in open list with lowest g-score
        # - make this the current node


def get_neighbours(coords):
    x, y = coords
    north = (x, y - 1)
    south = (x, y + 1)
    east = (x + 1, y)
    west = (x - 1, y)
    return [north, south, east, west]


class Pathnode:
    def __init__(self, coords, parent):
        self.coords = coords
        self.parent = parent
        self.distance = self.find_distance(coords, goal)


    def find_distance(self, coords, goal):
        diff_x = abs(coords[0] - goal[0])
        diff_y = abs(coords[1] - goal[1])
        return diff_x + diff_y