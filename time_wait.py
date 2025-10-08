def attack(self, inventory, direction, player, current_weapon):
        global attack_image
        self.arrow_im = pygame.image.load('basic_arrow.png')
        self.arrow_im = pygame.transform.scale(self.arrow_im, self.arrow_size)
        self.arrow_sur = pygame.mask.from_surface(self.arrow_im)
        self.arrow_rect = self.arrow_im.get_rect()
        if inventory['range'][1] == 'basic_bow' and current_weapon == 'basic_bow':
            if abs(self.reload_time_cooldown-time.time()) >= self.reload_time and attack_image <= 0:
                attack_image = self.starting_time
                self.reload_time_cooldown = time.time()


            if attack_image > 0:
                attack_image -= 1
                if direction == 'up':
                        self.arrow_rect.centerx = player.x+25
                        self.arrow_rect.centery = player.y-5
                        hit_box_blit180 = pygame.transform.rotate(self.arrow_im, 0)
                        window.blit(hit_box_blit180, self.arrow_rect)
                if direction == 'down':
                        self.arrow_rect.centerx = player.x+25
                        self.arrow_rect.centery = player.y+55
                        hit_box_blit0 = pygame.transform.rotate(self.arrow_im, 180)
                        window.blit(hit_box_blit0, self.arrow_rect)
                if direction == 'left' or direction == 'None':
                        self.arrow_rect.centerx = player.x-11
                        self.arrow_rect.centery = player.y+30
                        hit_box_blit270 = pygame.transform.rotate(self.arrow_im, 90)
                        window.blit(hit_box_blit270, self.arrow_rect)
                if direction == 'right':
                        self.arrow_rect.centerx = player.x+52
                        self.arrow_rect.centery = player.y+30
                        hit_box_blit90 = pygame.transform.rotate(self.arrow_im, 270)
                        window.blit(hit_box_blit90, self.arrow_rect)
                return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, attack_image, self.starting_time
            else:
                return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, -1, self.starting_time
        else:
             return self.arrow_sur, self.arrow_rect, self.damage, self.arrow_im, -1, self.starting_time
        

def attack(self, inventory, direction, p, current_weapon):
        self.hit_box_im = pygame.image.load("melee_AOE.png")
        self.hit_box_im = pygame.transform.scale(self.hit_box_im, (self.range, self.range))
        self.hit_box_pos = self.hit_box_im.get_rect()
        self.hit_box_sur = pygame.mask.from_surface(self.hit_box_im)
        global attack_image
        if inventory['sword'][1] == 'basic_sword' and current_weapon == 'basic_sword':
            if abs(self.reload_time_cooldown-time.time()) >= self.reload_time and attack_image <= 0:
                attack_image = self.starting_time
                self.reload_time_cooldown = time.time()


            if attack_image > 0:
                attack_image -= 1
                if direction == 'up':
                    self.hit_box_pos.x = p.x+12
                    self.hit_box_pos.y = p.y-15
                    hit_box_blit180 = pygame.transform.rotate(self.hit_box_im, 180)
                    window.blit(hit_box_blit180, self.hit_box_pos)
                if direction == 'down':
                    self.hit_box_pos.x = p.x+12
                    self.hit_box_pos.y = p.y+40
                    hit_box_blit0 = pygame.transform.rotate(self.hit_box_im, 0)
                    window.blit(hit_box_blit0, self.hit_box_pos)
                if direction == 'left' or direction == 'None':
                    self.hit_box_pos.x = p.x-12
                    self.hit_box_pos.y = p.y+12
                    hit_box_blit270 = pygame.transform.rotate(self.hit_box_im, 270)
                    window.blit(hit_box_blit270, self.hit_box_pos)
                if direction == 'right':
                    self.hit_box_pos.x = p.x+42
                    self.hit_box_pos.y = p.y+12
                    hit_box_blit90 = pygame.transform.rotate(self.hit_box_im, 90)
                    window.blit(hit_box_blit90, self.hit_box_pos)
                return  self.hit_box_sur, self.hit_box_pos, self.damage, self.hit_box_im, attack_image, self.starting_time
            else:
                return self.hit_box_sur, self.hit_box_pos, self.damage, self.hit_box_im, -1, self.starting_time
        else:
            return self.hit_box_sur, self.hit_box_pos, self.damage, self.hit_box_im, -1, self.starting_time
