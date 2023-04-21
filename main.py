# !usr/bin/python3

"""
This program is a pong game designed with the help of O.O.P and design patterns
to practice and improve the team's programming skills.

This program is written in a one file
"""

# Start
# Modules
import pygame

pygame.init()

# Creating variables
WIDTH, HEIGHT = 900, 600
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by V.road")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 10

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 120

SCORE_FONT = pygame.font.SysFont("comic sans", 50)

WINING_SCORE = 10


# ------


def draw(win, paddles, ball, left_score, right_score):
    """
    This function draws all game objects
    :param win:
    :param paddles:
    :param ball:
    :param left_score:
    :param right_score:
    """
    win.fill(BLACK)

    left_score_text = SCORE_FONT.render(f"{left_score}", True, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", True, WHITE)
    win.blit(left_score_text, (WIDTH / 4 - left_score_text.get_width() / 2, 20))
    win.blit(right_score_text, (WIDTH * (3 / 4) - right_score_text.get_width() / 2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 10):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH / 2, i, 10, HEIGHT // 20))

    ball.draw(win)

    pygame.display.update()


class Paddle:
    """
    This class performs the task of creating the paddle object
    """
    COLOR = WHITE
    VEL = 5

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, wn):
        pygame.draw.rect(wn, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        """
        This function moves the pedals with the help of the keyboard.
        :param up:
        """
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        """
        resets after game ends
        """
        self.x = self.original_x
        self.y = self.original_y


class Ball:
    """
    This class creates the ball.
    """
    MAX_VEL = 12  # ball speed
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):  # The movement of the ball using its coordinates
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):  # Reset after each game round
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def handle_collision(ball, left_paddle, right_paddle):
    """
    This function is very important, because by using coordinate calculations,
    it determines with what speed and acceleration the ball will return
    when it hits a paddle or the edge of the image, and also when it hits a paddle,
    if it hits the corner with a high speed. It returns, but if it hits the middle of it
    , it returns at a slow speed
    :param ball:
    :param left_paddle:
    :param right_paddle:
    """
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
    """
    This function installs the keyboard hardware to the program
    :param keys:
    :param left_paddle:
    :param right_paddle:
    """
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL - 5 >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height + 5 <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - left_paddle.VEL - 5 >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height + 5 <= HEIGHT:
        right_paddle.move(up=False)


def main():  # MAIN FUNCTION
    run_game = True
    clock = pygame.time.Clock()

    # creating paddle objects
    left_paddle = Paddle(10, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)  # ball object

    left_score = 0
    right_score = 0

    while run_game:  # while loop game
        clock.tick(60)  # max fps is 60

        draw(WN, [left_paddle, right_paddle], ball, left_score, right_score)

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        handle_collision(ball, left_paddle, right_paddle)
        ball.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        won = False
        if left_score >= WINING_SCORE:
            won = True
            win_text = "Left Player Won!"
        elif right_score >= WINING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            text = SCORE_FONT.render(win_text, True, WHITE)
            WN.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()

# End
