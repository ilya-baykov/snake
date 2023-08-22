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


class Snaky:
    SIZE_BOX = 50
    SNAKY_COORDINATES = [(50, 50), (50, 100), (50, 150), (50, 200)]

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
        if not eat_check:
            del cls.SNAKY_COORDINATES[-1]

    @classmethod
    def draw(cls):
        for elem in range(len(cls.SNAKY_COORDINATES)):
            pygame.draw.rect(screen, RED, (*cls.SNAKY_COORDINATES[elem], Snaky.SIZE_BOX, Snaky.SIZE_BOX), )


class Fruit:
    color_fruit = ""
    fruit_x, fruit_y = 0, 0

    @classmethod
    def fruit_coordinates(cls):
        cls.fruit_x = ((random.randint(Snaky.SIZE_BOX + 50,
                                       WIDTH - 50) // Snaky.SIZE_BOX) * Snaky.SIZE_BOX) - Snaky.SIZE_BOX / 2
        cls.fruit_y = (random.randint(Snaky.SIZE_BOX + 50,
                                      HEIGHT - 50) // Snaky.SIZE_BOX) * Snaky.SIZE_BOX - Snaky.SIZE_BOX / 2
        cls.color_fruit = random.choice([RED, BLUE, BLACK, WHITE, PURPLE])

    @classmethod
    def fruit_spawn(cls):
        pygame.draw.circle(screen, cls.color_fruit, (cls.fruit_x, cls.fruit_y), Snaky.SIZE_BOX // 4)


class GameLoop:

    def __init__(self):
        GameField.draw_field()
        self.on_display = True
        self.running = True
        self.button = "right"
        self.game_cycle()

    def click_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT or event.key == ord('d')) and self.button != "left":
                    self.button = "right"
                elif (event.key == pygame.K_LEFT or event.key == ord('a')) and self.button != "right":
                    self.button = "left"
                elif (event.key == pygame.K_UP or event.key == ord('w')) and self.button != "down":
                    self.button = "up"
                elif (event.key == pygame.K_DOWN or event.key == ord('s')) and self.button != "up":
                    self.button = "down"

    def game_cycle(self):
        while self.running:
            self.click_handling()
            if self.on_display:
                Fruit.fruit_coordinates()
                self.on_display = False
            Fruit.fruit_spawn()
            Snaky.move(self.button, False)
            Snaky.draw()
            pygame.display.update()
            time.sleep(0.1)
            GameField.draw_field()


start_game = GameLoop()
