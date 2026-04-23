from settings import *
from sprites import *

#player sprite
class Player(MultiDirectionalSprite):
    def __init__(self, pos, frames, groups):
        animation_speed = 5
        super().__init__(pos, frames, groups, animation_speed)
        #movment
        self.speed = 200 * SCALE
        self.direction = pygame.Vector2(0, 0)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt 
        self.check_collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt 
        self.check_collision('vertical')

    def 

    def check_collision(self, direction):
        pass

    def update(self, dt):
        self.input()
        self.move(dt)
