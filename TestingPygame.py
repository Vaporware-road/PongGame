# !usr/bin/python3

"""
Document
"""
# Start
# Modules
import pygame

pygame.init()

WIDTH, HEIGHT = 900, 600
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by V.road")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 120


def draw(win, paddles, ball):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 10):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH / 2, i, 10, HEIGHT // 20))

    ball.draw(win)

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
    MAX_VEL = 4.5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL - 5 >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height + 5 <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - left_paddle.VEL - 5 >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height + 5 <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run_game = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    while run_game:
        clock.tick(60)

        draw(WN, [left_paddle, right_paddle], ball)

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        handle_collision(ball, left_paddle, right_paddle)
        ball.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break

    pygame.quit()


if __name__ == '__main__':
    main()

# End
