# file imports
from settings import *
from groups import AllSprites
from sprites import *
from background import *


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_HEIGHT, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN
        pygame.display.set_caption("Galaxy of the Gods")
        self.clock = pygame.time.Clock()
        self.running = True

        # imports
        self.import_assets()

        # groups
        self.all_sprites = AllSprites(self.window)
        self.collision_sprites = pygame.sprite.Group()

        # backgrounds
        self.load_background()
        self.background = Backgrounds(self.backgrounds, "Plains", self.all_sprites, self.collision_sprites)

        # player
        self.player = (500, 500)

    def import_assets(self):
        pass

    def load_background(self):
        self.backgrounds = {}
        self.backgrounds['Plains'] = Map("Plains", "data", "maps", "world.tmx")
        

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
            self.all_sprites.update(dt)

            # draw
            self.all_sprites.draw(self.player)
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
