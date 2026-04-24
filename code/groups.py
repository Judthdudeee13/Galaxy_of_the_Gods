from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.offset = pygame.Vector2()

    def draw(self, target_pos):
        self.offset.x = -(int(target_pos[0] - WINDOW_WIDTH / 2))
        self.offset.y = -(int(target_pos[1] - WINDOW_HEIGHT / 2))
        ground_sprites = [sprite for sprite in self if sprite.isGround]
        object_sprites = [sprite for sprite in self if not sprite.isGround]

        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key=lambda sprite: sprite.rect.centery):
                self.window.blit(sprite.image, sprite.rect.topleft + self.offset)
