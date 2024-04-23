import pygame as pg


class Player(pg.sprite.Sprite):
	def __init__(self) -> None:
		"""
		Initialize a new Player instance.
		"""
		super().__init__()
		walk_1 = pg.image.load('static/graphics/player/walk_1.png').convert_alpha()
		walk_2 = pg.image.load('static/graphics/player/walk_2.png').convert_alpha()
		self.player_walk = [walk_1, walk_2]  # type: List[pg.Surface]
		self.player_index = 0  # type: int
		self.player_jump = pg.image.load('static/graphics/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]  # type: pg.Surface
		self.rect = self.image.get_rect(midbottom=(80, 300))  # type: pg.Rect
		self.gravity = 0  # type: int


	def player_input(self) -> None:
		"""
		Handle player input.
		"""
		keys = pg.key.get_pressed()
		if keys[pg.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -15


	def apply_gravity(self) -> None:
		"""
		Apply gravity to the player.
		"""
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300


	def animation_state(self) -> None:
		"""
		Update the player's animation state.
		"""
		if self.rect.bottom < 300:
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):
				self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]


	def update(self) -> None:
		"""
		Update the player's state.
		"""
		self.player_input()
		self.apply_gravity()
		self.animation_state()
		self.animation_state()
