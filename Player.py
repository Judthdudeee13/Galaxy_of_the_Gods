import pygame
import pytmx

class Player(pygame.sprite.Sprite):
    def __init__(self, tmx_file):
        super().__init__()
        self.load_from_tmx(tmx_file)

    def load_from_tmx(self, tmx_file):
        self.tmx = pytmx.load_pygame(tmx_file)
        layer = self.tmx.get_layer_by_name("Player")
        obj = list(layer)[0]
        self.x = obj.x
        self.y = obj.y
        self.image = self.tmx.get_tile_image_by_gid(obj.gid)
        self.rect = self.image.get_rect(
            topleft=(int(self.x), int(self.y)))

        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 2
        if keys[pygame.K_s]:
            self.y +=2
        if keys[pygame.K_a]:
            self.x -= 2
        if keys[pygame.K_d]:
            self.x += 2

        self.rect.topleft = ((self.x, self.y))