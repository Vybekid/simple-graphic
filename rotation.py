import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_wing(color, size, angle):
    """Draws one wing of the butterfly."""
    t.color(color)
    t.begin_fill()
    t.left(angle)
    t.forward(size)
    for _ in range(2):
        t.right(90)
        t.forward(size)
    t.right(90)
    t.forward(size)
    t.end_fill()

def main():
    """Main function to draw the butterfly."""
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.setheading(90)

    # Draw the wings
    draw_wing("orange", 100, 45)
    draw_wing("yellow", 80, 45)
    t.setheading(270)
    draw_wing("orange", 100, 45)
    draw_wing("yellow", 80, 45)

    # Draw the body
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("black")
    t.setheading(90)
    t.forward(200)

    # Draw the antennae
    t.left(30)
    t.forward(50)
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.setheading(150)
    t.forward(50)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()