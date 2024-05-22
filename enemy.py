import pygame
import random
from myMath import gcd
from number import Number
from timer import ErrorFast
from font import bigFont
from data import displayWidth
from color import *

def darken(color):
    return (
        color[0] * 2 // 3,
        color[1] * 2 // 3,
        color[2] * 2 // 3
    )

class Enemy:
    LOW = 4
    FAST = 16
    speed = LOW

    def __init__(self, line, a, b, game):
        self.line = line
        self.x = displayWidth * 10
        self.rect = pygame.rect.Rect(displayWidth,60 + 30 + 120 * self.line, 120, 60)
        self.a = Number(a, bigFont)
        self.b = Number(b, bigFont)
        self.answer = gcd(a, b)
        self.speed = self.__class__.speed
        self._setColor()
        self.repellMagic = game.repellMagic
        self.errorFast = ErrorFast()
    
    def _setColor(self):
        a = random.randint(1, 18)
        if a == 1:
            self.color = bombColor
        elif a == 2:
            self.color = sluggishColor
        elif a == 3:
            self.color = repellColor
        else:
            self.color = enemyColor
        self.darkenColor = darken(self.color)

    def setSpeed(self):
        self.speed = self.__class__.speed
        if self.errorFast.time > 0:
            self.errorFast.tick()
            if self.repellMagic.time < 1:
                self.speed = self.speed * 6 

    def move(self):
        self.setSpeed()
        self.x -= self.speed
        self.rect.x = self.x // 10

    def draw(self, canvas):
        pygame.draw.rect(canvas, self.color, self.rect)
        pygame.draw.rect(canvas, self.darkenColor, self.rect, width=3)
        pygame.draw.line(canvas, self.darkenColor, self.rect.midtop, (self.rect.centerx, self.rect.bottom - 1), 6)
        canvas.blit(self.a.image, (self.rect.x + 30 + self.a.offsetX, self.rect.centery + self.a.offsetY))
        canvas.blit(self.b.image, (self.rect.x + 90 + self.b.offsetX, self.rect.centery + self.b.offsetY))
