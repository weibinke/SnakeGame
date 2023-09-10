## game.py
import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, SNAKE_SPEED, SCORE
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.score = SCORE
        self.game_over = False
        self.paused = False
        self.snake = Snake()
        self.food = Food()

    def start_game(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')

    def end_game(self):
        self.game_over = True

    def pause_game(self):
        self.paused = True

    def resume_game(self):
        self.paused = False

    def increase_difficulty(self):
        global SNAKE_SPEED
        SNAKE_SPEED += 5

    def draw_score(self):
        # Defining the font style and size
        FONT_STYLE =  pygame.font.Font(None, 50)
        score_text = FONT_STYLE.render('Score: {0}'.format(self.score), True, WHITE)
        self.surface.blit(score_text, (WINDOW_WIDTH - 200, 10))

    def run(self):
        self.start_game()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        self.snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        self.snake.change_direction("DOWN")
                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        self.snake.change_direction("LEFT")
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        self.snake.change_direction("RIGHT")
                    elif event.key == pygame.K_p:
                        self.pause_game()
                    elif event.key == pygame.K_r:
                        self.resume_game()

            if not self.paused:
                self.snake.move()
                if self.snake.check_collision():
                    self.end_game()
                elif self.snake.get_head_position() == self.food.position:
                    self.snake.grow(self.food.position)
                    self.food.spawn()
                    self.score += 1
                    self.increase_difficulty()

            self.surface.fill(BLACK)
            self.snake.draw(self.surface)
            self.food.draw(self.surface)
            self.draw_score()
            pygame.display.update()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()
