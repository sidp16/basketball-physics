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
        pygame.draw.circle(window, BLACK, (self.x,self.y),self.radius)
        pygame.draw.circle(window, self.colour, (self.x,self.y),self.radius-3)

    def ballPath(startX, startY, ang, time):
        pass