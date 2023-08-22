from constance import *
import random
import time

import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(name_game)


class GameField:
    """Класс для отрисовки игрового поля"""
    SIZE_BLOCK = 50

    @classmethod
    def draw_field(cls):
        color = None
        """Создает игровое поле, в виде шахматной доски """
        for i in range(WIDTH // cls.SIZE_BLOCK):
            for j in range(HEIGHT // cls.SIZE_BLOCK):
                if (i + j) % 2 == 0:
                    color = DARK_GREEN
                else:
                    color = LIGHT_GREEN

                pygame.draw.rect(screen, color,
                                 (i * cls.SIZE_BLOCK, j * cls.SIZE_BLOCK, cls.SIZE_BLOCK, cls.SIZE_BLOCK))
            pygame.display.update()


class Snaky:
    SIZE_BOX = 50
    SNAKY_COORDINATES = [(50, 50), (50, 80), (50, 110), (50, 140)]

    @classmethod
    def move(cls, way_to_turn: str, eat_check: bool):
        head_x, head_y = cls.SNAKY_COORDINATES[0][0], cls.SNAKY_COORDINATES[0][1]
        if way_to_turn == "right":
            cls.SNAKY_COORDINATES.insert(0, (head_x + Snaky.SIZE_BOX, head_y))
        elif way_to_turn == "left":
            cls.SNAKY_COORDINATES.insert(0, (head_x - Snaky.SIZE_BOX, head_y))
        elif way_to_turn == "up":
            cls.SNAKY_COORDINATES.insert(0, (head_x, head_y - Snaky.SIZE_BOX))
        elif way_to_turn == "down":
            cls.SNAKY_COORDINATES.insert(0, (head_x, head_y + Snaky.SIZE_BOX))
        if eat_check:
            pass
        else:
            del cls.SNAKY_COORDINATES[-1]

    def growth_by_eating(self):
        pass

    def draw(self):
        pass


class Fruit:
    COLORS_FRUIT = [RED, BLUE, BLACK]
    fruit_x, fruit_y = 0, 0

    @classmethod
    def fruit_coordinates(cls):
        cls.fruit_x = ((random.randint(Snaky.SIZE_BOX + 50,
                                       WIDTH - 50) // Snaky.SIZE_BOX) * Snaky.SIZE_BOX) - Snaky.SIZE_BOX / 2
        cls.fruit_y = (random.randint(Snaky.SIZE_BOX + 50,
                                      HEIGHT - 50) // Snaky.SIZE_BOX) * Snaky.SIZE_BOX - Snaky.SIZE_BOX / 2
        print(cls.fruit_x)
        print(cls.fruit_y)

    @classmethod
    def fruit_spawn(cls):
        pygame.draw.circle(screen, random.choice(cls.COLORS_FRUIT), (cls.fruit_x, cls.fruit_y), Snaky.SIZE_BOX // 4)
        pygame.display.update()


GameField.draw_field()
on_display = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    if on_display:
        Fruit.fruit_coordinates()
        Fruit.fruit_spawn()
        on_display = not on_display
    Snaky.move("right", False)
