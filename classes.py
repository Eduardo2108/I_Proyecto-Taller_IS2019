# Libraries
import pygame
import time
# Settings
pygame.init()
transColor = pygame.Color(100, 100, 100)

# Clase que define los parametros del jugador principal (mario)
class Player:
    def __init__(self, x, y): #crea el jugador en una posicion x,y
        self.spriteSheet = pygame.image.load('data/playerSheet.png') #carga el sprite de mario...

        # Sprite que se usa cuando quieto
        self.spriteSheet.set_clip(27, 37, 75, 125)
        self.standing = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.standing.set_colorkey(transColor)

        # los sprites que se usan cuando hay movimiento hacia los lados
        self.spriteSheet.set_clip(25, 205, 75, 125)
        walking1 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking1.set_colorkey(transColor)
        self.spriteSheet.set_clip(155, 201, 75, 125)
        walking2 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking2.set_colorkey(transColor)
        self.spriteSheet.set_clip(285, 198, 75, 125)
        walking3 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking3.set_colorkey(transColor)
        self.spriteSheet.set_clip(416, 205, 75, 125)
        walking4 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking4.set_colorkey(transColor)
        self.walking = [walking1, walking2, walking3, walking4]


        # estados posibles de mario
        self.sprite = self.standing
        self.sprite_index = 0
        self.rect = self.sprite.get_rect() #rectangulo para colisiones
        self.rect.topleft = (x, y)
        self.action = 'standing' #cuando no camina
        self.state = 'right'#cuando si camina
        self.jumpTime = 1.5
        self.tag = 'player' # etiqueta, que lo identifica en el juego

    def __update__(self):
        if self.action == 'standing': #le dice que hacer si esta quieto
            if self.state == 'left':
                self.sprite = self.standing
                self.sprite = pygame.transform.flip(self.standing, True, False)
            elif self.state == 'right':
                self.sprite = self.standing
        elif self.action == 'walking': # le dice que hacer si camina o no
            if self.state == 'left':
                self.rect.left -= 7
                self.sprite = self.__get_sprite__(self.walking)

            elif self.state == 'right':
                self.rect.right += 7
                self.sprite = self.__get_sprite__(self.walking)
                self.sprite = pygame.transform.flip(self.sprite, True, False)

    def __draw__(self, frame): #dibuja a mario en la pantalla segun si camina o no
        pygame.draw.rect(frame, (255, 0, 0), self.rect)
        if self.action == 'standing':
            frame.blit(self.sprite, (self.rect.left, self.rect.top))

        elif self.action == 'walking':
            if self.state == 'left':
                frame.blit(self.sprite, (self.rect.left, self.rect.top + 10))

            elif self.state == 'right':
                frame.blit(self.sprite, (self.rect.left - 16, self.rect.top + 10))

    def __get_sprite__(self, sprites):
        self.sprite_index += 1
        if self.sprite_index >= (len(sprites)):
            self.sprite_index = 0
        return sprites[self.sprite_index]

# clase que crea los parametros de las plataformas
class plataformas:
    def __init__(self, x, y, width, height):
        # identificador de la plataforma, y el alto, ancho y posicion
        self.rect = (x, y, width, height)
        self.tag = 'block'

    def __draw__(self, frame):
        pygame.draw.rect(frame, (0, 255, 0), self.rect) #dibuja el rectangulo, con el color que uno elija

#clase que pone todos los elementos del juego juntos en la pantalla
class Juego():
    def __init__(self, frame): # de entrada tiene la variable que contiene a la pantalla
        self.frame = frame
        self.player = Player(0,500)
        self.platforms = [plataformas(0, 625, 1000, 25), plataformas(100, 550, 200, 25), plataformas(600, 400, 200, 25)]
        #self.plataforms = [0]
    #metodo que tiene por entrada el nivel del juego y crea las plataformas debidas
    #def niveles(self, level):
        #if level ==1:
            #self.plataforms =+
    def respawn(self):
        self.player = Player(0, 500)

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
                pass

    def __draw__(self): #metodo que dibuja el personaje
        playerFalling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                playerFalling = False

        if playerFalling:
            self.player.rect.top += 5

        self.frame.fill((0, 0, 255)) # fondo del juego
        self.player.__update__() # actualiza el jugador
        self.player.__draw__(self.frame) # dibuja el jugador
        for platform in self.platforms: # dibuja todas las plataformas
            platform.__draw__(self.frame)
        time.sleep(0.09) # delay de 0.09s



# Cierra pygame...
pygame.quit()
