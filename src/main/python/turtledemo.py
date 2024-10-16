import turtle
from PIL import Image

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=200, height=200)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Draw a 30px by 30px circle in the middle of the screen
t.penup()
t.goto(0, -15)  # Move to the starting position
t.pendown()
t.circle(15)  # Draw a circle with radius 15px

# Save the drawing to a PNG file
canvas = screen.getcanvas()
canvas.postscript(file="circle.eps")

# Convert EPS to PNG using Pillow
img = Image.open("circle.eps")
img.save("circle.png")

# Clean up
turtle.bye()

print("The circle has been drawn and saved as circle.png")
