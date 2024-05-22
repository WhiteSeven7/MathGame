import pygame.font

if not pygame.font.get_init():
    pygame.font.init()
bigFont = pygame.font.Font(None, 40)
smallFont = pygame.font.Font(None, 30)