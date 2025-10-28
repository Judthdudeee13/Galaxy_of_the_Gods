import pygame
import monster as mon
class backgrounds:
    def __init__(self, window, h, w):
        self.window = window
        self.hit_boxes = []
        self.interaction_boxes = []
        self.room_change = []
        self.interactions_results = []
        self.height = h
        self.width = w
        self.none = (-100, -100, -100, -100)
        self.current_monsters = []
        self.monsters_rect = []
        self.monsters_mask = []
        self.load_monsters()

    def load_monsters(self):
        self.monster1 = mon.monster_class()
        self.monster1.set_up(1, 1, 3, 2, 1, self.window, 32, 32, 50, 50, 500, 500)
        self.monster1_rect, self.monster1_mask = self.monster1.load_monster()
        self.current_monsters = []
        self.monsters = [self.monster1]
        self.monsters_rect = []
        self.monsters_mask = []
    def load_background1(self):
        keys = pygame.key.get_pressed()
        self.background = pygame.image.load("backgrounds/background1.PNG")
        self.background1 = pygame.transform.scale(self.background,(1300,700))
        self.back1 = self.background1.get_rect()
        self.back1.centerx = 650
        self.back1.centery = 350
        chest = pygame.image.load("chest.PNG")
        chest = pygame.transform.scale(chest,(150,100))
        chest_rect = chest.get_rect()
        chest_rect.centerx = 650
        chest_rect.centery = 100
        self.window.blit(self.background1, self.back1)
        self.window.blit(chest, chest_rect)
        self.hit_boxes = [
            (
                (613, 700, 0, 103),#left
                (610, 697, 0, 103),#right
                (613, 697, 0, 106), #up
                (self.none)#down
            ),
            (
                (0, 125, 0, self.height), #left
                (self.none),#right
                (self.none),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (1175, self.width, 0, self.height),#right
                (self.none),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (self.none),#right
                (0, self.width, 0, 100),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (self.none),#right
                (self.none),#up
                (0, self.width, 575, self.height)#down
            )
            
        ]
        self.room_change = [
            (215, 235, 0, 75, 2, keys[pygame.K_w], 230, 75)
        ]
        self.interaction_boxes = [
            (600, 700, 0, 150, 0, 0)
        ]
        self.interactions_results = [
            ('add_to_inventory', (('sword', 1, 'basic_sword'), ('range', 1, 'basic_bow')))
        ]

        
    def load_background2(self):
        keys = pygame.key.get_pressed()
        self.background = pygame.image.load("backgrounds/background2.PNG")
        self.background1 = pygame.transform.scale(self.background,(1300,700))
        self.back1 = self.background1.get_rect()
        self.back1.centerx = 650
        self.back1.centery = 350
        self.window.blit(self.background1, self.back1)
        self.hit_boxes = [
            (
                (0, 85, 0, self.height), #left
                (self.none),#right
                (self.none),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (1200, self.width, 0, self.height),#right
                (self.none),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (self.none),#right
                (0, self.width, 0, 75),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (self.none),#right
                (self.none),#up
                (0, self.width, 600, self.height)#down
            )
            
        ]
        self.room_change = [
            (215, 235, 0, 75, 1, keys[pygame.K_w], 230, 75),
            (1190, self.width, 440, 480, 3, keys[pygame.K_d], 90, 390)
        ]
        self.interaction_boxes = []
        self.interactions_results = []

        
    def load_background3(self):
        keys = pygame.key.get_pressed()
        self.background = pygame.image.load("backgrounds/background3.PNG")
        self.background1 = pygame.transform.scale(self.background,(1300,700))
        self.back1 = self.background1.get_rect()
        self.back1.centerx = 650
        self.back1.centery = 350
        self.window.blit(self.background1, self.back1)
        self.current_monsters = [self.monster1]
        self.monsters_rect = [self.monster1_rect]
        self.monsters_mask = [self.monster1_mask]

        self.hit_boxes = [
            (
                (0, 85, 0, self.height), #left
                (self.none),#right
                (self.none),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (1200, self.width, 0, self.height),#right
                (self.none),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (self.none),#right
                (0, self.width, 0, 75),#up
                (self.none)#down
            ),
            (
                (self.none),#left
                (self.none),#right
                (self.none),#up
                (0, self.width, 600, self.height)#down
            )
            
        ]
        self.room_change = [
            (0, 90, 370, 410, 2, keys[pygame.K_a], 1200, 460)
        ]
        self.interaction_boxes = []
        self.interactions_results = []

    def interactions(self, information_screens, number):
        if self.interactions_results[number][0] == 'add_to_inventory':
            for item in self.interactions_results[number][1]:
                information_screens[0].inventory_list[item[0]][item[1]] = item[2]

