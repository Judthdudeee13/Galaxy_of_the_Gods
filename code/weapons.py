from settings import *
from timer import Timer
from sprites import *

class Weapon:
    def __init__(self, damage, range, cool_down, name = None, damage_type = None):
        self.damage = damage
        self.range = range
        self.damage_type = damage_type
        self.cool_down_timer = Timer(cool_down)
        self.name = name

    def deal_damage(self, target, direction=None):
        if not self.cool_down_timer:
            target.health -= self.damage
            if not self.cool_down_timer:
                self.cool_down_timer.activate()
            target.knockback(direction)
            
    def update(self, _):
        self.cool_down_timer.update()

class Arrow(Weapon, Sprite):
    def __init__(self, image, pos, direction, speed, damage, type, groups, enemies, collision):
        Sprite.__init__(self, pos, image, groups)
        Weapon.__init__(self, damage, 0, 0, type)
        self.enemies = enemies
        self.collisions = collision
        self.direction = direction
        self.speed = speed * SCALE
        self.rect.center = pos
        self.timer = Timer(5000, autostart=True ,func = self.kill)
        self.move(0.06)
        self.move(0.06)
        self.update(0.06)
        

    #if hits obsticle kills self
    def check_collision(self):
        collision = pygame.sprite.spritecollide(self, self.collisions, False, pygame.sprite.collide_mask)
        if collision:
            self.kill()

    #check collisions with enimes
    def check_attack(self):
        collisions  = pygame.sprite.spritecollide(self, self.enemies, False)
        if collisions:
            collision = pygame.sprite.spritecollide(self, collisions, False, pygame.sprite.collide_mask)
            if collision:
                for sprite in collision:
                    self.deal_damage(sprite, self.direction)
                    self.kill()

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt

    #updates sprite
    def update(self, dt):
        self.timer.update()
        self.move(dt)
        self.check_attack()
        self.check_collision()
        

#basic bow class
class Bow(pygame.sprite.Sprite):
    def __init__(self, damage, cool_down, images, arrow, player, target, groups, enemies, collisions, name, fix = 180, distance = 10, damage_type=None):
        #adds self to allsprites
        super().__init__(groups)
        #checks to see if screen has an offset for position to place bow and arc correctly
        for group in self.groups():
            if hasattr(group, "offset"):
                self.offset_group = group

        #add name
        self.name = name

        #ranged def
        self.ranged = True
        
        #animation
        self.animation_speed = 3
        self.frame = -1
        self.image = images[self.frame]
        self.surf = images[self.frame]
        self.images = images
        self.center = self.surf.get_frect()

        #arrow setup
        self.arrow = arrow
        self.damage = damage
        self.cool_down = cool_down
        self.damage_type = damage_type
        self.isShoot = True
        self.angle = 0
        self.group = groups
        self.enemies = enemies
        self.collisions = collisions

        # bow direction setup
        self.player = player
        self.target = target
        self.fix = fix
        self.distance = distance*SCALE
        self.direction = pygame.Vector2(0, 0)
        
        #animation timer
        self.attack_timer = False

    def update_offset(self):
        self.offset = self.offset_group.offset

    def update_groups(self):
        for group in self.groups():
            if hasattr(group, "offset"):
                self.offset_group = group
        self.group = self.groups()

    def aim(self):
        #update offset
        self.update_offset()
        #if target is mouse (for player)
        if self.target == 'Mouse':
            pos = pygame.Vector2(pygame.mouse.get_pos())
            player = self.player.center + self.offset
            self.direction = (pos-player).normalize() if (pos-player) else pygame.Vector2(0,0)
            self.angle = degrees(atan2(self.direction.x, self.direction.y))- self.fix
            self.image = pygame.transform.rotozoom(self.surf, self.angle, 1)
            self.rect = self.image.get_frect()
        #if target is monsters or player
        #FINISH LATER
        else:
            pass

    #creat arrow sprite
    def create_arrow(self):
        Arrow(pygame.transform.rotozoom(self.arrow, self.angle+180, 1), self.rect.center, self.direction, 200, self.damage, self.damage_type, self.group, self.enemies, self.collisions)

    #if space key is pressed will work into player class
    def _attack(self, dt):
        self.frame = (self.frame + self.animation_speed * dt) % len(self.images)
        try:
            self.surf = self.images[int(self.frame)]
        except:
            self.surf = self.image[-1]
        if self.surf == self.images[-1] and not self.isShoot:
            self.create_arrow()
            self.isShoot = True
        if self.surf == self.images[-2]:
            self.isShoot = False
            self.frame += 1
            
    def attack(self):
        self.attack_timer = True

    def draw(self):
        self.aim()
        self.center.center = self.player.center + self.direction * self.distance
        self.rect.center = self.center.center

    def update(self, dt):
        if self.attack_timer or self.frame > 3:
             self._attack(dt)
        else:
            self.surf = self.images[-1]
            self.frame = -1
        self.attack_timer = False
        self.draw()


