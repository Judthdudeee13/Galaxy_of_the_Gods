from settings import *
from sprites import *


# player sprite
class Player(MiltiDirectionalSprite):
    def __init__(self, pos, folders, groups, collision_sprites):
        animation_speed = 5.88
        super().__init__(pos, folders, groups, animation_speed)
        # movment
        self.speed = 80 * SCALE
        self.direction = pygame.Vector2(0, 0)
        self.facing = "down"
        self.collision_sprites = collision_sprites
        self.collision_rect = self.rect.inflate(-7*SCALE, -15*SCALE)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )

    def move(self, dt):
        self.collision_rect.x += self.direction.x * self.speed * dt
        self.check_collision("horizontal")
        self.collision_rect.y += self.direction.y * self.speed * dt
        self.check_collision("vertical")

    def direction_check(self):
        if self.direction:
            if self.direction.x:
                if self.direction.x > 0:
                    self.facing = "right"
                else:
                    self.facing = "left"
            elif self.direction.y:
                if self.direction.y > 0:
                    self.facing = "down"
                else:
                    self.facing = "up"
        else:
            if self.facing == "right":
                self.facing = "idle_right"
            elif self.facing == "left":
                self.facing = "idle_left"
            elif self.facing == "up":
                self.facing = "idle_up"
            elif self.facing == "down":
                self.facing = "idle_down"

        self.update_direction(self.facing)

    def draw(self, dt):
        self.direction_check()
        self.animate(dt)

    def check_collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.collision_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0:
                        self.collision_rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.collision_rect.left = sprite.rect.right
                if direction == 'vertical':
                    if self.direction.y > 0:
                        self.collision_rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.collision_rect.top = sprite.rect.bottom
        self.rect.center = self.collision_rect.center

    def update(self, dt):
        self.input()
        self.move(dt)
        self.draw(dt)
