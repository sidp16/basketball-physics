import pygame

from colours import BLACK


class Wall:
    def __init__(self, startPos, endPos, colour, width):
        self.startPos = startPos
        self.endPos = endPos
        self.colour = colour
        self.width = width

    def draw(self, window):
        # start, end = int(self.start), int(self.end)
        pygame.draw.line(window, BLACK, self.startPos, self.endPos, self.width)
        pygame.draw.line(window, self.colour, self.startPos, self.endPos, self.width-10)

