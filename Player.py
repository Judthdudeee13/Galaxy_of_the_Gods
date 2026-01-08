import pygame, pytmx

class Player:
    def __init__(self, file):
        self.update_info(file)
    def update_info(self, file):
        self.file = pytmx.load_pygame(file)
        self.layer = self.file.get_layer_by_name("Player")
        self.obj = next(iter(self.layer))
        self.image_path = self.obj.properties.get("image", None)
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect(topleft = (int(self.obj.x), int(self.obj.y)))

    

# player = pygame.sprite.Sprite()
# player.image = pygame.Surface((16, 16))
# player.image.fill((255, 0, 0))
# player.rect = player.image.get_rect(topleft = (0, 0))


# #temporary player
#     if keys[pygame.K_w]:
#         player.rect.y -= 2
#     if keys[pygame.K_s]:
#         player.rect.y +=2
#     if keys[pygame.K_a]:
#         player.rect.x -= 2
#     if keys[pygame.K_d]:
#         player.rect.x += 2