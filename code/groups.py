from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.offset = pygame.Vector2()

    def draw(self, target_pos):
        #draws camera around target pos
        self.offset.x = -(int(target_pos[0] - WINDOW_WIDTH / 2))
        self.offset.y = -(int(target_pos[1] - WINDOW_HEIGHT / 2))
        # Camera culling: only consider sprites that intersect the screen.
        # This avoids sorting/blitting thousands of off-screen map sprites.
        view_rect = pygame.Rect(
            -self.offset.x,
            -self.offset.y,
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        ground_sprites = []
        object_sprites = []
        for sprite in self:
            if not sprite.rect.colliderect(view_rect):
                continue

            if hasattr(sprite, 'isGround') and sprite.isGround:
                ground_sprites.append(sprite)
            else:
                object_sprites.append(sprite)

        #draws ground before other objects then makes objects on screen on top of objects behind them
        for layer in [ground_sprites, object_sprites]:
            for sprite in sorted(layer, key=lambda sprite: sprite.rect.centery):
                self.window.blit(sprite.image, sprite.rect.topleft + self.offset)