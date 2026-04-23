from settings import *
from sprites import *

#player sprite
class Player(MiltiDirectionalSprite):
    def __init__(self, pos, folders, groups):
        animation_speed = 8
        super().__init__(pos, folders, groups, animation_speed)
        #movment
        self.speed = 100 * SCALE
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

    def direction_check(self):
        if self.direction.x:
            if self.direction.x > 0:
                self.update_direction('right')
            else:
                self.update_direction('left')
        elif self.direction.y:
            if self.direction.y > 0 :
                self.update_direction('down')
            else:
                self.update_direction('up')

    def draw(self, dt):
        self.direction_check()
        self.animate(dt)
        

    def check_collision(self, direction):
        pass

    def update(self, dt):
        self.input()
        self.move(dt)
        self.draw(dt)
