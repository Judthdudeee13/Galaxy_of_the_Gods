from settings import *
from sprites import *

#player sprite
class Player(MiltiDirectionalSprite):
    def __init__(self, pos, folders, groups):
        animation_speed = 7
        super().__init__(pos, folders, groups, animation_speed, idle_animation_seed)
        #movment
        self.speed = 100 * SCALE
        self.direction = pygame.Vector2(0, 0)
        self.facing = 'down'

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
        if self.direction:
            if self.direction.x:
                if self.direction.x > 0:
                    self.facing = 'right'
                else:
                    self.facing = 'left'
            elif self.direction.y:
                if self.direction.y > 0 :
                    self.facing = 'down'
                else:
                    self.facing = 'up'
        else:
            if self.facing == 'right':
                self.facing = 'idle_right'
            elif self.facing == 'left':
                self.facing = 'idle_left'
            elif self.facing == 'up':
                self.facing = 'idle_up'
            elif self.facing == 'down':
                self.facing = 'idle_down'
        
        self.update_direction(self.facing)

    def draw(self, dt):
        self.direction_check()
        self.animate(dt)
        

    def check_collision(self, direction):
        pass

    def update(self, dt):
        self.input()
        self.move(dt)
        self.draw(dt)
