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


class InfoBar(pygame.sprite.Sprite):
    def __init__(self, color, image, max, pos, groups, start = 0):
        super().__init__(groups)
        self.left, self.top = pos
        self.color = color
        #self.image = image
        self.max = max
        self.pos = pos
        self._current = start

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, value):
        self._current = max(0, min(self.current, self.max))

    def draw_rect(self):
        rect = pygame.FRect(0, 0, 50*SCALE, 5*SCALE)
        surface = pygame.Surface((rect.width+10*SCALE, rect.height+10*SCALE), pygame.SRCALPHA)
        pygame.draw.rect(surface, (100, 0, 0), rect, 0, 10*SCALE)
        self.draw_bar(surface, rect)
        self.image = surface
        self.rect = self.image.get_frect(topleft = (self.left, self.top))

    def draw_bar(self, surface, rect):
        ratio = rect.width / self.max
        progress_rect = pygame.FRect((0, 0), (self._current*ratio, rect.height))
        pygame.draw.rect(surface, self.color, progress_rect)

        

    def draw(self):
        self.draw_rect()

    def update(self):
        self.draw()

'''
rect = pygame.FRect(self.left, self.top, 250, 80)
pygame.draw.rect(self.window, COLORS['white'], rect, 0, 4)
pygame.draw.rect(self.window, COLORS['gray'], rect, 4, 4)

#data
name_surf = self.font.render(self.monster.name, True, COLORS['black'])
name_rect = name_surf.get_frect(topleft = rect.topleft + pygame.Vector2(rect.width*0.05, 12))
self.window.blit(name_surf, name_rect)

#health bar
health_rect = pygame.FRect(name_rect.left, name_rect.bottom + 10, rect.width * 0.9, 20)
pygame.draw.rect(self.window, COLORS['gray'], health_rect)
self.draw_bar(health_rect, self.monster.health, self.monster.max_health)

def draw_bar(self, rect, value, max_value):
ratio = rect.width / max_value
progress_rect = pygame.FRect(rect.topleft, (value*ratio, rect.height))
pygame.draw.rect(self.window, COLORS['red'], progress_rect)
'''