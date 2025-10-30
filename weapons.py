import pygame, time

#setup pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()


GAME_DEVELOPER_MACANICS = True

#set height and width
HEIGHT = 700
WIDTH = 1300

#set up window  
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('game')
keys = pygame.key.get_pressed()

#set up fonts
basic = pygame.font.SysFont(None, 75)
datas = pygame.font.SysFont(None, 25)
important = pygame.font.SysFont(None, 90)

BG = "#ebab34"
RED = '#FF0000'
GREEN = '#00ff00'
BLACK = "#000000"
WHITE = "#FFFFFF"
swing= False


class weapon:
    def __init__(self):
        pass
    def set_up(self, reload_time, ammo, damage, direction, range, starting_time):
        self.reload_time = reload_time
        self.ammo = ammo
        self.damage = damage
        self.direction = direction
        self.range = range
        self.reload_time_cooldown = time.time()
        self.starting_time = starting_time 
        self.attack_image = -1
        self.x = 0
        self.y= 0



class melee(weapon):
    def attack(self, inventory, direction, p, current_weapon, space, background):
        self.hit_box_im = pygame.image.load("weapons/melee_AOE.png")
        self.hit_box_im = pygame.transform.scale(self.hit_box_im, (self.range, self.range))
        self.hit_box_pos = self.hit_box_im.get_rect()
        self.hit_box_sur = pygame.mask.from_surface(self.hit_box_im)
        if inventory['sword'][1] == 'basic_sword' and current_weapon == 'basic_sword':
            if abs(self.reload_time_cooldown-time.time()) >= self.reload_time and self.attack_image <= 0 and space:
                self.attack_image = self.starting_time
                self.reload_time_cooldown = time.time()


            if self.attack_image > 0:
                self.attack_image -= 1
                if direction == 'up':
                    self.hit_box_pos.x = p.x+12
                    self.hit_box_pos.y = p.y-15
                    hit_box_blit180 = pygame.transform.rotate(self.hit_box_im, 180)
                    window.blit(hit_box_blit180, self.hit_box_pos)
                if direction == 'down':
                    self.hit_box_pos.x = p.x+12
                    self.hit_box_pos.y = p.y+40
                    hit_box_blit0 = pygame.transform.rotate(self.hit_box_im, 0)
                    window.blit(hit_box_blit0, self.hit_box_pos)
                if direction == 'left' or direction == 'None':
                    self.hit_box_pos.x = p.x-12
                    self.hit_box_pos.y = p.y+12
                    hit_box_blit270 = pygame.transform.rotate(self.hit_box_im, 270)
                    window.blit(hit_box_blit270, self.hit_box_pos)
                if direction == 'right':
                    self.hit_box_pos.x = p.x+42
                    self.hit_box_pos.y = p.y+12
                    hit_box_blit90 = pygame.transform.rotate(self.hit_box_im, 90)
                    window.blit(hit_box_blit90, self.hit_box_pos)
                return  self.hit_box_sur, self.hit_box_pos, self.damage, self.hit_box_im, self.attack_image, self.starting_time

            else:
                return self.hit_box_sur, self.hit_box_pos, self.damage, self.hit_box_im, -1, self.starting_time
        else:
            return self.hit_box_sur, self.hit_box_pos, self.damage, self.hit_box_im, -1, self.starting_time





