from math import radians, sin, cos

# force in newtons, angle inputted in degrees and converted to radians
def shootBall(ball, totalForce, angle):
    print(f"Input Angle:  {angle}")
    angle = radians(angle)
    print(f"Angle in radians: {angle}")
    y_force = sin(angle) * totalForce
    x_force = cos(angle) * totalForce
    print(f"X force: {x_force}, Y force: {y_force}")
    ball.addForce(x_force, y_force)