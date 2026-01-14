import pygame
import pytmx

#call pygame.sprite.sprite otherwise pyscroll can't use plaer for focus
class Player(pygame.sprite.Sprite):
    def __init__(self, tmx_file):
        #needed for sprites
        super().__init__()
        self.load_from_tmx(tmx_file)
        self.move_speed = 2
        self.direction = 'west'

    def load_from_tmx(self, tmx_file):
        self.tmx = pytmx.load_pygame(tmx_file)
        #pull player layer
        layer = self.tmx.get_layer_by_name("Player")
        #pull player obj
        obj = list(layer)[0]
        #get x and y coords
        self.x = obj.x
        self.y = obj.y
        #pull image
        self.image = self.tmx.get_tile_image_by_gid(obj.gid)
        self.rect = self.image.get_rect(topleft=(int(self.x), int(self.y)))

    #movement of the player
    def move(self):
        #takes current key inuts
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.move_speed
            self.direction = 'west'
        elif keys[pygame.K_d]:
            self.x += self.move_speed
            self.direction = 'east'
        elif keys[pygame.K_w]:
            self.y -= self.move_speed
            self.direction = 'north'
        elif keys[pygame.K_s]:
            self.y += self.move_speed
            self.direction = 'south'
        #repotions rect of player
        self.rect.topleft = ((self.x, self.y))
