# file imports
from settings import *
from assets import *
from groups import AllSprites
from sprites import *
from background import *
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # pygame.FULLSCREEN
        pygame.display.set_caption("Galaxy of the Gods")
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.running = True

        # imports
        self.import_assets()

        # groups
        self.ground_sprites = AllSprites(self.window)
        self.player_sprites = AllSprites(self.window)
        self.cover_sprites = AllSprites(self.window)
        self.collision_sprites = pygame.sprite.Group()

        # backgrounds
        self.load_background()
        self.background = Backgrounds(
            self.backgrounds, "Plains", self.ground_sprites, self.player_sprites, self.cover_sprites, self.collision_sprites
        )

        # player
        self.player = Player(self.background.player_start_pos, self.player_assets, self.player_sprites, self.collision_sprites)

    def import_assets(self):
        self.player_assets = folder_loader('images', 'player')

    def load_background(self):
        self.backgrounds = {}
        self.backgrounds["Plains"] = Map("Plains", "data", "maps", "plains.tmx")

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # update
            self.ground_sprites.update(dt)
            self.player_sprites.update(dt)
            self.cover_sprites.update(dt)

            # draw
            self.window.fill("black")
            self.ground_sprites.draw(self.player.rect.center)
            self.player_sprites.draw(self.player.rect.center)
            self.cover_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
