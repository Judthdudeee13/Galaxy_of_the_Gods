from settings import *

class Backgrounds:
    def __init__(self, maps, current_map, all_sprites, collision_sprites):
        self.maps = maps
        self.current_map = current_map
        self.player = player
        self.all_sprites = all_sprites
        self.collision_sprites = collision_sprites
        self.old_map = None

    def update_map(self):
        for sprite in self.current_map.group:
            self.all_sprites.add(sprite)
        for sprite in self.current_map.collision_group:
            pass

    
            




class Map:
    def __init__(self, name, background_group, *path):
        self.name = name
        self.map = pytmx.load_pygame(join(*path))
        self.group = pygame.sprite.Group()
        self.collision_group = pygame.sprite.Group()
        
    def load_map(self):
        for x, y, image in self.map.get_layer_by_name('Ground').tiles():
            Sprite((x*TILE_SIZE*SCALE, y*TILE_SZIE*SCALE), pygame.transfrom.scale_by(image, SCALE), self.group, True)
    
