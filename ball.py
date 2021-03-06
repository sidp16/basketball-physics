import pygame
from math import sqrt, degrees, acos, sin, cos, radians

from vector import Vector
from colours import BLACK, RED, ORANGE, GREEN, BLUE
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


    def doWallCollision(self, wall):
        length = wall.startPos.distTo(wall.endPos)
        distT = wall.startPos.distTo(self.position)
        distB = wall.endPos.distTo(self.position)
        # ( b^2 + c^2 - a^2 ) / (2 * b * c) > cosine rule (angle)
        top = ((distT**2) + (length**2) - (distB**2)) / (2*distT*length)
        bottom = ((distB**2) + (length**2) - (distT**2)) / (2*distB*length)
        try:
            angT = acos(top)
            angB = acos(bottom)
        except:
            return False

        if degrees(angT) <= 90 and degrees(angB) <= 90:
            distP = distT * sin(angT)
            if distP - 0.5*wall.width <= self.radius:
                self._resetPosition(wall, distB, distP)
                self._changeVelocity(wall)
                return True

        elif self.position.distTo(wall.startPos) <= self.radius:
            unitDirectionBall =  (self.position - wall.startPos).unit()
            self.position = wall.startPos + (unitDirectionBall * self.radius)
            self.velocity = - self.velocity
            return True

        elif self.position.distTo(wall.endPos) <= self.radius:
            unitDirectionBall =  (self.position - wall.endPos).unit()
            self.position = wall.endPos + (unitDirectionBall * self.radius)
            self.velocity = - self.velocity
            return True

        else:
            self.colour = RED
            return False

    def _changeVelocity(self, wall):
        directionWall = wall.endPos - wall.startPos
        if (directionWall.y < 0 and self.velocity.x < 0) or \
                (directionWall.y > 0 and self.velocity.x > 0) or \
                (directionWall.x > 0 and self.velocity.y < 0) or \
                (directionWall.x < 0 and self.velocity.y > 0):
            directionWall = -directionWall
        angleWithWall = self.velocity.angleWith(directionWall)
        self.velocity = -self.velocity.rotate(radians(180) - 2 * angleWithWall) * self.bounce

    def _resetPosition(self, wall, distB, distP):
        distX = sqrt((distB ** 2) - (distP ** 2)) # pythagoras
        directionWall = wall.startPos - wall.endPos
        unitDirectionWall = directionWall.unit()
        unitDirectionPerp = Vector(-unitDirectionWall.y, unitDirectionWall.x)

        # print(f"angP: {degrees(angP):4.2f}, distP: {distP:4.2f}, distB: {distB:4.2f}, distX: {distX}")
        impactPoint = wall.endPos + (unitDirectionWall * distX)
        if unitDirectionPerp.angleWith(self.velocity) < radians(90):
            unitDirectionPerp = -unitDirectionPerp

        resetPoint = impactPoint + (unitDirectionPerp * (self.radius + wall.width/2))
        self.position = resetPoint

    def addForce(self, x=0, y=0):
        if x:
            self.acceleration.x = x / self.mass

        if y:
            weight = self.mass * 9.8
            resultant_force = y + weight

            self.acceleration.y = resultant_force / self.mass

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.position.y = min(self.position.y, DISPLAY_HEIGHT - self.radius) # ball doesn't go through floor
        self.acceleration = Vector(0, 9.8)

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
            if self.doWallCollision(w):
                self.colour = GREEN
                break