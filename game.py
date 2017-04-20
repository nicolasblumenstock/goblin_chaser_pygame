# include pygame from pip
import pygame

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


hero = {
	"x": (screen['height']/2),
	"y": (screen['width']/2),
	"speed": 5
}

screen_size = (screen['height'], screen['width'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')

# //Main Game Loop\\
game_on = True
# while 1 loop
while game_on:
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

	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['right']:
		hero['x'] += hero['speed']
	elif keys_down['left']:
		hero['x'] -= hero['speed']


	# //RENDER\\
	# blit takes two arguments: What and Where
	pygame_screen.blit(background_image, [0,0])
	# draw the hero
	pygame_screen.blit(hero_image ,[hero['x'],hero['y']])


# 	to clear the screen for next time
	pygame.display.flip()