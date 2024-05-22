import pygame
from number import Number
from font import smallFont
from color import *

class Bullet:
    color = bulletColor

    def __init__(self, value, line, speed=44,color=None):
        self.value = value
        self.x10 = 110 * 10
        self.x = 110
        self.y = 60 + 60 + line * 120
        self.radius = 20
        self.number = Number(value, smallFont)
        self.speed = speed
        if color is not None:
            self.color = color
    
    def move(self):
        self.x10 += self.speed
        self.x = self.x10 // 10

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, (self.x, self.y), self.radius)
        canvas.blit(self.number.image, (self.x + self.number.offsetX, self.y + self.number.offsetY))

    def set(self, value):
        self.value = value
        self.speed = -25
        self.color = self.__class__.color
        self.number = Number(value, smallFont)
