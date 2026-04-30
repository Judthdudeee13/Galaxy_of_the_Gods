from settings import *
from sprites import *


# player sprite
class Player(MiltiDirectionalSprite):
    def __init__(self, pos, folders, groups, collision_sprites, health):
        animation_speed = 5.88
        super().__init__(pos, folders, groups, animation_speed)
        # movment
        self.speed = 80 * SCALE
        self.direction = pygame.Vector2(0, 0)
        self.facing = "down"
        self.collision_sprites = collision_sprites
        self.collision_rect = self.rect.inflate(-7*SCALE, -15*SCALE)
        self.health = health

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
        


class InfoBar(pygame.sprite.Sprite):
    def __init__(self, color, image, max, pos, groups, start = 0):
        super().__init__(groups)
        self.left, self.top = pos
        self.color = color
        self.logo = image
        self.max = max
        self.pos = pos
        self._current = start

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, value):
        self._current = max(0, min(value, self.max))

    def __call__(self):
        self._current

    def draw_rect(self):
        rect = pygame.FRect(5*SCALE, 5*SCALE, 50*SCALE, 5*SCALE)
        surface = pygame.Surface((rect.width+10*SCALE, rect.height+10*SCALE), pygame.SRCALPHA)
        pygame.draw.rect(
            surface, 
            (    max(0, self.color[0]-125), 
                 max(0, self.color[1]-125), 
                 max(0, self.color[2]-125)), 
             rect, 
             0, 
             10*SCALE)
        self.draw_bar(surface, rect)
        self.draw_image(surface, rect)
        self.image = surface
        self.rect = self.image.get_frect(topleft = (self.left, self.top))

    def draw_bar(self, surface, rect):
        ratio = rect.width / self.max
        progress_rect = pygame.FRect((5*SCALE, 5*SCALE), (self._current*ratio, rect.height))
        pygame.draw.rect(surface, self.color, progress_rect, 0, 10*SCALE)

    def draw_image(self, surface, rect):
        rect = self.logo.get_frect(center = (rect.left, rect.top+rect.height/2))
        surface.blit(self.logo, rect)

        

    def draw(self):
        self.draw_rect()

    def update(self):
        self.draw()