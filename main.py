import pygame
import random

#window constants
__window_title = 'Forward Snake'
__screen_resolution = (640, 640)

# colors constants
__white = (255, 255, 255)
__black = (0, 0, 0)

#grid constants
__grid_dimensions = (20, 20)
__grid_cell_width = 20
__grid_cell_height = 20
__grid_cell_padding_x = 2
__grid_cell_padding_y = 2
__grid_start_coordinates = (10, 10)


def quit():
	print('Bye!')
	pass

def init_snake():
	snake_coordinates = [(__grid_dimensions[0] // 2, __grid_dimensions[1] // 2)]A
	return snake_coordinates

def set_new_apple():
	# put an apple at random on the grid
	# ensure that the apple is not 'on' the snake

	#use the snake which is defined globally.
	global snake
	
	while True:
		apple_coords = (random.randrange(0, __grid_dimensions[0]), random.randrange(0, __grid_dimensions[1]))
		if apple_coords not in snake:
			return apple_coords

def update_snake():

	# use the global snake and appple.
	global snake
	global apple

	# move the snake's head one cell in its current direction
	new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
	
	# do some boundary checking
	if new_head[0] == -1:
		new_head[0] = __grid_dimensions[1]

	if new_head[0] == __grid_dimensions[1]:
		new_head[0] = 0

	if new_head[1] == -1:
		new_head[1] = __grid_dimensions[0]

	if new_head[1] == __grid_dimensions[0]:
		new_head[1] = 0

	#update the whole snake
	temp = new_head
	for i in range(len(snake)):
		new_temp = snake[i]
		snake[i] = temp
		temp = new_temp
		
	# if the snake's head is currently in the same position as the apple
	if new_head == apple:
		print("SNEK IS EAT APPLE.")
		# create a new head for the snake and set a new apple.
		snake = [apple] + snake
		apple = set_new_apple()

def make_grid():

	rows, cols = __grid_dimensions
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
# make snek
snake = init_snake()
# make the apple
apple = set_new_apple()
# setting snake direction as a vector. To left by default.
snake_direction = (-1, 0) 

while running:
	for event in pygame.event.get():
		running = not (event.type == pygame.QUIT)
		print(event)

	make_grid()
	pygame.display.update()
	clock.tick(2)

pygame.quit()
quit()