class Spear(Weapon, pygame.sprite.Sprite):
    def __init__(self, damage, range, cool_down, damage_type, images, groups, strenght, player, enemies, name):
        Weapon.__init__(self, damage, range, cool_down, name, damage_type)
        pygame.sprite.Sprite.__init__(self, groups)
        self.isAttacking = False
        self.images = images
        self.strenght = strenght
        self.direction = pygame.Vector2(0, 0)
        self.player = player
        self.melee = True
        self.enemies = enemies
        self.cool_down = Timer(cool_down)
        
        #animation
        self.animation_speed = 20
        self.frame = 0
        self.image = self.images[int(self.frame)]
        self.rect = self.image.get_frect(midleft = self.player.rect.midright)
        

    def attack(self, direction):
        if not self.cool_down:
            self.isAttacking = True
            self.cool_down.activate()

            if direction:
                if abs(direction.x) > abs(direction.y):
                    if direction.x > 0:
                        self.direction.x = 1
                        self.direction.y = 0
                    
                    else:
                        self.direction.x = -1
                        self.direction.y = 0
                else:      
                    if direction.y > 0:
                        self.direction.x = 0
                        self.direction.y = 1
                    else:
                        self.direction.x = 0
                        self.direction.y = -1
                    
            self.player.rect.x += self.direction.x * self.strenght*SCALE
            self.player.rect.y += self.direction.y * self.strenght*SCALE
        
    def _attack(self, dt):
        if self.isAttacking:
            self.frame += (self.animation_speed * dt) % len(self.images)
            self.image = self.images[int(self.frame)]
            if self.image == self.images[-1]:
                self.isAttacking = False
                
    def rotate(self):
        if self.direction.y > 0:
            self.image = pygame.transform.rotozoom(self.image, 180, 1)
            self.rect = self.image.get_frect()
            self.rect.midtop = self.player.rect.midbottom
        elif self.direction.x > 0 :
            self.image = pygame.transform.rotozoom(self.image, 270, 1)
            self.rect = self.image.get_frect()
            self.rect.midleft = self.player.rect.midright
        elif self.direction.x < 0 :
            self.image = pygame.transform.rotozoom(self.image, 90, 1)
            self.rect = self.image.get_frect()
            self.rect.midright = self.player.rect.midleft
        else:
            self.rect = self.image.get_frect()
            self.rect.midbottom = self.player.rect.midtop
        
    def check_attack(self):
        collisions  = pygame.sprite.spritecollide(self, self.enemies, False)
        if collisions:
            collision = pygame.sprite.spritecollide(self, collisions, False, pygame.sprite.collide_mask)
            if collision:
                for sprite in collision:
                    self.deal_damage(sprite, self.direction)
    
    def update_groups(self):
        pass
            
    def update(self, dt):
        self.cool_down.update()
        self.cool_down_timer.update()
        if self.isAttacking:
            self._attack(dt)
            self.rotate()
            self.check_attack()
        else:
            self.frame = 0
            self.image = self.images[self.frame]
            self.rect = self.image.get_frect(midleft = self.player.rect.midright)
        
        
