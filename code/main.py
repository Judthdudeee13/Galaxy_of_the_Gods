from settings import *
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Galaxy of the Gods')
        self.clock = pygame.time.Clock()
        self.running = True

        #imports
        self.import_assets()

        # groups 
        self.all_sprites = AllSprites(self.window)
        self.background_sprites = pygame.sprite.Group()

    def import_assets(self):
        pass

    def load_background(self):
        pass

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
    
if __name__ == '__main__':
    game = Game()
    game.run()