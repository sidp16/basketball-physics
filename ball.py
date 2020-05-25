import pygame
from math import sqrt, degrees, acos, sin, cos

from colours import BLACK, RED, ORANGE, GREEN
from config import DISPLAY_HEIGHT, DISPLAY_WIDTH
from gameObjects import walls


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
        self.mass = 5

    def __repr__(self):
        return f"{self.radius} at {self.x}, {self.y}"

    def draw(self, window):
        x, y = int(self.x), int(self.y)
        pygame.draw.circle(window, BLACK, (x, y), self.radius)
        pygame.draw.circle(window, self.colour, (x, y), self.radius - 1)

    def isTouchingFloor(self):
        return self.y >= DISPLAY_HEIGHT - self.radius or self.y <= 0 + self.radius

    def isTouchingSide(self):
        return self.x >= DISPLAY_WIDTH - self.radius or self.x <= 0 + self.radius

    def isTouchingWall(self, wall):
        global distP, distB
        length = sqrt((wall.startPos[0] - wall.endPos[0])**2 + (wall.startPos[1] - wall.endPos[1])**2)
        distT = sqrt((self.x - wall.startPos[0])**2 + (self.y - wall.startPos[1])**2)
        distB = sqrt((self.x - wall.endPos[0])**2 + (self.y - wall.endPos[1])**2)

        # ( b^2 + c^2 - a^2 ) / (2 * b * c) > cosine rule (angle)
        top = ((distT**2) + (length**2) - (distB**2)) / (2*distT*length)
        bottom = ((distB**2) + (length**2) - (distT**2)) / (2*distB*length)

        angT = acos(top)
        angB = acos(bottom)

        # print(f"top: {top:4.2f}, bottom: {bottom:4.2f}, t: {degrees(angT):4.2f}, b: {degrees(angB): 4.2f}")

        if degrees(angT) <= 90 and degrees(angB) <= 90:
            distP = distT * sin(angT)
            # print(f"distP: {distP:4.2f}, t: {degrees(angT):4.2f}, b: {degrees(angB): 4.2f}")
            self.colour = ORANGE
            return distP <= self.radius
        else:
            self.colour = RED
            return False

    def addForce(self, x=0, y=0):
        if x:
            self.aX = x / self.mass

        if y:
            weight = self.mass * 9.8
            resultant_force = y + weight

            self.aY = resultant_force / self.mass

    def resetPosition(self):
        # c^2 = a^2 + b^2 - 2ab * cos(C) > cosine rule (side)
        angP = acos(distP / distB)
        distX = (distB ** 2) + (distP ** 2) - (2 * distB * distP) * cos(angP)

        return distX
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

        for w in walls:
            if self.isTouchingWall(w):
                distX = self.resetPosition()
                print(f"distX: {distX:4.2f}")
                self.colour = GREEN
                self.vX = -self.vX * self.bounce
                self.vY = -self.vY * self.bounce
                break
