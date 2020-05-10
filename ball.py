import pygame

from colours import BLACK


class Ball:
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def __repr__(self):
        return f"{self.radius} at {self.x}, {self.y}"

    def draw(self, window):
        x, y = int(self.x), int(self.y)
        pygame.draw.circle(window, BLACK, (x, y), self.radius)
        pygame.draw.circle(window, self.colour, (x, y), self.radius - 4)

    def update(self, velocity, acceleration, bounce, display_height, gameDisplay):
        self.velocity = velocity
        self.acceleration = acceleration
        self.bounce = bounce
        self.display_height = display_height
        clock = pygame.time.Clock()

        while True:
            while self.y < display_height - self.radius:
                self.y = min(self.y + velocity, display_height - self.radius)
                velocity += acceleration
                gameDisplay.fill((64, 64, 64))
                self.draw(gameDisplay)
                clock.tick(60)
                pygame.display.update()
                print(f"speed: {velocity} | pos: {self.y} | going down")

            velocity = -velocity * bounce
            if abs(velocity) < 2.15:
                continue

            while velocity < 0:
                print(f"speed: {velocity} | pos: {self.y} | going up")
                self.y += velocity
                velocity += acceleration
                gameDisplay.fill((64, 64, 64))
                self.draw(gameDisplay)
                clock.tick(60)
                pygame.display.update()

