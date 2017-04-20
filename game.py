# include pygame from pip
import pygame

# in order to use pygame, we have to run the init method
pygame.init()
screen = {
	"height": 512,
	"width": 480
}

screen_size = (screen['height'], screen['width'])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

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