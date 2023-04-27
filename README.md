# Starting with Pygame

### This repository is projects lists where I learned the firsts steps with Pygame. 

> The goal this projects is learn algorithms, data structure and object orientation with creating games with Python. 


# [init01](./src/init01.py)
Init01 I learned how created a window with Pygame.
```python
import pygame, sys

pygame.init()
SCREEN = pygame.display.set_mode((300,300)) # set size of screen
pygame.display.set_caption('Init with Pygame')

while True:
	for event in pygame.event.get(): # get all events of pygame
		if event.type == QUIT: # check if the user closer window to closer window
			pygame.quit()
			sys.exit()
	pygame.draw.update()
```

# [init02](./src/init02.py)
init02 I learned how created object and creating movements.

[Gif](https://imgur.com/ZXdmRlZ)

# [init03](./src/init03.py)
init02 I learned how render text and set font.

[img](https://imgur.com/UdULD3K)

# [init04](./src/init04.py)
in this part I learned how to play sounds

```python
#play sounds
soundObj = pygame.mixer.Sound('../assets/sounds/sound.mp3')
soundObj.play()
time.sleep(10)
soundObj.stop()

# music in background and loop 
pygame.mixer.music.load('../assets/sounds/zeldaSound.mp3')
pygame.mixer.music.play(-1,0.0)
```

