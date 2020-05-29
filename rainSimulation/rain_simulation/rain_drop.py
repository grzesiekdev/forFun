import random
import pygame


class RainDrop:
    def __init__(self, window, screen_height, screen_width):
        red = random.randint(0, 70)
        green = random.randint(144, 206)
        blue = random.randint(160, 255)

        self.width = random.randint(2, 4)
        self.height = random.randint(8, 20)
        self.shade = (red, green, blue)
        self.velocity = random.uniform(0.4, 0.9)
        self.screen_height = screen_height
        self.window = window
        self.posx = random.randint(self.width, screen_width)
        self.posy = random.randint(self.height, 21)

    def __draw(self):
        pygame.draw.rect(self.window, self.shade, (self.posx, self.posy, self.width, self.height))

    def move(self):
        self.__draw()
        self.posy += self.velocity

    def __repr__(self):
        return f'Rain drop object, with {self.width}px width, {self.height}px height and {self.shade} shade of blue'
