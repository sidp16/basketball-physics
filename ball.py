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
        self.mass = 2
        self.weight = 0

    def __repr__(self):
        return f"{self.radius} at {self.x}, {self.y}"

    def draw(self, window):
        x, y = int(self.x), int(self.y)
        pygame.draw.circle(window, BLACK, (x, y), self.radius)
        pygame.draw.circle(window, self.colour, (x, y), self.radius - 4)

    def isTouchingFloor(self):
        return self.y >= display_height - self.radius

    def update(self, dt):
        # print(self.velocity, self.isTouchingFloor())
        if self.isTouchingFloor():
            if abs(self.velocity) < 3.3:
                self.velocity = 0
            else:
                self.acceleration = 9.8
                self.velocity = -self.velocity * self.bounce
                self.y = min(self.y + self.velocity * dt, display_height - self.radius)

        else:
            self.velocity += self.acceleration * dt
            self.y = min(self.y + self.velocity * dt, display_height - self.radius)
        self.acceleration = 9.8

    def addForce(self, externalForce):
        # f = ma
        # w = mg
        # Fr = Ef + g
        # Fr / m = a

        self.weight = self.mass * 9.8
        resultant_force = externalForce + self.weight
        self.acceleration = resultant_force / self.mass

