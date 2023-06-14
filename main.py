import pygame

#window constants
__window_title = 'Forward Snake'
__screen_resolution = (640, 640)

# colors constants
__white = (255, 255, 255)
__black = (0, 0, 0)

#grid constants
__grid_cell_width = 20
__grid_cell_height = 20
__grid_cell_padding_x = 2
__grid_cell_padding_y = 2
__grid_start_coordinates = (10, 10)

def quit():
	print('Bye!')
	pass

def make_grid(dimensions):

	rows, cols = dimensions
	start_x, start_y = __grid_start_coordinates

	current_x = start_x
	current_y = start_y

	for i in range(0, rows):
		for j in range(0, cols):
			pygame.draw.rect(screen, __white, [current_x, current_y, __grid_cell_width, __grid_cell_height])
			current_x += __grid_cell_width + __grid_cell_padding_x

		current_y += __grid_cell_height + __grid_cell_padding_y
		current_x = start_x
	


# initializing pygame
pygame.init()
screen = pygame.display.set_mode(__screen_resolution)
# setting the window title
pygame.display.set_caption(__window_title)

# A flag to keep or not keep the game loop running
running = True
# The in game clock.
clock = pygame.time.Clock()

#we will first make a 20 X 20 grid

while running:
	for event in pygame.event.get():
		running = not (event.type == pygame.QUIT)
		print(event)

	make_grid(dimensions=(20, 20))
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
