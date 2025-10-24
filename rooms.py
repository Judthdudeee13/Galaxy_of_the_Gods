import pygame

class backgrounds:
    def __init__(self, window, h, w):
        self.window = window
        self.hit_boxes = []
        self.interaction_boxes = []
        self.room_change = []
        self.height = h
        self.width = w
        self.none = (-100, -100, -100, -100)
    def load_background1(self, inventorys, ):
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
                (613, 697, 0, 103), #up
                (self.none)#down
            ),
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
            )
            (
                (self.none),#left
                (self.none),#right
                (0, self.width, 0, 75),#up
                (self.none)#down
            )
            
        ]
        '''if p.centerx >= 600 and p.centerx <= 700 and p.centery <= 150 and keys[pygame.K_e]:
            inventorys.inventory_list['range'][1] = 'basic_bow'
            self.inventory['sword'][1] = 'basic_sword'
            q = True
            inventorys.run(inventorys.inventory_list)
            bg = 0
        if p.centery <= 103 and p.centerx >= 613 and p.centerx <= 700:
            left = False
        if p.centery <= 103 and p.centerx >= 610 and p.centerx <= 697:
            right = False
        if p.centerx <= 85:
            left = False
        if p.centerx >= 1200:
            right = False
        if p.centery <= 75:
            up = False
        if p.centery >= 600:
            down = False
        if p.centery <= 106 and p.centerx >= 613 and p.centerx <= 697:
            up = False
        if p.centerx >= 215 and p.centerx <= 235 and p.centery <= 75 and keys[K_w] and abs(it1-time.time()) > 1:
            bg = 2
            it1 = time.time()'''