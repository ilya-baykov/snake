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
    SIZE_BOX = 30
    START_POSITION = [(50, 50), (50, 80), (50, 110), (50, 140)]

    def move(self):
        pass

    def growth_by_eating(self):
        pass

    def draw(self):
        pass


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    GameField.draw_field()
