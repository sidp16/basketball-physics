from math import sqrt, acos


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x},{self.y}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"{other}, found {type(other).__name__}, expected Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"{other}, found {type(other).__name__}, expected Vector")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"{other}, found {type(other).__name__}, expected Vector / int / float")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        else:
            raise TypeError(f"{other}, found {type(other).__name__}, expected int / float")

    def unit(self):
        return self / self.magnitude()

    def magnitude(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def distTo(self, other):
        if isinstance(other, Vector):
            return sqrt(((self.x - other.x) ** 2 + (self.y - other.y) ** 2))
        else:
            raise TypeError(f"{other}, found {type(other).__name__}, expected Vector")

    def angleWith(self, other):
        if isinstance(other, Vector):
            return acos((self * other) / (self.magnitude() * other.magnitude()))
        else:
            raise TypeError(f"{other}, found {type(other).__name__}, expected Vector")

if __name__ == "__main__":
    point2 = Vector(3,8)
    print(point2 / 3)