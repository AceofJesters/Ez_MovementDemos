def pathfind(start, goal):
    pass

    goaled = False
    current_node = Pathnode(start, None)

    while not goaled:
        pass

        
        # add each neighbour of current cell to open list w/ current node saved as parent
        neighbours_coords = get_neighbours(current_node.coords)
        # - for each neighbour
        for neighbour in neighbours_coords:
            # 	- ensure it's not on the open/closed list or a wall
            if neighbour not in open_list and neighbour not in closed_list and neighbour not in walls:
            # 	- create new node with current node as parent, heuristic calculation, parent cost, and sum
                new_node = Pathnode(neighbour, current_node)
            # 	- put neighbour in open list
                open_list.append(new_node)
        # put current cell in closed list
        closed_list.append(current_node)
        # select cell in open list with lowest g-score
        current_node = min(open_list, key=lambda node: node.distance)


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


path = pathfind((0, 0), (5, 5))