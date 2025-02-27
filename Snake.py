import random
import sys, pygame
from pygame import Vector2

pygame.init()
GREEN = (121, 230, 94)
DARK_GREEN = (28, 74, 16)

cell_size = 30
numer_of_cells = 25


class Food:
    def __init__(self):
        self.position = self.random_position()
    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size,self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)
    @staticmethod
    def random_position():
        x = random.randint(0, numer_of_cells - 1)
        y = random.randint(0, numer_of_cells - 1)
        position = Vector2(x, y)
        return position


class Snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
        self.direction = Vector2(1, 0)
    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 12, 7)
    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
    def draw(self):
        self.snake.draw()
        self.food.draw()
    def update(self):
        self.snake.update()


screen = pygame.display.set_mode((cell_size * numer_of_cells, cell_size * numer_of_cells))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

game = Game()
food_surface = pygame.image.load("Graphics/apple.png")

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 250)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)


    screen.fill(GREEN)
    game.draw()

    pygame.display.update()
    clock.tick(60)