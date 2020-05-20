import pygame

from colours import BLACK
from config import DISPLAY_HEIGHT, DISPLAY_WIDTH


class Ball:
    def __init__(self, x, y, radius, colour, bounciness):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.bounce = bounciness
        self.vY = 0
        self.aY = 9.8
        self.vX = 0
        self.aX = 0
        self.mass = 2

    def __repr__(self):
        return f"{self.radius} at {self.x}, {self.y}"

    def draw(self, window):
        x, y = int(self.x), int(self.y)
        pygame.draw.circle(window, BLACK, (x, y), self.radius)
        pygame.draw.circle(window, self.colour, (x, y), self.radius - 2)

    def isTouchingFloor(self):
        return self.y >= DISPLAY_HEIGHT - self.radius or self.y <= 0 + self.radius

    def isTouchingSide(self):
        return self.x >= DISPLAY_WIDTH - self.radius or self.x <= 0 + self.radius

    def addForce(self, x=0, y=0):
        if x:
            self.aX = x / self.mass

        if y:
            weight = self.mass * 9.8
            resultant_force = y + weight

            self.aY = resultant_force / self.mass

    def update(self, dt):
        self.vY += self.aY * dt
        self.y = min(self.y + self.vY * dt, DISPLAY_HEIGHT - self.radius)
        self.aY = 9.8

        self.vX += self.aX * dt
        self.x += self.vX * dt
        # print(f"Velocity X: {self.vX:.2f}, X coord:, {self.x:.2f}")
        self.aX = 0

        if self.isTouchingFloor():
            if abs(self.vY) < 3.5:
                self.vY = 0
            else:
                self.vY = -self.vY * self.bounce
                self.y = min(self.y + self.vY * dt, DISPLAY_HEIGHT - self.radius)
                self.aY = 9.8

        if self.isTouchingSide():
            self.vX = -self.vX * self.bounce
            self.x = min(self.x + self.vX * dt, DISPLAY_WIDTH - self.radius)
