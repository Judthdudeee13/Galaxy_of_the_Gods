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
attack_image = 0

class weapon:
    def __init__(self):
        pass
    def set_up(self, reload_time, ammo, damage, direction, range):
        self.reload_time = reload_time
        self.ammo = ammo
        self.damage = damage
        self.direction = direction
        self.range = range
        self.reload_time_cooldown = time.time()



class melee(weapon):
    def attack(self):
        if self.reload_time_cooldown - self.reload_time > 0:
            hit_box_im = pygame.image.load("melee_AOE.png")
            hit_box_im = pygame.transform.scale(hit_box_im, (self.range, self.range))
            hit_box_pos = hit_box_im.get_rect()
            hit_box_sur = pygame.mask.from_surface(hit_box_im)
            self.swing = True
            return hit_box_sur, hit_box_pos, self.damage, hit_box_im, self.reload_time

        
    def swing_blit(self, inventory, direction, p):
        hit_box_sur, hit_box_pos, damage, hit_box_im, relod_time = self.attack()
        self.swing = False
        global attack_image
        if inventory['sword'][1] == 'basic_sword':
            hit_box_sur10, hit_box_pos, damage_given, hit_box, reload_time1 = self.attack()
            if abs(self.reload_time_cooldown-time.time()) >= reload_time1:
                print(1)
                attack_image = 3
                hit_box_blit1 = hit_box
                hit_box_blit = hit_box
                hit_box_pos2 = hit_box_pos
                hit_box_sur = hit_box_sur10
                reload_time2 = reload_time1
                if direction == 'up':
                    hit_box_pos.x = p.x+12
                    hit_box_pos.y = p.y-15
                if direction == 'down':
                    hit_box_pos.x = p.x+12
                    hit_box_pos.y = p.y+40
                if direction == 'left' or direction == 'None':
                    hit_box_pos.x = p.x-12
                    hit_box_pos.y = p.y+12
                if direction == 'right':
                    hit_box_pos.x = p.x+42
                    hit_box_pos.y = p.y+12
                
                self.reload_time_cooldown = time.time()


        if attack_image > 0:
            attack_image -= 1
            try:
                hit_box_blit1 = hit_box_blit
                hit_box_pos1 = hit_box_pos2
                hit_box_sur1 = hit_box_sur
            except:
                hit_box_blit1 = hit_box_blit1
                hit_box_pos1 = hit_box_pos1
                hit_box_sur1 = hit_box_sur1

            if direction == 'up':
                hit_box_pos1.x = p.x+12
                hit_box_pos1.y = p.y-15
                hit_box_blit180 = pygame.transform.rotate(hit_box_blit1, 0)
                window.blit(hit_box_blit180, hit_box_pos1)
            if direction == 'down':
                hit_box_pos1.x = p.x+12
                hit_box_pos1.y = p.y+40
                hit_box_blit0 = pygame.transform.rotate(hit_box_blit1, 180)
                window.blit(hit_box_blit0, hit_box_pos1)
            if direction == 'left' or direction == 'None':
                hit_box_pos1.x = p.x-12
                hit_box_pos1.y = p.y+12
                hit_box_blit270 = pygame.transform.rotate(hit_box_blit1, 90)
                window.blit(hit_box_blit270, hit_box_pos1)
            if direction == 'right':
                hit_box_pos1.x = p.x+42
                hit_box_pos1.y = p.y+12
                hit_box_blit90 = pygame.transform.rotate(hit_box_blit1, 270)
                window.blit(hit_box_blit90, hit_box_pos1)
        return  hit_box_sur, hit_box_pos, damage, hit_box_im, attack_image





class range(weapon):
    def set_up1(self, arrow_size, image):
        self.arrow_size = arrow_size
        self.centerx = -1000
        self.centery = -1000
        self.bow = pygame.image.load(image)
        self.bow = pygame.transform.scale_by(self.bow, (1.5, 1.5))
        self.bow_rect = self.bow.get_rect()
    def blit(self, playerx, playery, direction):
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
                self.bow_rect.centerx = playerx+50
                self.bow_rect.centery = playery+25
                hit_box_blit90 = pygame.transform.rotate(self.bow, 0)
                window.blit(hit_box_blit90, self.bow_rect)
    def attack(self, playerx, playery, direction):
        arrow_im = pygame.image.load('basic_arrow.png')
        arrow_im = pygame.transform.scale(arrow_im, self.arrow_size)
