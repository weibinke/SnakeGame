import pygame
import random
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FOOD_SIZE

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        x = random.randint(0, WINDOW_WIDTH - FOOD_SIZE)
        y = random.randint(0, WINDOW_HEIGHT - FOOD_SIZE)
        self.position = (x//FOOD_SIZE * FOOD_SIZE, y//FOOD_SIZE * FOOD_SIZE)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, pygame.Color('Red'), pygame.Rect(self.position[0], self.position[1], FOOD_SIZE, FOOD_SIZE))

