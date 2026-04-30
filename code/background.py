from settings import *
from sprites import *


class Backgrounds:
    def __init__(self, maps, current_map, ground_sprites, player_sprites, cover_sprites, collision_sprites):
        self.maps = maps
        self.current_map = maps[current_map]
        self.ground_sprites = ground_sprites
        self.player_sprites = player_sprites
        self.cover_sprites = cover_sprites
        self.collision_sprites = collision_sprites
        self.old_map = None
        self.update_map(self.current_map)
        self.player_start_pos = self.current_map.player_start_pos

    def update_map(self, new_map):
        #check to make sure there was an old map
        if self.old_map:
            #remove old sprites
            #remove from ground ground
            for sprite in self.old_map.ground:
                self.ground_sprites.remove(sprite)
            #remove from player group
            for sprite in self.old_map.player_sprites:
                self.player_sprites.remove(sprite)
            #remove from cover group
            for sprite in self.old_map.top:
                self.cover_sprites.remove(sprite)
            # remove from collision group
            for sprite in self.old_map.collision_group:
                self.collision_sprites.remove(sprite)
        #add new sprites to group
        #add to ground group
        for sprite in new_map.ground:
            self.ground_sprites.add(sprite)
        #add to player group
        for sprite in new_map.player_sprites:
            self.player_sprites.add(sprite)
        #add to cover group
        for sprite in new_map.top:
            self.cover_sprites.add(sprite)
        #add to collision group
        for sprite in new_map.collision_group:
            self.collision_sprites.add(sprite)
        # set current map
        self.current_map = new_map


class Map:
    def __init__(self, name, *path):
        self.name = name
        self.map = pytmx.load_pygame(join(*path))
        self.ground = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.top = pygame.sprite.Group()
        self.collision_group = pygame.sprite.Group()
        self.load_map()
        self.player_start_pos = (800*SCALE, 800*SCALE)

    def load_map(self):
        #load water
        for x, y, image in self.map.get_layer_by_name("Water").tiles():
            Sprite(
                (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                pygame.transform.scale_by(image, SCALE),
                self.ground,
                True,
            )

        #load ground
        for x, y, image in self.map.get_layer_by_name("Ground").tiles():
            Sprite(
                (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                pygame.transform.scale_by(image, SCALE),
                self.ground,
                True,
            )

        #load base for high ground
        for x, y, image in self.map.get_layer_by_name("Elevation").tiles():
            Sprite(
                (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                pygame.transform.scale_by(image, SCALE),
                self.ground,
                True,
            )
        
        #load high ground
        for x, y, image in self.map.get_layer_by_name("Elevation_ground").tiles():
            Sprite(
                (x * TILE_SIZE * SCALE, y * TILE_SIZE * SCALE),
                pygame.transform.scale_by(image, SCALE),
                self.ground,
                True,
            )

        #load bushes
        for obj in self.map.get_layer_by_name("Bushes"):
            Sprite(
                (obj.x * SCALE, obj.y * SCALE),
                pygame.transform.scale_by(obj.image, SCALE),
                self.player_sprites
            )

        #load trees
        for obj in self.map.get_layer_by_name("Trees"):
            Sprite(
                (obj.x * SCALE, obj.y * SCALE),
                pygame.transform.scale_by(obj.image, SCALE),
                self.ground
            )
        
        #load tree cover
        for obj in self.map.get_layer_by_name("Leaves"):
            Sprite(
                (obj.x * SCALE, obj.y * SCALE),
                pygame.transform.scale_by(obj.image, SCALE),
                self.top
            )

        #find collisions
        for obj in self.map.get_layer_by_name('Collisions'):
            Sprite((obj.x*SCALE, obj.y*SCALE), 
                   pygame.transformS.scale_by(pygame.Surface((obj.width, obj.height)), 
                    SCALE), 
                    (self.collision_group)
                    )

        #find tree collisions
        for obj in self.map.get_layer_by_name("Trees"):
            tile_props = self.map.get_tile_properties_by_gid(obj.gid)
            if not tile_props or "colliders" not in tile_props:
                continue

            for shape in tile_props["colliders"]:
                Sprite((shape.x*SCALE+obj.x*SCALE, shape.y * SCALE + obj.y*SCALE), 
                   pygame.transform.scale_by(pygame.Surface((shape.width, shape.height)), 
                    SCALE), 
                    (self.collision_group)
                    )
                