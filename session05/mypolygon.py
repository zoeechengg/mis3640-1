import turtle


# print(andrew)

# for i in range(4):
#     andrew.fd(100)
#     andrew.lt(90)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


# square(andrew)

# daniel = turtle.Turtle()
# square(daniel)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# square(andrew, 50)

# def polygon(t, length, n):
#     angle = 360/n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)


# polygon(andrew, n=20, length=30)

import math


# def circle(t, r):
#     circumference = 2 * math.pi * r
#     length = circumference/40
#     polygon(t, length, 40)


# circle(andrew, 100)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle/360
#     n = int(arc_length/3) + 1
#     step_length = arc_length/n
#     step_angle = angle/n

#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)


# arc(andrew, 100, 180)
# arc(andrew, 100, 360)


def polyline(t, n, length, angle):
    """
    Draws n line segments with given length and angle (in degrees) between them.
    t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# polyline(andrew, n=4, length=100, angle=60)

def polygon(t, length, n):
    """
    Draws a n-sided polygon with given length. t is a turtle.
    """
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """
    Draws an arc with radius r and angle. t is a turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)


def circle(t, r):
    """
    Draws a circle with radius r. t is a turtle.
    """
    arc(t, r, 360)


def main():
    andrew = turtle.Turtle()
    # polygon(andrew, 100, 6) 
    # arc(andrew, 100, 270)
    circle(andrew, 150)

    turtle.mainloop()


if __name__ == "__main__":
    main()
