import pygame
from number import VariateNumber
from font import bigFont

class Player:
    def __init__(self, line):
        self.line = line
        self.rect = pygame.rect.Rect(20, 60 + 20 + 120 * line, 80, 80)
        self.number = VariateNumber(bigFont)

    def moveUp(self):
        self.line -= 1
        self.rect.y -= 120

    def moveDown(self):
        self.line += 1
        self.rect.y += 120

    def draw(self, canvas):
        pygame.draw.rect(canvas, (224, 178, 55), self.rect)
        canvas.blit(self.number.image, (self.rect.centerx + self.number.offsetX, self.rect.centery + self.number.offsetY))