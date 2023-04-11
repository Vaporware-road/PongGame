# !usr/bin/python3

"""
Document
"""
# Start
# Modules
import pygame

pygame.init()

HEIGHT, WIDTH = 700, 500
WN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Pong by V.road")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw(win):
    win.fill(WHITE)
    pygame.display.update()


def main():
    run_game = True
    clock = pygame.time.Clock()

    draw(WN)

    while run_game:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                break
    pygame.quit()


if __name__ == '__main__':
    main()

# End
