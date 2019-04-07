# Libraries
import pygame
import time
from player import *
from enemigos import *
# Settings
pygame.init()

#clase que crea los parametros para los barriles

# clase que crea los parametros de las plataformas
class plataformas:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        # identificador de la plataforma, y el alto, ancho y posicion
        self.rect = (x, y, width, height)
        self.tag = 'block'

    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 255, 255), self.rect) #dibuja el rectangulo, con el color que uno elija

#clase que pone todos los elementos del juego juntos en la pantalla
class Juego():
    def __init__(self, frame): # de entrada tiene la variable que contiene a la pantalla
        self.frame = frame
        self.player = Player(0, 500)
        self.x_plat = 100
        self.y_plat = 550
        self.W_plat = 600
        self.H_plat = 5
        self.flag = True
        self.level = 1

        self.enemies = [Enemy(-64, 0, (3, -1)), Enemy(760, 100, (-5, 1))]

        self.base = plataformas(0, 625, 1000, 5)

        self.p1 = plataformas(self.x_plat+550, self.y_plat+20, self.W_plat-400, self.H_plat)
        self.p2 = plataformas(self.x_plat+10, self.y_plat-140, self.W_plat-100, self.H_plat)
        self.p3 = plataformas(self.x_plat-80, self.y_plat-170, self.W_plat-50, self.H_plat)
        self.p4 = plataformas(self.x_plat+600, self.y_plat-300, self.W_plat-400, self.H_plat)

        self.p_Final = plataformas(self.x_plat+10, self.y_plat-210, self.W_plat-50, self.H_plat)
        self.level_plat = []
        self.plat_L1 = [self.base, plataformas(self.x_plat+550, self.y_plat+20, self.W_plat-400, self.H_plat),plataformas(self.x_plat+10, self.y_plat-40, self.W_plat-100, self.H_plat),plataformas(self.x_plat+600, self.y_plat-110, self.W_plat-400, self.H_plat), plataformas(self.x_plat+10, self.y_plat-210, self.W_plat-50, self.H_plat)]

        self.plat_L2 = [self.base, self.p1, self.p2,  self.p3, self.p_Final]

        self.plat_L3 = [self.base, self.p1, self.p2, self.p3,self.p4,self.p_Final]



    def __update__(self, event):


        if event.type == pygame.KEYUP: #si se suelta una tecla
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: # si son las de la izquierda
                self.player.action = 'standing' #se queda quedito, viendo a la izquierda
                self.player.state = 'left'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #si son las de la derecha, se queda quieto, viendo a la derecha
                self.player.action = 'standing'
                self.player.state = 'right'
        if event.type == pygame.KEYDOWN: # si se presiona una tecla
            if event.key == pygame.K_LEFT or event.key == pygame.K_a: #si son las de la izquierda,camina hacia la izquierda
                self.player.action = 'walking'
                self.player.state = 'left'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # si son las de la derecha, camina hacia la derecha
                self.player.action = 'walking'
                self.player.state = 'right'
            self.player.sprite_index = -1

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # si es el espacio, o la tecla de arriba, salta

                self.player.jump = 150

                if self.player.falling and self.player.jump <= 0:

                    self.player.rect.top += 80

                elif self.player.jump > 0:
                    self.player.jump -= 1
                    self.player.rect.top -= 80
        for enemy in self.enemies:
            enemy.__update__()


    def __draw__(self): #metodo que dibuja el personaje

        playerFalling = True

        for platform in self.plat_L1:
            if self.player.rect.colliderect(platform.rect):
                playerFalling = False

        for barril in self.enemies:
            if self.player.rect.colliderect(barril.rect):
                print("died")
        if playerFalling:
            self.player.rect.top += 15

        self.fondo = pygame.image.load("data/bg.jpg")

        self. frame.blit(self.fondo, (0,0))# fondo del juego
        self.player.__update__() # actualiza el jugador
        self.player.__draw__(self.frame)# dibuja el jugador

        if self.level == 1:
            self.level_plat = self.plat_L1
            for platform in self.level_plat: # dibuja todas las plataformas
                platform.__draw__(self.frame)
            time.sleep(0.009) # delay de 0.09s
        elif self.level == 2:
            self.level_plat = self.plat_L2
            for platform in self.level_plat:
                platform.__draw__(self.frame)
        elif self.level == 3:
            self.level_plat = self.plat_L3
            for platform in self.level_plat:
                platform.__draw__(self.frame)
        for enemy in self.enemies:

            enemy.__draw__(self.frame)

# Cierra pygame...
pygame.quit()
