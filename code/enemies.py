from settings import *
from sprites import *
from timer import Timer

class Enemy(MiltiDirectionalSprite):
	def __init__(self, pos, folders, groups, speed, player, collision_sprites):
		animation_speed = 5.88
		super().__init__(pos, folders, groups, animation_speed)
		self.speed = speed
		self.player = player
		self.direction = pygame.Vector2(0, 0)
		self.collision_sprites = collision_sprites
		self.redirect_timer = Timer(1000)
        

	def target(self):
		self.direction.x = 1 if self.player.rect.x > self.rect.x else -1
		self.direction.y = 1 if self.player.rect.y > self.rect.y else -1
		self.direction = self.direction.normalize() if self.direction else self.direction

	def move(self, dt):
		
		self.rect.x += self.direction.x * self.speed * dt
		self.check_collision("horizontal")
		self.rect.y += self.direction.y * self.speed * dt
		self.check_collision("vertical")

         
	def check_collision(self, direction):
		for sprite in self.collision_sprites:
			if sprite.rect.colliderect(self.rect):
				self.redirect_timer.activate()
				if direction == 'horizontal':
					if self.direction.x > 0:
						self.rect.right = sprite.rect.left
					if self.direction.x < 0:
						self.rect.left = sprite.rect.right
				if direction == 'vertical':
					if self.direction.y > 0:
						self.rect.bottom = sprite.rect.top
					if self.direction.y < 0:
						self.rect.top = sprite.rect.bottom
	
	def direction_check(self):
		if self.direction:
			if self.direction.x:
				if self.direction.x > 0:
					self.facing = "right"
				else:
					self.facing = "left"
			elif self.direction.y:
				if self.direction.y > 0:
					self.facing = "down"
				else:
					self.facing = "up"
		else:
			if self.facing == "right":
				self.facing = "idle_right"
			elif self.facing == "left":
				self.facing = "idle_left"
			elif self.facing == "up":
				self.facing = "idle_up"
			elif self.facing == "down":
				self.facing = "idle_down"

		self.update_direction(self.facing)

	def draw(self, dt):
		self.direction_check()
		self.animate(dt)

	def update(self, dt):
		self.redirect_timer.update()
		self.target()
		self.move(dt)
		self.draw(dt)
