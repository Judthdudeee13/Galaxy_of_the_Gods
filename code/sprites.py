from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, is_ground):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(topleft = pos)
        self.isGround = is_ground

class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups, animation_speed):
        image = frames[0]
        super().__init__(pos, image, groups, False)
        self.frames = frames
        self.animation_speed = animation_speed
        self.frame_index = 0

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index%len(self.frames))]

class MiltiDirectionalSprite(AnimatedSprite):
    def __init__(self, pos, folders, groups, animation_speed, sprint = False):
        super().__init__(pos, folders['down'], groups, animation_speed)
        self.folders = folders

    def update_direction(self, direction):
        self.frames = self.folders[direction]
