# include pygame from pip
import pygame

# bring in the math module so we can bring in the absolute value

from math import fabs

from random import randint

# in order to use pygame, we have to run the init method
pygame.init()


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


rand_init_spawn_x_gob = randint(0, screen['width'] - 100)
rand_init_spawn_y_gob = randint(0, screen['height'] - 100)
rand_init_spawn_x_mush = randint(0, screen['width'] - 100)
rand_init_spawn_y_mush = randint(0, screen['height'] - 100)
rand_init_spawn_x_death = randint(0, screen['width'] - 100)
rand_init_spawn_y_death = randint(0, screen['height'] - 100)


hero = {
	"x": (screen['height']/2),
	"y": (screen['width']/2),
	"speed": 2,
	"wins": 0,
	"health": 100,
	"lives": 5,
	"is_alive": True

}

goblin = {
	'x': rand_init_spawn_x_gob,
	'y': rand_init_spawn_y_gob,
	'speed': 3,
	'direction': "N",
}


mushroom = {
	'x': rand_init_spawn_x_mush,
	'y': rand_init_spawn_y_mush,
	'speed': 2,
	'direction': "S",
	'heal': 10,
}

death = {
	'x': rand_init_spawn_x_death,
	'y': rand_init_spawn_y_death,
	'speed': 3,
	'direction': "E",
	'damage': 20,
}

directions = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]




