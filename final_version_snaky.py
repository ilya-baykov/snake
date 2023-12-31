from constance import *
import random
import time

import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(name_game)
font = pygame.font.Font(None, 22)


class GameField:
    """Класс для отрисовки игрового поля"""
    SIZE_BLOCK = 50

    @classmethod
    def draw_field(cls):
        """Создает игровое поле, в виде шахматной доски """
        for i in range(WIDTH // cls.SIZE_BLOCK + 1):
            for j in range(HEIGHT // cls.SIZE_BLOCK + 1):
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
    color_fruit = BLUE
    fruit_x, fruit_y = Snaky.SIZE_BOX * 3 + Snaky.SIZE_BOX // 2, Snaky.SIZE_BOX * 3 + Snaky.SIZE_BOX // 2

    @classmethod
    def fruit_coordinates(cls):
        rand_x = (random.randint(Snaky.SIZE_BOX, WIDTH - Snaky.SIZE_BOX))
        rand_y = (random.randint(Snaky.SIZE_BOX, HEIGHT - Snaky.SIZE_BOX))
        cls.fruit_x = (rand_x - rand_x % Snaky.SIZE_BOX) + Snaky.SIZE_BOX // 2
        cls.fruit_y = (rand_y - rand_y % Snaky.SIZE_BOX) + Snaky.SIZE_BOX // 2
        cls.color_fruit = random.choice([RED, BLUE, BLACK, WHITE, PURPLE])

    @classmethod
    def fruit_spawn(cls):
        pygame.draw.circle(screen, cls.color_fruit, (cls.fruit_x, cls.fruit_y), Snaky.SIZE_BOX // 4)


class GameChanger:
    lvl = 1
    speed = 0.1

    @classmethod
    def lvl_up(cls):
        cls.lvl += 1
        df = 5
        if cls.lvl % 20 == 0:
            for coord in range(len(Snaky.SNAKY_COORDINATES)):
                Snaky.SNAKY_COORDINATES[coord] = (
                    Snaky.SNAKY_COORDINATES[coord][0] // Snaky.SIZE_BOX * (Snaky.SIZE_BOX - df),
                    Snaky.SNAKY_COORDINATES[coord][1] // Snaky.SIZE_BOX * (Snaky.SIZE_BOX - df))
            Snaky.SIZE_BOX = Snaky.SIZE_BOX - df
            GameField.SIZE_BLOCK = GameField.SIZE_BLOCK - df
        elif cls.lvl % 5 == 0:
            cls.speed = round(cls.speed * 0.95, 3)


class GameLoop:

    def __init__(self):
        self.score = 0
        self.running = True
        self.button = "right"
        GameField.draw_field()
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

    @staticmethod
    def fruit_eating_check():
        return pygame.Rect(*Snaky.SNAKY_COORDINATES[0], Snaky.SIZE_BOX, Snaky.SIZE_BOX).colliderect(
            pygame.Rect(Fruit.fruit_x, Fruit.fruit_y, Snaky.SIZE_BOX // 2, Snaky.SIZE_BOX // 2))

    @staticmethod
    def game_over():
        if not (WIDTH > Snaky.SNAKY_COORDINATES[0][0] > -Snaky.SIZE_BOX):  # Выход за границы по горизонтали
            return True
        if not (HEIGHT > Snaky.SNAKY_COORDINATES[0][1] > -Snaky.SIZE_BOX):  # Выход за границы по вертекали
            return True
        head = pygame.Rect(Snaky.SNAKY_COORDINATES[0][0], Snaky.SNAKY_COORDINATES[0][1], Snaky.SIZE_BOX, Snaky.SIZE_BOX)
        for elem in range(1, len(Snaky.SNAKY_COORDINATES)):
            if head.colliderect(
                    pygame.Rect(Snaky.SNAKY_COORDINATES[elem][0], Snaky.SNAKY_COORDINATES[elem][1], Snaky.SIZE_BOX,
                                Snaky.SIZE_BOX)):
                return True
        return False

    def game_cycle(self):
        while self.running:
            self.click_handling()
            score_text = font.render("SCORE:" + str(self.score), True, RED)
            lvl_text = font.render("lvl:" + str(GameChanger.lvl), True, RED)
            if self.fruit_eating_check():
                self.score += GameChanger.lvl * 50
                GameChanger.lvl_up()
                Fruit.fruit_coordinates()
                Snaky.move(self.button, True)
            Fruit.fruit_spawn()
            Snaky.move(self.button, False)
            if self.game_over():
                raise "Ты проиграл"
            Snaky.draw()
            pygame.display.update()
            time.sleep(GameChanger.speed)
            GameField.draw_field()
            screen.blit(score_text, (10, 20))
            screen.blit(lvl_text, (10, 30))


start_game = GameLoop()
