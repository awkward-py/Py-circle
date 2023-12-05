import turtle
import random

# Function to generate a random color
def random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

# Function to draw a colorful circle
def draw_circle(radius):
    turtle.color(random_color())
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw the beautiful design
def draw_beautiful_design():
    turtle.speed(2)
    turtle.width(2)

    for _ in range(36):
        draw_circle(50)
        turtle.right(10)

    turtle.hideturtle()
    turtle.done()

# Call the function to draw the beautiful design
draw_beautiful_design()
