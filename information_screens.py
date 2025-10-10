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

def mouse_buttons():
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        return 0
class inventory:
    def __init__(self):
        self.close = False
        self.inventory_melee = pygame.image.load("inventory/inventory_melee.png")
        self.inventory_range = pygame.image.load("inventory/inventory_ranged.png")
        self.inventory_magic = pygame.image.load("inventory/inventory_magic.png")
        self.inventory_armor = pygame.image.load("inventory/inventory_armor.png")
        self.inventory_inventory = pygame.image.load("inventory/inventory.png")
        self.inventory_map = pygame.image.load("inventory/inventory_map.png")
        self.inventory_person = pygame.image.load("inventory/inventory_person.png")
        self.inventory_quests = pygame.image.load("inventory/inventory_quests.png")
        self.background = self.inventory_melee
        self.inventory_spot = []
        self.current_weapon = 'basic_sword'
        for y in range(6):
                y_pos = (y*122)+150
                for x in range(13):
                    x_pos = (x*100)+50
                    self.inventory_spot.append((x_pos, y_pos))

    def run(self, inventory_list):
        self.inventory_list = inventory_list
        self.load_inventory_background()
        self.load_inventory()
        self.change_background()
        if self.close:
            self.close = False
            return False
        else:
            return True


    def load_inventory(self):
        if self.background  == self.inventory_melee:
            if self.inventory_list['sword'][1]:
                basic_sword = pygame.image.load('weapons/basic_sword(inv).png')
                basic_sword_rect = basic_sword.get_rect()
                basic_sword_rect.center = self.inventory_spot[0]
                window.blit(basic_sword, basic_sword_rect)
        elif self.background  == self.inventory_range:
            if self.inventory_list['range'][1]:
                basic_sword = pygame.image.load('weapons/basic_sword(inv).png')
                basic_sword_rect = basic_sword.get_rect()
                basic_sword_rect.center = self.inventory_spot[0]
                window.blit(basic_sword, basic_sword_rect)
            
        mouse_pos()
    def change_background(self):
        background = None
        melee_hit_box = pygame.Rect(0, 0, 147, 126)
        range_hit_box = pygame.Rect(147, 0, 147, 126)
        magic_hit_box = pygame.Rect(294, 0, 147, 126)
        armor_hit_box = pygame.Rect(441, 0, 147, 126)
        inventory_hit_box = pygame.Rect(588, 0, 147, 126)
        map_hit_box = pygame.Rect(735, 0, 147, 126)
        person_hit_box = pygame.Rect(882, 0, 147, 126)
        quests_hit_box = pygame.Rect(1029, 0, 147, 126)
        close_hit_box = pygame.Rect(1176, 0, 147, 126)
        hit_boxes = [melee_hit_box, range_hit_box, magic_hit_box, armor_hit_box, inventory_hit_box, map_hit_box, person_hit_box, quests_hit_box, close_hit_box]
        mouse_pos()
        for hit_box in hit_boxes:
            if mouse_buttons() == 0:
                if hit_box.colliderect(mouse_rect):
                    background = hit_box
        if background == melee_hit_box:
            self.background = self.inventory_melee
        if background == range_hit_box:
            self.background = self.inventory_range
        if background == magic_hit_box:
            self.background = self.inventory_magic
        if background == armor_hit_box:
            self.background = self.inventory_armor
        if background == inventory_hit_box:
            self.background = self.inventory_inventory
        if background == map_hit_box:
            self.background = self.inventory_map
        if background == person_hit_box:
            self.background = self.inventory_person
        if background == quests_hit_box:
            self.background = self.inventory_quests
        if background == close_hit_box:
            self.close = True
        

    
    def load_inventory_background(self):
        self.rect = self.background.get_rect()
        self.rect.center = (650, 350)
        window.blit(self.background, self.rect)