from typing import List
import pygame as pg

from random import randint


class Monster(pg.sprite.Sprite):
	"""
	A class representing a monster in the game.

	Attributes:
		frames (List[pg.Surface]): A list of images representing the monster's animations.
		animation_index (float): The index of the current animation frame.
		image (pg.Surface): The current animation frame.
		rect (pg.Rect): The rectangle representing the monster's position and size.

	Args:
		type (str): The type of monster ('bird', 'demon', 'crab').
	"""

	def __init__(self, type: str) -> None:
		super().__init__()

		if type == 'bird':
			bird_1 = pg.image.load('static/graphics/bird/bird1.png').convert_alpha()
			bird_2 = pg.image.load('static/graphics/bird/bird2.png').convert_alpha()
			bird_3 = pg.image.load('static/graphics/bird/bird3.png').convert_alpha()
			self.frames: List[pg.Surface] = [bird_1, bird_2, bird_3]
			y_pos: int = 210
		elif type == 'crab':
			crab_1 = pg.image.load('static/graphics/crab/crab1.png').convert_alpha()
			crab_2 = pg.image.load('static/graphics/crab/crab2.png').convert_alpha()
			self.frames: List[pg.Surface] = [crab_1, crab_2]
			y_pos: int = 300
		elif type == 'demon':
			demon_1 = pg.image.load('static/graphics/demon/demon_1.png').convert_alpha()
			demon_2 = pg.image.load('static/graphics/demon/demon_2.png').convert_alpha()
			self.frames: List[pg.Surface] = [demon_1, demon_2]
			y_pos: int = randint(220, 290)

		self.animation_index: float = 0.0
		self.image: pg.Surface = self.frames[int(self.animation_index)]
		self.rect: pg.Rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))


	def animation_state(self) -> None:
		"""
		Update the animation index and change the image to the next frame.
		"""
		self.animation_index += 0.1
		if self.animation_index >= len(self.frames):
			self.animation_index = 0.0
		self.image = self.frames[int(self.animation_index)]


	def update(self) -> None:
		"""
		Update the animation and move the monster to the left.
		"""
		self.animation_state()
		self.rect.x -= 6
		self.destroy()


	def destroy(self) -> None:
		"""
		Kill the monster if it has moved out of the screen.
		"""
		if self.rect.x <= -100:
			self.kill()
			self.kill()