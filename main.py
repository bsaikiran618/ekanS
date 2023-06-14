import pygame

__window_title = 'Forward Snake'

def quit():
	print('Bye!')
	pass

# initializing pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
# setting the window title
pygame.display.set_caption(__window_title)

# A flag to keep or not keep the game loop running
running = True
# The in game clock.
clock = pygame.time.Clock()

while running:
	for event in pygame.event.get():
		running = not (event.type == pygame.QUIT)
		print(event)

	pygame.draw.rect(screen, (255, 255, 255), [25, 25, 100, 100])
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
