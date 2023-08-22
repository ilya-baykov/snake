import random
import time

import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
SIZE_BOX = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
snaky_coordinate = [[50, 50], [50, 80], [50, 110], [50, 140]]

fruit_x = random.randint(0, 730)
fruit_y = random.randint(0, 530)


def move(_lst, where, more_sigment):
    lst = []
    if where == "right":
        lst = [[_lst[0][0] + SIZE_BOX, _lst[0][1]]]
    elif where == "left":
        lst = [[_lst[0][0] - SIZE_BOX, _lst[0][1]]]
    elif where == "up":
        lst = [[_lst[0][0], _lst[0][1] - SIZE_BOX]]
    elif where == "down":
        lst = [[_lst[0][0], _lst[0][1] + SIZE_BOX]]

    for elem in range(1, len(_lst)):
        lst.append(_lst[elem - 1])
    if more_sigment:
        lst.append(_lst[len(_lst) - 1])
    return lst


def draw_snaky(coordinates: list):
    screen.fill((0, 0, 0))
    for i in range(len(coordinates)):
        pygame.draw.rect(screen, (255, 0, 0), (*coordinates[i], SIZE_BOX, SIZE_BOX), 3)
    pygame.draw.circle(screen, (0, 0, 255), (fruit_x, fruit_y), 10, 2)
    pygame.display.update()


draw_snaky(snaky_coordinate)

running = True
button = "right"
on_display = False
game_difficulty = 0.1
counter = 0


def game_over():
    if snaky_coordinate[0][0] > 800 or snaky_coordinate[0][0] < 0 or snaky_coordinate[0][1] > 600 or \
            snaky_coordinate[0][1] < 10:
        return True
    head = pygame.Rect(snaky_coordinate[0][0], snaky_coordinate[0][1], SIZE_BOX, SIZE_BOX)
    for coord in range(1, len(snaky_coordinate)):
        if pygame.Rect(head).colliderect(*snaky_coordinate[coord], SIZE_BOX, SIZE_BOX):
            return True
    return False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == ord('d')) and button != "left":
                button = "right"
                continue
            elif (event.key == pygame.K_LEFT or event.key == ord('a')) and button != "right":
                button = "left"
                continue
            elif (event.key == pygame.K_UP or event.key == ord('w')) and button != "down":
                button = "up"
                continue
            elif (event.key == pygame.K_DOWN or event.key == ord('s')) and button != "up":
                button = "down"
                continue

    if pygame.Rect(*snaky_coordinate[0], SIZE_BOX, SIZE_BOX).colliderect(
            pygame.Rect(fruit_x - 10, fruit_y - 10, SIZE_BOX, SIZE_BOX)):
        fruit_x = random.randint(50, 750)
        fruit_y = random.randint(50, 550)
        snaky_coordinate = move(snaky_coordinate, button, True)
        counter += 1
        game_difficulty = game_difficulty * 0.95
    else:
        snaky_coordinate = move(snaky_coordinate, button, False)
    draw_snaky(snaky_coordinate)
    if game_over():
        print("КОНЕЦ ИГРЫ!")
        print("Ваш счет - ", counter)
        running = False
        break
    time.sleep(game_difficulty)
