import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

PLAYER_RGB = (255,0,0)

player_x = WIDTH/2
player_y = HEIGHT/2
player_height = 50
player_width = 50

player_pos = [player_x, player_y]
player_size = [player_height, player_width]

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
                player_x -= 10
            elif event.key == pygame.K_RIGHT:
                player_x += 10
            elif event.key == pygame.K_UP:
                player_y -= 10
            elif event.key == pygame.K_DOWN:
                player_y += 10
            player_pos = [player_x, player_y]

    pygame.draw.rect(screen, PLAYER_RGB, (player_pos[0], player_pos[1], player_size[0], player_size[1]))
    pygame.display.update()