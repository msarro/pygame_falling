import pygame
import sys
import random

pygame.init()

# Set the height and width of the display
WIDTH = 800
HEIGHT = 600

# Set the RGB value for the player
PLAYER_RGB = (255,0,0)

# Set the RGB value for the enemy
ENEMY_RGB = (0,255,0)

# Set the RGB background color
BACKGROUND_COLOR = (0,0,0)

# Set the size of the player
player_height = 50
player_width = 50

# Set the initial player location
player_x = WIDTH/2
player_y = HEIGHT-(2*player_height)

# Initial movement factor
movement_factor=2

# Set the initial position and size of the player
player_pos = [player_x, player_y]
player_size = [player_height, player_width]

# Enemy information
enemy_height = 50
enemy_width = 50
enemy_x = random.randint(0,WIDTH-enemy_width)
enemy_y = 0
enemy_pos = [enemy_x,enemy_y]
enemy_size = [enemy_height,enemy_width]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while game_over != True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            player_x = player_pos[0]
            player_y = player_pos[1]
            if event.key == pygame.K_LEFT:
                player_x -= 10 * movement_factor
            elif event.key == pygame.K_RIGHT:
                player_x += 10 * movement_factor
            elif event.key == pygame.K_UP:
                player_y -= 10 * movement_factor
            elif event.key == pygame.K_DOWN:
                player_y += 10 * movement_factor
            player_pos = [player_x, player_y]

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, ENEMY_RGB, (enemy_pos[0], enemy_pos[1], enemy_size[0], enemy_size[1]))
    pygame.draw.rect(screen, PLAYER_RGB, (player_pos[0], player_pos[1], player_size[0], player_size[1]))
    pygame.display.update()