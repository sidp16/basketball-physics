import pygame

from colours import BLACK
from vector import Vector


class Wall:
    def __init__(self, x, y, x2, y2, colour, width):
        self.startPos = Vector(x, y)
        self.endPos = Vector(x2, y2)
        self.colour = colour
        self.width = width

    def draw(self, window):
        # start, end = int(self.start), int(self.end)
        pygame.draw.line(window, BLACK, self.startPos, self.endPos, self.width)
        pygame.draw.line(window, self.colour, self.startPos, self.endPos, self.width-10)

