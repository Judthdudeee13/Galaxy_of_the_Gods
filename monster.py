import pygame
import time

class monster_class:
    def __init__(self):
        pass

    def set_up(self, name, damage, health, speed, times, window, width, height, player_width, player_height):
        self.player_width = player_width
        self.player_height = player_height
        self.name = name
        self.damage = damage
        self.health = health
        self.speed = speed
        self.damage_time = time.time()
        self.times = times
        self.window = window
        self.health = self.health
        self.load = True
        self.width = width
        self.height = height
    
    def load_monster(self):
        if self.load:
            image = pygame.image.load("moster_replace.png")
            image = pygame.transform.scale(image, (32, 32))
            rect = image.get_rect()
            rect2 = rect.inflate(4, 4)
            rect.x = 500
            rect.y = 500
            self.x = rect.x
            self.y = rect.y
            self.rect = rect
            self.rect2 = rect2
            self.image = image
            self.turn = 0
            self.mask = pygame.mask.from_surface(self.image)
            return rect, self.mask
        
    def targeting(self, p):
        if self.load:
            x = p.x - self.x
            y = p.y - self.y
            if x-self.width > 0:
                self.x += self.speed
            if y-self.height > 0:
                self.y += self.speed    
            if x+self.player_width < 0:
                self.x -= self.speed
            if y+self.player_width < 0:
                self.y -= self.speed
            self.turn += 1
        

    def blit(self):
        if self.load:
            self.rect.x = self.x
            self.rect.y = self.y
            self.rect2.x = self.rect.x-2
            self.rect2.y = self.rect.y-2
            #self.window.blit(self.rect2, self.rect)
            self.window.blit(self.image, self.rect)
        
        

    def damage_givin(self, p_rect):
        if self.load:
            if p_rect.colliderect(self.rect2):
                if abs(self.damage_time - time.time()) > self.times:
                    damage_taken = 0
                    damage_taken += 1
                    self.damage_time = time.time()
                    print(10)
                    return self.damage
    def recive_damage(self, player_mask, player_rect, damage):
        if self.load:
            try:
                if player_mask.overlap(self.mask, (self.rect.x - player_rect.x, self.rect.y - player_rect.y)):
                    self.health -= damage
            except Exception as e:
                print(e)
                print('THIS ONE DIDN\'T WORK this one') 


        if self.health <= 0:
            self.load = False
            self.rect.x = -1000
            self.rect.y = -1000