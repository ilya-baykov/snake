import random
import time

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
snaky_coordinate = [[50, 50], [50, 70], [50, 90], [50, 110]]

fruit_x = random.randint(0, 800)
fruit_y = random.randint(0, 600)


def move(_lst, where):
    lst = []
    if where == "right":
        lst = [[_lst[0][0] + 20, _lst[0][1]]]
    elif where == "left":
        lst = [[_lst[0][0] - 20, _lst[0][1]]]
    elif where == "up":
        lst = [[_lst[0][0], _lst[0][1] - 20]]
    elif where == "down":
        lst = [[_lst[0][0], _lst[0][1] + 20]]

    for elem in range(1, len(_lst)):
        lst.append(_lst[elem - 1])
    return lst


def draw_snaky(coordinates: list):
    screen.fill((0, 0, 0))
    for i in range(len(coordinates)):
        pygame.draw.rect(screen, (255, 0, 0), (*coordinates[i], 20, 20), 3)
        time.sleep(0.03)
    pygame.draw.circle(screen, (0, 0, 255), (fruit_x, fruit_y), 10, 2)
    pygame.display.update()


draw_snaky(snaky_coordinate)

running = True
button = "right"
on_display = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and button != "left":
                button = "right"
            elif event.key == pygame.K_LEFT and button != "right":
                button = "left"
            elif event.key == pygame.K_UP and button != "down":
                button = "up"
            elif event.key == pygame.K_DOWN and button != "up":
                button = "down"
    if abs(snaky_coordinate[0][0] - fruit_x) < 20 and abs(snaky_coordinate[0][1] - fruit_y) < 20:
        fruit_x = random.randint(0, 800)
        fruit_y = random.randint(0, 600)
    snaky_coordinate = move(snaky_coordinate, button)
    draw_snaky(snaky_coordinate)
