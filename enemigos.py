import pygame

class Enemy:
    def __init__(self, x, y):
        # Settings
        self.rect = pygame.Rect(x, y, 25, 25)

        self.falling = True
        self.dir = 'right'
        self.vel = 15
        self.x_pos = x
        self.stat = 0
        self.image = pygame.image.load('data/barrel.png')
        self.sprite = self.image
        self.rect = pygame.Rect(x, y, 25, 25)

    def __update__(self):
        #print(self.rect.left, self.rect.top)
        if self.falling:
            self.rect.top += self.vel

        if not self.falling:
            if self.dir == 'right':
                self.rect.left += self.vel

            else:
                self.rect.left -= self.vel
        if self.x_pos >= 600:
            self.dir ='left'
        elif self.x_pos <= 0:
            self.dir = 'right'

    def __draw__(self, frame):
        pygame.draw.rect(frame, (255, 255, 0), self.rect)
        frame.blit(self.image,(self.rect.left, self.rect.top))
