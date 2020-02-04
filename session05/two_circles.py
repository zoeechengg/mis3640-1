from turtle_shape import arc, circle, move, polygon
import turtle


def draw_two_circles(t):
    """
    Draws two circles. t is a turtle.
    """
    # large circle
    circle(t, 100)
    move(t, 100, 0)

    # another large circle
    circle(t, 100)

def main():
    t = turtle.Turtle()
    t.speed(0)
    draw_two_circles(t)
    turtle.mainloop()

if __name__ == "__main__":
    main()