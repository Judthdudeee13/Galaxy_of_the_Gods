from settings import *

class Weapon:
    def __init__(self, damage, range, damage_type = None):
        self.damage = damage
        self.range = range
        self.damage_type = damage_type

        