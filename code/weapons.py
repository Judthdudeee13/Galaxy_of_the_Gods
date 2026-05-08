from settings import *
from timer import Timer

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

class Arrow(Weapon, pygame.sprite.Sprite):
    def __init__(self, image, ):
        pass

class Bow(pygame.sprite.Sprite):
    def __init__(self, damage, cool_down, image, arrow, player, target, groups, fix = 90, distance = 10, damage_type=None):
        super().__init__(groups)
        self.image = image
        self.surf = image
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
        self.rect = self.image.get_frect(center = (self.player.centerx + 10*SCALE, self.player.centery + 10*SCALE))

    def aim(self):
        if self.target == 'Mouse':
            pos = pygame.Vector2(pygame.mouse.get_pos())
            player = pygame.Vector2(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
            self.direction = (player-pos).normalize() if (player-pos) else pygame.Vector2(0,0)
            angle = degrees(atan2(self.direction.x, self.direction.y))- self.fix
            self.image = pygame.transform.rotozoom(self.surf, angle, 1)
            self.image = pygame.transform.flip(self.image, False, True)
            

        else:
            pass

    def draw(self):
        self.aim()
        self.rect.center = self.player.center + self.direction * self.distance

    def update(self, dt):
        self.draw()


        
