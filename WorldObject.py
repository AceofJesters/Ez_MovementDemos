class WorldObject():

    def __init__(self, pos=(0,0)):
        self.pos = pos

    # Useful for path-finding. The monster could target any given object's position
    def get_position(self):
        return self.pos

    # Breaks encapsulation, but we're not shooting for good code (famous last words before trying to expand the codebase)
    def set_position(self, pos):
        self.pos = pos
    


        
