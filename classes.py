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
        self.y_plat = 350
        self.W_plat = 600
        self.X_enemies = 200
        self.Y_enemies = 100
        self.H_plat = 5
        self.flag = True
        self.level = 1
        self.enemies = [Enemy(self.X_enemies,self.Y_enemies)]
        self.base = plataformas(0, 625, 1000, 5)
        self.p_Final = plataformas(self.x_plat+150, self.y_plat-210, self.W_plat-50, self.H_plat)
        self.level_plat = []
        #plataformas nivel 1
        self.P1_l1 = plataformas(self.x_plat+600, self.y_plat+150, self.W_plat-400, self.H_plat)
        self.P2_l1 = plataformas(self.x_plat+110, self.y_plat+100, self.W_plat-100, self.H_plat)
        self.P3_l1 = plataformas(self.x_plat+600, self.y_plat+30, self.W_plat-400, self.H_plat)
        self.P_Final_l1 = plataformas(self.x_plat+110, self.y_plat-50, self.W_plat-100, self.H_plat)
        self.plat_L1 = [self.base, self.P1_l1, self.P2_l1,self.P3_l1, self.P_Final_l1]






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

            if event.key == pygame.K_SPACE or event.key == pygame.K_UP and Player.jump > 0: # si es el espacio, o la tecla de arriba, salta

                self.player.jump = 150

                if self.player.falling and self.player.jump <= 0 :

                    self.player.rect.top += 80

                elif self.player.jump > 0:
                    self.player.jump -= 1
                    self.player.rect.top -= 80




    def __draw__(self): #metodo que dibuja el personaje

        playerFalling = True

        for platform in self.level_plat:
            if self.player.rect.colliderect(platform.rect):
                playerFalling = False

        for enemy in self.enemies:
            enemy.__update__()
            enemy.falling = True

            for plat in self.level_plat:

                if enemy.rect.colliderect(plat.rect):
                    enemy.falling = False

                    if self.player.rect.colliderect(enemy.rect):
                        #metodo que mata al jugador
                        pass
                    if enemy.rect.left >= 720 and not enemy.falling :
                        enemy.dir = 'left'
                        print(enemy.x_pos)
                    elif enemy.rect.left <= 245 and not enemy.falling and enemy.rect.top < 600:
                        enemy.dir = 'right'
                        print(enemy.x_pos)
                    elif enemy.rect.top >= 600:
                        enemy.dir = 'left'
                    elif enemy.rect.left <-10:
                        

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
