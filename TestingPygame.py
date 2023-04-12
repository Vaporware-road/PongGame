# !usr/bin/python3

"""
Document
"""
# Start
# Modules
import pygame

pygame.init()

HEIGHT, WIDTH = 900, 600
WN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pong by V.road")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 120


def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH - 160, i, 10, HEIGHT // 20))

    pygame.display.update()


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, wn):
        pygame.draw.rect(wn, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


class Ball:
    pass


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL - 5 >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height + 305 <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - left_paddle.VEL - 5 >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height + 305 <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run_game = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 4, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH + WIDTH // 4 + WIDTH // 5 + 5, HEIGHT // 4, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run_game:
        clock.tick(60)

        draw(WN, [left_paddle, right_paddle])

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()

# End
