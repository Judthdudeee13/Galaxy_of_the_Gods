from settings import *

class Timer:
	def __init__(self, duration, repeat = False, autostart = False, func = None):
		self.duration = duration
		self.start_time = 0
		self.active = False
		self.repeat = repeat
		self.func = func
		
		if autostart:
			self.activate()

	def __bool__(self):
		return self.active

	def activate(self):
		self.active = True
		self.start_time = pygame.time.get_ticks()

	def deactivate(self):
		self.active = False
		self.start_time = 0
		if self.repeat:
			self.activate()

	def update(self):
		if self.active:
			if pygame.time.get_ticks() - self.start_time >= self.duration:
				if self.func and self.start_time != 0: self.func()
				self.deactivate()

class Clock(Timer):
	def __init__(self, cycle_length, recharge_time, value=(True, False), autostart=False, repeat=0, onFunc=None, offFunc=None):
		self.values = value
		self.isOn = True
		self.cycle_length = cycle_length
		self.recharge_time = recharge_time
		self.onFunc = onFunc
		self.offFunc = offFunc
		self.repeat = repeat
		self.set_up()
		if autostart:
			self.start()

	def __eq__(self, other):
		if isinstance(other, str):
			if self.isOn:
				return self.values[0] == other
		return self.values[1] == other
	
	def set_up(self):
		self.onTimer = Timer(self.cycle_length, func=self.start_off)
		self.offTimer = Timer(self.recharge_time, func=self.start_on)

	def start_off(self):
		self.offTimer.activate()
		self.isOn = False

	def start_on(self):
		if self.repeat or self.repeat == -1:
			self.repeat -= 1 if self.repeat else 0
			self.onTimer.activate()
			self.isOn = True
	
	def update(self):
		self.onTimer.update()
		self.offTimer.update()