import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


# pygame setup
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
