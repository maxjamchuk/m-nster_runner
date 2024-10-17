import information
import os
import pygame as pg
from random import choice
import sys

from Player import Player
from Monster import Monster
from constants import (
	BG_COLOR,
	FONT_PATH,
	FONT_SIZE,
	FPS,
	GAME_MESSAGE,
	GAME_NAME,
	GROUND_IMAGE_PATH,
	GROUND_POS,
	MONSTER_TIMER_DELAY,
	MONSTER_TYPES,
	SCORE_TEXT_COLOR,
	SCREEN_MSG_CENTER,
	SCREEN_SIZE,
	SKY_IMAGE_PATH,
	SKY_POS,
	START_IMAGE_CENTER,
	START_IMAGE_PATH,
	TEXT_COLOR,
	TITLE_CENTER,
)


def show_score() -> int:
	"""
	Shows the current score on the screen.

	Returns:
	int: The elapsed time in seconds.
	"""
	elapsed_time = pg.time.get_ticks() // 1000 - start_time
	score_text = test_font.render(f'Score: {elapsed_time}', True, SCORE_TEXT_COLOR)
	score_text_rect = score_text.get_rect(center=TITLE_CENTER)
	screen.blit(score_text, score_text_rect)
	
	return elapsed_time


def is_crash_sprite(player_sprite: pg.sprite.Sprite, monster_group: pg.sprite.Group) -> bool:
	"""
	Checks if the player's sprite collides with any sprite in the monster group.
	If a collision is detected, the monster group is emptied.

	Args:
	    player_sprite (pg.sprite.Sprite): The sprite of the player.
	    monster_group (pg.sprite.Group): The group of sprites representing the monsters.

	Returns:
	    bool: True if no collision is detected, False otherwise.
	"""
	if pg.sprite.spritecollide(player_sprite, monster_group, False):
		monster_group.empty()
		return False
	return True



pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption('GAME')
clock = pg.time.Clock()
test_font = pg.font.Font(FONT_PATH, FONT_SIZE)
game_active = False
start_time = 0
score = 0

player = pg.sprite.GroupSingle()
player.add(Player())

monster_group = pg.sprite.Group()

sky_surface = pg.image.load(SKY_IMAGE_PATH).convert()
ground_surface = pg.image.load(GROUND_IMAGE_PATH).convert()

start_image = pg.image.load(START_IMAGE_PATH).convert_alpha()
start_image = pg.transform.rotozoom(start_image, 0, 2)
start_image_rect = start_image.get_rect(center = START_IMAGE_CENTER)

game_name = test_font.render(GAME_NAME, False, TEXT_COLOR)
game_name_rect = game_name.get_rect(center = TITLE_CENTER)

game_message = test_font.render(GAME_MESSAGE, False, TEXT_COLOR)
game_message_rect = game_message.get_rect(center = SCREEN_MSG_CENTER)


monster_timer = pg.USEREVENT + 1
pg.time.set_timer(monster_timer, MONSTER_TIMER_DELAY)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit(0)

		if game_active:
			if event.type == monster_timer:
				monster_group.add(Monster(choice(MONSTER_TYPES)))
		
		else:
			if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
				game_active = True
				start_time = int(pg.time.get_ticks() / 1000)


	if game_active:
		screen.blit(sky_surface, SKY_POS)
		screen.blit(ground_surface, GROUND_POS)
		score = show_score()
		
		player.draw(screen)
		player.update()

		monster_group.draw(screen)
		monster_group.update()

		game_active = is_crash_sprite(player_sprite = player.sprite, monster_group = monster_group)
		
	else:
		screen.fill(BG_COLOR)
		screen.blit(start_image, start_image_rect)

		score_message = test_font.render(f'Your score: {score}', False, TEXT_COLOR)
		score_message_rect = score_message.get_rect(center = SCREEN_MSG_CENTER)
		screen.blit(game_name, game_name_rect)

		if score == 0: screen.blit(game_message, game_message_rect)
		else: screen.blit(score_message, score_message_rect)

	pg.display.update()
	clock.tick(FPS)
