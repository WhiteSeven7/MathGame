import pygame
from font import smallFont
from data import displayWidth
from color import *

class Info:
    def __init__(self):
        self.lives = 3
        self.lifeRects = [
            pygame.rect.Rect(20, 13, 30, 30),
            pygame.rect.Rect(70, 13, 30, 30),
            pygame.rect.Rect(120, 13, 30, 30)
            ]
        self.font = smallFont
        self.grade = 0
        self.repell = 2
        self.sluggish = 2
        self.bomb = 2
    
    def addByColor(self, color):
        if color == repellColor:
            self.repell += 1
        elif color == sluggishColor:
            self.sluggish += 1
        elif color == bombColor:
            self.bomb += 1

    def draw(self, canvas):
        pygame.draw.line(canvas, menuColor, (0 , 57), (displayWidth, 57), 6)
        for i in range(self.lives):
            pygame.draw.rect(canvas, playerColor, self.lifeRects[i])

        image = self.font.render(str(self.grade), True, 'white')
        canvas.blit(image, (250 - image.get_width() // 2, 30 - image.get_height() // 2))

        image = self.font.render(str(self.repell), True, repellColor)
        canvas.blit(image, (350 - image.get_width() // 2, 30 - image.get_height() // 2))

        image = self.font.render(str(self.sluggish), True, sluggishColor)
        canvas.blit(image, (450 - image.get_width() // 2, 30 - image.get_height() // 2))

        image = self.font.render(str(self.bomb), True, bombColor)
        canvas.blit(image, (550 - image.get_width() // 2, 30 - image.get_height() // 2))
