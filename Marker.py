from WorldObject import WorldObject
import pygame

# An object marking a physical location
# Cannot be moved once created (for now)
class Marker(pygame.sprite.Sprite, WorldObject):

    def __init__(self, pos=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        WorldObject.__init__(self, pos)
        
        # Visual indicator
        self.image = pygame.transform.scale_by(pygame.image.load("FuckassEvilGuy.jpg"), 0.2).convert_alpha()

        self.rect = self.image.get_rect()
        
        # Convert grid space into raw pixels
        self.rect.topleft = (self.pos[0]*5, self.pos[1]*5)
    


