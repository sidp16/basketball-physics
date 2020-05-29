import pygame

from colours import BLACK
from vector import Vector


class Wall:
    def __init__(self, startPos, endPos,  colour, width):
        self.startPos = Vector(*startPos)
        self.endPos = Vector(*endPos)
        self.colour = colour
        self.width = width

    def draw(self, window):
        # start, end = int(self.start), int(self.end)

        pygame.draw.line(window, BLACK, (self.startPos.x, self.startPos.y), (self.endPos.x, self.endPos.y), self.width)
        pygame.draw.line(window, self.colour, (self.startPos.x, self.startPos.y), (self.endPos.x, self.endPos.y), self.width-10)

