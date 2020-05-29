
import pygame
from rain_simulation.rain_drop import RainDrop
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def start_game():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rain simulation")

    run = True
    drops = []
    for _ in range(900):
        drops.append(RainDrop(window, SCREEN_HEIGHT, SCREEN_WIDTH))
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
        for drop in drops:
            if drop.posy >= SCREEN_HEIGHT:
                tmp_index = drops.index(drop)
                drops.remove(drop)
                drops.insert(tmp_index, RainDrop(window, SCREEN_HEIGHT, SCREEN_WIDTH))
            drop.move()
        pygame.display.update()
        window.fill((0, 0, 0))


if __name__ == '__main__':
    start_game()
