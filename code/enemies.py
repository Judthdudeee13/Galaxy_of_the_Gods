from heapq import heappop, heappush

from settings import *
from sprites import *


class Enemy(MiltiDirectionalSprite):
	def __init__(self, pos, folders, groups, speed, player, collision_sprites):
		animation_speed = 5.88
		super().__init__(pos, folders, groups, animation_speed)
		self.speed = speed
		self.player = player
		self.direction = pygame.Vector2(0, 0)
		self.collision_sprites = collision_sprites
		self.path = []
		self.path_timer = 0
		self.path_update_interval = 0.25

	def tile_pos(self, position):
		return int(position[0] // TILE_SIZE), int(position[1] // TILE_SIZE)

	def tile_center(self, tile):
		return pygame.Vector2((tile[0] + 0.5) * TILE_SIZE, (tile[1] + 0.5) * TILE_SIZE)

	def get_blocked_tiles(self):
		blocked = set()
		for sprite in self.collision_sprites:
			left = sprite.rect.left // TILE_SIZE
			right = (sprite.rect.right - 1) // TILE_SIZE
			top = sprite.rect.top // TILE_SIZE
			bottom = (sprite.rect.bottom - 1) // TILE_SIZE
			for x in range(left, right + 1):
				for y in range(top, bottom + 1):
					blocked.add((x, y))
		return blocked

	def heuristic(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	def find_path(self, start, goal):
		if start == goal:
			return []

		blocked = self.get_blocked_tiles()
		blocked.discard(start)
		blocked.discard(goal)

		open_nodes = []
		heappush(open_nodes, (0, start))
		came_from = {}
		g_score = {start: 0}

		while open_nodes:
			_, current = heappop(open_nodes)
			if current == goal:
				break

			for offset_x, offset_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
				neighbor = (current[0] + offset_x, current[1] + offset_y)
				if neighbor in blocked:
					continue

				tentative = g_score[current] + 1
				if tentative < g_score.get(neighbor, float('inf')):
					came_from[neighbor] = current
					g_score[neighbor] = tentative
					f_score = tentative + self.heuristic(neighbor, goal)
					heappush(open_nodes, (f_score, neighbor))

		if goal not in came_from:
			return []

		path = [goal]
		while path[-1] != start:
			path.append(came_from[path[-1]])
		path.reverse()
		return path[1:]

	def target(self, dt):
		self.path_timer -= dt
		if self.path_timer <= 0 or not self.path:
			start_tile = self.tile_pos(self.rect.center)
			goal_tile = self.tile_pos(self.player.rect.center)
			self.path = self.find_path(start_tile, goal_tile)
			self.path_timer = self.path_update_interval

		target_point = pygame.Vector2(self.player.rect.center)
		if self.path:
			next_tile = self.path[0]
			target_point = self.tile_center(next_tile)
			if target_point.distance_to(self.rect.center) <= max(2, self.speed * dt):
				self.path.pop(0)

		move_vector = target_point - pygame.Vector2(self.rect.center)
		self.direction = move_vector.normalize() if move_vector.length_squared() else pygame.Vector2()

	def move(self, dt):
		self.rect.x += self.direction.x * self.speed * dt
		self.check_collision("horizontal")
		self.rect.y += self.direction.y * self.speed * dt
		self.check_collision("vertical")

	def check_collision(self, direction):
		for sprite in self.collision_sprites:
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
		self.target(dt)
		self.move(dt)
		self.draw(dt)