class ranged(weapon):
    def set_up1(self, arrow_size, image):
        self.arrow_size = arrow_size
        self.left = -1000
        self.top = -1000
        self.bow = pygame.image.load(image)
        self.bow = pygame.transform.scale_by(self.bow, (1.5, 1.5))
        self.bow_rect = self.bow.get_rect()
        self.arrow_direction = 'up'  
        self.arrow_im = pygame.image.load('weapons/basic_arrow.png')
        self.arrow_im = pygame.transform.scale(self.arrow_im, self.arrow_size)
        self.arrow = pygame.transform.scale(self.arrow_im, self.arrow_size)
        self.arrow_sur = pygame.mask.from_surface(self.arrow_im)
        self.arrow_rect = self.arrow.get_rect()
    def blit(self, playerx, playery, direction, inventory, current_weapon):
        if inventory['range'][1] == 'basic_bow' and current_weapon == 'basic_bow':
            if direction == 'up':
                    self.bow_rect.centerx = playerx+13
                    self.bow_rect.centery = playery+10
                    hit_box_blit180 = pygame.transform.rotate(self.bow, 90)
                    window.blit(hit_box_blit180, self.bow_rect)
            if direction == 'down':
                    self.bow_rect.centerx = playerx+13
                    self.bow_rect.centery = playery+60
                    hit_box_blit0 = pygame.transform.rotate(self.bow, 270)
                    window.blit(hit_box_blit0, self.bow_rect)
            if direction == 'left' or direction == 'None':
                    self.bow_rect.centerx = playerx-3
                    self.bow_rect.centery = playery+25
                    hit_box_blit270 = pygame.transform.rotate(self.bow, 180)
                    window.blit(hit_box_blit270, self.bow_rect)
            if direction == 'right':
                    self.bow_rect.centerx = playerx+52
                    self.bow_rect.centery = playery+25
                    hit_box_blit90 = pygame.transform.rotate(self.bow, 0)
                    window.blit(hit_box_blit90, self.bow_rect)
    def attack(self, inventory, direction, player, current_weapon, space, background):
        self.arrow_sur = pygame.mask.from_surface(self.arrow_im)
        self.arrow_rect = self.arrow_im.get_rect()
        if inventory['range'][1] == 'basic_bow' and current_weapon == 'basic_bow':
            if abs(self.reload_time_cooldown-time.time()) >= self.reload_time and self.attack_image <= 0 and space:
                self.attack_image = self.starting_time
                self.reload_time_cooldown = time.time()
                self.x = 0
                self.y = 0
                if direction == 'up':
                        self.x = player.x+25
                        self.y = player.y-5
                        self.arrow_im = pygame.transform.rotate(self.arrow, 0)
                        self.arrow_rect = self.arrow_im.get_rect()
                        self.arrow_direction = 'up'
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if direction == 'down':
                        self.x = player.x+25
                        self.y = player.y+55
                        self.arrow_direction = 'down'
                        self.arrow_im = pygame.transform.rotate(self.arrow, 180)
                        self.arrow_rect = self.arrow_im.get_rect()
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if direction == 'left' or direction == 'None':
                        self.x = player.x-11
                        self.y = player.y+30
                        self.arrow_direction = 'left'
                        self.arrow_im = pygame.transform.rotate(self.arrow, 90)
                        self.arrow_rect = self.arrow_im.get_rect()
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if direction == 'right':
                        self.x = player.x+52
                        self.y = player.y+30
                        self.arrow_direction = 'right'
                        self.arrow_im = pygame.transform.rotate(self.arrow, 270)
                        self.arrow_rect = self.arrow_im.get_rect()
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, self.attack_image, self.starting_time


            elif self.attack_image > 0:
                up = True
                down = True
                right = True
                left = True
                for hit_box in background.hit_boxes:
                    print(hit_box)
                    for i in range(4):
                        print(self.x)
                        print(self.y)
                        if self.x >= hit_box[i][0] and self.x <= hit_box[i][1]-50 and self.y >= hit_box[i][2] and self.y <= hit_box[i][3]:
                            if i == 0:
                                left = False
                            if i == 1:
                                right = False
                            if i == 2:
                                up = False
                            if i == 3:
                                 down = False

                
                self.attack_image -= 1
                if self.arrow_direction == 'up' and up:
                        self.y -= 10
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if self.arrow_direction == 'down' and down:
                        self.y += 10
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if self.arrow_direction == 'left' and left or self.arrow_direction == 'None':
                        self.x-=10
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if self.arrow_direction == 'right' and right:
                        self.x+=10
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)


                if self.arrow_direction == 'up':
                        self.y -= 0
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if self.arrow_direction == 'down':
                        self.y += 0
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if self.arrow_direction == 'left' or self.arrow_direction == 'None':
                        self.x-=0
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                if self.arrow_direction == 'right':
                        self.x+=0
                        self.arrow_rect.left = self.x
                        self.arrow_rect.top = self.y
                        window.blit(self.arrow_im, self.arrow_rect)
                rect = pygame.draw.rect(window, '#000000', self.arrow_rect)
                return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, self.attack_image, self.starting_time
            else:
                return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, -1, self.starting_time
        else:
             return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, -1, self.starting_time

