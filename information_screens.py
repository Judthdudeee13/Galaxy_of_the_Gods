import pygame

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

def mouse_pos():
    global mouse_rect
    x, y = pygame.mouse.get_pos()
    mouse = pygame.image.load("mouse.png")
    mouse_rect = mouse.get_rect()
    mouse_rect.centerx = x
    mouse_rect.centery = y
    window.blit(mouse, mouse_rect)

class inventory:
    def __init__(self):
        self.inventory_melee = pygame.image.load("inventory/sword_inventory.png")
        self.inventory_bow = pygame.image.load("inventory/inventory_ranged.png")
        self.background = self.inventory_melee
        self.inventory_spot = []
        for y in range(6):
                y_pos = (y*122)+150
                for x in range(13):
                    x_pos = (x*100)+50
                    self.inventory_spot.append((x_pos, y_pos))

    def run(self, inventory_list):
        self.inventory_list = inventory_list
        self.load_inventory_background()
        self.load_inventory()


    def load_inventory(self):
        if self.background  == self.inventory_melee:
            if self.inventory_list['sword'][1]:
                basic_sword = pygame.image.load('weapons/basic_sword(inv).png')
                basic_sword_rect = basic_sword.get_rect()
                basic_sword_rect.center = self.inventory_spot[0]
                window.blit(basic_sword, basic_sword_rect)
        elif self.background  == self.inventory_bow:
            if self.inventory_list['range'][1]:
                basic_sword = pygame.image.load('weapons/basic_sword(inv).png')
                basic_sword_rect = basic_sword.get_rect()
                basic_sword_rect.center = self.inventory_spot[0]
                window.blit(basic_sword, basic_sword_rect)
            
        mouse_pos()
        
    
    def load_inventory_background(self):
        self.rect = self.background.get_rect()
        self.rect.center = (650, 350)
        window.blit(self.background, self.rect)