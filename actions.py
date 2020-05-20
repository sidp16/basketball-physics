from math import radians, sin, cos

# force in newtons, angle inputted in degrees and converted to radians
def shootBall(ball, totalForce, angle):
    angle = radians(angle)
    y_force = sin(angle) * totalForce
    x_force = cos(angle) * totalForce
    print(f"xF: {x_force:4.2f}, yF: {y_force:4.2f}, {angle:4.2f} radians")
    ball.addForce(x_force, y_force)