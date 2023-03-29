import pygame
import random

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Змейка")

background_color = (0, 0, 0)
snake_color = (255, 255, 255)

snake_size = 10
snake_speed = 10

snake = [[300, 300]]

direction = "right"

food = [random.randint(0, screen_width - snake_size) // snake_size * snake_size,
        random.randint(0, screen_height - snake_size) // snake_size * snake_size]

food_color = (255, 0, 0)

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

    head = snake[0].copy()
    if direction == "up":
        head[1] -= snake_speed
    if direction == "down":
        head[1] += snake_speed
    if direction == "left":
        head[0] -= snake_speed
    if direction == "right":
        head[0] += snake_speed

    if head[0] < 0 or head[0] >= screen_width or head[1] < 0 or head[1] >= screen_height or head in snake:
        running = False

    snake.insert(0, head)

    if head == food:
        food = [random.randint(0, screen_width - snake_size) // snake_size * snake_size,
                random.randint(0, screen_height - snake_size) // snake_size * snake_size]
    else:
        snake.pop()

    screen.fill(background_color)

    for segment in snake:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], snake_size, snake_size))

    pygame.draw.rect(screen, food_color, (food[0], food[1], snake_size, snake_size))

    pygame.display.flip()

    clock.tick(snake_speed)
