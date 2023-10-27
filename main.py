import pygame

pygame.inet()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            run=False

pygame.quit()