import pygame, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock() 

FPS = 30
WIDTH  = 400
HEIGHT = 400

pixel_x = WIDTH  / 2
pixel_y = HEIGHT / 2

DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT)) # size of screen
pygame.display.set_caption('Hello World pygame')


direction = 'right'

while True:
   DISPLAYSURF.fill(color=(145,251,246)) # set background color scree

   for event in pygame.event.get(): # get all events
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   if direction == 'right':
      pixel_x += 5
      if pixel_x == 280:
         direction = 'down'
   elif direction == 'down':
      pixel_y += 5
      if pixel_y == 220:
         direction = 'left'
   elif direction == 'left':
      pixel_x -= 5
      if pixel_x == 10:
         direction = 'up'
   elif direction == 'up':
      pixel_y -= 5
      if pixel_y == 10:
         direction = 'right'
   
   pygame.draw.rect(DISPLAYSURF, (255,0,0),(pixel_x,pixel_y, 25, 25))
   pygame.display.update()
   fpsClock.tick(FPS)
   
