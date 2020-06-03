import pygame

from colours import BLACK
from vector import Vector


class Wall:
    def __init__(self, startPos, endPos,  colour, width):
        self.startPos = startPos
        self.endPos = endPos
        self.colour = colour
        self.width = width

    def __repr__(self):
        return f"{self.startPos} -> {self.endPos}"

    def draw(self, window):
        pygame.draw.line(window, self.colour, (self.startPos.x, self.startPos.y), (self.endPos.x, self.endPos.y), self.width)