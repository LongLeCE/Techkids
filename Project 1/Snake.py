import pygame
import random
import sys
import cv2
import numpy as np
from pygame.locals import*
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window_height = 300
window_width = 400
display_surf = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
fps = 20
fps_clock = pygame.time.Clock()


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate(self):
        pygame.draw.rect(display_surf, WHITE, pygame.Rect(self.x, self.y, 10, 10))


class Snake:
    def __init__(self, x, y, s, food_pos):
        self.g = 0
        self.food_pos = food_pos
        self.x = 60
        self.y = 40
        self.cells = [(x - 20, y), (x - 10, y), (x, y)]
        self.dir_x = 1
        self.dir_y = 0
        self.speed = s

    def move(self):
        del self.cells[0]
        self.cells.append((self.cells[-1][0]+self.dir_x*10*self.speed, self.cells[-1][1]+self.dir_y*10*self.speed))

    def draw(self):
        for i in self.cells:
            pygame.draw.rect(display_surf, WHITE, pygame.Rect(int(i[0]+1), int(i[1]+1), 8, 8))

    def grow(self):
        self.cells.insert(0, self.cells[0])

    # def hit_food(self):
    #     if (self.cells[-1][1] == self.food_pos[1] and ((self.dir_x == -1 and self.cells[-1][0] < self.food_pos[0]+10) or (self.dir_x == 1 and self.cells[-1][0] + 10 > self.food_pos[0]))) or (self.cells[-1][0] == self.food_pos[0] and ((self.dir_y == -1 and self.cells[-1][1] < self.food_pos[1]+10) or (self.dir_y == 1 and self.cells[-1][1]+10 > self.food_pos[1]))):
    #         return True
    #     else:
    #         return False

    def hit_ceiling(self):
        if self.dir_y == -1 and self.cells[-1][1] + 10 <= 0:
            return True
        else:
            return False

    def hit_floor(self):
        if self.dir_y == 1 and self.cells[-1][1] >= window_height:
            return True
        else:
            return False

    def hit_wall(self):
        if (self.dir_x == -1 and self.cells[-1][0] + 10 <= 0) or (self.dir_x == 1 and self.cells[-1][0] >= window_width - 0):
            return True
        else:
            return False

    # def hit_self(self):
    #     for i in range(len(self.cells) - 1):
    #         if (self.cells[-1][1] == self.cells[i][1] and ((self.dir_x == -1 and self.cells[i][0]+10-self.cells[-1][0]<1) or (self.dir_x == 1 and self.cells[-1][0]+10-self.cells[i][0]<1))) or (self.cells[-1][0] == self.cells[i][0] and ((self.dir_y == -1 and self.cells[i][1]+10-self.cells[-1][1]<1) or (self.dir_y == 1 and self.cells[-1][1]+10-self.cells[i][1]<1))):
    #             self.g = 1
    #             break
    #     if self.g == 1:
    #         return True
    #     else:
    #         return False


class ScoreBoard:
    def __init__(self, font_size=20, score=0):
        self.x = window_width - 150
        self.y = 20
        self.score = score
        self.font = pygame.font.Font('freesansbold.ttf', font_size)

    def display(self, score):
        result_srf = self.font.render('Score : %s' % score, True, WHITE)
        result_rect = result_srf.get_rect()
        result_rect.topleft = (window_width - 150, 20)
        display_surf.blit(result_srf, result_rect)


class Game:
    def __init__(self, line_thickness=10, speed=1):
        self.line_thickness = line_thickness
        self.speed = speed
        snake_x = window_width / 2
        snake_y = window_height / 2
        x = 10 * random.randint(1, 38)
        y = 10 * random.randint(1, 28)
        self.food = Food(x, y)
        self.food.generate()
        self.snake = Snake(snake_x, snake_y, self.speed, (self.food.x, self.food.y))
        self.score = ScoreBoard()

    def collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + 10:
            if y2 <= y1 < y2 + 10:
                return True
        else:
            return False

    def draw_arena(self):
        display_surf.fill((255, 255, 255))
        pygame.draw.rect(display_surf, BLACK, (10, 10, window_width - 20, window_height - 20))

    def update(self):
        self.draw_arena()
        self.food.generate()
        self.snake.food_pos = (self.food.x, self.food.y)
        self.snake.draw()
        self.snake.move()
        if self.collision(self.food.x, self.food.y, self.snake.cells[-1][0], self.snake.cells[-1][1]):
            x = 10 * random.randint(1, 38)
            y = 10 * random.randint(1, 28)
            self.food = Food(x, y)
            self.snake.grow()
            self.food.generate()


def main():
    q = 0
    pygame.init()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 273 and (not game.snake.dir_y == 1):  # Len
                    game.snake.dir_y = -1
                    game.snake.dir_x = 0
                if event.key == 274 and (not game.snake.dir_y == -1):  # Xuong
                    game.snake.dir_y = 1
                    game.snake.dir_x = 0
                if event.key == 276 and (not game.snake.dir_x == 1):  # Trai
                    game.snake.dir_y = 0
                    game.snake.dir_x = -1
                if event.key == 275 and (not game.snake.dir_x == -1):  # Phai
                    game.snake.dir_y = 0
                    game.snake.dir_x = 1
        game.update()
        if game.snake.hit_wall() or game.snake.hit_floor() or game.snake.hit_ceiling():
            break
        for i in range(len(game.snake.cells) - 1):
            if game.collision(game.snake.cells[i][0]+5, game.snake.cells[i][1]+5, game.snake.cells[-1][0], game.snake.cells[-1][1]):
                q = 1
                break
        if q == 1:
            break
        pygame.display.update()
        fps_clock.tick(fps)
    # print('Your score:', game.score.score)


if __name__ == '__main__':
    main()
