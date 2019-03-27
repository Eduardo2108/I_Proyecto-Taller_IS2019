# Libraries
import pygame
from classes import *

# Settings
pygame.init()
displayWidth = 1000
displayHeight = 650

def main():
    displayFlag = True

    frame = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption('Donkey Kong')
    clock = pygame.time.Clock()

    game_screen = GameScreen(frame)

    while displayFlag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                displayFlag = False

            game_screen.__update__(event)
        game_screen.__draw__()

        pygame.display.flip()
        clock.tick(30)

main()

pygame.quit()
quit()
