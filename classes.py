# Libraries
import pygame
import time
# Settings
pygame.init()
transColor = pygame.Color(100, 100, 100)

# Player Class
class Player:
    def __init__(self, x, y):
        self.spriteSheet = pygame.image.load('data/playerSheet.png')

        # Standing sprite
        self.spriteSheet.set_clip(27, 37, 75, 125)
        self.standing = self.spriteSheet.subsurface(self.spriteSheet.get_clip()).convert()
        self.standing.set_colorkey(transColor)

        # Walking sprites
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

        # Climbing sprites

        # Settings
        self.sprite = self.standing
        self.sprite_index = 0
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (x, y)
        self.action = 'standing'
        self.state = 'right'
        self.jumpTime = 1.5
        self.tag = 'player'

    def __update__(self):
        if self.action == 'standing':
            if self.state == 'left':
                self.sprite = self.standing
                self.sprite = pygame.transform.flip(self.standing, True, False)
            elif self.state == 'right':
                self.sprite = self.standing
        elif self.action == 'walking':
            if self.state == 'left':
                self.rect.left -= 7
                self.sprite = self.__get_sprite__(self.walking)
                self.sprite = pygame.transform.flip(self.sprite, True, False)
            elif self.state == 'right':
                self.rect.right += 7
                self.sprite = self.__get_sprite__(self.walking)

    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 0, 0), self.rect)
        if self.action == 'standing':
            #frame.blit(self.sprite, (self.rect.left, self.rect.top))
            pass
        elif self.action == 'walking':
            if self.state == 'left':
                #frame.blit(self.sprite, (self.rect.left, self.rect.top + 10))
                pass
            elif self.state == 'right':
                #frame.blit(self.sprite, (self.rect.left - 16, self.rect.top + 10))
                pass
    def __get_sprite__(self, sprites):
        self.sprite_index += 1
        if self.sprite_index >= (len(sprites)):
            self.sprite_index = 0
        return sprites[self.sprite_index]
# Block Class
class Block:
    def __init__(self, x, y, width, height):
        # Settings
        self.rect = (x, y, width, height)
        self.tag = 'block'

    def __draw__(self, frame):
        pygame.draw.rect(frame, (0, 255, 0), self.rect)

# Game Screen
class GameScreen():
    def __init__(self, frame):
        self.frame = frame
        self.player = Player(475, 100)
        self.platforms = [Block(0, 625, 1000, 25), Block(100, 550, 200, 25), Block(600, 400, 200, 25)]

    def respawn(self):
        self.player = Player(475, 100)

    def __update__(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'standing'
                self.player.state = 'left'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'standing'
                self.player.state = 'right'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.player.action = 'walking'
                self.player.state = 'left'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.player.action = 'walking'
                self.player.state = 'right'
            self.player.sprite_index = -1

            if event.key == pygame.K_SPACE:
                self.respawn()

    def __draw__(self):
        playerFalling = True
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect):
                playerFalling = False
        if playerFalling:
            self.player.rect.top += 7

        self.frame.fill((0, 0, 255))
        self.player.__update__()
        self.player.__draw__(self.frame)
        for platform in self.platforms:
            platform.__draw__(self.frame)
        time.sleep(0.09)

# Closing pygame
pygame.quit()
