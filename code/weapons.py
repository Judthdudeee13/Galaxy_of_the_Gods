from settings import *
from timer import Timer
from sprites import *

class Weapon:
    def __init__(self, damage, range, cool_down, damage_type = None):
        self.damage = damage
        self.range = range
        self.damage_type = damage_type
        self.cool_down_timer = Timer(cool_down)

    def deal_damage(self, target):
        if not self.cool_down_timer:
            target.health -= self.damage
            self.cool_down_timer.activate()
            
    def update(self):
        self.cool_down_timer.update()

class Arrow(Weapon, Sprite):
    def __init__(self, image, pos, direction, speed, damage, type, groups):
        Sprite.__init__(pos, image, groups)

class Bow(pygame.sprite.Sprite):
    def __init__(self, damage, cool_down, images, arrow, player, target, groups, fix = 180, distance = 10, damage_type=None):
        super().__init__(groups)
        for group in self.groups():
            if hasattr(group, "offset"):
                self.offset_group = group
        self.frame = -1
        self.image = images[self.frame]
        self.surf = images[self.frame]
        self.images = images
        self.center = self.surf.get_frect()
        self.arrow = arrow
        self.damage = damage
        self.cool_down = cool_down
        self.damage_type = damage_type
        self.player = player
        self.target = target
        self.fix = fix
        self.isGround = False
        self.distance = distance*SCALE
        self.direction = pygame.Vector2(0, 0)
        self.animation_speed = 1
        self.isShoot = False
        self.angle = 0
        self.group = group
        self.rect = self.image.get_frect(center = (self.player.centerx + 10*SCALE, self.player.centery + 10*SCALE))

    def update_offset(self):
        self.offset = self.offset_group.offset

    def aim(self):
        self.update_offset()
        if self.target == 'Mouse':
            pos = pygame.Vector2(pygame.mouse.get_pos())
            player = self.player.center + self.offset
            self.direction = (pos-player).normalize() if (pos-player) else pygame.Vector2(0,0)
            self.angle = degrees(atan2(self.direction.x, self.direction.y))- self.fix
            self.image = pygame.transform.rotozoom(self.surf, self.angle, 1)
            self.rect = self.image.get_frect()
            

        else:
            pass

    def create_arrow(self):
        Arrow(pygame.transform.rotozoom(self.arrow, self.angle, 1), self.rect.center, self.direction, 100, self.damage, self.damage_type, self.group)
        print('worked')

    def attack(self, dt):
        self.frame = (self.frame + self.animation_speed * dt) % len(self.images)
        self.surf = self.images[int(self.frame)]
        if self.surf == self.images[-2] and not self.isShoot:
            self.create_arrow()
            self.isShoot = True
        if self.surf == self.images[-1]:
            self.isShoot = False

    def draw(self):
        self.aim()
        self.center.center = self.player.center + self.direction * self.distance
        self.rect.center = self.center.center

    def update(self, dt):
        self.attack(dt)
        self.draw()


        
