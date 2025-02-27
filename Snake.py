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
    def random_position(self):
        x = random.randint(0, numer_of_cells - 1)
        y = random.randint(0, numer_of_cells - 1)
        position = Vector2(x, y)
        return position


screen = pygame.display.set_mode((cell_size * numer_of_cells, cell_size * numer_of_cells))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

food = Food()
food_surface = pygame.image.load("Graphics/apple.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    clock.tick(90)
    screen.fill(GREEN)
    food.draw()