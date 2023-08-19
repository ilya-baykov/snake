import time

import pygame

pygame.init()
size_block = 50
WIDTH = size_block * 20
HEIGHT = size_block * 15
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
DARK_GREEN = (68, 148, 74)
LIGHT_GREEN = (24, 255, 74)


def draw_field():
    for i in range(20):
        for j in range(15):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, DARK_GREEN, (i * size_block, j * size_block, size_block, size_block))
            else:
                pygame.draw.rect(screen, LIGHT_GREEN, (i * size_block, j * size_block, size_block, size_block))
    pygame.display.update()


x = int(WIDTH / 2) + size_block / 2
y = int(HEIGHT / 2)
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    draw_field()
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.update()
    clock.tick(30)
print("Конец игры")
