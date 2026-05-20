from settings import *
from sprites import *
from weapons import *
from timer import *

class Enemy(MiltiDirectionalSprite):
	def __init__(self, pos, folders, groups, speed, player, collision_sprites, health):
		animation_speed = 5.88
		super().__init__(pos, folders, groups, animation_speed)
		self.speed = speed
		self.player = player
		self.direction = pygame.Vector2(0, 0)
		self.collision_sprites = collision_sprites
		self.weapon = Weapon(1, 2, 1000)
		self._health = health
		self.name = "Enemy"
		self.hit_timer = Timer(150)
		self.mask_image = pygame.mask.from_surface(self.image).to_surface(setcolor = DAMAGE_FLASH, unsetcolor=(0, 0, 0, 0))

	@property
	def health(self):
		return self._health
	
	@health.setter
	def health(self, value):
		self.hit_timer.activate()
		self._health = value

	def knockback(self, direction):
		self.rect.x += direction.x * 700 * 0.06
		self.rect.y += direction.y * 700 * 0.06

	def target(self):
     #targetting the player
		self.direction.x = 1 if self.player.rect.x > self.rect.x else -1
		self.direction.y = 1 if self.player.rect.y > self.rect.y else -1
		self.direction = self.direction.normalize() if self.direction else self.direction

	def move(self, dt):
	#actully moving the enemy
		self.rect.x += self.direction.x * self.speed * dt
		self.check_collision("horizontal")
		self.rect.y += self.direction.y * self.speed * dt
		self.check_collision("vertical")

         
	def check_collision(self, direction):
     #checks for collisions
		nearby_area = self.rect.inflate(96 * SCALE, 96 * SCALE)
		for sprite in self.collision_sprites:
			if self == sprite:
				continue
			
			if not sprite.rect.colliderect(nearby_area):
				continue

			if sprite.rect.colliderect(self.rect):
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
     #checks for animation state
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

	def attack(self):
		if self.rect.colliderect(self.player.rect):
			self.weapon.deal_damage(self.player)

	def check_death(self):
		if self.health <= 0:
			self.kill()	

	def draw(self, dt):
     #updates player position
		self.direction_check()
		self.animate(dt)

	def update(self, dt):
		if not self.hit_timer:
			self.check_death()
			self.attack()
			self.weapon.update(None)
			self.target()
			self.move(dt)
			self.draw(dt)
		else:
			self.image = self.mask_image
			self.hit_timer.update()
			
