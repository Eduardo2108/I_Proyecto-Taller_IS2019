import pygame

class Enemy:
    def __init__(self, x, y, speed):
        # Settings
        self.rect = pygame.Rect(x, y, 64, 64)
        self.speed = speed
        self.falling = True
        self.dir = 'r'

    def __update__(self):

        if self.falling == True:
            self.rect.top += 10
        if self.dir == 'r':
            self.rect.left += 10
        elif self.dir =='l':
            self.rect.left -= 10


    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 255, 0), self.rect)
