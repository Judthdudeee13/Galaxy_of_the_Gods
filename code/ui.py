from settings import *

class Inventory:
    def __init__(self, player, window):
        self.player = player
        self.font = pygame.font.Font(None, 12*SCALE)
        self.player_weapons = player.weapon
        self.screen = self.weapons
        self.window = window
        self.blit_obj = []
        
    def load(self):
        self.blit_obj = []
        self.screen()
        

    def weapons(self):
        text_size = 14*SCALE
        for x in range(len(self.player_weapons)):
            text = self.player_weapons[x].name
            text = self.font.render(text, True, BLACK)
            text_rect = text.get_frect(topleft = (10*SCALE, 10*SCALE+(text_size*x)))
            self.blit_obj.append((text, text_rect))

    def update(self):
        self.player_weapons = self.player.weapon
        self.window.fill(DAMAGE_FLASH)
        for obj in self.blit_obj:
            self.window.blit(obj[0], obj[1])