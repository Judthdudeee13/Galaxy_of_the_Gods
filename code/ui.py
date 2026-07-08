from settings import *

class Inventory:
    def __init__(self, player, window):
        self.player = player
        self.font = pygame.font.Font(None, 30*SCALE)
        self.player_weapons = player.weapon
        self.screen = self.weapons
        self.window = window
        self.blit_obj = []
        
    def load(self):
        self.open = True
        self.screen()
        self.blit_obj = []

    def weapons(self):
        text = self.player_weapons[0].name
        text = self.font.render(text, True, BLACK)
        text_rect = text.get_frect(center = (100, 100))
        self.blit_obj.append((text, text_rect))

    def update(self):
        if self.open:
            self.window.fill(DAMAGE_FLASH)
            for obj in self.blit_obj:
                self.window.blit(obj[0], obj[1]*pygame.Vector2(SCALE, SCALE))

        self.player_weapons = self.player.weapon
        