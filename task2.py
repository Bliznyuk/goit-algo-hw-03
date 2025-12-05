import turtle
import sys


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Recursively draws a Koch curve fractal.
    """
    if order == 0:
        # Base case: draw a straight line segment
        t.forward(size)
    else:
        # Recursive case: divide the segment into four parts with specific angles
        # Each part is 1/3 the size and forms the characteristic Koch curve pattern
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: float = 300) -> None:
    """
    Draws a Koch snowflake fractal using turtle graphics.
    The snowflake is created by drawing three Koch curves arranged
    in an equilateral triangle pattern.
    """
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    # Set maximum drawing speed for faster rendering
    t.speed(0)
    # Position the turtle to center the snowflake
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Draw three Koch curves rotated 120° to form a snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # Hide the turtle cursor for a cleaner final image
    t.hideturtle()

    # Keep the window open until closed by the user
    window.mainloop()


# Example function call with default order of 3
draw_koch_snowflake(3)


if __name__ == "__main__":
    # Default recursion level
    order = 3

    # Parse command-line argument if provided
    if len(sys.argv) > 1:
        try:
            order = int(sys.argv[1])
            if order < 0:
                print("Error: Order must be a non-negative integer.")
                sys.exit(1)
        except ValueError:
            print("Error: Order must be an integer.")
            sys.exit(1)

    draw_koch_snowflake(order)
