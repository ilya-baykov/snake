import random
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

fruit_x = random.randint(0, WIDTH - 20)
fruit_y = random.randint(0, HEIGHT - 20)


def draw_field():
    for i in range(20):
        for j in range(15):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, DARK_GREEN, (i * size_block, j * size_block, size_block, size_block))
            else:
                pygame.draw.rect(screen, LIGHT_GREEN, (i * size_block, j * size_block, size_block, size_block))


x = int(WIDTH / 2) + size_block / 2
y = int(HEIGHT / 2)
speed = 5
radius = 15
running = True
while running and x < WIDTH - 20 and y < HEIGHT - 20 and x > 20 and y > 20:
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
    pygame.display.update()
    draw_field()
    pygame.draw.circle(screen, (0, 0, 255), (fruit_x, fruit_y), 15)
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    if abs(fruit_x - x - radius) < 38 and abs(fruit_y - y - radius) < 38:
        print("Фрукт съеден")
        radius += 10
        fruit_x = random.randint(0, WIDTH - 20)
        fruit_y = random.randint(0, HEIGHT - 20)
        speed += 1
    clock.tick(30)
print("Конец игры")
