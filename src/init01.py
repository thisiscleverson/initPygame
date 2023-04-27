import pygame, sys

pygame.init()
SCREEN = pygame.display.set_mode((300,300)) # set size of screen
pygame.display.set_caption('Init with Pygame')

while True:
	for event in pygame.event.get(): # get all events of pygame
		if event.type == QUIT: # check if the user closer windows
			pygame.quit()
			sys.exit()
	pygame.draw.update()