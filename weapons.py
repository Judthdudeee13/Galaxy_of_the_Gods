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
    def set_up(self, reload_time, ammo, damage, direction, range, attack_image):
        self.reload_time = reload_time
        self.ammo = ammo
        self.damage = damage
        self.direction = direction
        self.range = range
        self.reload_time_cooldown = time.time()
        self.attack_image = attack_image



class melee(weapon):
    def attack(self):
        if self.reload_time_cooldown - self.reload_time > 0:
            hit_box_im = pygame.image.load("melee_AOE.png")
            hit_box_im = pygame.transform.scale(hit_box_im, (self.range, self.range))
            hit_box_pos = hit_box_im.get_rect()
            hit_box_sur = pygame.mask.from_surface(hit_box_im)
            self.swing = True
            return hit_box_sur, hit_box_pos, self.damage, hit_box_im, self.reload_time

        
    def swing_blit(self):
        hit_box_sur, hit_box_pos, damage, hit_box_im, relod_time = self.attack()
        self.swing = False
        return  hit_box_sur, hit_box_pos, damage, hit_box_im, relod_time, self.attack_image





class range(weapon):
    pass

