import pygame

from colours import BLACK
from config import display_height


class Ball:
    def __init__(self, x, y, radius, colour, bounciness):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.bounce = bounciness
        self.velocity = 0
        self.acceleration = 9.8


    def __repr__(self):
        return f"{self.radius} at {self.x}, {self.y}"

    def draw(self, window):
        x, y = int(self.x), int(self.y)
        pygame.draw.circle(window, BLACK, (x, y), self.radius)
        pygame.draw.circle(window, self.colour, (x, y), self.radius - 4)

    def TouchingFloor_Check(self):
        return self.y >= display_height - self.radius

    def update(self, dit):
        print(self.velocity, self.TouchingFloor_Check())
        if self.TouchingFloor_Check():
            if abs(self.velocity) <  2.15:
                self.velocity = 0
            else:
                self.velocity = -self.velocity * self.bounce
                self.y = min(self.y + self.velocity * dit, display_height - self.radius)

        else:
            self.velocity += self.acceleration * dit
            self.y = min(self.y + self.velocity * dit, display_height - self.radius)
