from classes import *
transColor = pygame.Color(255,0,0)
class Player:
    def __init__(self, x, y): #crea el jugador en una posicion x,y
        self.spriteSheet = pygame.image.load('data/playerSheet.png') #carga el sprite de mario...

        # Sprite que se usa cuando quieto
        self.spriteSheet.set_clip(0, 0, 34, 49)
        self.standing = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.standing.set_colorkey(transColor)

        # los sprites que se usan cuando hay movimiento hacia los lados
        self.spriteSheet.set_clip(110, 3, 35, 45)
        walking1 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking1.set_colorkey(transColor)
        self.spriteSheet.set_clip(143, 6, 46, 43)
        walking2 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking2.set_colorkey(transColor)
        self.spriteSheet.set_clip(190, 1, 39, 48)
        walking3 = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        walking3.set_colorkey(transColor)
        self.spriteSheet.set_clip(228, 2, 47, 49)
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
        self.falling = True
        self.jump = 0

    def __update__(self):
        if self.action == 'standing': #le dice que hacer si esta quieto
            if self.state == 'left':
                self.sprite = self.standing
                self.sprite = self.standing
            elif self.state == 'right':
                self.sprite = self.standing
                self.sprite = pygame.transform.flip(self.sprite, True, False)
        elif self.action == 'walking': # le dice que hacer si camina o no
            if self.state == 'left':
                self.rect.left -= 10
                self.sprite = self.__get_sprite__(self.walking)
                self.sprite = pygame.transform.flip(self.sprite, True, False)
            elif self.state == 'right':
                self.rect.right += 10
                self.sprite = self.__get_sprite__(self.walking)


    def __draw__(self, frame): #dibuja a mario en la pantalla segun si camina o no
       #pygame.draw.rect(frame, (255, 0, 0), self.rect)
        if self.action == 'standing':
            frame.blit(self.sprite, (self.rect.left, self.rect.top))

        elif self.action == 'walking':
            if self.state == 'left':
                frame.blit(self.sprite, (self.rect.left, self.rect.top))

            elif self.state == 'right':
                frame.blit(self.sprite, (self.rect.left, self.rect.top))

    def __get_sprite__(self, sprites):
        self.sprite_index += 1
        if self.sprite_index >= (len(sprites)):
            self.sprite_index = 0
        return sprites[self.sprite_index]
