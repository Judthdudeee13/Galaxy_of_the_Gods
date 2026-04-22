from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, is_ground):
        super().__init__(groups)
        self.image = image
        self.rect = rect
        self.isGround = is_ground