#importa pygame, e importa los demas archivos del juego

import pygame
from classes import *

#Inicia pygame
pygame.init()
WIDTH = 1000
HEIGHT = 650

#Bucle principal del juego...
def main():

    flag_juego = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Donkey Kong')
    clock = pygame.time.Clock()

    pantalla_juego = Juego(screen)
    Juego.level = 1
    while flag_juego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_juego = False

            pantalla_juego.__update__(event)
        pantalla_juego.__draw__()

        pygame.display.flip()
        clock.tick(60)

main()

pygame.quit()
quit()
