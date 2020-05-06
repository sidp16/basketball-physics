import pygame
from colours import BLACK


class Ball:
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def __repr__(self):
        return f"{self.radius} at {self.x}, {self.y}"


    def draw(self,window):
        x,y = int(self.x), int(self.y)
        pygame.draw.circle(window, BLACK, (x,y),self.radius)
        pygame.draw.circle(window, self.colour, (x,y),self.radius-3)
