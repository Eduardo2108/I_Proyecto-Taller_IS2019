import pygame
class Enemy:
    def __init__(self, x, y, speed):
        # Settings
        self.rect = pygame.Rect(x, y, 64, 64)
        self.speed = speed
        
    def __update__(self):

        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]

        if self.rect.left < -64:
            self.rect.left = 760
        elif self.rect.left > 760:
            self.rect.left = -64
        if self.rect.top < -64:
            self.rect.top = 420
        elif self.rect.top > 420:
            self.rect.top = -64

    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 255, 0), self.rect)
