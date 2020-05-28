import pygame
from math import sqrt, degrees, acos, sin, cos

from vector import Vector
from colours import BLACK, RED, ORANGE, GREEN
from config import DISPLAY_HEIGHT, DISPLAY_WIDTH
from gameObjects import walls


class Ball:
    def __init__(self, x, y, radius, colour, bounciness):
        self.position = Vector(x, y)
        self.acceleration = Vector(0, 9.8)
        self.velocity = Vector(0,0)
        self.mass = 5
        self.radius = radius
        self.colour = colour
        self.bounce = bounciness

    def __repr__(self):
        return f"{self.radius} at {self.position}, {self.position.x}"

    def draw(self, window):
        x, y = int(self.position.x), int(self.position.y)
        pygame.draw.circle(window, BLACK, (x, y), self.radius)
        pygame.draw.circle(window, self.colour, (x, y), self.radius - 1)

    def isTouchingFloor(self):
        return self.position.y >= DISPLAY_HEIGHT - self.radius or self.position.y <= 0 + self.radius

    def isTouchingSide(self):
        return self.position.x >= DISPLAY_WIDTH - self.radius or self.position.x <= 0 + self.radius

    def isTouchingWall(self, wall):
        length = sqrt((wall.startPos.x - wall.endPos.x)**2 + (wall.startPos.y - wall.endPos.y)**2)
        distT = sqrt((self.position.x - wall.startPos.x)**2 + (self.position.y - wall.startPos.y)**2)
        distB = sqrt((self.position.x - wall.endPos.x)**2 + (self.position.y - wall.endPos.y)**2)

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
            if distP <= self.radius:
                self.resetPosition(wall, distB, distP)
                return True
        else:
            self.colour = RED
            return False

    def addForce(self, x=0, y=0):
        if x:
            self.acceleration.x = x / self.mass

        if y:
            weight = self.mass * 9.8
            resultant_force = y + weight

            self.acceleration.y = resultant_force / self.mass

    def resetPosition(self, wall, distB, distP):
        # a^2 = b^2 + c^2 - 2bc * cos(A) > cosine rule (side)
        angP = acos(distP / distB)
        distX = (distB ** 2) + (distP ** 2) - (2 * distB * distP) * cos(angP)
        direction = Vector(wall.startPos.x - wall.endPos.x, wall.startPos.y - wall.endPos.y)
        length = direction.magnitude()
        unitLength1 = direction / length

        print(f"angP: {degrees(angP):4.2f}, distP: {distP:4.2f}, distB: {distB:4.2f}, distX: {distX}")
        # print(f"direction: {direction}, length: {length}, unitLength1: {unitLength1})
        # impactPoint = wall.endPos + (distX * unitLength1)

    def update(self, dt):
        # print(f"x: {self.position.x}, y: {self.position.y}")
        # print(f"velX: {self.velocity.x}, velY: {self.position.y}")

        self.velocity += self.acceleration * dt

        self.position += self.velocity * dt
        self.position.y = min(self.position.y, DISPLAY_HEIGHT - self.radius) # ball doesn't go through floor

        self.acceleration = Vector(0, 9.8)

        # print(f"speed: {self.velocity.mag():4.2f}")
        # print(f"Velocity X: {self.velocity.x:.2f}, X coord:, {self.position.x:.2f}")

        if self.isTouchingFloor():
            if abs(self.velocity.y) < 3.5:
                self.velocity.y = 0
            else:
                self.velocity.y = -self.velocity.y * self.bounce
                self.position.y = min(self.position.y + self.velocity.y * dt, DISPLAY_HEIGHT - self.radius)
                self.acceleration = Vector(0, 9.8)

        if self.isTouchingSide():
            self.velocity.x = -self.velocity.x * self.bounce
            self.position.x = min(self.position.x + self.velocity.x * dt, DISPLAY_WIDTH - self.radius)

        for w in walls:
            if self.isTouchingWall(w):
                self.colour = GREEN
                # self.velocity.x = -self.velocity.x * self.bounce
                # self.velocity.y = -self.velocity.y * self.bounce
                break