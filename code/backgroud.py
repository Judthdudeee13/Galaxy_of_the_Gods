from settings import *

class Backgrounds:
    def __init__(self, maps, current_map, player):
        self.maps = maps
        self.current_map = current_map
        self.player = player



class Map:
    def __init__(self, name, bakcground_group, *path):
        self.name = name
        self.map_data = pytmx.load_pygame(join(*path))
