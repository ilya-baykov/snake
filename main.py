import time

import pygame

pygame.init()
WIGHT = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(30)
print("Конец игры")
