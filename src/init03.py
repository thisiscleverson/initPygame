import pygame, sys
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((500,500))
pygame.display.set_caption('init03')


font = pygame.font.Font('../assets/fonts/Sigmar-Regular.ttf',32)

"""
 O parâmetro 'antialias' na função 'render' da biblioteca Pygame
 é usado para determinar se o texto renderizado deve ser suavizado (antialiasing) 
 ou não
"""
textRender = font.render('Hello Pygame',True, (255,0,0)) # text | antialias | color

textRender 
textRectObj = textRender.get_rect()
textRectObj.center = (250,250) # set position 

while True:

   #pygame.draw.aaline(SCREEN, (0,200,0), (60, 80), (130, 100), 1)

   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   SCREEN.blit(textRender, textRectObj)
   pygame.display.update()