screen_size = (screen['height'], screen['width'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/mariobackground.png')
hero_image = pygame.image.load('images/hero.png')
# hero_image_scaled = pygame.transform.scale(hero_image, (50, 50))
goblin_image = pygame.image.load('images/goblin.png')
# goblin_image_scaled = pygame.transform.scale(goblin_image ,(100, 100))
mushroom_image = pygame.image.load('images/mushroom.png')
death_image = pygame.image.load('images/monster.png')
# death_image_scaled = pygame.transform.scale(death_image, (32, 32))

# add music filesw
pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('sounds/win.wav')
lose_sound = pygame.mixer.Sound('sounds/lose.wav')
tick = 0;
timer = 0


# //Main Game Loop\\
game_on = True
# while 1 loop
while game_on:
	tick += 1
	for event in pygame.event.get():
	# adding in a quit even
	# looping through all events that happen this game loop cycle
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
			game_on = False
			# update our boolean, so pygame can escape the loop
		elif event.type == pygame.KEYDOWN:
			# print event.key
			if event.key == keys['up']:
				keys_down['up'] = True
				# print("User Pressed UP")
				# hero['y'] -= hero['speed']
			elif event.key == keys['down']:
				keys_down['down'] = True
				# hero['y'] += hero['speed']
				# print("User Pressed DOWN")
			elif event.key == keys['right']:
				keys_down['right'] = True
				# hero['x'] += hero['speed']
				# print("User Pressed RIGHT")
			elif event.key == keys['left']:
				keys_down['left'] = True
				# hero['x'] -= hero['speed']
				# print("User Pressed LEFT")
		elif event.type == pygame.KEYUP:
			# print "the user let go of the key"
			if event.key == keys['up']:
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
	if (keys_down['up'] and hero['y'] > 0):
		hero['y'] -= hero['speed']
	elif (keys_down['down'] and hero['y'] < screen['height'] - 85):
		hero['y'] += hero['speed']
	if (keys_down['right'] and hero['x'] < screen['width'] - 15):
		hero['x'] += hero['speed']
	elif (keys_down['left'] and hero['x'] > 0):
		hero['x'] -= hero['speed']


	if (tick % 30 == 0):
		timer += 1


	# gob_move = randint(0,11)
	# counter_gob = 1
	# if (gob_move >= 0 and gob_move <= 2 and counter_gob > 0):
	# 	goblin['x'] -= goblin['speed']
	# 	counter_gob -= 1
	# if (gob_move > 2 and gob_move <= 5 and counter_gob > 0):
	# 	goblin['x'] += goblin['speed']
	# 	counter_gob -= 1
	# if (gob_move > 5 and gob_move <= 8 and counter_gob > 0):
	# 	goblin['y'] -= goblin['speed']
	# 	counter_gob -= 1
	# if (gob_move > 8 and gob_move <= 11 and counter_gob > 0):
	# 	goblin['y'] += goblin['speed']
	# 	counter_gob -= 1

	# mush_move = randint(0,11)
	# counter_mush = 1
	# if (mush_move >= 0 and mush_move <= 2 and counter_mush > 0):
	# 	mushroom['x'] -= mushroom['speed']
	# 	counter_mush -= 1
	# if (mush_move > 2 and mush_move <= 5 and counter_mush > 0):
	# 	mushroom['x'] += mushroom['speed']
	# 	counter_mush -= 1
	# if (mush_move > 5 and mush_move <= 8 and counter_mush > 0):
	# 	mushroom['y'] -= mushroom['speed']
	# 	counter_mush -= 1
	# if (mush_move > 8 and mush_move <= 11 and counter_mush > 0):
	# 	mushroom['y'] += mushroom['speed']
	# 	counter_mush -= 1

	# death_move = randint(0,11)
	# counter_death = 1
	# if (death_move >= 0 and death_move <= 2 and counter_death > 0):
	# 	death['x'] -= death['speed']
	# 	counter_death -= 1
	# if (death_move > 2 and death_move <= 5 and counter_death > 0):
	# 	death['x'] += death['speed']
	# 	counter_death -= 1
	# if (death_move > 5 and death_move <= 8 and counter_death > 0):
	# 	death['y'] -= death['speed']
	# 	counter_death -= 1
	# if (death_move > 8 and death_move <= 11 and counter_death > 0):
	# 	death['y'] += death['speed']
	# 	counter_death -= 1



	if (goblin['direction'] == 'N'):
		goblin['y'] -= goblin['speed']
	elif (goblin['direction'] == 'S'):
		goblin['y'] += goblin['speed']
	elif (goblin['direction'] == 'E'):
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'W'):
		goblin['x'] -= goblin['speed']		
	elif (goblin['direction'] == 'NE'):
		goblin['y'] -= goblin['speed']
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'NW'):
		goblin['y'] -= goblin['speed']
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'SE'):
		goblin['y'] += goblin['speed']
		goblin['x'] += goblin['speed']
	elif (goblin['direction'] == 'SW'):
		goblin['y'] += goblin['speed']
		goblin['x'] -= goblin['speed']

	if (tick % 30 == 0):
		new_dir_index = randint(0, (len(directions)- 1))
		goblin['direction'] = directions[new_dir_index]

	if (mushroom['direction'] == 'N'):
		mushroom['y'] -= mushroom['speed']
	elif (mushroom['direction'] == 'S'):
		mushroom['y'] += mushroom['speed']
	elif (mushroom['direction'] == 'E'):
		mushroom['x'] += mushroom['speed']
	elif (mushroom['direction'] == 'W'):
		mushroom['x'] -= mushroom['speed']		
	elif (mushroom['direction'] == 'NE'):
		mushroom['y'] -= mushroom['speed']
		mushroom['x'] += mushroom['speed']
	elif (mushroom['direction'] == 'NW'):
		mushroom['y'] -= mushroom['speed']
		mushroom['x'] += mushroom['speed']
	elif (mushroom['direction'] == 'SE'):
		mushroom['y'] += mushroom['speed']
		mushroom['x'] += mushroom['speed']
	elif (mushroom['direction'] == 'SW'):
		mushroom['y'] += mushroom['speed']
		mushroom['x'] -= mushroom['speed']

	if (tick % 30 == 0):
		new_dir_index_mush = randint(0, (len(directions)- 1))
		mushroom['direction'] = directions[new_dir_index_mush]





	# if (hero['x'] < 0):
	# 	hero['x'] = (screen['width'] - 25)
	# 	# key['right'] = False
	# if (hero['x'] > (screen['width'] - 25)):
	# 	hero['x'] = 0
	# 	# hero['speed'] = 0
	# if (hero['y'] < 0):
	# 	hero['y'] = (screen['height'] - 100)
	# 	# hero['speed'] = 0
	# if (hero['y'] > (screen['height'] - 100)):
	# 	hero['y'] = 0
	# 	# hero['speed'] = 0

	if (goblin['x'] < 0):
		goblin['x'] = (screen['width'] - 50)
	if (goblin['x'] > (screen['width'] - 50)):
		goblin['x'] = 0
	if (goblin['y'] < 0):
		goblin['y'] = (screen['height'] - 150)
	if (goblin['y'] > (screen['height'] - 150)):
		goblin['y'] = 0


	if (mushroom['x'] < 0):
		mushroom['x'] = (screen['width'] - 16)
	if (mushroom['x'] > (screen['width'] - 16)):
		mushroom['x'] = 0
	if (mushroom['y'] < 0):
		mushroom['y'] = (screen['height'] - 48)
	if (mushroom['y'] > (screen['height'] - 48)):
		mushroom['y'] = 0

	if (death['x'] < 0):
		death['x'] = (screen['width'] - 16)
	if (death['x'] > (screen['width'] - 16)):
		death['x'] = 0
	if (death['y'] < 0):
		death['y'] = (screen['height'] - 48)
	if (death['y'] > (screen['height'] - 48)):
		death['y'] = 0



		# collision detection!
	distance_between_gob = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if (distance_between_gob < 32):
		# hero and goblin are touching if 32 x 32 images
		# print("Collision!")
		# generate a random X > 0, X < screen['width']
		# generate a random Y > 0, Y < screen['height']
		rand_spawn_x_gob = randint(0, screen['width'] - 100)
		rand_spawn_y_gob = randint(0, screen['height'] - 100)
		goblin['x'] = rand_spawn_x_gob
		goblin['y'] = rand_spawn_y_gob
		# update the hero's wins
		hero['wins'] += 1
		goblin['speed'] += 1
		win_sound.play()

	distance_between_mush = fabs(hero['x'] - mushroom['x']) + fabs(hero['y'] - mushroom['y'])
	if (distance_between_mush < 32):
		rand_spawn_x_mush = randint(0, screen['width'] - 100)
		rand_spawn_y_mush = randint(0, screen['height'] - 100)	
		mushroom['x'] = rand_spawn_x_mush
		mushroom['y'] = rand_spawn_y_mush
		if (hero['health'] < 100):
			hero['health'] += mushroom['heal']

	distance_between_death = fabs(hero['x'] - death['x']) + fabs(hero['y'] - death['y'])
	if (distance_between_death < 32):
		rand_spawn_x_death = randint(0, screen['width'] - 100)
		rand_spawn_y_death = randint(0, screen['height'] - 100)		
		death['x'] = rand_spawn_x_death
		death['y'] = rand_spawn_y_death
		if (hero['health'] > 0 and hero['lives'] > 0):
			if hero['health'] < death['damage']:
				hero['health'] = 100,
				hero['lives'] -= 1
			else:
				hero['health'] -= death['damage']
		elif (hero['health'] <= 0 and hero['lives'] > 0):
			hero['health'] = 100
			hero['lives'] -= 1
		lose_sound.play()


	elif (distance_between_death > 100):
		if (distance_between_death > 5):
			if (death['x'] > hero['x']):
				death['x'] -= death['speed']
			elif (death['x'] < hero['x']):
				death['x'] += death['speed']
			if (death['y'] > hero['y']):
				death['y'] -= death['speed']
			elif (death['y'] < hero['y']):
				death['y'] += death['speed']
	# elif (distance_death > 32):
	# 	death['x'] 

	# //RENDER\\
	# blit takes two arguments: What and Where
	pygame_screen.blit(background_image, [0,0])
	


	# draw the hero

	pygame_screen.blit(hero_image , [hero['x'],hero['y']])

	pygame_screen.blit(mushroom_image , [mushroom['x'],mushroom['y']])

	pygame_screen.blit(death_image , [death['x'], death['y']])

	pygame_screen.blit(goblin_image , [goblin['x'],goblin['y']])


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
	timer_text = font.render("Time Elapsed: %d" % timer, True, (0,0,0))
	pygame_screen.blit(timer_text, [40, 100])

# 	to clear the screen for next time
	pygame.display.flip()