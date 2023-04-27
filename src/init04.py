import pygame, sys
from pygame.locals import *
import time

pygame.init()
SCREEN = pygame.display.set_mode((500,500))
pygame.display.set_caption('pygame - init04')


#play sounds
soundObj = pygame.mixer.Sound('../assets/sounds/zeldaSound.mp3')
soundObj.play()
time.sleep(10)
soundObj.stop()



# music in background and loop 
pygame.mixer.music.load('../assets/sounds/zeldaSound.mp3')
pygame.mixer.music.play(-1,0.0)



while True:
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         sys.exit()

   pygame.display.update()