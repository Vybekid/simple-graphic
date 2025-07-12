import turtle 

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white") 

# Create a turtle object
t = turtle.Turtle()
t.speed(3) # Set the drawing speed 

# Function to draw a semicircle
def draw_semicircle(radius, color):
 t.color(color)
 t.begin_fill()
 t.circle(radius, 180)
 t.end_fill() 

# Draw the left wing
t.penup()
t.goto(-50, 0)
t.pendown()
draw_semicircle(80, "skyblue") 

# Draw the right wing
t.penup()
t.goto(50, 0)
t.setheading(180) # Point the turtle to the left
t.pendown()
draw_semicircle(80, "skyblue") 

# Draw the body
t.penup()
t.goto(0, 80)
t.pendown()
t.color("purple")
t.begin_fill()
t.right(90)
t.forward(160)
t.left(90)
t.circle(5)
t.end_fill() 

# Draw the antennae
t.penup()
t.goto(0, 80)
t.pendown()
t.left(45)
t.forward(50)
t.penup()
t.goto(0, 80)
t.pendown()
t.right(90)
t.forward(50) 

# Hide the turtle
t.hideturtle() 

# Keep the window open
turtle.done()