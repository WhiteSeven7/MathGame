import pygame
from color import * 
from data import displayWidth, displayHeight
from font import bigFont

class PauseMenu:
    def __init__(self):
        self.color = menuColor
        self.rect = pygame.rect.Rect(displayWidth // 2 - 200, displayHeight // 2 - 200, 400, 400)
        self.image = bigFont.render('Press the space to continue', True, 'white')
        self.x = (displayWidth - self.image.get_width()) // 2
        self.y = (displayHeight - self.image.get_height()) // 2
    
    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)
        canvas.blit(self.image, (self.x, self.y))

class DeathMenu:
    def __init__(self):
        self.color = red
        self.rect = pygame.rect.Rect(displayWidth // 2 - 250, displayHeight // 2 - 200, 500, 400)

        self.image1 = bigFont.render('You as lost', True, 'white')
        self.x1 = (displayWidth - self.image1.get_width()) // 2
        self.y1 = (displayHeight - self.image1.get_height()) // 2 - 80

        self.image2 = None
        self.x2 = 0
        self.y2 = 0

        self.image3 = bigFont.render('Press the space to restart', True, 'white')
        self.x3 = (displayWidth - self.image3.get_width()) // 2
        self.y3 = displayHeight // 2 + 80
    
    def setGrade(self, grade):
        self.image2 = bigFont.render(f'Your grade is {grade}', True, enemyColor)
        self.x2 = (displayWidth - self.image2.get_width()) // 2
        self.y2 = (displayHeight - self.image2.get_height()) // 2

    def draw(self, canvas):
        if self.image2 is None:
            return
        pygame.draw.rect(canvas, self.color, self.rect)
        canvas.blit(self.image1, (self.x1, self.y1))
        canvas.blit(self.image2, (self.x2, self.y2))
        canvas.blit(self.image3, (self.x3, self.y3))
