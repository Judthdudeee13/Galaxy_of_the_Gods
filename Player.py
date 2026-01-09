import pygame
import pytmx
import os

class Player:
    def __init__(self, tmx_file):
        self.update_info(tmx_file)

    def update_info(self, tmx_file):
        self.file = pytmx.load_pygame(tmx_file)
        self.layer = self.file.get_layer_by_name("Player")
        self.obj = list(self.layer)[0]  # first player object

        # Coordinates
        self.x = int(self.obj.x)
        self.y = int(self.obj.y)

        # Get image property
        image_file = self.obj.properties.get("image")
        if not image_file:
            raise ValueError("Player object in TMX is missing 'image' property")

        # Join path relative to TMX folder
        tmx_dir = os.path.dirname(tmx_file)
        self.image_path = os.path.join(tmx_dir, image_file)

        if not os.path.isfile(self.image_path):
            raise FileNotFoundError(f"Cannot find player image: {self.image_path}")

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

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
        