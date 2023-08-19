import time

import pygame

pygame.init()
size_block = 80
WIGHT = size_block * 10
HEIGHT = size_block * 10
screen = pygame.display.set_mode((WIGHT, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
DARK_GREEN = (167, 252, 0)
LIGHT_GREEN = (24, 255, 74)

for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            pygame.draw.rect(screen, DARK_GREEN, (i * size_block, j * size_block, size_block, size_block))
        else:
            pygame.draw.rect(screen, LIGHT_GREEN, (i * size_block, j * size_block, size_block, size_block))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(30)
print("Конец игры")
