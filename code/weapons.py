from settings import *
from timer import Timer

class Weapon:
    def __init__(self, damage, range, cool_down, damage_type = None):
        self.damage = damage
        self.range = range
        self.damage_type = damage_type
        self.cool_down_timer = Timer(cool_down)

    def deal_damage(self, target):
        if not self.cool_down_timer:
            target.health -= self.damage
            self.cool_down_timer.activate()
    
    def update(self):
        self.cool_down_timer.update()

        