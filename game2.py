# IMPORT
import pygame
from math import fabs
from random import randint

# init pygame
pygame.init()

# define variables
screen = {
	"height": 512,
	"width": 480
}

keys = {
	"right": 100,
	"left": 97,
	"up": 119,
	"down": 115
}

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}

hero = {
	"x": (screen['width'] / 2),
	"y": 400,
	"speed": 2,
	"wins": 0,
	"health": 100,
	"lives": 5,
	"is_alive": True
}

enemy = {
	'x': (screen['width'] / 2),
	'y': 32,
	'speed': 3,
	'direction': "N",
}


buff = {
	'x': (screen['width'] / 3),
	'y': 32,
	'speed': 2,
	'direction': "S",
	'heal': 10,
}

debuff = {
	'x': (screen['width'] / 4),
	'y': 32,
	'speed': 1,
	'direction': "E",
	'damage': 20,
}

directions = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]

# images
screen_size = (screen['height'], screen['width'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("enemy Chase")
background_image = pygame.image.load('images/mariobackground.png')
hero_image = pygame.image.load('images/hero.png')
enemy_image = pygame.image.load('images/goblin.png')
buff_image = pygame.image.load('images/mushroom.png')
debuff_image = pygame.image.load('images/monster.png')
# music
pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('sounds/win.wav')
lose_sound = pygame.mixer.Sound('sounds/lose.wav')

# framerate/timer
tick = 0
time = 0

# game on
game_on = True

# define functions
def keypress():
		if event.type == pygame.KEYDOWN:
			if event.key == keys['up']:
				keys_down['up'] = True
			elif event.key == keys['down']:
				keys_down['down'] = True
			elif event.key == keys['right']:
				keys_down['right'] = True
			elif event.key == keys['left']:
				keys_down['left'] = True
		elif event.type == pygame.KEYUP:
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
def hero_move():
	if (keys_down['up'] and hero['y'] > 0):
		hero['y'] -= hero['speed']
	elif (keys_down['down'] and hero['y'] < screen['height'] - 85):
		hero['y'] += hero['speed']
	if (keys_down['right'] and hero['x'] < screen['width'] - 15):
		hero['x'] += hero['speed']
	elif (keys_down['left'] and hero['x'] > 0):
		hero['x'] -= hero['speed']
def framerate():
	global tick
	global time
	tick += 1
	if (tick % 60 == 0):
		time += 1
	print tick
	print time
def evil_move(enemytype):
	if (enemytype['direction'] == 'N'):
		enemytype['y'] -= enemytype['speed']
	elif (enemytype['direction'] == 'S'):
		enemytype['y'] += enemytype['speed']
	elif (enemytype['direction'] == 'E'):
		enemytype['x'] += enemytype['speed']
	elif (enemytype['direction'] == 'W'):
		enemytype['x'] -= enemytype['speed']		
	elif (enemytype['direction'] == 'NE'):
		enemytype['y'] -= enemytype['speed']
		enemytype['x'] += enemytype['speed']
	elif (enemytype['direction'] == 'NW'):
		enemytype['y'] -= enemytype['speed']
		enemytype['x'] += enemytype['speed']
	elif (enemytype['direction'] == 'SE'):
		enemytype['y'] += enemytype['speed']
		enemytype['x'] += enemytype['speed']
	elif (enemytype['direction'] == 'SW'):
		enemytype['y'] += enemytype['speed']
		enemytype['x'] -= enemytype['speed']

	if (tick % 30 == 0):
		new_dir_index = randint(0, (len(directions)- 1))
		enemytype['direction'] = directions[new_dir_index]

	if (enemytype['x'] < 0):
		enemytype['x'] = (screen['width'] - 32)
	if (enemytype['x'] > (screen['width'] - 32)):
		enemytype['x'] = 0
	if (enemytype['y'] < 0):
		enemytype['y'] = (screen['height'] - 32)
	if (enemytype['y'] > (screen['height'] - 32)):
		enemytype['y'] = 0
# def collision(hero, enemy)
while game_on:
	tick += 1
	# if (tick % 60 == 0):
	# 	time += 1
	framerate()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_on = False
	keypress()
	hero_move()
	evil_move(enemy)
	evil_move(buff)

	distance_between_gob = fabs(hero['x'] - enemy['x']) + fabs(hero['y'] - enemy['y'])
	if (distance_between_gob < 32):
		# hero and enemy are touching if 32 x 32 images
		# print("Collision!")
		# generate a random X > 0, X < screen['width']
		# generate a random Y > 0, Y < screen['height']
		rand_spawn_x_gob = randint(0, screen['width'] - 100)
		rand_spawn_y_gob = randint(0, screen['height'] - 100)
		enemy['x'] = rand_spawn_x_gob
		enemy['y'] = rand_spawn_y_gob
		# update the hero's wins
		hero['wins'] += 1
		enemy['speed'] += 1
		win_sound.play()

	distance_between_mush = fabs(hero['x'] - buff['x']) + fabs(hero['y'] - buff['y'])
	if (distance_between_mush < 32):
		rand_spawn_x_mush = randint(0, screen['width'] - 100)
		rand_spawn_y_mush = randint(0, screen['height'] - 100)	
		buff['x'] = rand_spawn_x_mush
		buff['y'] = rand_spawn_y_mush
		if (hero['health'] < 100):
			hero['health'] += buff['heal']

	distance_between_debuff = fabs(hero['x'] - debuff['x']) + fabs(hero['y'] - debuff['y'])
	if (distance_between_debuff < 32):
		rand_spawn_x_debuff = randint(0, screen['width'] - 100)
		rand_spawn_y_debuff = randint(0, screen['height'] - 100)		
		debuff['x'] = rand_spawn_x_debuff
		debuff['y'] = rand_spawn_y_debuff
		if (hero['health'] > 0 and hero['lives'] > 0):
			if hero['health'] < debuff['damage']:
				hero['health'] = 100,
				hero['lives'] -= 1
			else:
				hero['health'] -= debuff['damage']
		elif (hero['health'] <= 0 and hero['lives'] > 0):
			hero['health'] = 100
			hero['lives'] -= 1
		lose_sound.play()


	elif (distance_between_debuff > 0):
		if (distance_between_debuff > 0):
			if (debuff['x'] > hero['x']):
				debuff['x'] -= debuff['speed']
			elif (debuff['x'] < hero['x']):
				debuff['x'] += debuff['speed']
			if (debuff['y'] > hero['y']):
				debuff['y'] -= debuff['speed']
			elif (debuff['y'] < hero['y']):
				debuff['y'] += debuff['speed']
	# elif (distance_debuff > 32):
	# 	debuff['x'] 

	# //RENDER\\
	# blit takes two arguments: What and Where
	pygame_screen.blit(background_image, [0,0])
	


	# draw the hero

	pygame_screen.blit(hero_image , [hero['x'],hero['y']])

	pygame_screen.blit(buff_image , [buff['x'],buff['y']])

	pygame_screen.blit(debuff_image , [debuff['x'], debuff['y']])

	pygame_screen.blit(enemy_image , [enemy['x'],enemy['y']])


	# draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Captures: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40, 40])

	font = pygame.font.Font(None, 25)
	lives_text = font.render("Lives: %d" % hero['lives'], True, (0,0,0))
	pygame_screen.blit(lives_text, [40, 60])

	font = pygame.font.Font(None, 25)
	health_text = font.render("HP: %d" % (hero['health']), True, (0,0,0))
	pygame_screen.blit(health_text, [40, 80])

	font = pygame.font.Font(None, 25)
	timer_text = font.render("Time Elapsed: %d" % time, True, (0,0,0))
	pygame_screen.blit(timer_text, [40, 100])

# 	to clear the screen for next time
	pygame.display.flip()


