from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, is_ground):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(topleft = pos)
        self.isGround = is_ground

class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups):
        image = frames
        super().__init__(pos, image, groups, False)