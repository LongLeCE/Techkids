import pygame
import random
from time import sleep
from pygame.locals import*
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window_height = 600
window_width = 800
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
    def __init__(self, x, y, food_pos):
        self.g = 0
        self.food_pos = food_pos
        self.x = 60
        self.y = 40
        self.cells = [(x - 20, y), (x - 10, y), (x, y)]
        self.dir_x = 1
        self.dir_y = 0

    def move(self):
        del self.cells[0]
        self.cells.append((self.cells[-1][0]+self.dir_x*10, self.cells[-1][1]+self.dir_y*10))

    def draw(self):
        for i in self.cells:
            pygame.draw.rect(display_surf, WHITE, pygame.Rect(int(i[0]+1), int(i[1]+1), 8, 8))

    def grow(self):
        self.cells.insert(0, self.cells[0])

    def hit_ceiling(self):
        if self.cells[-1][1] <= 0:
            return True
        else:
            return False

    def hit_floor(self):
        if self.cells[-1][1]+10 >= window_height:
            return True
        else:
            return False

    def hit_wall(self):
        if self.cells[-1][0] <= 0 or self.cells[-1][0]+10 >= window_width:
            return True
        else:
            return False


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
    def __init__(self):
        self.q = 0
        snake_x = window_width / 2
        snake_y = window_height / 2
        x = 10 * random.randint(1, 38)
        y = 10 * random.randint(1, 28)
        self.food = Food(x, y)
        self.food.generate()
        self.snake = Snake(snake_x, snake_y, (self.food.x, self.food.y))
        self.score = ScoreBoard()

    @staticmethod
    def collision(x1, y1, x2, y2):
        if x2 < x1 < x2 + 10:
            if y2 < y1 < y2 + 10:
                return True
        else:
            return False

    @staticmethod
    def draw_arena():
        display_surf.fill((255, 255, 255))
        pygame.draw.rect(display_surf, BLACK, (10, 10, window_width - 20, window_height - 20))

    def update(self):
        self.draw_arena()
        self.food.generate()
        self.snake.food_pos = (self.food.x, self.food.y)
        self.snake.move()
        self.snake.draw()
        if self.snake.hit_wall() or self.snake.hit_floor() or self.snake.hit_ceiling():
            pygame.mixer.music.load("D:\\Python\\Lesson 1\\Death.mp3")
            pygame.mixer.music.play(0)
            self.q = 1
        for i in range(len(self.snake.cells) - 1):
            if self.collision(self.snake.cells[-1][0]+5, self.snake.cells[-1][1]+5, self.snake.cells[i][0], self.snake.cells[i][1]):
                pygame.mixer.music.load("D:\\Python\\Lesson 1\\Death.mp3")
                pygame.mixer.music.play(0)
                self.q = 1
                break
        if self.collision(self.snake.cells[-1][0]+5, self.snake.cells[-1][1]+5, self.food.x, self.food.y):
            pygame.mixer.music.load("D:\\Python\\Lesson 1\\Eat.mp3")
            pygame.mixer.music.play(0)
            x = 10 * random.randint(1, 78)
            y = 10 * random.randint(1, 58)
            self.food = Food(x, y)
            self.snake.grow()
            self.food.generate()
            self.score.score += 1
        self.score.display(self.score.score)


def main():
    pygame.init()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 273 and not game.snake.dir_y == 1:
                        game.snake.dir_y = -1
                        game.snake.dir_x = 0
                elif event.key == 274 and not game.snake.dir_y == -1:
                        game.snake.dir_y = 1
                        game.snake.dir_x = 0
                elif event.key == 276 and not game.snake.dir_x == 1:
                        game.snake.dir_y = 0
                        game.snake.dir_x = -1
                elif event.key == 275 and not game.snake.dir_x == -1:
                        game.snake.dir_y = 0
                        game.snake.dir_x = 1
        game.update()
        if game.q == 1:
            sleep(1.3)
            break
        pygame.display.update()
        fps_clock.tick(fps)
    print('Your score:', game.score.score)


if __name__ == '__main__':
    main()
