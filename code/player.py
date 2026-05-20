from settings import *
from sprites import *
from weapons import *


# player sprite
class Player(MiltiDirectionalSprite):
    def __init__(self, pos, folders, groups, collision_sprites, weapon_sprites, enemies, health):
        animation_speed = 5.88
        super().__init__(pos, folders, groups, animation_speed)
        # movment
        self.speed = 80 * SCALE
        self.direction = pygame.Vector2(0, 0)
        self.facing = "down"
        self.collision_sprites = collision_sprites
        self.collision_rect = self.rect.inflate(-7*SCALE, -15*SCALE)
        self._health = health
        self.weapon_group = pygame.sprite.Group()
        self.weapon = [Bow(10, 1000, weapon_sprites['Bow']['Bow'], weapon_sprites['Bow']['Arrow'], self.rect, "Mouse", self.weapon_group, enemies, collision_sprites), Spear(10, 0, 2, 'Normal', weapon_sprites['Spear']['Spear'], self.weapon_group, 100, self)]
        self.current_weapon = self.weapon[0]
        self.current_groups = groups
        self.current_weapon.add(self.current_groups)
        self.current_weapon.update_groups()
        

    @property
    def health(self):
        return self._health.current

    @health.setter
    def health(self, value):
        self._health.current = value

    def knockback(self, _):
        pass

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )

        if keys[pygame.K_SPACE]:
            if hasattr(self.current_weapon, 'melee'):
                self.current_weapon.attack()

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            if hasattr(self.current_weapon, 'ranged'):
                self.current_weapon.attack()
        

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
        nearby_area = self.rect.inflate(96 * SCALE, 96 * SCALE)
        for sprite in self.collision_sprites:
            if self == sprite:
                continue
			
            if not sprite.rect.colliderect(nearby_area):
                continue

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
        self._max = max
        self.pos = pos
        self._current = start
        self.vrect = pygame.FRect(5*SCALE, 5*SCALE, 50*SCALE, 5*SCALE)
        surface = pygame.Surface((self.vrect.width+10*SCALE, self.vrect.height+10*SCALE), pygame.SRCALPHA)
        self.image = surface
        self.rect = self.image.get_frect(topleft = (self.left, self.top))
        self.ratio = self.vrect.width / self._max

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, value):
        self._current = max(0, min(value, self.max))

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
        self.update_max()

    def __call__(self):
        self._current

    def update_max(self):
        self.ratio = self.vrect.width / self._max

    def draw_rect(self):
        pygame.draw.rect(
            self.image, 
            (    max(0, self.color[0]-125), 
                 max(0, self.color[1]-125), 
                 max(0, self.color[2]-125)), 
             self.vrect, 
             0, 
             10*SCALE)
        self.draw_bar()
        self.draw_image()
        
        
    def draw_bar(self):
        progress_rect = pygame.FRect((5*SCALE, 5*SCALE), (self._current*self.ratio, self.vrect.height))
        pygame.draw.rect(self.image, self.color, progress_rect, 0, 10*SCALE)

    def draw_image(self):
        rect = self.logo.get_frect(center = (self.vrect.left, self.vrect.top+self.vrect.height/2))
        self.image.blit(self.logo, rect)

    def update(self):
        self.image.fill((0, 0, 0, 0))
        self.draw_rect()

    
