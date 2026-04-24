from settings import *
from sprites import *


class Backgrounds:
    def __init__(self, maps, current_map, all_sprites, collision_sprites):
        self.maps = maps
        self.current_map = maps[current_map]
        self.all_sprites = all_sprites
        self.collision_sprites = collision_sprites
        self.old_map = None
        self.update_map(self.current_map)
        self.player_start_pos = self.current_map.player_start_pos

    def update_map(self, new_map):
        if self.old_map:
            for sprite in self.old_map.group:
                self.all_sprites.remove(sprite)
            for sprite in self.old_map.collision_group:
                self.collision_sprites.remove(sprite)
        for sprite in new_map.group:
            self.all_sprites.add(sprite)
        for sprite in new_map.collision_group:
            self.collision_sprites.add(sprite)
        self.current_map = new_map


class Map:
    def __init__(self, name, *path):
        self.name = name
        self.map = pytmx.load_pygame(join(*path))
        self.group = pygame.sprite.Group()
        self.collision_group = pygame.sprite.Group()
        self.load_map()

    def load_map(self):
        for x, y, image in self.map.get_layer_by_name("Ground").tiles():
            Sprite(
                (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                pygame.transform.scale_by(image, SCALE),
                self.group,
                True,
            )
        for x, y, image in self.map.get_layer_by_name("Designs").tiles():
            Sprite(
                (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                pygame.transform.scale_by(image, SCALE),
                self.group,
                True,
            )
        self.player_start_pos = (1500*SCALE, 1500*SCALE)
        for obj in self.map.get_layer_by_name("Objects"):
            Sprite(
                (obj.x * SCALE, obj.y * SCALE),
                pygame.transform.scale_by(obj.image, SCALE),
                self.group,
                True,
            )
