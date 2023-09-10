## snake.py
import pygame
from constants import SNAKE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT

class Snake:
    def __init__(self):
        self.body = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = "RIGHT"

    def move(self):
        head = self.get_head_position()
        if self.direction == "RIGHT":
            self.body.insert(0, (head[0] + SNAKE_SIZE, head[1]))
        elif self.direction == "LEFT":
            self.body.insert(0, (head[0] - SNAKE_SIZE, head[1]))
        elif self.direction == "UP":
            self.body.insert(0, (head[0], head[1] - SNAKE_SIZE))
        elif self.direction == "DOWN":
            self.body.insert(0, (head[0], head[1] + SNAKE_SIZE))
        self.body.pop()

    def grow(self, food_position):
        self.body.append(food_position)

    def check_collision(self):
        head = self.get_head_position()
        return head in self.body[1:] or head[0] < 0 or head[0] >= WINDOW_WIDTH or head[1] < 0 or head[1] >= WINDOW_HEIGHT

    def get_head_position(self):
        return self.body[0]

    def change_direction(self, new_direction):
        self.direction = new_direction

    def draw(self, surface: pygame.Surface):
        for part in self.body:
            pygame.draw.rect(surface, pygame.Color('Green'), pygame.Rect(part[0], part[1], SNAKE_SIZE, SNAKE_SIZE))
