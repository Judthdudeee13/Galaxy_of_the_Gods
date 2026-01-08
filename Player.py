import pygame, pytmx

class Player:
    def __init__(self, file):
        self.update_info(file)
    def update_info(self, file):
        self.file = pytmx.load_pygame(file)
        self.image = self.file.get_layer_by_name("Player")
        self.rect = None

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